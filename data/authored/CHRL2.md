---
topic: Greedy
subtopic: Pipelined counters along a fixed pattern
time: $O(|S|)$
space: $O(1)$
---
Each move deletes a subsequence spelling `CHEF`, and the moves are disjoint, so the question is how many disjoint `CHEF` subsequences the string admits. Scanning left to right, maintain three counters — partial matches that have reached `C`, `CH` and `CHE` — and promote greedily:

- `C`: start a new partial match.
- `H`: if some match is waiting at `C`, advance it.
- `E`: if some match is waiting at `CH`, advance it.
- `F`: if some match is waiting at `CHE`, complete it and score.

Promoting as early as possible is optimal because the letters are interchangeable within their stage: if an optimal solution uses a later `C` where the greedy used an earlier one, swapping them keeps the solution valid, since the earlier `C` leaves at least as much room to the right. The same exchange applies at each stage, so the greedy never loses a match.

A letter that finds no waiting match is simply discarded, which is why the trailing `FFF` in the sample contributes nothing — there are no `CHE` prefixes left to close.

$$\text{answer} = \text{number of } \texttt{F}\text{s that find a waiting } \texttt{CHE}$$

Note the input has **no leading $T$**: the whole input is one string.

For `CHEFCHEFFFF` the first four characters complete one match and the next four complete a second; the remaining three `F`s are wasted, giving $2$. Were the string `CCHHEEFF`, the counters would pipeline two matches out of the same letters — which is why the counters must be kept per stage rather than just counting occurrences of each letter.

## Edge cases

- **Four pipelined counters replace any search.** A `C` starts a new partial match; an `H` promotes one waiting at `C`; an `E` promotes one waiting at `CH`; an `F` completes one waiting at `CHE` and scores.
- **A letter with nothing to promote is discarded**, which is why the trailing `FFF` in the first sample contributes nothing — there are no `CHE` prefixes left to close.
- **Promoting greedily is optimal**, since the matches are interchangeable: advancing any waiting prefix is as good as advancing another, so there is never a reason to hold one back.
- **The subsequences need not be contiguous**, which is exactly what the counters model — the letters of one `CHEF` may be far apart.
- **Letters arriving out of order are wasted**: the second sample's `CHHHEEEFF` scores only once, because the extra `H`s and `E`s find no partial match at the right stage.
- **Trailing `C`s accumulate harmlessly**, as the second sample's final `CC` shows.
- **There is no test-case count**: the input is the single string.

## Dry run

First sample: `CHEFCHEFFFF`.

| letter | waiting at `C` | at `CH` | at `CHE` | completed |
|---|---:|---:|---:|---:|
| C | 1 | 0 | 0 | 0 |
| H | 0 | 1 | 0 | 0 |
| E | 0 | 0 | 1 | 0 |
| F | 0 | 0 | 0 | 1 |
| C H E F | — | — | — | 2 |
| F F F | 0 | 0 | 0 | 2 |

Output `2`.
