[&larr; 646. Array Sum](SUMARRAY.md) &middot; [Index](../../README.md) &middot; [653. Non Zero Subarray Xor &rarr;](SUBARRAYXOR.md)

# 652. LCM Mania

> CodeChef problem code [`LCMMANIA`](https://www.codechef.com/problems/LCMMANIA) &middot; difficulty **2098** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Constructive |
| **Technique** | Three explicit families, impossible only for powers of two |
| **Time** | $O(1)$ per test case |
| **Space** | $O(1)$ |
| **Roadmap course** | 2000 to 2500 difficulty problems (Level 5) |

## Question

hErd gives you an integer $N$. Find any three **positive** integers $A, B, C$ such that:
- $N = lcm(A,B) + lcm(B,C) + lcm(C,A)$; where $lcm$ denotes the [least common multiple](https://en.wikipedia.org/wiki/Least_common_multiple).

If there is no solution, print $-1$.
If there are multiple solutions, you may print any of them.

**Input**

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- The first and only line of each test case contains an integer $N$.

**Output**

For each test case, output on a new line, three space-separated integers $A, B, C$ satisfying the condition.

If there is no solution, print $-1$.
If there are multiple solutions, you may print any of them.

## Constraints

- $1 \leq T \leq 10^5$
- $1 \leq N \leq 10^{9}$

## Sample

**Sample input**

```
3
1
6
15
```

**Sample output**

```
-1
2 2 2
5 5 1
```

<details><summary>Explanation</summary>

**Test case $1$:** It can be shown that no solution exists.

**Test case $2$:** Consider $A=2 , B=2, C=2$. Thus, $6 = lcm(2,2) + lcm(2,2) + lcm(2,2)$.

**Test case $3$:** Consider $A=5 , B=5, C=1$. Thus, $15 = lcm(5,5) + lcm(5,1) + lcm(5,1)$.
Note that $(5,5,1), (1,5,5)$ and $(5,1,5)$ are all considered valid.

</details>

## Approach

Three constructions cover almost everything:

- $N$ divisible by 3: $A = B = C = N/3$ gives $3 \cdot N/3$.
- $N$ odd, $N \ge 3$: $(1, 1, (N-1)/2)$ gives $1 + 2 \cdot (N-1)/2 = N$.
- $N = 2^a \cdot m$ with $m$ odd and $m \ge 3$: scale the previous idea by $2^a$: $(2^a, 2^a, 2^a (m-1)/2)$ gives $2^a + 2 \cdot 2^a (m-1)/2 = 2^a m$.

What is left are $N < 3$ and the powers of two, and those are impossible. Sort the exponents of 2 in $A, B, C$ as $x \le y \le z$; the three lcms then have exponents $y, z, z$. If $y < z$ the sum is $2^y$ times (odd + even), an odd number that is at least $1 + 2 + 2 = 5$; if $y = z$ it is $2^y$ times a sum of three odd numbers, an odd number at least 3. Either way the sum has an odd factor greater than 1.

## Solution (Python)

```python
import sys


def main() -> None:
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    out = []
    for _ in range(next(tokens)):
        n = next(tokens)
        if n < 3:
            out.append('-1')
        elif n % 3 == 0:
            out.append(f'{n // 3} {n // 3} {n // 3}')
        elif n % 2:
            out.append(f'1 1 {(n - 1) // 2}')
        else:
            power = n & -n
            odd_part = n // power
            out.append('-1' if odd_part == 1 else f'{power} {power} {power * ((odd_part - 1) // 2)}')
    print('\n'.join(out))


if __name__ == "__main__":
    main()
```

## Complexity

- **Time:** $O(1)$ per test case
- **Space:** $O(1)$
- Auxiliary space excludes the buffered input and output.

## Edge cases

- $N = 1, 2$: three positive lcms sum to at least 3.
- Powers of two (4, 8, 16, ...) have no solution.
- Multiples of 3 that are also even are handled by the first rule.
- Any valid triple is accepted.

## Dry run

- `N = 6`: divisible by 3 - `2 2 2`.
- `N = 7`: odd - `1 1 3`: $1 + 3 + 3 = 7$.
- `N = 20 = 4 * 5`: `4 4 8`: $4 + 8 + 8 = 20$.
- `N = 8`: a power of two - `-1`.

---

Same problem in rating order (#606 of 735): [../../by-rating/606-LCMMANIA.md](../../by-rating/606-LCMMANIA.md)
