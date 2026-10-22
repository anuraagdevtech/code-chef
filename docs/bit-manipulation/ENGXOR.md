[&larr; 348. Maximum Damage](MAXDMGE.md) &middot; [Index](../../README.md) &middot; [351. XOR with Subset &rarr;](XORSUB.md)

# 349. XOR Engine

> CodeChef problem code [`ENGXOR`](https://www.codechef.com/problems/ENGXOR) &middot; difficulty **1632** &middot; time limit **1.5s**

| | |
|---|---|
| **Topic** | Bit Manipulation |
| **Technique** | Popcount parity is additive under XOR |
| **Time** | $O(N + Q)$ per test case |
| **Space** | $O(1)$ |
| **Roadmap course** | Jump from 2* to 3* (Level 3) |

## Question

A sophomore Computer Science student is frustrated with boring college lectures. Professor X agreed to give him some questions; if the student answers all questions correctly, then minimum attendance criteria will not apply to him.

Professor X chooses a sequence $A_1, A_2, \ldots, A_N$ and asks $Q$ queries. In each query, the student is given an integer $P$; he has to construct a sequence $B_1, B_2, \ldots, B_N$, where $P \oplus A_i = B_i$ for each valid $i$ ($\oplus$ denotes bitwise XOR), and then he has to find the number of elements of this sequence which have an even number of $1$-s in the binary representation and the number of elements with an odd number of $1$-s in the binary representation. Help him answer the queries.

**Input**
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains two space-separated integers $N$ and $Q$.
- The second line contains $N$ space-separated integers $A_1, A_2, \ldots, A_N$.
- $Q$ lines follow. Each of these lines contains a single integer $P$ describing a query.

**Output**
For each query, print a single line containing two space-separated integers ― the number of elements with an even number of $1$-s and the number of elements with an odd number of $1$-s in the binary representation.

**Constraints**
- $1 \le T \le 100$
- $1 \le N, Q \le 10^5$
- $ T \cdot (N+Q) \leq 4 \cdot 10^6 $
- $1 \le A_i \le 10^8$ for each valid $i$
- $1 \le P \le 10^5$

**The input/output is quite large, please use fast reading and writing methods.**

**Subtasks**
**Subtask #1 (30 points):** $N, Q \le 1,000$

**Subtask #2 (70 points):** original constraints

## Constraints

- $1 \le T \le 100$
- $1 \le N, Q \le 10^5$
- $ T \cdot (N+Q) \leq 4 \cdot 10^6 $
- $1 \le A_i \le 10^8$ for each valid $i$
- $1 \le P \le 10^5$
**The input/output is quite large, please use fast reading and writing methods.**

## Sample

**Sample input**

```
1
6 1
4 2 15 9 8 8
3
```

**Sample output**

```
2 4
```

<details><summary>Explanation</summary>

**Example case 1:** The elements of the sequence $B$ are $P \oplus 4 = 7$, $P \oplus 2 = 1$, $P \oplus 15 = 12$, $P \oplus 9 = 10$, $P \oplus 8 = 11$ and $P \oplus 8 = 11$. The elements which have an even number of $1$-s in the binary representation are $12$ and $10$, while the elements with an odd number of $1$-s are $7$, $1$, $11$ and $11$.

</details>

## Approach

The queries look independent — each $P$ builds a whole new sequence $B$ — but the quantity asked for is only the **parity** of the popcount, and parity behaves linearly under XOR:

$$\mathrm{popcount}(P \oplus A_i) \equiv \mathrm{popcount}(P) + \mathrm{popcount}(A_i) \pmod 2$$

(each bit position where $P$ and $A_i$ agree contributes $0$ or $2$ ones, both even; each position where they differ contributes exactly $1$ to both sides.)

So $B_i$ has odd popcount iff $\mathrm{popcount}(P)$ and $\mathrm{popcount}(A_i)$ have *different* parity. The entire array collapses to two numbers, $E$ and $O$ — how many $A_i$ have even and odd popcount — computed once:

- $\mathrm{popcount}(P)$ **even**: the parities are unchanged, so the answer is $(E, O)$.
- $\mathrm{popcount}(P)$ **odd**: every parity flips, so the answer is $(O, E)$.

Each query is then $O(1)$, which is what makes $T \cdot (N + Q) \leq 4 \times 10^6$ tractable. Precomputing a popcount table over $P \leq 10^5$ is unnecessary — a single `bit_count()` per query suffices.

In the sample, $A = [4, 2, 15, 9, 8, 8]$ has popcounts $1, 1, 4, 2, 1, 1$, so $E = 2$ and $O = 4$. The query $P = 3$ has popcount $2$, which is even, so the answer is `2 4` unchanged. Had $P$ been $1$, the same precomputation would immediately give `4 2`.

The statement's own warning about large I/O is the real difficulty: read the whole stream at once and join the output rather than printing per query.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n, q = int(data[pos]), int(data[pos + 1])
        pos += 2
        odd = 0
        for tok in data[pos:pos + n]:
            odd += int(tok).bit_count() & 1
        pos += n
        even = n - odd
        for tok in data[pos:pos + q]:
            # XOR adds the two popcounts mod 2, so odd P just swaps the tallies.
            if int(tok).bit_count() & 1:
                out.append(f"{odd} {even}")
            else:
                out.append(f"{even} {odd}")
        pos += q
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(N + Q)$ per test case
- **Space:** $O(1)$

## Edge cases

- **Popcount parity is additive under XOR.** The parity of $\mathrm{popcount}(P \oplus A_i)$ is $\mathrm{popcount}(P) \oplus \mathrm{popcount}(A_i)$ modulo $2$ — so an odd $P$ simply swaps the two tallies and an even $P$ leaves them alone.
- **That makes every query $O(1)$** after one pass over $A$: no per-query recomputation, which matters at $T(N+Q) \leq 4 \times 10^6$.
- **An even-popcount $P$ preserves the tallies** (the sample, where $P = 3$ has popcount $2$), so the output is $A$'s own counts.
- **An odd-popcount $P$ exchanges them**, and the two branches differ only in the order of the two numbers.
- **The output order is (even count, odd count)**, which the sample's `2 4` pins down.
- **$A_i \geq 1$ and $P \geq 1$**, so no zero with its popcount of $0$ needs special thought.
- **`int.bit_count()` is the exact popcount**, and masking with $1$ gives the parity directly.

## Dry run

Sample: $A = 4, 2, 15, 9, 8, 8$.

| value | popcount | parity |
|---:|---:|---|
| 4 | 1 | odd |
| 2 | 1 | odd |
| 15 | 4 | even |
| 9 | 2 | even |
| 8 | 1 | odd |
| 8 | 1 | odd |

Four odd, two even. Query $P = 3$ has popcount $2$, even, so the tallies carry over unchanged: output `2 4`.

---

Same problem in rating order (#367 of 486): [../../by-rating/367-ENGXOR.md](../../by-rating/367-ENGXOR.md)
