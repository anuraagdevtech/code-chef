[&larr; 206. Maximise the Subsequence Sum](206-SIGNFLIP.md) &middot; [Index](README.md) &middot; [208. Arranging Cup-cakes &rarr;](208-RESQ.md)

# 207. Chopsticks

> [`TACHSTCK`](https://www.codechef.com/problems/TACHSTCK) &middot; difficulty **1320** &middot; time limit **7s** &middot; Level up from 1* to 2* (Level 2)

## Topic used

| | |
|---|---|
| **Topic** | Greedy |
| **Technique** | Pairing adjacent elements after sorting |
| **Complexity class** | Linearithmic $O(n \log n)$ |
| **Time** | $O(N \log N)$ |
| **Space** | $O(N)$ |

## Question

**[**Chopsticks** (singular: **chopstick**) are short, frequently tapered sticks used in pairs of equal length, which are used as the traditional eating utensils of China, Japan, Korea and Vietnam. Originated in ancient China, they can also be found in some areas of Tibet and Nepal that are close to Han Chinese populations, as well as areas of Thailand, Laos and Burma which have significant Chinese populations. Chopsticks are most commonly made of wood, bamboo or plastic, but in China, most are made out of bamboo. Chopsticks are held in the dominant hand, between the thumb and fingers, and used to pick up pieces of food.]

 Retrieved from [wikipedia](http://en.wikipedia.org/wiki/Chopsticks)

Actually, the two sticks in a pair of chopsticks need not be of the same length. A pair of sticks can be used to eat as long as the difference in their length is at most **D**. The Chef has **N** sticks in which the i^th stick is **L[i]** units long. A stick can't be part of more than one pair of chopsticks. Help the Chef in pairing up the sticks to form the maximum number of usable pairs of chopsticks.

**Input**

The first line contains two space-separated integers **N** and **D**. The next **N** lines contain one integer each, the i^th line giving the value of **L[i]**.

**Output**

Output a single line containing the maximum number of pairs of chopsticks the Chef can form.

**Constraints**

- **1** ≤ **N** ≤ **100,000 (10^5) **

- **0** ≤ **D** ≤ **1,000,000,000 (10^9) **

- **1** ≤ **L[i]** ≤ **1,000,000,000 (10^9)** for all integers **i** from **1** to **N**

## Constraints

- 1 ≤ N ≤ 100,000 (10^ 5 )
- 0 ≤ D ≤ 1,000,000,000 (10^ 9 )
- 1 ≤ L[i] ≤ 1,000,000,000 (10^ 9 ) for all integers i from 1 to N

## Sample

**Sample input**

```
5 2
1
3
3
9
4
```

**Sample output**

```
2
```

<details><summary>Explanation</summary>

The 5 sticks have lengths 1, 3, 3, 9 and 4 respectively. The maximum allowed difference in the lengths of two sticks forming a pair is at most 2.
It is clear that the 4th stick (length 9) cannot be used with any other stick.
The remaining 4 sticks can can be paired as (1st and 3rd) and (2nd and 5th) to form 2 pairs of usable chopsticks.

</details>

## Approach

Sort the lengths, then sweep left to right: if the current stick and the next differ by at most $D$, pair them and skip both; otherwise discard the current one and move on.

Two facts make this greedy optimal.

**An optimal pairing can always be taken between sorted neighbours.** If sticks $a < b$ are paired and some unpaired $c$ lies between them, then $c$ is within $D$ of both, so re-pairing to use $c$ costs nothing. Repeating this argument pushes every pair onto adjacent positions.

**Pairing the smallest available stick with its immediate successor is never worse.** The smallest stick is the hardest to place — only larger sticks are left, and the next one is the closest. If it cannot pair with its neighbour it cannot pair with anything, so discarding it loses nothing.

Together these justify the single sweep. Sorting is the dominant cost at $O(N \log N)$, and the sweep is linear.

Tracing the sample, $[1,3,3,4,9]$ with $D = 2$: $1$ pairs with $3$ (gap $2$), then $3$ pairs with $4$ (gap $1$), and $9$ is left alone — $2$ pairs. Note the greedy does *not* pair the two identical $3$s; doing so would still give $2$ pairs here, but the sweep's choice is what the proof covers.

Note there is **no $T$**: the first line holds $N$ and $D$, then $N$ lengths follow one per line. $D$ may be $0$, in which case only exactly equal sticks pair.

## Solution

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    # No test-case count: first line is N and D.
    n, d = int(data[0]), int(data[1])
    lengths = sorted(int(v) for v in data[2:2 + n])
    pairs = 0
    i = 0
    while i + 1 < n:
        # Smallest remaining stick pairs with its nearest neighbour or not at all.
        if lengths[i + 1] - lengths[i] <= d:
            pairs += 1
            i += 2
        else:
            i += 1
    print(pairs)


main()
```

## Edge cases

- **No test-case count**: the first line holds $N$ and $D$ together, then $N$ lines of lengths — reading a leading $T$ consumes the first stick.
- **The smallest remaining stick pairs with its nearest neighbour or not at all.** Any stick it could pair with is at least as far away as its immediate successor, so pairing it with the successor never forecloses a better option — the exchange argument behind the greedy.
- **$D = 0$**: only exactly equal lengths pair, which still works — the two $3$s in the sample would pair at $D = 0$.
- **An unpairable stick advances the index by one, not two**, so the next stick keeps its chance: with $D = 2$ on $1, 9, 10$, skipping the $1$ lets $9$ and $10$ pair.
- **$N = 1$**: the loop never runs and the answer is $0$.
- **Odd $N$** always leaves at least one stick over, which falls out of the two-step walk without a special case.
- Lengths and $D$ up to $10^9$; differences stay well inside the integer range.

## Dry run

$N = 5$, $D = 2$, lengths $1, 3, 3, 9, 4$ sorted to $1, 3, 3, 4, 9$.

| $i$ | pair considered | difference | $\leq D$? | pairs | next $i$ |
|---:|---|---:|:---:|---:|---:|
| 0 | $1, 3$ | 2 | yes | 1 | 2 |
| 2 | $3, 4$ | 1 | yes | 2 | 4 |
| 4 | — | — | — | 2 | stop |

The $9$ is left unpaired. Output `2`.

---

Same problem grouped by topic: [../docs/greedy/TACHSTCK.md](../docs/greedy/TACHSTCK.md)
