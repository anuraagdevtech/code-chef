[&larr; 622. Musical Rods](622-MUSROD.md) &middot; [Index](README.md) &middot; [624. Chef Goes Shopping &rarr;](624-CHEFSHOPPING.md)

# 623. Binary Substitution

> [`SUBSBIN`](https://www.codechef.com/problems/SUBSBIN) &middot; difficulty **2161** &middot; time limit **1s** &middot; 2000 to 2500 difficulty problems (Level 5)

## Topic used

| | |
|---|---|
| **Topic** | Constructive |
| **Technique** | Fix the imbalance one unit per operation, then collapse the whole string |
| **CodeChef tags** | `Data Structures`, `Algorithms`, `Constructive`, `String`, `ad-hoc` |
| **Complexity class** | Quadratic $O(n^2)$ |
| **Time** | $O(N^2)$ per test case with $N \le 1000$ |
| **Space** | $O(N)$ |

## Question

Chef has binary string $S$ of length $N$.

Chef can perform the following operation on the string:
- Choose a contiguous subarray $S_L, S_{L + 1}, \ldots , S_R$ such that the count of set bits in the subarray is **equal** to the count of unset bits in the subarray.
- Replace the chosen subarray with either a set bit or an unset bit.

Chef wants to reduce the string to **minimum** possible length using **minimum** number of given operations. Help Chef by telling him the **minimum** length and also the operations required to obtain that. If there are multiple ways to obtain the answer, print any.

**Input**

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- The first line of each test case contains a single integer $N$, denoting the length of the binary string.
- The second line of each test case contains a binary string $S$.

**Output**

For each test case, output $K+1$ lines:
- The first line should contain two space-separated integers $M$ and $K$, denoting the **minimum** length that can be obtained and the **minimum** number of operations required to obtain it respectively.
- Then, $K$ lines follow, where the $i^{th}$ line denotes the $i^{th}$ operation:
    - Each operation is denoted using three space separated integers $L$, $R$, and $B$.
The integers $L$ and $R$ denote the chosen substring such that $(1\le L\lt R \le |S|)$ and the substring $S[L, R]$ has equal count of set and unset bits. Note that, $|S|$ denotes the length of the current string.
The integer $B$ denotes the bit with which the substring is replaced.

## Constraints

- $1 \leq T \leq 100$
- $1 \leq N \leq 1000$

## Sample

**Sample input**

```
3
4
1100
1
1
5
11000
```

**Sample output**

```
1 1
1 4 0
1 0
1 2
1 4 1
1 2 1
```

<details><summary>Explanation</summary>

**Test case $1$:** We can reduce the string to a string of length $1$. We require only $1$ operation to do so:
- Choose $L = 1, R = 4,$ and $B = 0$. We chose the substring $S[1,4]$ which contains $2$ set bits and $2$ unset bits. We can replace the chosen substring with bit $0$.

**Test case $2$:** The given string is of length $1$. Thus, we cannot reduce it any further.

**Test case $3$:** We can reduce the string to a string of length $1$. We require $2$ operations to do so:
- Operation $1$: Choose $L = 1, R = 4,$ and $B = 1$. We chose the substring $S[1,4]$ which contains $2$ set bits and $2$ unset bits. We can replace the chosen substring with bit $1$. Thus, the string after this operation is $S = 10$.
- Operation $2$: Choose $L = 1, R = 2,$ and $B = 1$. We chose the substring $S[1,2]$ which contains $1$ set bit and $1$ unset bit. We can replace the chosen substring with bit $1$. Thus, the string after this operation is $S = 1$.

</details>

## Approach

An operation removes a balanced substring and inserts one bit, so it changes (number of zeros $-$ number of ones) by exactly one, in either direction.

If the string contains only one kind of bit, no balanced substring exists and nothing can be done: the answer is the length itself with 0 operations.

Otherwise the string can be reduced to length 1: the last operation must take the whole current string, which therefore has to be balanced. If the initial imbalance is $d$, at least $d$ operations are needed before that, for a total of at least $d + 1$. This bound is reached: while the string is unbalanced it still contains both bits, hence an adjacent pair `01` or `10`; replace that pair by the minority bit, which removes one majority bit and lowers the imbalance by one. After $d$ such steps the string is balanced and one final operation replaces it by a single bit.

## Solution

```python
import sys


def main() -> None:
    tokens = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(tokens))):
        n = int(next(tokens))
        bits = next(tokens).decode()
        ones = bits.count('1')
        zeros = n - ones
        if min(ones, zeros) == 0:
            out.append(f'{n} 0')
            continue
        imbalance = abs(ones - zeros)
        minority = '0' if ones > zeros else '1'
        operations = []
        for _ in range(imbalance):
            i = next((i for i in range(len(bits) - 1) if bits[i] != bits[i + 1]))
            operations.append(f'{i + 1} {i + 2} {minority}')
            bits = bits[:i] + minority + bits[i + 2:]
        operations.append(f'1 {len(bits)} 0')
        out.append(f'1 {len(operations)}')
        out.extend(operations)
    print('\n'.join(out))


if __name__ == "__main__":
    main()
```

## Edge cases

- A uniform string (including length 1) prints its length and 0 operations.
- An already balanced string needs exactly one operation.
- Indices in later operations refer to the current, already shortened string.
- Many operation sequences are optimal, so the output is validated by a checker.

## Dry run

`S = 11000`: two ones, three zeros, imbalance 1, minority bit `1`.

- The first unequal adjacent pair is at positions 2-3 (`10`); replace it by `1`: the string becomes `1100`. Operation `2 3 1`.
- Now balanced: replace positions 1-4 by `0`. Operation `1 4 0`.

Output `1 2` followed by the two operations.

---

Same problem grouped by topic: [../docs/constructive/SUBSBIN.md](../docs/constructive/SUBSBIN.md)
