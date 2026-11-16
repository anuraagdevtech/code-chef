[&larr; 643. Parity Permutation](PARPER.md) &middot; [Index](../../README.md) &middot; [666. Sum of Goodness &rarr;](SEQGOODNESS.md)

# 661. SUM OR

> CodeChef problem code [`AWESUM_OR`](https://www.codechef.com/problems/AWESUM_OR) &middot; difficulty **2152** &middot; time limit **1.5s**

| | |
|---|---|
| **Topic** | Combinatorics |
| **Technique** | No carries - distribute the set bits of N among three non-empty owners |
| **Time** | $O(\log N)$ per test case |
| **Space** | $O(1)$ |
| **Roadmap course** | 2000 to 2500 difficulty problems (Level 5) |

## Question

You are given a positive integer $N$.
Find the number of triples $(X, Y, Z)$ such that:
- $0\lt X, Y, Z \lt N$;
- $X+Y+Z=N$;
- $X$ $|$ $Y$ $|$ $Z=N,$ where $|$ represents the [bitwise OR operation](https://en.wikipedia.org/wiki/Bitwise_operation#OR).

Since the number of triples can be huge, print them modulo $10^9+7$.

**Input**

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of a single integer $N$, as mentioned in the statement.

**Output**

For each test case, output on a new line, the number of triples satisfying the condition, modulo $10^9 + 7$.

## Constraints

- $1 \leq T \leq 10^5$
- $1 \le N \lt 2^{60}$

## Sample

**Sample input**

```
2
3
7
```

**Sample output**

```
0
6
```

<details><summary>Explanation</summary>

**Test case $1$:** There are no triples $(X, Y, Z)$ satisfying the given conditions.

**Test case $2$:** The following $6$ tuples satisfy the conditions: $\{(1, 2, 4), (1, 4, 2), (2, 1, 4), (2, 4, 1), (4, 1, 2), (4, 2, 1)\}$.

For example, in the tuple $(1, 2, 4)$, $1+2+4 = 7$ and $1$ $|$ $2$ $|$ $4 = 7$.

</details>

## Approach

For non-negative integers, $X + Y + Z \ge X \mid Y \mid Z$, with equality exactly when no bit is set in more than one of the three numbers. Both expressions must equal $N$, so the three numbers have pairwise disjoint bits and together use exactly the set bits of $N$.

So a triple is an assignment of each of the $p = \text{popcount}(N)$ set bits to one of $X, Y, Z$: $3^p$ assignments. All three numbers must be positive, i.e. each must receive at least one bit; by inclusion-exclusion the number of surjective assignments is

$$3^p - 3 \cdot 2^p + 3.$$

The upper bounds $X, Y, Z < N$ follow automatically once all three are positive.

## Solution (Python)

```python
import sys


def main() -> None:
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    out = []
    MOD = 10 ** 9 + 7
    for _ in range(next(tokens)):
        bits = next(tokens).bit_count()
        out.append(str((pow(3, bits, MOD) - 3 * pow(2, bits, MOD) + 3) % MOD))
    print('\n'.join(out))


if __name__ == "__main__":
    main()
```

## Complexity

- **Time:** $O(\log N)$ per test case
- **Space:** $O(1)$
- Auxiliary space excludes the buffered input and output.

## Edge cases

- Fewer than three set bits: the formula gives 0 for $p = 1$ and $p = 2$.
- The triples are ordered, which the assignment count respects.
- The subtraction must be reduced to a non-negative residue modulo $10^9 + 7$.
- $N < 2^{60}$, so the popcount is at most 60.

## Dry run

`N = 7 = 111_2`, $p = 3$: $27 - 24 + 3 = 6$ - the six orderings of $(1, 2, 4)$.

`N = 3 = 11_2`, $p = 2$: $9 - 12 + 3 = 0$.

> CodeChef tags: `Special`, `Mathematics`

---

Same problem in rating order (#621 of 735): [../../by-rating/621-AWESUM_OR.md](../../by-rating/621-AWESUM_OR.md)
