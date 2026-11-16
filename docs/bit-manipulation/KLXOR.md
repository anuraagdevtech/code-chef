[&larr; 502. Binod](BIN_OD.md) &middot; [Index](../../README.md) &middot; [598. Offer for Chef &rarr;](CHEFOFR.md)

# 507. Again XOR problem

> CodeChef problem code [`KLXOR`](https://www.codechef.com/problems/KLXOR) &middot; difficulty **1786** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Bit Manipulation |
| **Technique** | XOR prefix parity for each output position |
| **Time** | $O(N)$ per test case |
| **Space** | $O(N)$ |
| **Roadmap course** | 1600 to 1800 difficulty problems (Level 3) |

## Question

You may have solved a lot of problems related to XOR and we are sure that you liked them, so here is one more problem for you.

You are given a binary string $S$ of length $N$. Let string $T$ be the result of taking the XOR of **all** substrings of size $K$ of $S$. You need to find the number of `1` bits in $T$.

**Note**:
- A substring is a continuous part of string which can be obtained by deleting some (may be none) character's from the beginning and some (may be none) character's from the end.
- XOR of many similar-sized strings is defined [here](https://en.wikipedia.org/wiki/Exclusive_or).

**Input**

- The first line of the input contains an integer $T$ - the number of test cases. The test cases then follow.
- The first line of each test case contains two integers $N$ and $K$.
- The second line of each test case contains a binary string $S$ of size $N$.

**Output**

For each test case, output on a single line number of `1` bits in the XOR of all substrings of size $K$ of $S$.

## Constraints

- $1 \leq T \leq 10$
- $1 \leq K \le N \leq 2 \cdot 10^5$
- $|S| = N$
- $S$ only contains characters `0` and `1`.

## Sample

**Sample input**

```
4
4 1
1010
4 2
1001
4 3
1111
4 4
0110
```

**Sample output**

```
0
2
0
2
```

<details><summary>Explanation</summary>

- **Test case $1$**: All $1$-sized substrings of $S$ are:
    - `0`
    - `1`
    - `1`
    - `0`

The XOR of these strings is `0`, therefore the number of `1` bits is $0$.
- **Test case $2$**: All $2$-sized substrings of $S$ are:
    - `10`
    - `00`
    - `01`

The XOR of these strings is `11`, therefore the number of `1` bits is $2$.
- **Test case $3$**: All $3$-sized substrings of $S$ are:
    - `111`
    - `111`

The XOR of these strings is `000`, therefore the number of `1` bits is $0$.
- **Test case $4$**: All $4$-sized substrings of $S$ are:
    - `0110`

The XOR of these strings is `0110`, therefore the number of `1` bits is $2$.

</details>

## Approach

For zero-based output position $j$, the contributing characters are $S_j,S_{j+1},\ldots,S_{j+N-K}$. They form one contiguous window of length $N-K+1$ in the original string.

Build prefix XORs of the bits. The $j$-th output bit is the XOR of that window, found from two prefix values. Sum these bits over the $K$ output positions.

## Solution (Python)

```python
import sys


def main() -> None:
    tokens = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(tokens))):
        n, k = int(next(tokens)), int(next(tokens))
        s = next(tokens)
        prefix = [0]*(n+1)
        for i, digit in enumerate(s):
            prefix[i+1] = prefix[i] ^ (digit-48)
        width = n-k+1
        out.append(str(sum(prefix[j+width]^prefix[j] for j in range(k))))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
```

## Complexity

- **Time:** $O(N)$ per test case
- **Space:** $O(N)$
- Auxiliary space excludes the buffered input and output.

## Edge cases

- For $K=N$, each output bit is the original bit.
- For $K=1$, only the parity of all input bits matters.
- Substrings overlap but each contributes independently.

## Dry run

For `1001`, $K=2$, the contributing windows are `100` and `001`; both have XOR one. The output has two ones.

> CodeChef tags: `Data Structures`, `Mathematics`, `Bit Manipulation`, `Algorithms`, `Simple Algos`

---

Same problem in rating order (#507 of 735): [../../by-rating/507-KLXOR.md](../../by-rating/507-KLXOR.md)
