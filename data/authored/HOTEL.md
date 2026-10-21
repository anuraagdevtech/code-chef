---
topic: Sorting
subtopic: Event sweep
time: $O(N \log N)$ per test case
space: $O(N)$
---
Turn each reservation into two **events** — $+1$ at the arrival time, $-1$ at the departure — then sweep them in time order, tracking a running occupancy and its maximum.

The whole problem lives in how ties are broken. The statement says a guest arriving exactly as another leaves are *never* simultaneous, so at a shared timestamp the **departure must be processed first**. Sorting by `(time, delta)` achieves this for free, since $-1 < +1$ puts departures ahead of arrivals.

Sample case 2 is built entirely on that rule: five guests arrive at $1,2,3,4,5$ and depart at $2,3,4,5,6$, so each leaves exactly as the next arrives. The answer is $1$. Process arrivals first and every handover briefly shows two guests, giving $2$ — a classic off-by-one in sweep problems.

Sample case 1 has three guests whose stays overlap completely, giving $3$, and case 3 has partial overlaps peaking at $3$.

The alternative here, given times bounded by $1000$, is a difference array over the timeline: add $+1$ at arrival, $-1$ at departure, then prefix-sum and take the maximum. That is $O(\text{maxtime} + N)$ and sidesteps the sort — but it still needs the same half-open convention, marking the interval as $[\text{arrival}, \text{departure})$.

The event sweep is the shape worth knowing, since it keeps working when times are large or unbounded.

## Edge cases

- **A departure at time $x$ frees the room for an arrival at $x$.** Sorting by `(time, delta)` puts $-1$ before $+1$ since $-1 < 1$, which is the entire reason the second sample answers $1$ and not $2$ — every departure there coincides with the next arrival.
- **All stays overlapping** (the first row) → the answer is $N$.
- **The peak can be in the middle** — the third row reaches $3$ twice, once around time $8$ and again at $13$ — so the running maximum has to be tracked rather than read off the end.
- **Arrivals and departures are on separate lines**, $N$ values each, not interleaved as pairs; reading them as pairs scrambles every case.
- **Times are confined to $1 \dots 1000$**, so a counting array would work too, but the event sweep needs no such bound.
- **$N \leq 100$**: the sort is trivial, and correctness rests entirely on the tie-break.

## Dry run

Second sample: arrivals $1,2,3,4,5$ and departures $2,3,4,5,6$.

| time | event | occupancy | peak |
|---:|---|---:|---:|
| 1 | arrive | 1 | 1 |
| 2 | **depart first** | 0 | 1 |
| 2 | arrive | 1 | 1 |
| 3 | depart | 0 | 1 |
| 3 | arrive | 1 | 1 |
| … | alternating | … | 1 |

Output `1`. Reversing the tie-break makes every pair overlap and reports `2`.
