# 346. Chef and Chefina

> CodeChef problem code [`CHFNA`](https://www.codechef.com/problems/CHFNA) &middot; difficulty **1400** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Bit Manipulation |
| **Technique** | Independent bits give a closed form |
| **Time** | $O(1)$ per test case |
| **Space** | $O(1)$ |
| **Roadmap course** | Jump from 2* to 3* (Level 3) |

## Question

Chef wants to impress Chefina but she gave him a problem. Chef is not good in problem-solving so he wants your help to find the minimum of $(A⊕X) + (A⊕Y)$ for any $A$, where ⊕ is Bit-wise XOR.

### Input:
- First-line will contain $T$, the number of test cases. Then the test cases follow:
- Each test case contains a single line of input, two integers $X, Y$.

### Output:
For each test case, output in a single line minimum of $(A⊕X) + (A⊕Y)$.

### Constraints
- $1 \leq T \leq 10^4$
- $1 \leq X, Y \leq 10^9$

## Constraints

- $1 \leq T \leq 10^4$
- $1 \leq X, Y \leq 10^9$

## Sample

**Sample input**

```
1   
6 12
```

**Sample output**

```
10
```

<details><summary>Explanation</summary>

You can choose $A = 4$ and the value will be $(4?6) + (4?12)  = 10$. It can be shown that this is the smallest possible value.

</details>

## Approach

XOR and addition of the two terms both act bit by bit here, with no carries to couple the positions — $(A \oplus X)$ and $(A \oplus Y)$ contribute $0$, $2^b$ or $2 \cdot 2^b$ at bit $b$ depending only on bit $b$ of $A$, $X$ and $Y$. So each bit of $A$ can be chosen independently, and the minimum is the sum of the per-bit minima.

Fix a bit $b$ and let $x, y$ be the corresponding bits of $X, Y$:

- **$x = y$:** pick $a = x$. Both XORs give $0$ at this bit, contributing nothing.
- **$x \neq y$:** whichever $a$ is chosen, it agrees with one of them and differs from the other, so exactly one term contributes $2^b$ — unavoidable.

So the differing bits each cost exactly $2^b$ and the matching bits cost nothing, which is the definition of XOR:

$$\min_A \bigl[(A \oplus X) + (A \oplus Y)\bigr] = X \oplus Y$$

Notice the bound is attained by *any* $A$ that agrees with $X$ and $Y$ on their common bits — $A = X$ and $A = Y$ both work — so the minimiser is not unique even though the minimum is.

The sample has $X = 6 = 0110_2$ and $Y = 12 = 1100_2$, which differ in bits $1$ and $3$, giving $2 + 8 = 10$. Taking $A = 6$ confirms it: $0 + (6 \oplus 12) = 10$.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        x, y = int(data[1 + 2 * i]), int(data[2 + 2 * i])
        # Matching bits cost nothing, differing bits cost 2^b whatever A does.
        out.append(str(x ^ y))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(1)$ per test case
- **Space:** $O(1)$
