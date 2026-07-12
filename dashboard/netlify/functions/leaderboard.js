const https = require('https');

const GITHUB_OWNER = process.env.GITHUB_OWNER || "REPLACE_ME";
const GITHUB_REPO  = process.env.GITHUB_REPO  || "samsung-genai";
const BRANCH       = process.env.SUBMISSIONS_BRANCH || "main";
const TOTAL_DAYS   = parseInt(process.env.TOTAL_DAYS || "5", 10);

const CACHE_MS = 25000;
let cache = {};

function fetchJSON(url) {
  return new Promise((resolve) => {
    const req = https.get(url, { headers: { 'Cache-Control': 'no-cache', 'User-Agent': 'Samsung-GenAI-Dashboard/1.0' } }, (res) => {
      let data = '';
      res.on('data', chunk => data += chunk);
      res.on('end', () => {
        try { resolve(JSON.parse(data)); }
        catch { resolve(null); }
      });
    });
    req.on('error', () => resolve(null));
  });
}

function rosterUrl() {
  return `https://raw.githubusercontent.com/${GITHUB_OWNER}/${GITHUB_REPO}/${BRANCH}/roster.json`;
}

function submissionUrl(username, day) {
  return `https://raw.githubusercontent.com/${username}/${GITHUB_REPO}/${BRANCH}/submissions/day${day}.json`;
}

function scoreFromSubmission(sub) {
  if (!sub) return null;
  if (typeof sub.score === 'number') return sub.score;
  const achMap = { diamond: 3, gold: 2, silver: 1 };
  if (sub.achievement && achMap[sub.achievement] != null) return achMap[sub.achievement];
  if (sub.student_name && sub.student_name.trim().length > 2) return 0.5;
  return null;
}

function tierFromSubmission(sub, rankIndex, totalSubmitted) {
  if (sub.achievement) {
    const map = { diamond: 'gold', gold: 'silver', silver: 'bronze' };
    return map[sub.achievement] || 'entry';
  }
  const pct = (rankIndex + 1) / totalSubmitted;
  if (pct <= 0.10) return 'gold';
  if (pct <= 0.35) return 'silver';
  if (pct <= 0.70) return 'bronze';
  return 'entry';
}

async function buildForDay(roster, day) {
  const results = await Promise.all(
    roster.map(async (s) => {
      const sub = await fetchJSON(submissionUrl(s.github, day));
      return { github: s.github, name: s.name || s.github, submission: sub };
    })
  );

  const submitted = results
    .filter((r) => scoreFromSubmission(r.submission) !== null)
    .map((r) => ({ ...r, _score: scoreFromSubmission(r.submission) }));

  submitted.sort((a, b) => b._score - a._score);

  const ranked = submitted.map((r, i) => ({
    github: r.github,
    name: r.name,
    score: r._score,
    tasks_completed: r.submission.tasks_completed ?? null,
    tasks_total: r.submission.tasks_total ?? null,
    rank: i + 1,
    tier: tierFromSubmission(r.submission, i, submitted.length),
  }));

  const submittedGithubs = new Set(submitted.map((r) => r.github));
  const pending = results
    .filter((r) => !submittedGithubs.has(r.github))
    .map((r) => ({ github: r.github, name: r.name }));

  return { day, ranked, pending, submitted_count: submitted.length };
}

exports.handler = async (event) => {
  const headers = { 'Content-Type': 'application/json', 'Cache-Control': 'no-store' };

  const roster = await fetchJSON(rosterUrl());
  if (!Array.isArray(roster) || roster.length === 0) {
    return {
      statusCode: 200,
      headers,
      body: JSON.stringify({ error: 'roster_empty', message: 'roster.json not found (or empty) at the repo root.' }),
    };
  }

  const requestedDay = parseInt(event.queryStringParameters?.day, 10);
  let day = requestedDay >= 1 && requestedDay <= TOTAL_DAYS ? requestedDay : null;

  if (day) {
    const c = cache[day];
    if (c && Date.now() - c.ts < CACHE_MS) {
      return { statusCode: 200, headers, body: JSON.stringify(c.data) };
    }
    const result = await buildForDay(roster, day);
    const payload = { ...result, total_days: TOTAL_DAYS, total_students: roster.length, generated_at: new Date().toISOString() };
    cache[day] = { data: payload, ts: Date.now() };
    return { statusCode: 200, headers, body: JSON.stringify(payload) };
  }

  for (let d = TOTAL_DAYS; d >= 1; d--) {
    const c = cache[d];
    const result = c && Date.now() - c.ts < CACHE_MS ? c.data : await buildForDay(roster, d);
    if (result.submitted_count > 0 || d === 1) {
      const payload = { ...result, total_days: TOTAL_DAYS, total_students: roster.length, generated_at: new Date().toISOString() };
      cache[d] = { data: payload, ts: Date.now() };
      return { statusCode: 200, headers, body: JSON.stringify(payload) };
    }
  }

  return { statusCode: 200, headers, body: JSON.stringify({ error: 'no_data' }) };
};
