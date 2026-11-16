[&larr; 582. Barcelona Gameplay Tactics](FCBARCA.md) &middot; [Index](../../README.md) &middot; [602. Lucky Sum &rarr;](LUCKY3.md)

# 595. Sereja and Arrays

> CodeChef problem code [`SEARRAYS`](https://www.codechef.com/problems/SEARRAYS) &middot; difficulty **1999** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Combinatorics |
| **Technique** | Counting tilings with a single zero and a block of K ones |
| **Time** | $O(N)$ per test case |
| **Space** | $O(N)$ |
| **Roadmap course** | Rise from 3* to 4* (Level 4) |

## Question

**Sereja and Arrays**

Sereja have an array that consist of <span class="tex-span">*n*</span> integers <span class="tex-span">*a*_1</span>, <span class="tex-span">*a*_2</span>, <span class="tex-span">...</span>, <span class="tex-span">*a*_*n*</span> <span class="tex-span">(0 ≤ *a*_*i* ≤ 1)</span>. Sereja can make next operation:
-  fix some integer <span class="tex-span">*i*</span> <span class="tex-span">(1 ≤ *i* ≤ *n* - *k* + 1)</span>
-  <span class="tex-span">

subtract *1*</span> from values: <span class="tex-span">*a*_*i*</span>, <span class="tex-span">*a*_*i* + 1</span>, <span class="tex-span">...</span>, <span class="tex-span">*a*_*i* + *k* - 1</span>

Sereja call array <span class="tex-span">*a*</span> <span class="tex-span">*good*</span> if it is possible to make some operations, that he can and get array that contain only zeros. Now Sereja interested in next question: how many good arrays <span class="tex-span">*a*</span> with length <span class="tex-span">*n*</span> exist?

**Input**

First line contain integer <span class="tex-span">*T*</span> — number of testcases. <span class="tex-span">*T*</span> tests follow. Each testcase is given by two integers <span class="tex-span">*n*</span> and <span class="tex-span">*k*</span>.

**Constraints**
 -  <span class="tex-span">1 ≤ *T* ≤ 10</span>
 -  <span class="tex-span">1 ≤ *k* ≤ *n* ≤ 10^5</span>

**Output**

For each testcase output answer modulo <span class="tex-span">10^9 + 7</span>.

**Note**

**Test #0-1(25 points) n  ≤ **15

**Test #2(25 points) n  ≤ **100

**Test #3(50 points) n  ≤ **100000

## Constraints

- 1 <= T <= 10.
- 1 <= k <= n <= 10^5.

## Sample

**Sample input**

```
3
3 3
5 2
5 1
```

**Sample output**

```
2
8
32
```

## Approach

An operation subtracts 1 from $K$ consecutive positions, and the entries are only 0 or 1, so no position may be covered twice: a good array is exactly a union of disjoint length-$K$ segments of ones. Equivalently every maximal run of ones has a length divisible by $K$, and cutting such a run into consecutive blocks of $K$ is unique.

So good arrays of length $n$ correspond one-to-one to tilings of a strip of length $n$ with tiles `0` (length 1) and `11...1` (length $K$):

$$f(i) = f(i-1) + f(i-K), \qquad f(i) = 1 \text{ for } i < K.$$

## Solution (Python)

```python
import sys


def main() -> None:
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    out = []
    for _ in range(next(tokens)):
        n, k = (next(tokens), next(tokens))
        ways = [1] * (n + 1)
        for i in range(k, n + 1):
            ways[i] = (ways[i - 1] + ways[i - k]) % 1000000007
        out.append(str(ways[n]))
    print('\n'.join(out))


if __name__ == "__main__":
    main()
```

## Complexity

- **Time:** $O(N)$ per test case
- **Space:** $O(N)$
- Auxiliary space excludes the buffered input and output.

## Edge cases

- $K = 1$: both tiles have length 1 and are different, so the count is $2^n$ - the recurrence gives exactly that.
- $K = n$: only all zeros or all ones, answer 2.
- $i < K$: only the all-zero array, answer 1.
- Reduce modulo $10^9 + 7$ at every step.

## Dry run

`n = 5, K = 2`: $f = 1, 1, 2, 3, 5, 8$ for $i = 0 \dots 5$, the Fibonacci numbers. Answer 8.

`n = 3, K = 3`: $f(3) = f(2) + f(0) = 2$ - the arrays `000` and `111`.

---

Same problem in rating order (#566 of 735): [../../by-rating/566-SEARRAYS.md](../../by-rating/566-SEARRAYS.md)
