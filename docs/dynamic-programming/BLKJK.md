[&larr; 578. Chef and Pepperoni Pizza Again](PEPPERA.md) &middot; [Index](../../README.md) &middot; [580. Mean Mean Medians &rarr;](MEANMEDI.md)

# 579. Blackjack

> CodeChef problem code [`BLKJK`](https://www.codechef.com/problems/BLKJK) &middot; difficulty **2903** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Dynamic Programming |
| **Technique** | Earliest-prefix dominance and cardinality subset-sum bitsets |
| **Time** | $O((NC+NQ+CY)Y/w)$ word operations per test case for $C=\min(N,Y)$ and $Q$ an initial valid swap bound |
| **Space** | $O(NQY/w+NC/w)$ machine words |
| **Roadmap course** | Rise from 3* to 4* (Level 4) |

## Question

Chef is playing a card game called Blackjack. He starts with a deck of $N$ cards (numbered $1$ through $N$), where for each valid $i$, the $i$-th card has an integer $A_i$ written on it. Then he starts dealing the cards one by one in the order from card $1$ to card $N$. Chef wins if at some moment in time, the sum of all the cards dealt so far is between $X$ and $Y$ inclusive; if this never happens, Chef loses.

We want Chef to win the game, so without him noticing, we will swap some pairs of cards (possibly none) before the game starts. Find the smallest number of swaps we need so that Chef would win the game, or determine that it is impossible to make Chef win.

**Input**
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains three space-separated integers $N$, $X$ and $Y$.
- The second line contains $N$ space-separated integers $A_1, A_2, \ldots, A_N$.

**Output**
For each test case, print a single line containing one integer ― the smallest required number of swaps or $-1$ if Chef cannot win.

**Constraints**
- $1 \leq T \leq 100$
- $1 \leq N,X,Y \leq 10^3$
- $X \leq Y$
- $1 \leq A_i \leq 10^3$ for each valid $i$
- the sum of $N$ over all test cases does not exceed $10^4$

**Subtasks**
**Subtask #1 (22 points):** Chef can win if we make up to $2$ swaps

**Subtask #2 (34 points):**
- $1 \leq N,X,Y \leq 400$
- $1 \leq A_i \leq 400$ for each valid $i$
- the sum of $N$ over all test cases does not exceed $4,000$

**Subtask #3 (44 points):** original constraints

## Constraints

- $1 \leq T \leq 100$
- $1 \leq N,X,Y \leq 10^3$
- $X \leq Y$
- $1 \leq A_i \leq 10^3$ for each valid $i$
- the sum of $N$ over all test cases does not exceed $10^4$

## Sample

**Sample input**

```
3
3 4 5
1 2 3
3 3 4
1 2 3
2 20 30
40 10
```

**Sample output**

```
1
0
-1
```

<details><summary>Explanation</summary>

**Example case 1:** We can swap the last card with one of the first two cards.

**Example case 2:** No swaps are necessary, Chef wins after dealing the first two cards.

**Example case 3:** The order of the cards in the deck does not matter, Chef cannot win.

</details>

## Approach

A winning prefix selects some original cards. If it has length $k$, the required swaps are exactly the number of selected indices at least $k$: exchange those cards with the unselected positions inside the prefix.

First test the original prefixes, then ordinary subset reachability. If no sum in $[X,Y]$ is possible, return minus one. Otherwise reconstruct any winning subset to obtain a valid swap upper bound.

For each selection cardinality and sum, retain its earliest reachable prefix. If that prefix has length $i$ and selects $j$ cards, its exclusion count is $i-j$. Store its sum bit in a table indexed by prefix length and allowed exclusions, then make this table cumulative in both indices.

Sweep suffixes from right to left with exact-cardinality bitsets. A newly reachable suffix sum with $q$ selected cards can improve the answer when the earlier prefix table allows at most $q$ exclusions and some complementary sum in $[X-s,Y-s]$. Test that interval with a bitmask intersection. First occurrences suffice by earliest-prefix dominance; counts no better than the current upper bound are skipped.

See the [CodeChef editorial](https://discuss.codechef.com/t/blkjk-editorial/83432) for the dominance argument.

## Solution (Python)

```python
import sys


def main() -> None:
    tokens = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(tokens))):
        n,x,y = (int(next(tokens)) for _ in range(3))
        a = [int(next(tokens)) for _ in range(n)]
        total = 0
        already = False
        for value in a:
            total += value
            if x <= total <= y:
                already = True
        if already:
            out.append('0')
            continue
        mask = (1 << (y+1))-1
        history = [1]
        for value in a:
            history.append(history[-1]|((history[-1] << value)&mask))
        valid = history[-1]&(((1 << (y+1))-1)^((1 << x)-1))
        if not valid:
            out.append('-1')
            continue
        target = (valid&-valid).bit_length()-1
        selected = []
        for i in range(n-1,-1,-1):
            if not (history[i] >> target)&1:
                selected.append(i)
                target -= a[i]
        best = sum(i >= len(selected) for i in selected)
        if best <= 1:
            out.append(str(best))
            continue
        qmax = best-1
        count_limit = min(n,y)
        prefix = [[0]*(qmax+1) for _ in range(n+1)]
        prefix[0] = [1]*(qmax+1)
        reachable = [0]*(count_limit+1)
        reachable[0] = 1
        for length,value in enumerate(a,1):
            row = prefix[length]
            if value <= y:
                for count in range(min(length,count_limit),0,-1):
                    shifted = (reachable[count-1] << value)&mask
                    added = shifted&~reachable[count]
                    reachable[count] |= shifted
                    exclusions = length-count
                    if exclusions <= qmax:
                        row[exclusions] |= added
            previous = prefix[length-1]
            cumulative = 0
            for q in range(qmax+1):
                cumulative |= row[q]|previous[q]
                row[q] = cumulative
        suffix = [0]*(qmax+1)
        suffix[0] = 1
        for i in range(n-1,-1,-1):
            value = a[i]
            if value > y:
                continue
            for count in range(min(qmax,n-i,best-1),0,-1):
                shifted = (suffix[count-1] << value)&mask
                added = shifted&~suffix[count]
                suffix[count] |= shifted
                options = prefix[i][count]
                if not options:
                    continue
                while added:
                    bit = added&-added
                    s = bit.bit_length()-1
                    low,high = max(0,x-s),y-s
                    if high >= low and options&(((1 << (high+1))-1)^((1 << low)-1)):
                        best = count
                        break
                    added -= bit
            if best == 1:
                break
        out.append(str(best))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
```

## Complexity

- **Time:** $O((NC+NQ+CY)Y/w)$ word operations per test case for $C=\min(N,Y)$ and $Q$ an initial valid swap bound
- **Space:** $O(NQY/w+NC/w)$ machine words
- Auxiliary space excludes the buffered input and output.

## Edge cases

- A subset may exist even when the original prefix sums skip the target interval.
- Cards have positive values, so sums above $Y$ can be discarded.
- Maintain exact selection cardinalities during both sweeps.
- One exchange brings in one missing prefix card.

## Dry run

For `[1,2,3]` and interval `[4,5]`, original prefix sums are 1, 3, and 6. Select cards 1 and 3 for sum four; one selected index lies outside a length-two prefix, so one swap suffices.

> CodeChef tags: `Mathematics`, `Algorithms`, `Dynamic Programming`, `Knapsack`

---

Same problem in rating order (#713 of 735): [../../by-rating/713-BLKJK.md](../../by-rating/713-BLKJK.md)
