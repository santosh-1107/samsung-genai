const MEDAL = {
  diamond:   { icon: '💎', label: 'Diamond', color: '#00D4AA' },
  gold:      { icon: '🥇', label: 'Gold',    color: '#FFD700' },
  silver:    { icon: '🥈', label: 'Silver',  color: '#C0C8D8' },
  submitted: { icon: '✅', label: 'Done',    color: '#4A6FA5' },
};

let pollTimer = null;
let totalDays = 5;

async function fetchData() {
  const res = await fetch('/api/leaderboard', { cache: 'no-store' });
  return res.json();
}

function medalCell(achievement) {
  if (!achievement) return `<td class="day-cell empty">—</td>`;
  const m = MEDAL[achievement] || MEDAL.submitted;
  return `<td class="day-cell" title="${m.label}"><span class="medal" style="color:${m.color}">${m.icon}</span></td>`;
}

// Top-3 medal — keyed on true score rank, shown next to the name, independent
// of where the row actually sits in the (now alphabetical) table order.
function topMedal(rank) {
  if (rank === 1) return { icon: '🥇', cls: 'gold-rank' };
  if (rank === 2) return { icon: '🥈', cls: 'silver-rank' };
  if (rank === 3) return { icon: '🥉', cls: 'bronze-rank' };
  return null;
}

// Per-day breakdown — "Total Students" up top stays a single overall number,
// but submitted-count and top-score are date-wise (per day), not summed across days.
function renderDayStats(students, totalDays, totalStudents) {
  let cards = '';
  for (let d = 1; d <= totalDays; d++) {
    const dayEntries = students
      .map(s => (s.days || []).find(x => x.day === d))
      .filter(Boolean);
    const submittedCount = dayEntries.filter(x => x.achievement !== null).length;
    const scores = dayEntries.map(x => x.score || 0);
    const topScore = scores.length ? Math.max(...scores) : 0;

    cards += `
      <div class="day-stat">
        <div class="day-stat-label">Day ${d}</div>
        <div class="day-stat-row">
          <span class="day-stat-num">${submittedCount}/${totalStudents}</span>
          <span class="day-stat-sub">submitted</span>
        </div>
        <div class="day-stat-row">
          <span class="day-stat-num gold-num">${topScore > 0 ? (topScore % 1 === 0 ? topScore.toFixed(0) : topScore.toFixed(1)) : '—'}</span>
          <span class="day-stat-sub">top score</span>
        </div>
      </div>`;
  }
  document.getElementById('day-stats-bar').innerHTML = cards;
}

function render(data) {
  if (data.error === 'roster_empty') {
    document.getElementById('content').innerHTML =
      `<div class="msg error">roster.json not found or empty — add student GitHub usernames to roster.json.</div>`;
    return;
  }

  totalDays = data.total_days || 5;
  const students = data.students || [];

  document.getElementById('stat-total').textContent = data.total_students ?? '–';
  document.getElementById('updated').textContent =
    data.generated_at ? `Updated ${new Date(data.generated_at).toLocaleTimeString()}` : '';

  renderDayStats(students, totalDays, data.total_students ?? students.length);

  if (students.length === 0) {
    document.getElementById('content').innerHTML =
      `<div class="msg">No students found in roster.</div>`;
    return;
  }

  // Build day header columns
  let dayHeaders = '';
  for (let d = 1; d <= totalDays; d++) {
    dayHeaders += `<th class="day-header">Day ${d}</th>`;
  }

  // Build student rows — table order is alphabetical, so "#" is just the row
  // position in that list. Actual score standing (top-3 medal) is shown next
  // to the name instead, since it no longer matches row position.
  let rows = '';
  students.forEach((s, i) => {
    const position = i + 1;
    const dayCells = s.days.map(d => medalCell(d.achievement)).join('');
    const hasAny = s.daysSubmitted > 0;
    const medal = topMedal(s.rank);
    const medalHTML = medal
      ? ` <span class="rank-badge ${medal.cls}" title="Rank #${s.rank} overall by score">${medal.icon} #${s.rank}</span>`
      : '';
    rows += `
      <tr class="${hasAny ? 'active-row' : 'pending-row'}">
        <td class="rank-cell"><span class="rank-num">${position}</span></td>
        <td class="name-cell">
          <div class="student-name">${escapeHTML(s.name)}${medalHTML}</div>
          <div class="student-github">@${escapeHTML(s.github)}</div>
        </td>
        ${dayCells}
        <td class="score-cell">${s.totalScore > 0 ? s.totalScore.toFixed(0) + ' pts' : '—'}</td>
      </tr>`;
  });

  document.getElementById('content').innerHTML = `
    <div class="table-wrap">
      <table class="scoreboard">
        <thead>
          <tr>
            <th class="rank-header">#</th>
            <th class="name-header">Student</th>
            ${dayHeaders}
            <th class="score-header">Points</th>
          </tr>
        </thead>
        <tbody>${rows}</tbody>
      </table>
    </div>
    <div class="legend">
      <span>💎 Diamond (3 pts)</span>
      <span>🥇 Gold (2 pts)</span>
      <span>🥈 Silver (1 pt)</span>
      <span>✅ Submitted</span>
      <span>— Not yet</span>
    </div>`;
}

function escapeHTML(str) {
  const d = document.createElement('div');
  d.textContent = str ?? '';
  return d.innerHTML;
}

async function load() {
  try {
    const data = await fetchData();
    render(data);
  } catch {
    document.getElementById('content').innerHTML =
      `<div class="msg error">Cannot reach the leaderboard function. Check Netlify deployment.</div>`;
  }
}

function startPolling() {
  if (pollTimer) clearInterval(pollTimer);
  pollTimer = setInterval(load, 20000);
}

load();
startPolling();
