[&larr; 604. Little Elephant and Median](MEDIAN.md) &middot; [Index](../../README.md) &middot; [633. Maximum And Or &rarr;](MAXANDOR.md)

# 629. NASA

> CodeChef problem code [`PALIXOR`](https://www.codechef.com/problems/PALIXOR) &middot; difficulty **2014** &middot; time limit **2.5s**

| | |
|---|---|
| **Topic** | Bit Manipulation |
| **Technique** | Counting pairs by xor value, directly or with a Walsh-Hadamard transform |
| **Time** | $O(\min(D \cdot P,\; U \log U))$ per test case with $D$ distinct values, $P$ palindromes below $U = 2^{15}$ |
| **Space** | $O(U)$ |
| **Roadmap course** | 2000 to 2500 difficulty problems (Level 5) |

## Question

*I'ma need space, I'ma, I'ma need \
You know I'm a star; space, I'ma need space \
I'ma need space, I'ma, I'ma need space (N-A-S-A)*

Given an array $A$ of size $N$.
Find total number of pairs in the array $(i, j)$ $(1\le i\le j \le N)$ such that:
- $A_i \oplus  A_j$ is a [palindrome](https://en.wikipedia.org/wiki/Palindrome#Numbers) (in **decimal** representation), where $\oplus$ denotes the [bitwise xor operator](https://en.wikipedia.org/wiki/Bitwise_operation#XOR).

**Input**

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of multiple lines of input.
    - The first line of each test case contains one integer $N$ - the size of the array.
    - The next line contains $N$ space-seperated integers as array elements.

**Output**

For each test case, output on a new line, the number of pairs satisfying the given condition.

## Constraints

- $1 \leq T \leq 10^{2}$
- $1 \leq N \leq 10^{5}$
- $0 \leq A_i \lt 2^{15}$
- The sum of N over all test cases does not exceed $2\cdot 10^{5}$.

## Sample

**Sample input**

```
2
4
13 27 12 26
3
2 2 2
```

**Sample output**

```
8
6
```

<details><summary>Explanation</summary>

**Test case $1$:** The pairs which form palindrome are :
- $13 \oplus  13 = 0$
- $13 \oplus  27 = 22$
- $13 \oplus  12 = 1$
- $27 \oplus  27 = 0$
- $27 \oplus  26 = 1$
- $12 \oplus  12 = 0$
- $12 \oplus  26 = 22$
- $26 \oplus  26 = 0$

**Test case $2$:** All the pairs form palindrome.

</details>

## Approach

All values are below $2^{15}$, so the xor of a pair is too, and there are only a few hundred decimal palindromes in that range. Count the ordered pairs $(i, j)$ whose xor is a palindrome; the pairs with $i = j$ have xor 0, a palindrome, and are counted once, while every other unordered pair is counted twice. Hence the required number of pairs with $i \le j$ is (ordered $+ N$) / 2.

Two ways to count the ordered pairs, chosen by size:

- few distinct values: for every distinct value $x$ and every palindrome $p$, add `freq[x] * freq[x ^ p]`;
- many distinct values: the xor-convolution of the frequency array with itself gives the number of ordered pairs for every xor value at once. It is computed with the Walsh-Hadamard transform - transform, square pointwise, transform again, divide by $U$ - and then summed over the palindromes.

## Solution (Python)

```python
import sys
from collections import Counter


def main() -> None:
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    out = []
    palindromes = [x for x in range(32768) if str(x) == str(x)[::-1]]

    def transform(table):
        half = 1
        n = len(table)
        while half < n:
            for j in range(0, n, 2 * half):
                for i in range(j, j + half):
                    x = table[i]
                    y = table[i + half]
                    table[i] = x + y
                    table[i + half] = x - y
            half *= 2
    for _ in range(next(tokens)):
        n = next(tokens)
        freq = Counter((next(tokens) for _ in range(n)))
        if len(freq) * len(palindromes) < 1500000:
            total = sum((v * freq.get(x ^ p, 0) for x, v in freq.items() for p in palindromes))
        else:
            table = [0] * 32768
            for x, v in freq.items():
                table[x] = v
            transform(table)
            table = [x * x for x in table]
            transform(table)
            total = sum((table[p] for p in palindromes)) // 32768
        out.append(str((total + n) // 2))
    print('\n'.join(out))


if __name__ == "__main__":
    main()
```

## Complexity

- **Time:** $O(\min(D \cdot P,\; U \log U))$ per test case with $D$ distinct values, $P$ palindromes below $U = 2^{15}$
- **Space:** $O(U)$
- Auxiliary space excludes the buffered input and output.

## Edge cases

- 0 is a palindrome, so every element pairs with itself and equal elements pair with each other.
- The inverse Walsh-Hadamard transform is the same transform followed by a division by the size.
- Single-digit xor values are palindromes too.
- The direct method is used whenever it is cheaper, which keeps small tests fast.

## Dry run

`A = [2, 2, 2]`. One distinct value with frequency 3.

Ordered pairs with a palindromic xor: only $p = 0$ contributes, $3 \cdot 3 = 9$.

Answer $(9 + 3) / 2 = 6$ - all pairs $i \le j$.

> CodeChef tags: `Advanced Algorithms`, `Mathematics`, `Bit Manipulation`

---

Same problem in rating order (#576 of 735): [../../by-rating/576-PALIXOR.md](../../by-rating/576-PALIXOR.md)
