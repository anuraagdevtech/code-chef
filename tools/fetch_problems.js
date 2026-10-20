/*
 * Fetch full problem payloads for a list of problem codes.
 *
 * Unlike the practice course pages, this endpoint IS reachable by fetch() and
 * works signed out, so the whole batch can run in a single call.
 *
 *   GET /api/contests/{contest}/problems/{code}
 *
 * `PRACTICE` works as a universal contest code for roadmap problems.
 */
async function fetchProblems(codes, contest = 'PRACTICE') {
  const out = {};
  for (const code of codes) {
    try {
      const r = await fetch(`/api/contests/${contest}/problems/${code}`, { credentials: 'include' });
      const j = await r.json();
      const pc = j.problemComponents || {};
      out[code] = {
        code: j.problem_code,
        name: j.problem_name,
        rating: j.difficulty_rating,
        timeLimit: j.max_timelimit,
        status: j.problem_status,
        computedTags: j.computed_tags || [],
        userTags: j.user_tags || [],
        statement: pc.statement || '',
        constraints: pc.constraints || '',
        inputFormat: pc.inputFormat || '',
        outputFormat: pc.outputFormat || '',
        subtasks: pc.subtasks || '',
        samples: pc.sampleTestCases || [],
      };
    } catch (e) {
      out[code] = { code, error: String(e) };
    }
  }
  return out;
}
