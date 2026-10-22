[&larr; 77. Dracula Eats](CHEAT.md) &middot; [Index](../../README.md) &middot; [90. Primality Test &rarr;](PRB01.md)

# 80. Mutated Minions

> CodeChef problem code [`CHN15A`](https://www.codechef.com/problems/CHN15A) &middot; difficulty **970** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Number Theory |
| **Technique** | Divisibility after a uniform shift |
| **Time** | $O(N)$ per test case |
| **Space** | $O(1)$ |
| **Roadmap course** | 500 to 1000 difficulty rating (Level 1) |

## Question

Gru has not been in the limelight for a long time and is, therefore, planning something particularly nefarious. Frustrated by his minions' incapability which has kept him away from the limelight, he has built a transmogrifier — a machine which mutates minions.

Each minion has an intrinsic characteristic value (similar to our DNA), which is an integer. The transmogrifier adds an integer **K** to each of the minions' characteristic value.

Gru knows that if the new characteristic value of a minion is divisible by 7, then it will have Wolverine-like mutations.

Given the initial characteristic integers of **N** minions, all of which are then transmogrified, find out how many of them become Wolverine-like.

**Input**

The first line contains one integer, **T**, which is the number of test cases. \
Each test case contains of $2$ lines of input.
- The first line contains two integers **N** and **K**, as described in the statement
- The next line contains **N** integers, which denote the initial characteristic values for the minions

**Output**

For each testcase, output one integer in a new line, which is the number of Wolverine-like minions after the transmogrification.

## Constraints

- **1 ≤ T ≤ 100**

- **1 ≤ N ≤ 100**

- **1 ≤ K ≤ 100**

- All initial characteristic values lie between 1 and 10^5, both inclusive.

## Sample

**Sample input**

```
1
5 10
2 4 1 35 1
```

**Sample output**

```
1
```

<details><summary>Explanation</summary>

After transmogrification, the characteristic values become {12,14,11,45,11}, out of which only 14 is divisible by 7. So only the second minion becomes Wolverine-like.

</details>

## Approach

Every minion's characteristic value gains the same $K$, and a minion mutates when the result is divisible by $7$. So the answer counts the values satisfying

$$(A_i + K) \equiv 0 \pmod 7$$

a single pass with a counter, in $O(N)$ time and $O(1)$ space.

Because the shift is uniform, there is a neater way to see it. The condition rearranges to

$$A_i \equiv -K \pmod 7$$

so the qualifying minions are exactly those whose *original* value already sits in one fixed residue class mod $7$. Computing `(-k) % 7` once per test case and comparing each `a % 7` against it does the same work with one modulo per element instead of an addition and a modulo — and, more usefully, it shows that $K$ only ever matters through $K \bmod 7$. Adding $K = 10$ and adding $K = 3$ produce identical answers.

The direct form `(a + k) % 7 == 0` is used below because it mirrors the statement; at these bounds the difference is immaterial. Note that Python's `%` always returns a non-negative result for a positive modulus, so `(-k) % 7` is well behaved — in C it would not be.

Walking the sample: $K = 10$ against $[2, 4, 1, 35, 1]$ gives $12, 14, 11, 45, 11$, of which only $14$ is a multiple of $7$ — one mutation.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n, k = int(data[pos]), int(data[pos + 1])
        vals = data[pos + 2:pos + 2 + n]
        pos += 2 + n
        # Equivalently: count the values already congruent to -k (mod 7).
        out.append(str(sum(1 for v in vals if (int(v) + k) % 7 == 0)))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(N)$ per test case
- **Space:** $O(1)$

## Edge cases

- **$K$ may exceed $7$** (it is $10$ in the sample), so it is not pre-reduced. Adding it and then taking the remainder handles that automatically; reducing $K$ first would also work but is an extra step to get wrong.
- **A value already divisible by $7$** counts only when $K$ is too — the shift is uniform, so the test is equivalently $v \equiv -K \pmod 7$.
- **$N = 1$**: a single minion.
- **Values up to $10^5$ and $K$ up to $100$**: the sum stays small, so no overflow.
- The shift applies to every value equally, which is what turns "will become divisible" into a plain residue count.

## Dry run

$N = 5$, $K = 10$, values $2, 4, 1, 35, 1$:

| value | $v + K$ | $\bmod 7$ | counts? |
|---:|---:|---:|:---:|
| 2 | 12 | 5 | no |
| 4 | 14 | 0 | **yes** |
| 1 | 11 | 4 | no |
| 35 | 45 | 3 | no |
| 1 | 11 | 4 | no |

One minion qualifies, so `1`. Note $35$ is divisible by $7$ on its own and still fails, because $K$ is not.

> CodeChef tags: `Mathematics`, `Modular Arithmetic`, `Algorithms`

---

Same problem in rating order (#159 of 486): [../../by-rating/159-CHN15A.md](../../by-rating/159-CHN15A.md)
