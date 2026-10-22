# 408. Range Assign, Number of Distinct Elements Minimize

> CodeChef problem code [`RANGEASSIGN`](https://www.codechef.com/problems/RANGEASSIGN) &middot; difficulty **1648** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Conditionals & Case Work |
| **Technique** | Fixed endpoints bound what the operation can reach |
| **Time** | $O(N)$ per test case |
| **Space** | $O(1)$ |
| **Roadmap course** | 1600 to 1800 difficulty problems (Level 3) |

## Question

You are given an array $A$ of $N$ **positive** integers.

In one operation, you can do the following:
- Choose integers $i$ and $j$ $(1 \le i < j \le N)$, such that $A_i = A_j$;
- For all $k$ $(i < k < j)$, change the value of $A_k$ to $A_i$.

Find out whether $A$ can have **at most $2$ distinct** values after using **any** (possibly zero) number of operations.

**Input**

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of two lines of input:
    - The first line of each test case contains $N$ - the size of the array.
    - The next line contains $N$ integers, $A_1, A_2, A_3, \ldots, A_N$ - the elements of the array.

**Output**

For each test case, print `YES` if $A$ can have **at most $2$ distinct** values after using **any** (possibly zero) number of operations and `NO` otherwise.

You may print each character of the string in uppercase or lowercase (for example, the strings `YES`, `yEs`, `yes`, and `yeS` will all be treated as identical).

## Constraints

- $1 \leq T \leq 1000$
- $1 \leq N \leq 10^5$
- $1 \leq A_i \leq 10^9$
- The sum of $N$ over all test cases won't exceed $10^5$.

## Sample

**Sample input**

```
4
5
5 9 5 5 5
3
1 2 3
4
1 2 1 3
4
1 2 3 1
```

**Sample output**

```
YES
NO
YES
YES
```

<details><summary>Explanation</summary>

**Test case $1$:** The array $A$ already has $2$ distinct elements.

**Test case $2$:** It is impossible to make operations such that $A$ has $2$ distinct elements.

**Test case $3$:** We can make an operation as:
- Choose $i = 1$ and $j = 3$. Thus, we change $A_2$ to $A_1 = 1$.

The final array is $[1,1,1,3]$ which has two distinct elements.

**Test case $4$:** We can make an operation as:
- Choose $i = 1$ and $j = 4$. Thus, we change $A_2$ and $A_3$ to $A_1 = 1$.

The final array is $[1,1,1,1]$ which has one distinct element.

</details>

## Approach

The operation only rewrites indices **strictly between** $i$ and $j$, so $A_1$ and $A_N$ can never change. Everything follows from that.

**If $A_1 = A_N$**, applying the operation to the pair $(1, N)$ overwrites the entire interior, leaving one distinct value. Always `YES`.

**If $A_1 \neq A_N$**, the final array already contains two distinct values, so *every* element must end up equal to $A_1$ or $A_N$. The best reach is:

- let $p$ be the **last** index with $A_p = A_1$; the operation $(1, p)$ makes $A_1 \ldots A_p$ all $A_1$;
- let $q$ be the **first** index with $A_q = A_N$; the operation $(q, N)$ makes $A_q \ldots A_N$ all $A_N$.

Those two sweeps are the furthest either value can spread, because an operation needs a matching pair of endpoints and no copy of $A_1$ lies beyond $p$, nor of $A_N$ before $q$. So the answer is `YES` exactly when the two ranges leave no gap:

$$q \leq p + 1$$

Anything stranded in $(p, q)$ is doomed: by definition it equals neither $A_1$ nor $A_N$, and flattening it with some inner pair would only install a *third* value.

The samples show each branch. $[5,9,5,5,5]$ has equal ends, so one operation flattens it. $[1,2,1,3]$ has $p = 3$ and $q = 4$, touching exactly, so the $2$ is absorbed. $[1,2,3,1]$ again has equal ends. And $[1,2,3]$ has $p = 1$, $q = 3$, leaving the $2$ unreachable — there is no matching pair anywhere, so nothing can be done at all.

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
        a = data[pos + 1:pos + 1 + n]
        pos += 1 + n
        if a[0] == a[-1]:
            out.append("YES")                 # one sweep flattens everything
            continue
        # The two values can spread no further than their outermost copies.
        last_first = max(i for i in range(n) if a[i] == a[0])
        first_last = min(i for i in range(n) if a[i] == a[-1])
        out.append("YES" if first_last <= last_first + 1 else "NO")
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(N)$ per test case
- **Space:** $O(1)$

## Edge cases

- **The first and last elements can never change.** An operation only rewrites indices strictly between $i$ and $j$, so $A_1$ and $A_N$ survive everything — which both bounds the answer and drives the whole case split.
- **If $A_1 = A_N$ one operation flattens the array** to a single value, so the answer is `YES` regardless of what lies between (the first and fourth rows).
- **Otherwise both $A_1$ and $A_N$ must remain, so the target is exactly two values** — and each can spread only as far as its own outermost copy: $A_1$ rightward to its last occurrence, $A_N$ leftward to its first.
- **The two spreads must meet or touch**, hence $\text{first occurrence of } A_N \leq \text{last occurrence of } A_1 + 1$. A gap between them leaves a third value stranded.
- **No equal pair at all** means no operation is possible (the second row, $1,2,3$), and three distinct values remain.
- **Touching exactly** (the third row, where the spreads are adjacent at indices $2$ and $3$) is enough, which is why the bound is non-strict with the $+1$.
- **Values are compared as raw byte tokens**, safe since the input has no leading zeros.

## Dry run

Third sample: $A = 1, 2, 1, 3$.

| quantity | value |
|---|---:|
| last index holding $A_1 = 1$ | 3 (1-based) |
| first index holding $A_N = 3$ | 4 |
| is $4 \leq 3 + 1$? | yes |

Output `YES`: one operation on the two $1$s at indices $1$ and $3$ gives $1, 1, 1, 3$ — two distinct values.

> CodeChef tags: `Special`, `Algorithms`

---

Same problem in rating order (#380 of 486): [../../by-rating/380-RANGEASSIGN.md](../../by-rating/380-RANGEASSIGN.md)
