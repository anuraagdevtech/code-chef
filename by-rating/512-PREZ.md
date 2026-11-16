[&larr; 511. Chef and Hamming Distance of arrays](511-CHEFHAM.md) &middot; [Index](README.md) &middot; [513. Server Trouble &rarr;](513-SVRT.md)

# 512. Prefix Zeros

> [`PREZ`](https://www.codechef.com/problems/PREZ) &middot; difficulty **1790** &middot; time limit **8s** &middot; 1600 to 1800 difficulty problems (Level 3)

## Topic used

| | |
|---|---|
| **Topic** | Greedy |
| **Technique** | Maintain the exact cost of zeroing each prefix |
| **CodeChef tags** | `Algorithms`, `Greedy` |
| **Complexity class** | Linear $O(n)$ |
| **Time** | $O(N)$ per test case |
| **Space** | $O(1)$ |

## Question

You are given a string $S$ of length $N$, which consists of digits from $0$ to $9$. You can apply the following operation to the string:

- Choose an integer $L$ with $1\le L \le N$ and apply $S_i = (S_i + 1) \mod 10$ for each $1 \le i \le L$.

For example, if $S=39590$, then choosing $L=3$ and applying the operation yields the string $S=\underline{406}90$.

The prefix of string $S$ of length $l\;(1 \leq l \leq \mid S \mid )$ is string $S_1 S_2 \dots S_l$. A prefix of length $l$ is called good if $S_1=0, S_2=0, \dots, S_l=0$. Find the length of the **longest good prefix** that can be obtained in string $S$ by applying the given operation maximum $K$ times.

**Input**

- The first line of input contains an integer $T$, denoting the number of test cases. The $T$ test cases then follow:
- The first line of each test case contains two space-separated integers $N, K$.
- The second line of each test case contains the string $S$.

**Output**

For each test case, output in a single line the length of the longest good prefix that can be obtained in string $S$ by applying the given operation maximum $K$ times.

## Constraints

- $1 \leq T \leq 10^5$
- $1 \leq N \leq 10^5$
- $0 \leq K \leq 10^9$
- $\mid S \mid = N$
- $S$ contains digits from $0$ to $9$
- Sum of $N$ over all test cases does not exceed $3 \cdot 10^5$.

**Subtasks**

- **Subtask 1 (100 points):** Original constraints

## Sample

**Sample input**

```
6
3 5
380
3 9
380
4 2
0123
5 13
78712
6 10
051827
8 25
37159725
```

**Sample output**

```
0
3
1
3
2
5
```

<details><summary>Explanation</summary>

**Test case $1$:** There is no way to obtain zeros on the prefix of the string $S = 380$ by applying the given operation maximum $5$ times.

**Test case $2$:** The optimal strategy is: choose $L = 2$ and apply the operation twice, resulting in $S=500$, then choose $L = 1$ and apply the operation $5$ times, resulting in $S=000$.

**Test case $4$:** One of the possible sequence of operations is the following:
- Choose $L = 5$ and apply the operation thrice, resulting in $S=01045$.
- Choose $L = 2$ and apply the operation $9$ times, resulting in $S=90045$.
- Choose $L = 1$ and apply the operation once, resulting in $S=00045$.

</details>

## Approach

For a prefix ending with digit $d$, let $r=(-d)\bmod10$ be its required number of increments modulo ten. Reading right to left, consecutive required residues determine the least nonnegative number of operations ending at each boundary.

When extending a prefix, replace its old last-position cost `previous` by the new last-position cost `required`, and add `(previous-required) % 10` for the new internal boundary. This updates the exact minimum cost in constant time. Prefix feasibility is monotone, since making a longer prefix zero also makes every shorter prefix zero.

## Solution

```python
import sys


def main() -> None:
    tokens = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(tokens))):
        n, budget = int(next(tokens)), int(next(tokens))
        s = next(tokens)
        cost = previous = answer = 0
        for i, digit in enumerate(s):
            required = (48-digit)%10
            if i == 0:
                cost = required
            else:
                cost += required-previous+(previous-required)%10
            previous = required
            if cost <= budget:
                answer = i+1
        out.append(str(answer))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
```

## Edge cases

- Zero digits may still need operations if later digits change them.
- Costs can exceed ten because operations end at different boundaries.
- With $K=0$, only an already-zero prefix is feasible.

## Dry run

For `380`, required residues are `7,2,0`. Prefix costs are `7`, `7-7+2+5=7`, and `7-2+0+2=7`. Budget 5 reaches none; budget 9 reaches all three.

---

Same problem grouped by topic: [../docs/greedy/PREZ.md](../docs/greedy/PREZ.md)
