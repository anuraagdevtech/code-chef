[&larr; 656. Maximal Expression](MAXIMALEXP.md) &middot; [Index](../../README.md) &middot; [665. Minimize swaps &rarr;](DIVBY3.md)

# 659. Love Squares Hate Cubes

> CodeChef problem code [`SQRTCBRT`](https://www.codechef.com/problems/SQRTCBRT) &middot; difficulty **2150** &middot; time limit **2s**

| | |
|---|---|
| **Topic** | Basic Math |
| **Technique** | The answer is a square - iterate to the least fixed point |
| **Time** | $O(1)$ expected per test case - a handful of iterations |
| **Space** | $O(1)$ |
| **Roadmap course** | 2000 to 2500 difficulty problems (Level 5) |

## Question

Kulyash loves **perfect squares** and hates **perfect cubes**.
For any natural number $N$,
$F(N) = \texttt{number of perfect squares smaller than or equal to } N - \texttt{number of positive perfect cubes smaller than or equal to } N$.

Kulyash gives you an integer $X$ and asks you to find the minimum value of $N$, such that $F(N) \geq X$.

**Input**

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of a single line of input.
    - The first and only line of each test case contains an integer $X$.

**Output**

For each test case, output on a new line, the minimum value of $N$ such that $F(N) \geq X$.

## Constraints

- $1 \leq T \leq 10^5$
- $1 \leq X \leq 10^9$

## Sample

**Sample input**

```
3
1
3
3151
```

**Sample output**

```
4
25
11397376
```

<details><summary>Explanation</summary>

**Test case $1$**: There are $2$ perfect squares from $1$ to $4$, and $1$ perfect cube from $1$ to $4$, so $F(4) = 2 - 1 = 1$, as required.

**Test case $2$**: There are $5$ perfect squares from $1$ to $25$, and $2$ perfect cubes from $1$ to $25$, so $F(25) = 5 - 2 = 3$, as required.

**Test case $3$**: There are $3376$ perfect squares from $1$ to $11397376$, and $225$ perfect cubes from $1$ to $11397376$, so $F(11397376) = 3376 - 225 = 3151$, as required.

</details>

## Approach

$F$ only increases at perfect squares, so the smallest $N$ with $F(N) \ge X$ is a perfect square $j^2$. There, $F(j^2) = j - \lfloor \sqrt[3]{j^2} \rfloor$: $j$ squares minus the cubes up to $j^2$. (A sixth power counts on both sides, which the formula handles by itself.)

As $j$ grows by one the cube count grows by at most one, so $g(j) = j - \lfloor \sqrt[3]{j^2} \rfloor$ is non-decreasing and we need the smallest $j$ with $g(j) \ge X$, i.e. $j \ge X + \lfloor \sqrt[3]{j^2} \rfloor$.

Iterate $j \leftarrow X + \lfloor \sqrt[3]{j^2} \rfloor$ starting from $j = X$. The sequence is increasing, never jumps over the smallest feasible $j$ (the right-hand side is monotone), and stops exactly there. Because the cube root grows slowly, a few rounds suffice. The integer cube root is taken from a float estimate and then corrected by one in either direction.

## Solution (Python)

```python
import sys


def main() -> None:
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    out = []

    def cube_root(n):
        estimate = int(n ** (1 / 3))
        while (estimate + 1) ** 3 <= n:
            estimate += 1
        while estimate ** 3 > n:
            estimate -= 1
        return estimate
    for _ in range(next(tokens)):
        need = next(tokens)
        root = need
        while True:
            candidate = need + cube_root(root * root)
            if candidate == root:
                break
            root = candidate
        out.append(str(root * root))
    print('\n'.join(out))


if __name__ == "__main__":
    main()
```

## Complexity

- **Time:** $O(1)$ expected per test case - a handful of iterations
- **Space:** $O(1)$
- Auxiliary space excludes the buffered input and output.

## Edge cases

- The float cube root can be off by one; the correction loops make it exact.
- $X = 1$ gives $N = 4$, not 1, because 1 is both a square and a cube.
- $j^2$ reaches about $10^{18}$, fine for Python integers.
- The answer is $j^2$, not $j$.

## Dry run

`X = 3`.

- $j = 3$: $3 + \lfloor \sqrt[3]{9} \rfloor = 3 + 2 = 5$
- $j = 5$: $3 + \lfloor \sqrt[3]{25} \rfloor = 3 + 2 = 5$ - fixed point

Answer $5^2 = 25$: five squares and two cubes (1 and 8) up to 25.

> CodeChef tags: `Algorithms`, `Searching`

---

Same problem in rating order (#619 of 735): [../../by-rating/619-SQRTCBRT.md](../../by-rating/619-SQRTCBRT.md)
