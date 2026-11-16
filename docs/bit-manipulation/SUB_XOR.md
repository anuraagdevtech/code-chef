[&larr; 468. Xor and Multiply](XORMUL.md) &middot; [Index](../../README.md) &middot; [502. Binod &rarr;](BIN_OD.md)

# 487. Subarray XOR

> CodeChef problem code [`SUB_XOR`](https://www.codechef.com/problems/SUB_XOR) &middot; difficulty **1757** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Bit Manipulation |
| **Technique** | Parity of contributions to each output bit |
| **Time** | $O(N)$ per test case |
| **Space** | $O(1)$ |
| **Roadmap course** | 1600 to 1800 difficulty problems (Level 3) |

## Question

Mary loves binary strings.
Given a binary string $S$, she defines the *beauty* of the string as the [bitwise XOR](https://en.wikipedia.org/wiki/Bitwise_operation#XOR) of **decimal representations** of **all substrings** of $S$.

Find the *beauty* of string $S$. Since the answer can be huge, print it modulo $998244353$.

For example, the decimal representation of binary string $1101$ is $1\cdot 2^3 + 1\cdot 2^2 + 0\cdot 2^1 + 1\cdot 2^0 = 8 + 4 + 0+1 = 13$. Kindly refer sample explanation for more such examples.

A string $A$ is a substring of a string $B$ if $A$ can be obtained from $B$ by deleting several (possibly zero) characters from the beginning and several (possibly zero) characters from the end.

**Input**

- The first line of input contains a single integer $T$, denoting the number of test cases. The description of test cases follow.
- First line of each test case contains one integer $N$ - the length of the binary string.
- Second line of each test case contains the binary string $S$.

**Output**

For each test case, output in a single line, beauty of the string modulo $998244353$.

## Constraints

- $1 \leq T \leq 100$
- $1 \leq N \leq 10^5$
- Sum of $N$ over all test cases does not exceed $2 \cdot 10^5$

## Sample

**Sample input**

```
3
2
10
3
101
4
1111
```

**Sample output**

```
3
6
12
```

<details><summary>Explanation</summary>

**Test Case $1$:** All substrings of the string $S = 10$ are $[1, 0, 10]$. The decimal representation of these substrings is denoted by the array $[1, 0, 2]$. Bitwise XOR of all these values is $1 \oplus 0 \oplus 2 = 3$.

**Test Case $2$:** All substrings of the string $S = 101$ are $[1, 0, 1, 10, 01, 101]$. The decimal representation of these substrings is denoted by the array $[1, 0, 1, 2, 1, 5]$. Bitwise XOR of all these values is: $1 \oplus 0 \oplus 1 \oplus 2 \oplus 1 \oplus 5 = 6$.

**Test Case $3$:** All substrings of the string $S = 1111$ are $[1, 1, 1, 1, 11, 11, 11, 111, 111, 1111]$. The decimal representation of these substrings is denoted by the array $[1, 1, 1, 1, 3, 3, 3, 7, 7, 15]$. Bitwise XOR of all these values is: $1 \oplus 1 \oplus 1 \oplus 1 \oplus 3 \oplus 3 \oplus 3 \oplus 7 \oplus 7 \oplus 15 = 12$.

</details>

## Approach

Fix an output bit $b$. A one at zero-based index $i$ contributes to it when the substring ends at $i+b$. There are $i+1$ possible starting positions, so only even $i$ survive XOR cancellation. The bit is therefore the parity of ones at even indices up to $N-1-b$.

Scan these prefix parities from left to right. At index $i$, the parity is exactly output bit $N-1-i$. Folding with `answer = 2 * answer + parity` reconstructs the integer modulo $998244353$ without constructing enormous integers.

## Solution (Python)

```python
import sys


def main() -> None:
    tokens = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(tokens))):
        n = int(next(tokens))
        s = next(tokens)
        parity = answer = 0
        for i, digit in enumerate(s):
            if i % 2 == 0:
                parity ^= digit - 48
            answer = (2 * answer + parity) % 998244353
        out.append(str(answer))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
```

## Complexity

- **Time:** $O(N)$ per test case
- **Space:** $O(1)$
- Auxiliary space excludes the buffered input and output.

## Edge cases

- Leading zeros still occupy positions.
- Only even zero-based indices contribute.
- Apply the modulus during the fold, after deciding each bit.

## Dry run

For `101`, the prefix parities at even indices are `1, 1, 0`. These form binary `110`, so the answer is `6`.

> CodeChef tags: `Mathematics`, `Probability`, `Expected Value`

---

Same problem in rating order (#483 of 735): [../../by-rating/483-SUB_XOR.md](../../by-rating/483-SUB_XOR.md)
