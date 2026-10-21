# 1879 &middot; XOR with Subset

> CodeChef problem code [`XORSUB`](https://www.codechef.com/problems/XORSUB) &middot; time limit **1.5s** &middot; Jump from 2* to 3* (Level 3)

## Topics used

| | |
|---|---|
| **Topic** | Bit Manipulation |
| **Technique** | XOR linear basis over GF(2) |
| **CodeChef category** | main |
| **Time** | $O(N \log V + \log^2 V)$ per test case |
| **Space** | $O(\log V)$ |

Same write-up grouped by topic: [../docs/bit-manipulation/XORSUB.md](../docs/bit-manipulation/XORSUB.md)

## Question

You have an array of integers **A_1, A_2, ..., A_N**. The function **F(P)**, where **P** is a [subset](http://en.wikipedia.org/wiki/Subset) of **A**, is defined as the [XOR](http://en.wikipedia.org/wiki/Exclusive_or) (represented by the symbol **⊕**) of all the integers present in the subset. If **P** is empty, then **F(P)**=0.

Given an integer **K**, what is the maximum value of **K** **⊕** **F(P)**, over all possible subsets **P** of **A**?

**Input**

The first line contains **T**, the number of test cases. Each test case consists of **N** and **K** in one line, followed by the array **A** in the next line.

**Output**

For each test case, print the required answer in one line.

**Constraints**

- **1** ≤ **T** ≤ **10**

- **1** ≤ **K**, **A_i** ≤ **1000**

- Subtask 1 (30 points):**1** ≤ **N** ≤ **20**

- Subtask 2 (70 points):**1** ≤ **N** ≤ **1000**

## Constraints

- 1 ≤ T ≤ 10
- 1 ≤ K, A_i ≤ 1000
- Subtask 1 (30 points):1 ≤ N ≤ 20
- Subtask 2 (70 points):1 ≤ N ≤ 1000

## Sample

**Sample input**

```
1
3 4
1 2 3
```

**Sample output**

```
7
```

<details><summary>Explanation</summary>

Considering all subsets:

F({}) = 0 ? 4 **?** 0 = 4

F({1}) = 1 ? 4 **?** 1 = 5

F({1,2}) = 3 ? 4 **?** 3 = 7

F({1,3}) = 2 ? 4 **?** 2 = 6

F({1,2,3}) = 0 ? 4 **?** 0 = 4

F({2}) = 2 ? 4 **?** 2 = 6

F({2,3}) = 1 ? 4 **?** 1 = 5

F({3}) = 3 ? 4 **?** 3 = 7

Therefore, the answer is 7.

</details>

## Approach

There are $2^N$ subsets, but far fewer distinct XOR values. Viewing each $A_i$ as a vector over $\mathrm{GF}(2)$, the subset XORs are exactly the **linear span** of $\{A_1, \ldots, A_N\}$ — a subspace, closed under XOR, with $2^r$ elements where $r$ is the rank. Since $A_i \leq 1000 < 2^{10}$, the rank is at most $10$, so the span has at most $1024$ members however large $N$ gets.

Build a basis in reduced form: keep one vector per pivot bit, and insert $v$ by repeatedly cancelling against the basis vector owning $v$'s highest set bit; if the slot is empty, $v$ claims it, and if $v$ reduces to $0$ it was already dependent.

Then maximise greedily from the top bit down. Start with $\mathrm{res} = K$ and for each pivot bit $b$ from high to low, if $\mathrm{res}$ has bit $b$ clear, XOR in the basis vector for $b$. This is correct because that vector is the only one in the basis that can touch bit $b$, so turning $b$ on is worth more than anything the lower bits could lose:

$$2^b > \sum_{j < b} 2^j$$

The empty subset is allowed, so $0$ is always in the span and the answer is at least $K$.

For the sample, $[1, 2, 3]$ has rank $2$ — $3 = 1 \oplus 2$ is dependent — so the span is $\{0,1,2,3\}$. With $K = 4 = 100_2$, bit $2$ is already set and no basis vector reaches it; bits $1$ and $0$ are clear and the basis supplies $2$ and $1$, giving $4 \oplus 3 = 7$.

Note that brute-forcing $2^N$ passes only subtask 1 ($N \leq 20$); the basis handles $N \leq 1000$ in the same code. An alternative is a reachability bitset over the $1024$ possible XOR values, which is also fine at these bounds, but the basis is the technique that scales to 64-bit values.

## Solution (Python)

```python
import sys

BITS = 10          # A_i <= 1000 < 2^10


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n, k = int(data[pos]), int(data[pos + 1])
        pos += 2
        basis = [0] * BITS          # basis[b] has its highest set bit at b
        for tok in data[pos:pos + n]:
            v = int(tok)
            for b in range(BITS - 1, -1, -1):
                if not v >> b & 1:
                    continue
                if not basis[b]:
                    basis[b] = v
                    break
                v ^= basis[b]       # cancel and keep reducing
        pos += n
        res = k
        for b in range(BITS - 1, -1, -1):
            # 2^b outweighs every lower bit, so take the bit whenever we can.
            if basis[b] and not res >> b & 1:
                res ^= basis[b]
        out.append(str(res))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(N \log V + \log^2 V)$ per test case
- **Space:** $O(\log V)$
