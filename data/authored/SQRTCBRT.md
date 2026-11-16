---
topic: Basic Math
subtopic: The answer is a square - iterate to the least fixed point
time: $O(1)$ expected per test case - a handful of iterations
space: $O(1)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
$F$ only increases at perfect squares, so the smallest $N$ with $F(N) \ge X$ is a perfect square $j^2$. There, $F(j^2) = j - \lfloor \sqrt[3]{j^2} \rfloor$: $j$ squares minus the cubes up to $j^2$. (A sixth power counts on both sides, which the formula handles by itself.)

As $j$ grows by one the cube count grows by at most one, so $g(j) = j - \lfloor \sqrt[3]{j^2} \rfloor$ is non-decreasing and we need the smallest $j$ with $g(j) \ge X$, i.e. $j \ge X + \lfloor \sqrt[3]{j^2} \rfloor$.

Iterate $j \leftarrow X + \lfloor \sqrt[3]{j^2} \rfloor$ starting from $j = X$. The sequence is increasing, never jumps over the smallest feasible $j$ (the right-hand side is monotone), and stops exactly there. Because the cube root grows slowly, a few rounds suffice. The integer cube root is taken from a float estimate and then corrected by one in either direction.

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
