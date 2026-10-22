# 467. Maximum Value

> CodeChef problem code [`MVALUE`](https://www.codechef.com/problems/MVALUE) &middot; difficulty **1738** &middot; time limit **0.5s**

| | |
|---|---|
| **Topic** | Basic Math |
| **Technique** | Factoring the expression, then checking the extremes |
| **Time** | $O(N \log N)$ per test case |
| **Space** | $O(N)$ |
| **Roadmap course** | 1600 to 1800 difficulty problems (Level 3) |

## Question

Given an array $A$ of size $N$. Find the maximum value of the expression $a * b + a - b$ where $a$ and $b$ are $2$ distinct elements of the array.

**Input:**
- First line will contain $T$, number of testcases. Then the testcases follow.
- Each testcase contains of two lines of input.
- First line will contain $N$, number of elements of the array.
- Second line contains $N$ space separated integers, elements of the array $A$.

**Output:**
For each testcase, output in a single line answer to the problem.

**Constraints**
- $1 \leq T \leq 20$
- $2 \leq N \leq 10^5$
- $-10^9 \leq A_i \leq 10^9$

## Constraints

- $1 \leq T \leq 20$
- $2 \leq N \leq 10^5$
- $-10^9 \leq A_i \leq 10^9$

## Sample

**Sample input**

```
2
2   
2 2
3
5 3 2
```

**Sample output**

```
4
17
```

<details><summary>Explanation</summary>

**Case 1:** Only possible pair is $[2, 2]$ for which answer = $2 * 2 + 2 - 2$ = $4$.

**Case 2:** There are six possible pairs.

For pairs $[2, 3]$ and $[3, 2]$, answer = $2 * 3 + max(2 - 3, 3 - 2)$ = $7$

For pairs $[3, 5]$ and $[5, 3]$ answer = $5 * 3 + max(3 - 5, 5 - 3)$ = $17$ and

For the pairs $[2, 5]$ and $[5, 2]$, answer = $2 * 5 + max(2 - 5, 5 - 2)$ = $13$.

So final answer is maximum of $\{7, 17, 13\}$ = $17$.

</details>

## Approach

The expression factors:

$$ab + a - b = (a-1)(b+1) + 1$$

so maximising it means maximising a **product of two shifted elements**, with $a$ and $b$ taken from distinct positions. That asymmetry matters — $a$ is shifted down and $b$ up — so the pair is ordered and both orders must be tried.

A product of two terms is largest when both factors are large positive or both are large negative, so the optimum uses only the array's extremes: $a$ wants either the maximum (to make $a-1$ big) or the minimum (to make $a-1$ very negative), and the same for $b$. Taking the three smallest and three largest entries of the sorted array and trying every ordered pair among them therefore suffices, in constant time after the sort — and taking three of each leaves room for the ties and duplicates that a two-of-each window could mishandle.

$$\text{answer} = 1 + \max_{i \neq j} (A_i - 1)(A_j + 1)$$

Note values can be negative, so the answer can be too, and the product reaches $10^{18}$ — `long long` territory in C++, free in Python.

The second sample shows the ordering effect: with $[5,3,2]$ the best is $a = 5$, $b = 3$ giving $4 \cdot 4 + 1 = 17$, while swapping them gives only $2 \cdot 6 + 1 = 13$. The first sample, $[2,2]$, uses the two equal elements at distinct positions for $1 \cdot 3 + 1 = 4$ — the values may repeat as long as the positions differ.

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
        a = sorted(int(x) for x in data[pos + 1:pos + 1 + n])
        pos += 1 + n
        # A product peaks at the extremes, so only the ends can matter.
        edge = sorted(set(list(range(min(3, n))) + list(range(max(0, n - 3), n))))
        best = None
        for i in edge:
            for j in edge:
                if i == j:
                    continue
                val = (a[i] - 1) * (a[j] + 1) + 1
                if best is None or val > best:
                    best = val
        out.append(str(best))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(N \log N)$ per test case
- **Space:** $O(N)$

## Edge cases

- **The expression factors**: $ab + a - b = (a-1)(b+1) + 1$, which turns the search into maximising a product and makes the extremes the only candidates.
- **It is not symmetric**, so both orderings of a pair must be tried — on $5, 3, 2$ the best is $a = 5$ with $b = 3$ giving $17$, while swapping them gives $13$.
- **Negative values matter.** With $A_i$ down to $-10^9$, two large negatives can multiply to a large positive, so the smallest few elements are candidates alongside the largest few.
- **Three from each end is enough**, since $(a-1)$ and $(b+1)$ are each monotone in their argument and the two indices must differ — a margin of three covers every tie and exclusion.
- **The two elements must be distinct positions**, which the `i == j` guard enforces; distinct *values* are not required.
- **$N = 2$** leaves exactly two ordered pairs, both of which the window covers.
- **Products reach $10^{18}$**, past 32-bit and at the edge of 64-bit, though exact in Python.

## Dry run

Second sample: $A = 5, 3, 2$, sorted to $2, 3, 5$.

| $a$ | $b$ | $(a-1)(b+1) + 1$ |
|---:|---:|---:|
| 2 | 3 | $1 \cdot 4 + 1 = 5$ |
| 2 | 5 | $1 \cdot 6 + 1 = 7$ |
| 3 | 2 | $2 \cdot 3 + 1 = 7$ |
| 3 | 5 | $2 \cdot 6 + 1 = 13$ |
| 5 | 2 | $4 \cdot 3 + 1 = 13$ |
| 5 | 3 | $4 \cdot 4 + 1 = $ **17** |

Output `17`.

> CodeChef tags: `Mathematics`, `Algorithms`, `Constructive`

---

Same problem in rating order (#439 of 486): [../../by-rating/439-MVALUE.md](../../by-rating/439-MVALUE.md)
