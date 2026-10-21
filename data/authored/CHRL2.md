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
