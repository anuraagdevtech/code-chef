[&larr; 227. Hotel Bytelandia](227-HOTEL.md) &middot; [Index](README.md) &middot; [229. Array Halves &rarr;](229-ARRHALVES.md)

# 228. Mighty Friend

> [`MTYFRI`](https://www.codechef.com/problems/MTYFRI) &middot; difficulty **1406** &middot; time limit **2.5s** &middot; 1400 to 1600 difficulty problems (Level 2)

## Topic used

| | |
|---|---|
| **Topic** | Greedy |
| **Technique** | Exchange the largest for the smallest |
| **CodeChef tags** | `Data Structures`, `Maps` |
| **Complexity class** | Linearithmic $O(n \log n)$ |
| **Time** | $O(N \log N)$ per test case |
| **Space** | $O(N)$ |

## Question

Motu and Tomu are very good friends who are always looking for new games to play against each other and ways to win these games. One day, they decided to play a new type of game with the following rules:
- The game is played on a sequence $A_0, A_1, \dots, A_{N-1}$.
- The players alternate turns; Motu plays first, since he's earlier in lexicographical order.
- Each player has a score. The initial scores of both players are $0$.
- On his turn, the current player has to pick the element of $A$ with the lowest index, add its value to his score and delete that element from the sequence $A$.
- At the end of the game (when $A$ is empty), Tomu wins if he has **strictly greater** score than Motu. Otherwise, Motu wins the game.

In other words, Motu starts by selecting $A_0$, adding it to his score and then deleting it; then, Tomu selects $A_1$, adds its value to his score and deletes it, and so on.

Motu and Tomu already chose a sequence $A$ for this game. However, since Tomu plays second, he is given a different advantage: before the game, he is allowed to perform at most $K$ swaps in $A$; afterwards, the two friends are going to play the game on this modified sequence.

Now, Tomu wants you to determine if it is possible to perform up to $K$ swaps in such a way that he can win this game.

**Input**
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains two space-separated integers $N$ and $K$ denoting the number of elements in the sequence and the maximum number of swaps Tomu can perform.
- The second line contains $N$ space-separated integers $A_0, A_1, \dots, A_{N-1}$.

**Output**
For each test case, print a single line containing the string `"YES"` if Tomu can win the game or `"NO"` otherwise (without quotes).

**Constraints**
- $1 \le T \le 100$
- $1 \le N \le 10,000$
- $0 \le K \le 10,000$
- $1 \le A_i \le 10,000$ for each valid $i$

**Subtasks**
**Subtask #1 (20 points):** $1 \le N \le 100$

**Subtask #2 (80 points):** original constraints

## Constraints

- $1 \le T \le 100$
- $1 \le N \le 10,000$
- $0 \le K \le 10,000$
- $1 \le A_i \le 10,000$ for each valid $i$

## Sample

**Sample input**

```
2
6 0
1 1 1 1 1 1
5 1
2 4 6 3 4
```

**Sample output**

```
NO
YES
```

<details><summary>Explanation</summary>

**Example case 1:** At the end of the game, both Motu and Tomu will have scores $1+1+1 = 3$. Tomu is unable to win that game, so the output is `"NO"`.

**Example case 2:** If no swaps were performed, Motu's score would be $2+6+4 = 12$ and Tomu's score would be $4+3 = 7$. However, Tomu can swap the elements $A_2 = 6$ and $A_3 = 3$, which makes Motu's score at the end of the game equal to $2+3+4 = 9$ and Tomu's score equal to $4+6 = 10$. Tomu managed to score higher than Motu, so the output is `"YES"`.

</details>

## Approach

Play proceeds strictly left to right, so Motu takes the even-indexed elements and Tomu the odd ones — the positions are fixed, and only *which values sit in them* can change.

A swap moves one value out of Motu's set and one into it. The useful kind trades one of **Motu's largest** for one of **Tomu's smallest**: if Motu holds $m$ and Tomu holds $u$ with $m > u$, swapping shifts the score gap by $2(m - u)$ in Tomu's favour — he gains $m - u$ and Motu loses the same.

So sort Motu's values descending and Tomu's ascending, then pair them off: the first swap trades Motu's biggest for Tomu's smallest, the second his next biggest for her next smallest, and so on for up to $K$ swaps. Stop early once $m \leq u$, because from there every remaining trade would shrink the gap rather than widen it.

The greedy is optimal because the swaps are independent — each takes one element from each side — and the gains $2(m_i - u_i)$ are sorted descending by construction, so taking the $K$ largest gains is best possible.

Swapping within one player's own set is pointless, since it changes neither total.

Sample case 1 has $K = 0$ and equal totals of $3$; Tomu needs **strictly** greater, so a tie is a loss — `NO`. Sample case 2 trades Motu's $6$ for Tomu's $3$, turning $12$–$7$ into $9$–$10$.

## Solution

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n, k = int(data[pos]), int(data[pos + 1])
        a = [int(v) for v in data[pos + 2:pos + 2 + n]]
        pos += 2 + n
        motu = sorted(a[0::2], reverse=True)       # Motu plays first
        tomu = sorted(a[1::2])
        ms, ts = sum(motu), sum(tomu)
        for i in range(min(k, len(motu), len(tomu))):
            # Trade Motu's biggest for Tomu's smallest while that still helps.
            if motu[i] <= tomu[i]:
                break
            ms += tomu[i] - motu[i]
            ts += motu[i] - tomu[i]
        out.append("YES" if ts > ms else "NO")
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Edge cases

- **Motu plays the odd-numbered rounds**, which is `a[0::2]` in 0-based indexing; getting the parity backwards exchanges the two sums and flips both sample answers.
- **$K = 0$** (the first row): no trades, so the raw sums decide — and they tie, which answers `NO`.
- **A strict win is required.** The first row's $3$ against $3$ is not enough for Tomu.
- **A useless trade must be refused.** The loop breaks once Motu's $i$-th largest is no greater than Tomu's $i$-th smallest, since swapping equal or already-favourable values cannot raise Tomu's total — forcing all $K$ trades can actively hurt.
- **Odd $N$ gives Motu one extra round**, so the trade count is bounded by `min(k, len(motu), len(tomu))`; the second row has three against two.
- **Each trade moves twice the difference between the totals**, which is why both sums are updated rather than just one.

## Dry run

Second sample: $A = 2, 4, 6, 3, 4$ with $K = 1$.

| | values | sorted for trading | sum |
|---|---|---|---:|
| Motu (rounds 1,3,5) | $2, 6, 4$ | $6, 4, 2$ descending | 12 |
| Tomu (rounds 2,4) | $4, 3$ | $3, 4$ ascending | 7 |

One trade swaps Motu's $6$ for Tomu's $3$:

| | before | after |
|---|---:|---:|
| Motu | 12 | 9 |
| Tomu | 7 | **10** |

$10 > 9$, so `YES`.

---

Same problem grouped by topic: [../docs/greedy/MTYFRI.md](../docs/greedy/MTYFRI.md)
