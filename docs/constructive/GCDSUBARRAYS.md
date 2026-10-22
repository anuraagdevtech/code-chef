[&larr; 267. Exactly N plus 1 Values](N1VALUES.md) &middot; [Index](../../README.md) &middot; [271. Palindrome Pain &rarr;](PALINPAIN.md)

# 268. Gcd of Subarrays

> CodeChef problem code [`GCDSUBARRAYS`](https://www.codechef.com/problems/GCDSUBARRAYS) &middot; difficulty **1498** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Constructive |
| **Technique** | Starting from the minimum and adding the slack |
| **Time** | $O(N)$ per test case |
| **Space** | $O(N)$ |
| **Roadmap course** | 1400 to 1600 difficulty problems (Level 2) |

## Question

You are given positive integers $N$ and $K$.

You have to construct an array $A$ of length $N$ such that :
- $1 \leq A_i \leq 10^{18}$
- $\sum_{i=1}^{N} \sum_{j=i}^{N} F(i,j) = K$, where $F(i,j)$ denotes the [gcd](https://en.wikipedia.org/wiki/Greatest_common_divisor) of all elements of the subarray $A[i, j]$.

If multiple such arrays exist, print any.
Report $-1$ if no such array exists.

Note that $A[l, r]$ denotes the subarray $[A_l ,A_{l+1}, \ldots, A_{r-1}, A_r]$.

**Input**

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of single line of input.
    - The only line of each test case contains two space-separated integers $N$ and $K$ — the number of elements and required sum.

**Output**

For each test case, output on a new line $N$ space-separated integers, denoting array $A$.
Report $-1$ if no such array exists.

## Constraints

- $1 \leq T \leq 100$
- $1 \leq N \leq 100$
- $1 \leq K \leq 10^{18}$
- The sum of $N$ over all test cases won't exceed $1000$.

## Sample

**Sample input**

```
3
1 5
2 4
3 1
```

**Sample output**

```
5
1 2
-1
```

<details><summary>Explanation</summary>

**Test case $1$:** The only possible array of size $1$ such that the sum of gcd of all subarrays is $5$ is $A = [5]$.

**Test case $2$:** Consider an array of size $2$ as $A = [1, 2]$. The subarrays of the array are:
- $[1]$: The gcd of this subarray is $1$.
- $[1, 2]$: The gcd of this subarray is $gcd(1, 2) = 1$.
- $[2]$: The gcd of this subarray is $2$.

The sum of gcd of all subarrays is $1+1+2= 4$.

**Test case $3$:** It can be proven that there exists no subarray of size $3$ such that the sum of gcd of all subarrays of the array is $1$.

</details>

## Approach

Every subarray gcd is at least $1$, and there are $\binom{N+1}{2} = \frac{N(N+1)}{2}$ subarrays. So the **minimum achievable total** is

$$B = \frac{N(N+1)}{2}$$

reached by the all-ones array, where every gcd is exactly $1$. If $K < B$ the target is unreachable and the answer is $-1$.

When $K \geq B$, the slack $K - B$ has to be injected without disturbing anything else — and placing one large value at the end does exactly that. Take

$$A = [\underbrace{1, 1, \ldots, 1}_{N-1},\ x], \qquad x = K - B + 1$$

Only the single-element subarray $[x]$ has a gcd other than $1$: any subarray reaching further left includes a $1$, and $\gcd(1, \cdot) = 1$. So the total rises from $B$ by exactly $x - 1$, landing on $K$.

The isolating property of $1$ under gcd is what makes this clean — a large value anywhere else would still be fenced off by its neighbours, but putting it at the end makes the argument immediate.

The bound holds: $x = K - B + 1 \leq K \leq 10^{18}$, and $x \geq 1$ precisely when $K \geq B$.

Sample case 2 is a good check: $N = 2$ gives $B = 3$ and $x = 4 - 3 + 1 = 2$, so $A = [1, 2]$ with subarray gcds $1$, $2$ and $\gcd(1,2) = 1$, totalling $4$. Sample case 3 asks for $K = 1$ with $N = 3$, below the floor of $6$, so $-1$.

**Any valid array is accepted**, so this is judged by a checker.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        n, k = int(data[1 + 2 * i]), int(data[2 + 2 * i])
        base = n * (n + 1) // 2          # every gcd is at least 1
        if k < base:
            out.append("-1")
            continue
        # A 1 next to it forces every wider subarray back to gcd 1, so only
        # the singleton [x] carries the slack.
        x = k - base + 1
        out.append(" ".join(["1"] * (n - 1) + [str(x)]))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(N)$ per test case
- **Space:** $O(N)$

## Edge cases

- **$n(n+1)/2$ is the unavoidable floor**, since every one of the $n(n+1)/2$ subarrays has a gcd of at least $1$. If $K$ is below it, the answer is $-1$ — the third row needs $K \geq 6$ and has $K = 1$.
- **A neighbouring $1$ collapses every wider subarray.** Any subarray containing one of the $n-1$ ones has gcd exactly $1$, so the only subarray that can carry the slack is the singleton holding $x$ — which is what makes the arithmetic a single subtraction.
- **$n = 1$** has no ones at all, and the single element simply equals $K$ (the first row).
- **Exactly at the floor** ($K = n(n+1)/2$) gives $x = 1$, an array of all ones — valid, and the boundary is inclusive.
- **$x \leq 10^{18}$ holds automatically**, because $x = K - n(n+1)/2 + 1 \leq K \leq 10^{18}$.
- **$K$ up to $10^{18}$** demands exact integers, and the triangular number at $n = 100$ is only $5050$, so no overflow risk arises.

## Dry run

Second sample: $n = 2$, $K = 4$. Floor is $2 \cdot 3/2 = 3$, so $x = 4 - 3 + 1 = 2$ and $A = [1, 2]$.

| subarray | gcd |
|---|---:|
| $[1]$ | 1 |
| $[2]$ | **2** |
| $[1, 2]$ | 1 |

Total $1 + 2 + 1 = 4 = K$ ✓

> CodeChef tags: `Number Theory`

---

Same problem in rating order (#293 of 486): [../../by-rating/293-GCDSUBARRAYS.md](../../by-rating/293-GCDSUBARRAYS.md)
