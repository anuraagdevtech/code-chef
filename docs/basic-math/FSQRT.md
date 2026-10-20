# 47. Finding Square Roots

> CodeChef problem code [`FSQRT`](https://www.codechef.com/problems/FSQRT) &middot; difficulty **420** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Basic Math |
| **Technique** | Exact integer square root |
| **Time** | $O(1)$ per test case in practice |
| **Space** | $O(1)$ |
| **Roadmap course** | 500 to 1000 difficulty rating (Level 1) |

## Question

*In olden days finding square roots seemed to be difficult but nowadays it can be easily done using in-built functions available across many languages *
.

Assume that you happen to hear the above words and you want to give a try in finding the square root of any given integer using in-built functions. So here's your chance.

**Input**

The first line of the input contains an integer T, the number of test cases. T lines follow. Each line contains an integer N whose square root needs to be computed.

**Output**

For each line of the input, output the square root of the input integer, rounded down to the nearest integer, in a new line.

**Constraints**

1<=T<=20

1<=N<=10000

## Constraints

1<=T<=20
1<=N<=10000

## Sample

**Sample input**

```
3
10
5
10000
```

**Sample output**

```
3
2
100
```

## Approach

The task is $\lfloor \sqrt{N} \rfloor$. The obvious `int(math.sqrt(n))` passes here, but it is the wrong habit and the reason is worth understanding.

`math.sqrt` returns a 64-bit float. For a perfect square the true root is representable exactly, but the computed result can land a hair below it — so `math.sqrt(x*x)` may evaluate to something like $k - 10^{-9}$, and truncating yields $k - 1$. The failure only appears for large $N$, which makes it a nasty bug: it passes every small test and breaks in the one case the problem cares about.

`math.isqrt`, added in Python 3.8, is the correct tool. It works entirely in integers and is *defined* to return the exact floor of the square root for any non-negative `int`, with no floating point anywhere. It is also the only version that stays correct once $N$ exceeds $2^{53}$, where floats can no longer represent consecutive integers.

With $N \leq 10^4$ here neither approach can actually fail, so this problem is really a vocabulary lesson: reach for `isqrt` whenever an integer square root is wanted.

Sample case 3 is the perfect square $10000 \to 100$, exactly the shape that would expose a float rounding error at larger magnitudes.

## Solution (Python)

```python
import math
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    # isqrt is exact; int(math.sqrt(n)) can round a perfect square down by one.
    out = [str(math.isqrt(int(data[1 + i]))) for i in range(t)]
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(1)$ per test case in practice
- **Space:** $O(1)$

> CodeChef tags: `Basic Programming Concepts`
