[&larr; 214. Maximum Trio](MXMTRIO.md) &middot; [Index](../../README.md) &middot; [250. Approximately II &rarr;](APPROX2.md)

# 221. Hotel Bytelandia

> CodeChef problem code [`HOTEL`](https://www.codechef.com/problems/HOTEL) &middot; difficulty **1405** &middot; time limit **0.5s**

| | |
|---|---|
| **Topic** | Sorting |
| **Technique** | Event sweep |
| **Time** | $O(N \log N)$ per test case |
| **Space** | $O(N)$ |
| **Roadmap course** | 1400 to 1600 difficulty problems (Level 2) |

## Question

A holiday weekend is coming up,
and Hotel Bytelandia needs to find out if it has enough rooms to accommodate all potential guests.
A number of guests have made reservations.
Each reservation consists of an arrival time, and a departure time.
The hotel management has hired you to calculate the maximum number of guests that will be at the hotel simultaneously.
Note that if one guest arrives at the same time another leaves, they are never considered to be at the hotel simultaneously
(see the second example).

**Input**

Input will begin with an integer T, the number of test cases.
Each test case begins with an integer N, the number of guests.
Two lines follow, each with exactly N positive integers.
The i-th integer of the first line is the arrival time of the i-th guest,
and the i-th integer of the second line is the departure time of the i-th guest
(which will be strictly greater than the arrival time).

**Output**

For each test case, print the maximum number of guests that are simultaneously at the hotel.

**Constraints**

- T≤100

- N≤100

- All arrival/departure times will be between 1 and 1000, inclusive

## Constraints

- T≤100
- N≤100
- All arrival/departure times will be between 1 and 1000, inclusive

## Sample

**Sample input**

```
3
3
1 2 3
4 5 6
5
1 2 3 4 5
2 3 4 5 6
7
13 6 5 8 2 10 12
19 18 6 9 9 11 15
```

**Sample output**

```
3
1
3
```

## Approach

Turn each reservation into two **events** — $+1$ at the arrival time, $-1$ at the departure — then sweep them in time order, tracking a running occupancy and its maximum.

The whole problem lives in how ties are broken. The statement says a guest arriving exactly as another leaves are *never* simultaneous, so at a shared timestamp the **departure must be processed first**. Sorting by `(time, delta)` achieves this for free, since $-1 < +1$ puts departures ahead of arrivals.

Sample case 2 is built entirely on that rule: five guests arrive at $1,2,3,4,5$ and depart at $2,3,4,5,6$, so each leaves exactly as the next arrives. The answer is $1$. Process arrivals first and every handover briefly shows two guests, giving $2$ — a classic off-by-one in sweep problems.

Sample case 1 has three guests whose stays overlap completely, giving $3$, and case 3 has partial overlaps peaking at $3$.

The alternative here, given times bounded by $1000$, is a difference array over the timeline: add $+1$ at arrival, $-1$ at departure, then prefix-sum and take the maximum. That is $O(\text{maxtime} + N)$ and sidesteps the sort — but it still needs the same half-open convention, marking the interval as $[\text{arrival}, \text{departure})$.

The event sweep is the shape worth knowing, since it keeps working when times are large or unbounded.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n = int(data[pos])
        arrive = data[pos + 1:pos + 1 + n]
        depart = data[pos + 1 + n:pos + 1 + 2 * n]
        pos += 1 + 2 * n
        events = [(int(v), 1) for v in arrive] + [(int(v), -1) for v in depart]
        # Sorting by (time, delta) puts -1 before +1, so a guest leaving at
        # time x never overlaps one arriving at x.
        events.sort()
        cur = best = 0
        for _, delta in events:
            cur += delta
            if cur > best:
                best = cur
        out.append(str(best))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(N \log N)$ per test case
- **Space:** $O(N)$

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

---

Same problem in rating order (#227 of 486): [../../by-rating/227-HOTEL.md](../../by-rating/227-HOTEL.md)
