# CodeChef - Become 5 Star roadmap

Worked documentation for the problems I have solved on the CodeChef [Become 5 Star](https://www.codechef.com/roadmap/become-5-star) roadmap - statement, constraints, an explained Python solution, its complexity, and the topic each problem belongs to.

## Progress

| Level | Course | Solved | Total |
|---|---|---:|---:|
| 1 | 500 to 1000 difficulty rating | 156 | 156 |
| 2 | Level up from 1* to 2* | 66 | 66 |
| 2 | 1400 to 1600 difficulty problems | 85 | 85 |
| 3 | Jump from 2* to 3* | 96 | 96 |
| 3 | 1600 to 1800 difficulty problems | 98 | 128 |
| 4 | Rise from 3* to 4* | 1 | 118 |
| 5 | 2000 to 2500 difficulty problems | 0 | 112 |
| | **Total** | **502** | **761** |

Documented so far: **10** problems.

## Problems by topic

### Arrays (1)

| # | Problem | Difficulty | Technique | Time |
|---:|---|---:|---|---|
| 6 | [Mahasena](docs/arrays/AMR15A.md) | 720 | Parity counting in a single pass | $O(N)$ |

### Basic Math (7)

| # | Problem | Difficulty | Technique | Time |
|---:|---|---:|---|---|
| 1 | [Greater Average](docs/basic-math/AVGPROBLEM.md) | 500 | Integer arithmetic, avoiding floats | $O(1)$ per test case |
| 2 | [Subscriptions](docs/basic-math/SUBSCRIBE_.md) | 504 | Ceiling division | $O(1)$ per test case |
| 3 | [Janmansh and Assignments](docs/basic-math/JASSIGNMENTS.md) | 513 | Conditional arithmetic | $O(1)$ per test case |
| 4 | [Exams](docs/basic-math/EXAMCHEF.md) | 519 | Percentage comparison without division | $O(1)$ per test case |
| 5 | [Chef in his Office](docs/basic-math/OFFICE.md) | 532 | Direct formula | $O(1)$ per test case |
| 7 | [CRED Coins](docs/basic-math/CREDCOINS.md) | 539 | Floor division | $O(1)$ per test case |
| 10 | [Minimum Pizzas](docs/basic-math/MINPIZZA.md) | 546 | Ceiling division | $O(1)$ per test case |

### Conditionals & Case Work (2)

| # | Problem | Difficulty | Technique | Time |
|---:|---|---:|---|---|
| 8 | [Water Filling](docs/conditionals-case-work/WATERFILLING.md) | 541 | Counting flags instead of enumerating cases | $O(1)$ per test case |
| 9 | [Sale Season](docs/conditionals-case-work/SALESEASON.md) | 541 | Ordered threshold ladder | $O(1)$ per test case |

## Repository layout

```
docs/<topic>/<CODE>.md   generated problem write-ups
solutions/<CODE>.py      runnable Python solutions
data/raw/<CODE>.json     problem payloads fetched from CodeChef
data/authored/<CODE>.md  hand written approach + metadata
tools/                   fetch, build and verify scripts
```

Docs are generated - edit `data/authored/<CODE>.md` or `solutions/<CODE>.py` and re-run `python3 tools/build_docs.py`.
