[&larr; 577. Coin Partition](COINPART.md) &middot; [Index](../../README.md) &middot; [579. Blackjack &rarr;](BLKJK.md)

# 578. Chef and Pepperoni Pizza Again

> CodeChef problem code [`PEPPERA`](https://www.codechef.com/problems/PEPPERA) &middot; difficulty **2516** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Dynamic Programming |
| **Technique** | Partition row imbalances and reconstruct the reversals |
| **Time** | $O(N^2+ND/w)$ word operations per test case for $D\le N^2/2$ total absolute imbalance |
| **Space** | $O(N^2+ND/w)$ machine words and stored row characters |
| **Roadmap course** | Rise from 3* to 4* (Level 4) |

## Question

Chef is fond of pepperoni pizza, as we saw [here](https://www.codechef.com/problems/PEPPERON). Once again, he has a pepperoni pizza in the shape of a grid with $N$ rows (numbered $1$ through $N$ from top to bottom) and $N$ columns (numbered $1$ through $N$ from left to right). Some cells of this grid contain pepperoni, while other ones do not.

Chef wants to cut the pizza vertically in half and give the two halves to two of his friends. Formally, one friend should get everything in columns $1$ through $N/2$ and the other friend should get everything in the columns $N/2+1$ through $N$.

Before cutting the pizza, Chef may perform the following operation any number of times (including zero): choose an integer $x$ ($1 \le x \le N$) and reverse the $x$-th row of the grid ― in other words, for each valid $i$, the cell in the $i$-th column and $x$-th row is moved to the $N+1-i$-th column in the same row.

After the pizza is cut, let's denote the number of cells containing pepperoni in the first half and in the second half by $p_1$ and $p_2$ respectively. Chef wants to minimise their absolute difference $|p_1-p_2|$, but he is lazy, so he just wants you to perform any valid sequence of operations such that the absolute difference in the final grid is minimized.

You need to find a final grid (the grid after performing all operations) such that $|p_1 - p_2|$ for this grid is the smallest possible. If there are multiple final grids that minimise $|p_1 - p_2|$, you may find any one.

**Input**
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains a single integer $N$.
- $N$ lines follow. For each $i$ ($1 \le i \le N$), the $i$-th of these lines contains a string with length $N$ describing the $i$-th row of the grid; for each valid $j$, the $j$-th character of this string is '1' if the cell in the $i$-th row and $j$-th column contains pepperoni or '0' if it does not.

**Output**
For each test case, print $N$ lines. For each valid $i$, the $i$-th of these lines should contain a string with length $N$ describing the $i$-th row of the grid after performing all operations, in the same format as on the input. It must be possible to obtain this grid from the initial grid using some valid sequence of operations.

**Constraints**
- $1 \le T \le 30$
- $2 \le N \le 150$
- $N$ is even
- the sum of $N$ over all test cases does not exceed $300$

## Constraints

- $1 \le T \le 30$
- $2 \le N \le 150$
- $N$ is even
- the sum of $N$ over all test cases does not exceed $300$

## Sample

**Sample input**

```
2
2
01
01
4
0111
0001
1010
1010
```

**Sample output**

```
10
01
1110
0001
1010
1010
```

<details><summary>Explanation</summary>

**Example case 1:** We need to reverse either of the rows, leading to $|p_1-p_2| = 0$. Either of these solutions would be accepted.

**Example case 2:** It is optimal to reverse the first row, leading to exactly $4$ pepperoni on each side (and $|p_1-p_2| = 0$ again).

</details>

## Approach

A row contributes the difference between its left-half and right-half pepperoni counts. Reversing it negates that contribution. Let $d_i$ be the absolute difference for each row. The problem is to choose signs minimising $|\sum \pm d_i|$, equivalent to subset sum as close as possible to half of $D=\sum d_i$.

Use a bitset to find reachable sums at most $D//2$. Retain the reachable bitset after each row. Reconstruct a maximum reachable sum backwards: skip a row when the previous bitset already reaches the current target, otherwise select it and reduce the target by its imbalance. Give those selected rows negative signs. Orient every row to realise its desired sign, preserving the row itself or reversing it.

## Solution (Python)

```python
import sys


def main() -> None:
    tokens = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(tokens))):
        n = int(next(tokens))
        rows = [next(tokens).decode() for _ in range(n)]
        difference = [row[:n//2].count('1')-row[n//2:].count('1') for row in rows]
        amounts = [abs(d) for d in difference]
        target = sum(amounts)//2
        mask = (1 << (target+1))-1
        reachable = 1
        history = [reachable]
        for value in amounts:
            reachable |= (reachable << value)&mask
            history.append(reachable)
        chosen = set()
        value = reachable.bit_length()-1
        for i in range(n-1,-1,-1):
            if not (history[i] >> value)&1:
                chosen.add(i)
                value -= amounts[i]
        for i,row in enumerate(rows):
            desired = -amounts[i] if i in chosen else amounts[i]
            out.append(row if difference[i] == desired else row[::-1])
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
```

## Complexity

- **Time:** $O(N^2+ND/w)$ word operations per test case for $D\le N^2/2$ total absolute imbalance
- **Space:** $O(N^2+ND/w)$ machine words and stored row characters
- Auxiliary space excludes the buffered input and output.

## Edge cases

- Rows with equal half counts need no change.
- Reverse whole rows only; do not exchange characters arbitrarily.
- If exact balance is impossible, the nearest reachable half is optimal.

## Dry run

For two rows `01`, each absolute imbalance is one. Select one row for the negative contribution and orient the other positively, yielding `10` and `01` with zero total difference.

---

Same problem in rating order (#702 of 735): [../../by-rating/702-PEPPERA.md](../../by-rating/702-PEPPERA.md)
