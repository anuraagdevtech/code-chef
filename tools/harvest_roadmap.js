/*
 * Harvest the "Become 5 Star" roadmap catalog + per-problem solved status.
 *
 * Run in the page context of www.codechef.com while signed in.
 * The practice pages are a React SPA: the course payload is only present on
 * `window.syllabusData` AFTER a real navigation (a bare fetch() of the URL
 * returns a ~10KB shell), so this must be driven one course at a time.
 *
 * Usage (per course, after navigating to /practice/<slug>?roadmapSlug=become-5-star):
 *     harvestCurrentCourse()
 */
function harvestCurrentCourse() {
  const sd = window.syllabusData;
  if (!sd || !sd.modules) return { error: 'syllabusData not present yet' };
  const problems = [];
  sd.modules.forEach((m) =>
    (m.submodules || []).forEach((s) =>
      (s.problems_with_status || []).forEach((p) =>
        problems.push({
          code: p.code,
          name: p.name,
          rating: p.difficulty_rating,
          status: p.status,          // unattempted | attempted | solved
          contest: s.contest_code,   // needed for the statement API
          module: m.name,
          submodule: s.name,
        })
      )
    )
  );
  return {
    slug: sd.slug,
    title: sd.title,
    solved: sd.problems_solved,
    total: sd.total_problems,
    problems,
  };
}

/* The 7 courses that make up the roadmap, in level order. */
const ROADMAP_COURSES = [
  { slug: 'logical-problems',           level: 1, label: '500 to 1000 difficulty rating' },
  { slug: '1to2stars',                  level: 2, label: 'Level up from 1* to 2*' },
  { slug: '2-star-difficulty-problems', level: 2, label: '1400 to 1600 difficulty problems' },
  { slug: '2to3stars',                  level: 3, label: 'Jump from 2* to 3*' },
  { slug: '3-star-difficulty-problems', level: 3, label: '1600 to 1800 difficulty problems' },
  { slug: '3to4stars',                  level: 4, label: 'Rise from 3* to 4*' },
  { slug: '5-star-and-above-problems',  level: 5, label: '2000 to 2500 difficulty problems' },
];
