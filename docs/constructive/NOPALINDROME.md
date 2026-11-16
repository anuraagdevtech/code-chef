[&larr; 639. Mountain](MOUNTAIN.md) &middot; [Index](../../README.md) &middot; [646. Array Sum &rarr;](SUMARRAY.md)

# 640. No Palindrome

> CodeChef problem code [`NOPALINDROME`](https://www.codechef.com/problems/NOPALINDROME) &middot; difficulty **2054** &middot; time limit **1.5s**

| | |
|---|---|
| **Topic** | Constructive |
| **Technique** | The greedy smallest number is periodic - count the digits in one period |
| **Time** | $O(1)$ per test case |
| **Space** | $O(1)$ |
| **Roadmap course** | 2000 to 2500 difficulty problems (Level 5) |

## Question

Given positive integers $N$ and $K$, let $S$ denote the **smallest number** of $N$ digits (with no leading zeros) such that:
- No substring of $S$ having length **strictly greater** than $K$ is a [palindrome](https://en.wikipedia.org/wiki/Palindrome#Numbers).

Find the **sum of digits** of $S$.

Note:
- A substring of a number is obtained by deleting some (possibly zero) digits from the beginning of the number and some (possibly zero) digits from the end of the number. For example, some substrings of the number $3010$ are $3010, 301, 010, 01, 10$ and $0$.
- **Leading zeros** are **considered** in a substring. In the above example, $010$ and $01$ are **valid** substrings.

**Input**

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of two space-separated integers $N$ and $K$ — as mentioned in the statement.

**Output**

For each test case, output on a new line, the sum of digits of the smallest number of $N$ digits satisfying the given condition.

## Constraints

- $1 \leq T \leq 5000$
- $1 \leq K \lt N \leq 10^9$

## Sample

**Sample input**

```
2
2 1
3 2
```

**Sample output**

```
1
1
```

<details><summary>Explanation</summary>

**Test case $1$:** The smallest number of $2$ digits satisfying the condition is $10$. Here no substring of length greater than $1$ is a palindrome.

**Test case $2$:** The smallest number of $3$ digits satisfying the condition is $100$. The sum of its digits is $1$.

</details>

## Approach

Build the smallest number greedily from the left. It must start with 1. Then zeros are best, but $K + 1$ zeros in a row would be a palindrome longer than $K$, so exactly $K$ zeros follow. The next digit cannot be 0, and it cannot be 1 either, because `1 0...0 1` is a palindrome of length $K + 2$; so it is 2.

After the 2, zeros are again preferred, but a palindrome centred on the 2 grows by two with every zero, mirroring the zeros before it: `0..0 2 0..0` with $z$ zeros on each side has length $2z + 1$, which must stay at most $K$, so $z \le \lfloor (K-1)/2 \rfloor$. Then a 1 is allowed, and from there the situation is the same as at the start.

So the answer is the prefix of length $N$ of the periodic word

$$1 \; \underbrace{0 \dots 0}_{K} \; 2 \; \underbrace{0 \dots 0}_{\lfloor (K-1)/2 \rfloor}$$

with period $K + 2 + \lfloor (K-1)/2 \rfloor$ and digit sum 3 per period. A partial period contributes 1 if it is non-empty and 3 once it is long enough to include the 2, i.e. longer than $K + 1$.

## Solution (Python)

```python
import sys


def main() -> None:
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    out = []
    for _ in range(next(tokens)):
        n = next(tokens)
        k = next(tokens)
        period = k + 2 + (k - 1) // 2
        blocks, tail = divmod(n, period)
        out.append(str(3 * blocks + (3 if tail > k + 1 else 1 if tail else 0)))
    print('\n'.join(out))


if __name__ == "__main__":
    main()
```

## Complexity

- **Time:** $O(1)$ per test case
- **Space:** $O(1)$
- Auxiliary space excludes the buffered input and output.

## Edge cases

- $N$ is up to $10^9$, so only counting is possible.
- A partial period of length exactly $K + 1$ ends just before the 2 and contributes only 1.
- $K = 1$: the period is `102`.
- Substrings may have leading zeros and still count as palindromes, which is what limits the zero runs.

## Dry run

`N = 5, K = 1`: period `1 0 2` of length 3.

$5 = 1 \cdot 3 + 2$: one full period (sum 3) and a tail `1 0` of length 2, which is not longer than $K + 1 = 2$, so it adds 1.

The number is `10210` and the answer is 4.

> CodeChef tags: `Mathematics`, `Algorithms`

---

Same problem in rating order (#591 of 735): [../../by-rating/591-NOPALINDROME.md](../../by-rating/591-NOPALINDROME.md)
