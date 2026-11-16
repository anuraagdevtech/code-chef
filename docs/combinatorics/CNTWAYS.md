[&larr; 617. Gifts at Olympics](OLYMPIC.md) &middot; [Index](../../README.md) &middot; [619. Adi and the Matrix &rarr;](ADIMAT.md)

# 618. The Uncountable Ways

> CodeChef problem code [`CNTWAYS`](https://www.codechef.com/problems/CNTWAYS) &middot; difficulty **1992** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Combinatorics |
| **Technique** | Lattice paths split at the unique step that passes below the cut-out corner |
| **Time** | $O(\max(N + M) + \sum N)$ |
| **Space** | $O(\max(N + M))$ |
| **Roadmap course** | Rise from 3* to 4* (Level 4) |

## Question

Little Chef loves mathematics.Every day, he solves some mathematical problems to improve his skill.

A few days ago, he found a popular problem about turtles. The problem is as follows. Little Chef is given **R** rectangles, numbered 1 through **R**. The width and height of the **i**-th rectangle are **N_i** and **M_i** unit respectively. There is a turtle located on the top-left corner of each rectangle. For each rectangle, count the number of ways the turtle can reach the bottom-right corner, if each turtle can only move right or down 1 unit at any time.The turtle is not allowed to move outside the rectangle, but, of course, the turtle can move on the boundary of the rectangle.

In less than one second, this problem was solved for all rectangles.He felt that the problem was too easy. This morning, Little Chef wanted more challenges. Thus, for each rectangle **i**, he cut and removed a rectangle of **A_i** × **B_i** unit from the top-right corner. See the following figure for detail.

<img src="https://codechef.com/download/CNTWAYS1.png" width="280" height="85" alt="CNTWAYS1.png" />
He could not solve this new version of the problem easily. Help him count the number of ways each turtle can reach the bottom-right corner using the same rule as before.

**Input**

The first line of the input contains a single integer **R**. The description of **R** rectangles follows. Each description consists of a single line containing four space-separated integers **N_i**, **M_i**, **A_i**, and **B_i**.

**Output**

For each rectangle, output a single line containing the number of ways, modulo 1,000,000,007.

**Constraints**

1 ≤ **R** ≤ 10
 2 ≤ **N_i**, **M_i** ≤ 400,000
1 ≤ **A_i** < **N_i**
1 ≤ **B_i** < **M_i**

## Constraints

1 ≤ R ≤ 10
 2 ≤ N_i, M_i ≤ 400,000
1 ≤ A_i < N_i
1 ≤ B_i < M_i

## Sample

**Sample input**

```
1
2 2 1 1
```

**Sample output**

```
5
```

<details><summary>Explanation</summary>

In the sample case, there are 5 ways the turtle can reach the bottom right corner as follows:

<img src="https://codechef.com/download/CNTWAYS2.png" width="211" height="116" alt="CNTWAYS2.png" />

</details>

## Approach

The turtle walks from the top-left to the bottom-right corner of an $N \times M$ rectangle from which an $A \times B$ rectangle has been cut out of the top-right corner. It may walk along the boundary of the cut but not through its interior.

Every valid path goes down from height $B - 1$ to height $B$ exactly once, and it must do so at a horizontal position $x \le N - A$, i.e. to the left of the cut (or along its left edge). Classifying paths by that position $x$ counts each path once:

$$\text{answer} = \sum_{x=0}^{N-A} \binom{x + B - 1}{x} \cdot \binom{(N - x) + (M - B)}{N - x}.$$

The first factor counts the ways to reach $(x, B-1)$, the second the ways to finish from $(x, B)$, where nothing is in the way any more. Binomials come from factorial tables.

## Solution (Python)

```python
import sys


def main() -> None:
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    cases = [(next(tokens), next(tokens), next(tokens), next(tokens)) for _ in range(next(tokens))]
    MOD = 1000000007
    limit = max((n + m for n, m, a, b in cases), default=0)
    fact = [1] * (limit + 1)
    for i in range(1, limit + 1):
        fact[i] = fact[i - 1] * i % MOD
    inv_fact = [1] * (limit + 1)
    inv_fact[limit] = pow(fact[limit], MOD - 2, MOD)
    for i in range(limit, 0, -1):
        inv_fact[i - 1] = inv_fact[i] * i % MOD

    def choose(n, k):
        return fact[n] * inv_fact[k] % MOD * inv_fact[n - k] % MOD
    out = []
    for n, m, a, b in cases:
        answer = 0
        for x in range(n - a + 1):
            answer = (answer + choose(x + b - 1, x) * choose(n - x + m - b, n - x)) % MOD
        out.append(str(answer))
    print('\n'.join(out))


if __name__ == "__main__":
    main()
```

## Complexity

- **Time:** $O(\max(N + M) + \sum N)$
- **Space:** $O(\max(N + M))$
- Auxiliary space excludes the buffered input and output.

## Edge cases

- Walking along the edge of the cut is allowed, which is why $x = N - A$ is included.
- The sum of $N$ over the test cases bounds the total work of the loops.
- Factorials are needed up to $N + M$.
- All arithmetic is modulo $10^9 + 7$.

## Dry run

`N = 2, M = 2, A = 1, B = 1`. The sum runs over $x = 0, 1$:

- $x = 0$: $\binom{0}{0} \cdot \binom{2 + 1}{2} = 3$
- $x = 1$: $\binom{1}{1} \cdot \binom{1 + 1}{1} = 2$

Answer 5 - the 6 unrestricted paths minus the one that runs through the removed corner.

---

Same problem in rating order (#564 of 735): [../../by-rating/564-CNTWAYS.md](../../by-rating/564-CNTWAYS.md)
