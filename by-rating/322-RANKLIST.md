# 322. Let us play with rank list

> [`RANKLIST`](https://www.codechef.com/problems/RANKLIST) &middot; difficulty **1543** &middot; time limit **1s** &middot; 1400 to 1600 difficulty problems (Level 2)

## Topic used

| | |
|---|---|
| **Topic** | Greedy |
| **Technique** | How much deficit a given number of edits can absorb |
| **CodeChef tags** | `Algorithms`, `Constructive`, `Greedy`, `ad-hoc`, `Observation` |
| **Complexity class** | Square root $O(\sqrt{n})$ |
| **Time** | $O(\sqrt{S})$ per test case |
| **Space** | $O(1)$ |

## Question

A **rank list** is a list of ranks of persons in a programming contest. Note that some of the persons might be having same rank. {1, 2}, {1, 2, 2} and {1, 1, 2, 3, 4, 4} are few examples of rank lists whereas {1, 3}, {0, 2}, {1, 2, 4} are not rank lists.
Also note that a rank list need not to be sorted e.g. {2, 2, 1} and {3, 3, 2, 1} are valid rank lists.

Mathematically, a **rank list** is an array of numbers when sorted will have the starting element as 1 and difference between any two consecutive elements less than or equal to 1.

A rank list is said to be an **ideal rank list** if no two persons gets equal rank in it.

You can convert any rank list into an ideal rank list by applying following operations. In a single operation, you can change value of any one element of the rank list to any value.

Chandan now wonders about minimum number of operations needed to convert a rank list of size **n** with sum of its element equal to **s** in to an ideal rank list. Please help Chandan find this minimum number of operations needed to create an ideal rank list.

Note that you are guaranteed that values of **n, s** will be given in such a way that there will exist a valid rank list.

**Input**

First line of input will give an integer **T** denoting number of test cases.
Then for next **T** lines, each line will contain two space separated integers **n, s**.

**Output**

For each test case, print a single line containing a single integer corresponding to the answer of the problem.

**Constraints**

- **1** ≤ **T** ≤ **10**

- **1** ≤ **n** ≤ **10^5**

- **1** ≤ **s** ≤ **10^10**

## Constraints

- 1 ≤ T ≤ 10
- 1 ≤ n ≤ 10^5
- 1 ≤ s ≤ 10^10

## Sample

**Sample input**

```
4
1 1
3 6
3 5
3 3
```

**Sample output**

```
0
0
1
2
```

<details><summary>Explanation</summary>

**Example case 1.**
Only possible rank list in this case is {1}, As it is already an ideal rank list, hence you need zero operations.

**Example case 2.**
Only possible rank list in this case is {1 2 3}, As it is already an ideal rank list, hence you need zero operations.

**Example case 3.**
One of the possible rank list is {1 2 2}, You can convert it into an ideal rank list by changing any 2 to 3 i.e. {1, 2, 3}, hence you need one operations.

**Example case 4.**
Only possible rank list is {1 1 1}, You can convert it into an ideal rank list by changing a 1 to 2 and another 1 to 3 i.e. {1, 2, 3}, hence you need two operations.

</details>

## Approach

An ideal rank list is exactly $\{1, 2, \ldots, n\}$ with total $T = \frac{n(n+1)}{2}$. Any valid rank list has sum at most $T$, since sorted it satisfies $a_1 = 1$ and $a_{i+1} \leq a_i + 1$, forcing $a_i \leq i$. So the given list runs a **deficit**

$$D = T - s \geq 0$$

Now ask: with $k$ elements free to change, what is the largest deficit the *rest* of the list can carry while staying a valid rank list? Keeping the smallest $n-k$ values as $1, 2, \ldots, n-k$ and pushing the remaining $k$ as low as the rank-list rule allows — all equal to $n-k$ — gives a shortfall of

$$\sum_{j=n-k+1}^{n} j \;-\; k(n-k) \;=\; \frac{k(k+1)}{2}$$

Neatly, the $n$ cancels: **$k$ edits can absorb at most $\frac{k(k+1)}{2}$ of deficit**, whatever the list length. So the answer is the smallest $k$ with

$$\frac{k(k+1)}{2} \geq D$$

found by walking $k$ upward (or by inverting the triangular number).

Sample case 4, $n=3, s=3$, has $T = 6$ and $D = 3$: one edit absorbs only $1$, two absorb $3$, so the answer is $2$ — the list must have been $\{1,1,1\}$. Sample case 3, $D = 1$, needs a single edit. Sample cases 1 and 2 have $D = 0$ and need none.

With $s$ up to $10^{10}$, $T$ reaches about $5 \times 10^9$, so this is **64-bit** arithmetic outside Python; $k$ never exceeds about $10^5$.

## Solution

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        n, s = int(data[1 + 2 * i]), int(data[2 + 2 * i])
        deficit = n * (n + 1) // 2 - s
        # k edits can absorb at most k(k+1)/2 of deficit, independent of n.
        k = 0
        while k * (k + 1) // 2 < deficit:
            k += 1
        out.append(str(k))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Edge cases

- **The deficit is $n(n+1)/2 - s$**, and it is never negative: the ideal list has the largest possible sum for a rank list of size $n$, so $s$ can only fall short.
- **$k$ edits can raise the sum by at most $k(k+1)/2$**, independent of $n$ — the best possible is to lift $k$ chosen elements onto the $k$ largest missing ranks. So the answer is the smallest $k$ meeting the deficit.
- **Zero deficit** → $0$ edits, which the first two rows show ($n = 1, s = 1$ and $n = 3, s = 6$ are already ideal).
- **The bound is independent of which rank list the input came from**, which is why only $n$ and $s$ are given and no array is read.
- **Validity is guaranteed**, so the deficit always corresponds to a real rank list and no infeasible case arises.
- **The loop runs $O(\sqrt{S})$ times** at most, around $1.4 \times 10^5$ for $s$ near $10^{10}$ — cheap at $T \leq 10$, though the quadratic formula would also serve.

## Dry run

| $n$ | $s$ | ideal sum | deficit | smallest $k$ with $k(k+1)/2 \geq$ deficit | output |
|---:|---:|---:|---:|---|---:|
| 1 | 1 | 1 | 0 | $k = 0$ | `0` |
| 3 | 6 | 6 | 0 | $k = 0$ | `0` |
| 3 | 5 | 6 | 1 | $k = 1$ (gain 1) | `1` |
| 3 | 3 | 6 | 3 | $k = 2$ (gain 3) | `2` |

The last row starts from $\{1,1,1\}$; changing two elements to $2$ and $3$ gives the ideal list.

---

Same problem grouped by topic: [../docs/greedy/RANKLIST.md](../docs/greedy/RANKLIST.md)
