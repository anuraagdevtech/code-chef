# 353. Break Free

> [`REMOSET`](https://www.codechef.com/problems/REMOSET) &middot; difficulty **1612** &middot; time limit **1s** &middot; 1400 to 1600 difficulty problems (Level 2)

## Topic used

| | |
|---|---|
| **Topic** | Combinatorics |
| **Technique** | A condition pinned down by its singletons |
| **CodeChef tags** | `Mathematics`, `Basic Math`, `Combinatorics` |
| **Complexity class** | Linear $O(n)$ |
| **Time** | $O(N)$ per test case |
| **Space** | $O(1)$ |

## Question

*This is the part when I say I don't want ya \
I'm stronger than I've been before \
This is the part when I break free \
'Cause I can't resist it no more*

Chef has an array $A$ of length $N$.

Let $B$ denote the array obtained by removing any **non-empty** subset of **indices** from the array $A$.
The removal of subset of indices is said to be *good* if:
- Sum of the subarray $B[i, j]$ is divisible by $2$ for all pairs of indices $(1 \leq i \leq j \leq |B|)$.

Find the number of *good* removals. Since the answer can be huge, print it modulo $10^9 + 7$.

**Note:**
- The sum of an empty array is $0$, which is divisible by $2$.
- $B[i, j]$ denotes the subarray $[B_i, B_{i+1}, \ldots, B_j]$.

**Input**

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of multiple lines of input.
    - The first line of each test case contains a single integer $N$, the length of the array.
    - The next line contains $N$ space-separated integers, denoting the elements of the array.

**Output**

For each test case, output on a new line, total number of *good* removals modulo $10^9 + 7$.

## Constraints

- $1 \leq T \leq 10^4$
- $1 \leq N \leq 2 \cdot 10^5$
- $0 \leq A_{i} \leq 2 \cdot 10^5$
- The sum of $N$ over all test cases won't exceed $2 \cdot 10^5$.

## Sample

**Sample input**

```
2
3
2 1 4
3
1 2 3
```

**Sample output**

```
4
2
```

<details><summary>Explanation</summary>

**Test case $1$:** There are $4$ *good* removals.
- Remove subset $\{2\}$. Final array: $[2,4]$.
- Remove subset $\{1,2,3\}$. Final array: $[]$.
- Remove subset $\{2,3\}$. Final array: $[2]$.
- Remove subset $\{1,2\}$. Final array: $[4]$.

</details>

## Approach

The condition must hold for **every** subarray of $B$, including the length-one ones $B[i,i]$. So every surviving element must itself be even — and conversely, if all survivors are even then every subarray sum is a sum of evens and automatically even.

So a removal is good exactly when the elements left behind are all even. That means **every odd element must be removed**, while each even element may independently be kept or removed:

$$2^{e}, \qquad e = \#\{i : A_i \text{ even}\}$$

choices in total, where the empty $B$ is allowed because the statement declares the empty sum to be $0$.

The one adjustment is that the removal must be **non-empty**. If the array contains at least one odd element, every one of the $2^e$ choices removes it and is automatically non-empty. But if there are no odd elements, the choice that keeps all the evens removes nothing — so subtract one:

$$\text{answer} = \begin{cases} 2^{e} & \text{some } A_i \text{ odd} \\ 2^{e} - 1 & \text{all } A_i \text{ even} \end{cases}$$

Reducing an all-subarrays condition to its singletons is the move worth keeping; it is the same collapse that appeared in the *Magic Set* problem.

Sample case 1, $[2,1,4]$, has two evens and one odd, giving $2^2 = 4$. Sample case 2, $[1,2,3]$, has one even and two odds, giving $2$.

The power is taken modulo $10^9+7$ with `pow(2, e, MOD)`, and the $-1$ applied afterwards.

## Solution

```python
import sys

MOD = 10 ** 9 + 7


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n = int(data[pos])
        evens = sum(1 for v in data[pos + 1:pos + 1 + n] if int(v) % 2 == 0)
        pos += 1 + n
        # Every odd must go; each even is a free choice. The removal must be
        # non-empty, which only bites when there is nothing odd to remove.
        ways = pow(2, evens, MOD)
        if evens == n:
            ways -= 1
        out.append(str(ways % MOD))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Edge cases

- **The singletons carry the condition.** Every subarray sum of $B$ must be even, and the length-one subarrays force every element of $B$ to be even — after which all longer sums are automatically even.
- **So every odd element must be removed**, and each even element is a free choice: keep it or remove it. That gives $2^{\text{evens}}$ removals.
- **The removal must be non-empty**, which only bites when there are no odd elements at all: then "remove nothing" is one of the $2^{\text{evens}}$ options and has to be subtracted. The second sample row has one even and two odds, so nothing is subtracted.
- **$B$ may be empty.** Removing everything is a valid good removal, since an empty array has no subarrays to violate the condition — which is why the count is $2^{\text{evens}}$ and not $2^{\text{evens}} - 1$ in general.
- **$A_i = 0$ counts as even**, so a zero is a free choice like any other even value.
- **The modular subtraction needs a final `%`**, since $2^{\text{evens}} \bmod p$ can be $0$ and $0 - 1$ would be negative.
- **Sum of $N \leq 2 \cdot 10^5$**: one pass counting evens, then one modular power.

## Dry run

| $N$ | array | evens | odds | $2^{\text{evens}}$ | subtract 1? | output |
|---:|---|---:|---:|---:|:---:|---:|
| 3 | $2, 1, 4$ | 2 | 1 | 4 | no | `4` |
| 3 | $1, 2, 3$ | 1 | 2 | 2 | no | `2` |

For the first row the odd $1$ must go, and the two evens give four choices: keep both, keep either, or keep neither.

---

Same problem grouped by topic: [../docs/combinatorics/REMOSET.md](../docs/combinatorics/REMOSET.md)
