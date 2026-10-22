[Index](../../README.md) &middot; [51. X Jumps &rarr;](XJUMP.md)

# 34. Maximise the Tastiness

> CodeChef problem code [`MAXTASTE`](https://www.codechef.com/problems/MAXTASTE) &middot; difficulty **627** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Greedy |
| **Technique** | Independent choices optimised separately |
| **Time** | $O(1)$ per test case |
| **Space** | $O(1)$ |
| **Roadmap course** | 500 to 1000 difficulty rating (Level 1) |

## Question

Chef is making a dish that consists of exactly two ingredients. He has four ingredients $A, B, C$ and $D$ with tastiness $a, b, c,$ and $d$ respectively. He can use either $A$ or $B$ as the first ingredient and either $C$ or $D$ as the second ingredient.

The tastiness of a dish is the sum of tastiness of its ingredients. Find the **maximum** possible tastiness of the dish that the chef can prepare.

**Input**

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- The first and only line of each test case contains four space-separated integers $a, b, c,$ and $d$ — the tastiness of the four ingredients.

**Output**

For each test case, output on a new line the maximum possible tastiness of the dish that chef can prepare.

## Constraints

- $1 \leq T \leq 100$
- $1 \leq a, b, c, d \leq 100$

## Sample

**Sample input**

```
2
3 5 6 2
16 15 5 4
```

**Sample output**

```
11
21
```

<details><summary>Explanation</summary>

**Test case $1$:** Chef can prepare a dish with ingredients $B$ and $C$ with a tastiness of $5+6=11$.

**Test case $2$:** Chef can prepare a dish with ingredients $A$ and $C$ with a tastiness of $16+5=21$.

</details>

## Approach

The dish takes one ingredient from $\{A, B\}$ and one from $\{C, D\}$, and its tastiness is the sum of the two. There are only four combinations, so brute force works — but the structure is worth naming, because it generalises.

The two choices are **independent**: picking $A$ over $B$ places no restriction on whether $C$ or $D$ may be used. When a total is a sum of independent parts, maximising the whole is the same as maximising each part on its own. So

$$\max \text{tastiness} = \max(a, b) + \max(c, d)$$

This is the simplest possible greedy argument, and the reason it is valid is exactly the independence. The moment a constraint couples the choices — say, two ingredients that cannot be combined — the decomposition breaks and the four cases must genuinely be compared. Recognising when choices separate is what turns an exponential search into a linear one in larger problems.

Checking sample case 2: $\max(16, 15) + \max(5, 4) = 16 + 5 = 21$.

Note that the first ingredient must come from the first pair — Chef cannot take both $A$ and $B$. Reading it as "pick the two tastiest of the four" would give $16 + 15 = 31$ here, which is wrong.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        a, b, c, d = map(int, data[1 + 4 * i:5 + 4 * i])
        # The two picks are independent, so maximise each pair separately.
        out.append(str(max(a, b) + max(c, d)))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(1)$ per test case
- **Space:** $O(1)$

## Edge cases

- **The two largest values in the same pair** is the trap, and the sample's second row is it: $16, 15, 5, 4$ has $16$ and $15$ as the two biggest overall, but both come from the first pair, so only one may be taken and the answer is $16 + 5 = 21$, not $31$. Sorting all four and adding the top two is wrong.
- **A tie inside a pair** ($a = b$): either choice gives the same total, so no tie-break is needed.
- **All four equal**: the answer is twice that value.
- The two picks are genuinely independent — one from each pair — which is why maximising them separately is optimal rather than merely convenient.

## Dry run

| $a$ | $b$ | $c$ | $d$ | $\max(a,b)$ | $\max(c,d)$ | total | output |
|---:|---:|---:|---:|---:|---:|---:|---|
| 3 | 5 | 6 | 2 | 5 | 6 | 11 | `11` |
| 16 | 15 | 5 | 4 | 16 | 5 | 21 | `21` |

Row 2 shows $15$ going unused despite being the second largest value present.

> CodeChef tags: `Algorithms`

---

Same problem in rating order (#41 of 486): [../../by-rating/041-MAXTASTE.md](../../by-rating/041-MAXTASTE.md)
