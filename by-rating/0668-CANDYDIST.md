# 668 &middot; Candy Distribution

> CodeChef problem code [`CANDYDIST`](https://www.codechef.com/problems/CANDYDIST) &middot; time limit **1s** &middot; 500 to 1000 difficulty rating (Level 1)

## Topics used

| | |
|---|---|
| **Topic** | Number Theory |
| **Technique** | Divisibility by a composite modulus |
| **CodeChef tags** | `Mathematics`, `Basic Programming Concepts`, `Basic Math` |
| **CodeChef category** | school |
| **Time** | $O(1)$ per test case |
| **Space** | $O(1)$ |

Same write-up grouped by topic: [../docs/number-theory/CANDYDIST.md](../docs/number-theory/CANDYDIST.md)

## Question

Chef has $N$ candies. He has to distribute them to exactly $M$ of his friends such that each friend gets **equal** number of candies and each friend gets **even** number of candies. Determine whether it is possible to do so.

**NOTE:** Chef will not take any candies himself and will distribute **all** the candies.

**Input**

- First line will contain $T$, number of test cases. Then the test cases follow.
- Each test case contains of a single line of input, two integers $N$ and $M$, the number of candies and the number of friends.

**Output**

For each test case, the output will consist of a single line containing `Yes` if Chef can distribute the candies as per the conditions and `No` otherwise.

You may print each character of the string in uppercase or lowercase (for example, the strings `yes`, `Yes`, `yEs`, and `YES` will all be treated as identical).

## Constraints

- $1 \leq T \leq 1000$
- $1 \leq N,M \leq 1000$

## Sample

**Sample input**

```
4
9 3
4 1
4 2
8 3
```

**Sample output**

```
No
Yes
Yes
No
```

<details><summary>Explanation</summary>

**Test case $1$:** Since Chef has $9$ candies and $3$ friends, each friend will get $\frac{9}{3} = 3$ candies. Since $3$ is not even, Chef doesn't satisfy the conditions.

**Test case $2$:** Since Chef has $4$ candies and $1$ friend, each friend will get $\frac{4}{1} = 4$ candies. Since $4$ is even, Chef satisfies all the conditions.

**Test case $3$:** Since Chef has $4$ candies and $2$ friends, each friend will get $\frac{4}{2} = 2$ candies. Since $2$ is even, Chef satisfies all the conditions.

**Test case $4$:** Since Chef has $8$ candies and $3$ friends. Since Chef won't be able to distribute all the candies equally, Chef does not satisfy all the conditions.

</details>

## Approach

Two conditions must hold at once. Every one of the $M$ friends gets the same number of candies, so $M$ must divide $N$; and that shared amount $N/M$ must itself be even.

Written directly:

$$M \mid N \quad\text{and}\quad \frac{N}{M} \equiv 0 \pmod 2$$

Both are needed, and each one alone is insufficient. Sample case 1 ($N=9$, $M=3$) divides evenly into $3$ candies each, but $3$ is odd. Sample case 4 ($N=8$, $M=3$) fails the divisibility outright.

There is a neater way to see it. "Divisible by $M$, and the quotient divisible by $2$" is exactly "divisible by $2M$":

$$N \equiv 0 \pmod{2M}$$

a single modulo instead of a division followed by a parity test. This also sidesteps any worry about evaluating `n // m` when `n % m != 0` — with the combined form there is no intermediate quotient at all.

Both formulations are given in the code below, with the compact one used. The guarantee that $N, M \geq 1$ means $2M$ is never zero, so the modulo is always well defined.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        n, m = int(data[1 + 2 * i]), int(data[2 + 2 * i])
        # "n divisible by m, and n // m even" is exactly "n divisible by 2m".
        out.append("Yes" if n % (2 * m) == 0 else "No")
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(1)$ per test case
- **Space:** $O(1)$
