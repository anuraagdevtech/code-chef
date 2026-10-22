[&larr; 319. Flip the String](319-FLIP.md) &middot; [Index](README.md) &middot; [321. Magic Rankings &rarr;](321-MGCRNK.md)

# 320. Javelin Qualification

> [`JAVELIN`](https://www.codechef.com/problems/JAVELIN) &middot; difficulty **1538** &middot; time limit **1s** &middot; Jump from 2* to 3* (Level 3)

## Topic used

| | |
|---|---|
| **Topic** | Sorting |
| **Technique** | Two-stage selection |
| **Complexity class** | Linearithmic $O(n \log n)$ |
| **Time** | $O(N \log N)$ per test case |
| **Space** | $O(N)$ |

## Question

There are $N$ players with IDs from $1$ to $N$, who are participating in the Javelin throw competition which has two rounds. The first is the qualification round, followed by the final round. The qualification round has gotten over, and you are given the longest distance that each of the $N$ players has thrown as $A_1, A_2, \ldots, A_N$. Now, the selection process for the final round happens in the following two steps:

1) If the longest throw of a player in the qualification round is greater than or equal to the qualification mark of $M$ cm, they qualify for the final round.

2) If after step $1$, less than $X$ players have qualified for the finals, the remaining spots are filled by players who have thrown the maximum distance among the players who have not qualified yet.

You are given the best throws of the $N$ players in the qualification round $A_1, A_2, \ldots, A_N$ and the integers $M$ and $X$. Print the list of the players who will qualify for the finals in increasing order of their IDs.

**Input**

- The first line of input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains three space-separated integers $N, M, X$.
- The second line of each test case contains $N$ space-separated integers $A_1, A_2, \dots, A_N$.

**Output**

- For each test case, print a single line containing $K + 1$ space-separated integers, where $K$ is the number of players qualified.
- First, print the integer $K$, then followed by a space, print $K$ space-separated integers $ID_1, ID_2, \dots, ID_K$ where $ID_i$ denotes the players' *ID* who qualified for the finals.
- You have to print the IDs of the qualified players in increasing order.

## Constraints

- $1 \leq T \leq 1000$
- $2 \leq X \leq N \leq 30$
- $5000 \leq A_i \leq 8000$
- $7000 \leq M \leq 8000$
- All $A_i$-s are distinct

## Sample

**Sample input**

```
3
3 8000 2
5000 5001 5002
3 5000 2
7999 7998 8000
4 6000 3
5999 5998 6000 6001
```

**Sample output**

```
2 2 3
3 1 2 3
3 1 3 4
```

<details><summary>Explanation</summary>

**Test Case $1$:** Since no player crosses the qualification mark, they are chosen based on the distance thrown. So player $3$ who has thrown the maximum distance gets selected followed by the player $2$. Now since we have got the required number of players, player $1$ isn't selected.

**Test Case $2$:** Since all the players cross the qualification mark, they all are selected.

**Test Case $3$:** The player $3$ and player $4$ cross the qualification mark. So for the third and final spot in the final, the player $1$ is selected since he has the maximum distance thrown amongst the remaining two players.

</details>

## Approach

The selection runs in two passes, and they must be applied **in order**.

**Stage 1** admits everyone whose throw reaches the qualifying mark: $A_i \geq M$. This is a threshold, not a ranking — any number of players may clear it, possibly more than $X$.

**Stage 2** only fires if stage 1 produced **fewer than $X$** qualifiers. It then tops up the field with the longest throws among those *not already in*, until $X$ players are selected.

Two things are easy to get wrong. The top-up draws only from the **non-qualifiers**, so a player already admitted is not reconsidered. And stage 2 never *removes* anyone — if stage 1 already yielded more than $X$ players, they all stay and the final count exceeds $X$.

Sample case 2 is exactly that overflow: the mark is a lenient $5000$, all three players clear it, and the answer lists three even though $X = 2$.

Sample case 1 is the opposite extreme: nobody reaches $8000$, so stage 1 is empty and the two longest throws fill both spots.

Sample case 3 mixes them: two players clear $6000$, and one more is drawn from the remainder — the $5999$, not the $5998$.

Output is the count followed by the IDs **in increasing order**, so the selected set is sorted by ID at the end even though the top-up ranked by distance. The guarantee that all $A_i$ are distinct means that ranking has no ties to break.

## Solution

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n, m, x = int(data[pos]), int(data[pos + 1]), int(data[pos + 2])
        a = [int(v) for v in data[pos + 3:pos + 3 + n]]
        pos += 3 + n
        qualified = {i + 1 for i, v in enumerate(a) if v >= m}
        if len(qualified) < x:
            # Top up from the non-qualifiers only, longest throws first.
            rest = sorted(((v, i + 1) for i, v in enumerate(a)
                           if i + 1 not in qualified), reverse=True)
            for _, pid in rest[:x - len(qualified)]:
                qualified.add(pid)
        ids = sorted(qualified)
        out.append(" ".join(map(str, [len(ids)] + ids)))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Edge cases

- **More than $X$ may qualify on merit, and all of them advance.** The second row has three players past the mark with $X = 2$, and the answer sends all three — the top-up is a floor, not a cap.
- **Top-ups come only from the non-qualifiers**, longest throws first, which is why the already-qualified ids must be excluded from the candidate sort.
- **The qualifying mark is inclusive.** The third row's throw of exactly $6000$ cm meets $M = 6000$ and qualifies outright.
- **All $A_i$ are distinct**, so the top-up order is unambiguous and no tie-break at the cut is needed.
- **Nobody may qualify at all** (the first row, with $M = 8000$ against throws near $5000$), in which case the whole field of $X$ comes from the top-up.
- **The output is the count followed by the sorted ids**, so the set must be sorted at the end regardless of the order it was assembled in.
- **$X \leq N$ is guaranteed**, so the top-up never runs out of candidates.

## Dry run

Third sample: $N = 4$, $M = 6000$, $X = 3$, throws $5999, 5998, 6000, 6001$.

| id | throw | $\geq M$? |
|---:|---:|:---:|
| 1 | 5999 | no |
| 2 | 5998 | no |
| 3 | 6000 | **yes** |
| 4 | 6001 | **yes** |

Two qualified, one short of $X = 3$. The best non-qualifier is id $1$ at $5999$, so it is added.

Output `3 1 3 4`.

---

Same problem grouped by topic: [../docs/sorting/JAVELIN.md](../docs/sorting/JAVELIN.md)
