[&larr; 597. Kirito in labyrinth](KIRLAB.md) &middot; [Index](../../README.md) &middot; [624. Maximum Factors Problem &rarr;](MXFACS.md)

# 607. Odd Binomial Coefficients

> CodeChef problem code [`ODDBIN`](https://www.codechef.com/problems/ODDBIN) &middot; difficulty **2107** &middot; time limit **0.919425s**

| | |
|---|---|
| **Topic** | Number Theory |
| **Technique** | Polynomials over GF(2) split at the highest exponent bit |
| **Time** | $O(60 \cdot 2^{M} \cdot M)$ worst case per test case with memoisation, $M \le 15$ |
| **Space** | $O(60 \cdot 2^{M})$ worst case |
| **Roadmap course** | Rise from 3* to 4* (Level 4) |

## Question

If P(x) is a polynomial in x with integer coefficients, let W(P(x)) = number of odd coefficients of P(x).

Given a_1, a_2, ... , a_m, find W( (1+x)^a_1 + (1+x)^a_2 + ... + (1+x)^a_m ).

**Input**

First line contains TC, the number of test cases.
Each test case consists of a single line in the format:
m a_1 a_2 ... a_m

****Limits****

1 <= m <= 15
0 <= a_i < 2^60
1 <= TC <= 1000

**Output**

Output one line per test case, the value W( (1+x)^a_1 + (1+x)^a_2 + ... + (1+x)^a_m ).

## Constraints

- 1 <= TC <= 1000.
- 1 <= m <= 15.
- 0 <= a_i < 2^60.

## Sample

**Sample input**

```
4
1 1
1 3
2 1 3
3 1 2 3
```

**Sample output**

```
2
4
2
2
```

<details><summary>Explanation</summary>

```
(1+x) + (1+x)^3 = 2 + 4x + 3x^2 + x^3. Hence the output for "2 1 3" is 2. (2 odd coefficients)
(1+x) + (1+x)^2 + (1+x)^3 = 3 + 6x + 4x^2 + x^3. Hence the output for "3 1 2 3" is 2.

```

</details>

## Approach

Only parities matter, so work with polynomials over GF(2). Two equal exponents cancel, so first reduce the list to the set of exponents that occur an odd number of times.

Over GF(2), $(1+x)^{2^b} = 1 + x^{2^b}$. Let $2^b$ be the highest bit of the largest exponent and split the set into the exponents that have this bit (group $H$, with the bit removed) and those that do not (group $L$). Then

$$\sum (1+x)^{a} = P_L(x) + (1 + x^{2^b}) P_H(x),$$

where both $P_L$ and $P_H$ have degree below $2^b$. The coefficients below $x^{2^b}$ are those of $P_L + P_H$, and the coefficients from $x^{2^b}$ up are those of $P_H$, so

$$W = W(P_L + P_H) + W(P_H).$$

$P_L + P_H$ is again a sum of powers of $(1+x)$, over the symmetric difference of the two exponent sets, so the same routine recurses on smaller exponents. A single exponent $a$ contributes $2^{\text{popcount}(a)}$ odd coefficients by Lucas' theorem, and an empty set contributes 0.

## Solution (Python)

```python
import sys
from functools import lru_cache


def main() -> None:
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    out = []
    for _ in range(next(tokens)):
        count = next(tokens)
        exponents = set()
        for _ in range(count):
            x = next(tokens)
            if x in exponents:
                exponents.remove(x)
            else:
                exponents.add(x)

        @lru_cache(None)
        def solve(values):
            if not values:
                return 0
            if len(values) == 1:
                return 1 << values[0].bit_count()
            bit = 1 << values[-1].bit_length() - 1
            low = set()
            high = []
            for x in values:
                if x & bit:
                    high.append(x ^ bit)
                    x ^= bit
                if x in low:
                    low.remove(x)
                else:
                    low.add(x)
            return solve(tuple(sorted(low))) + solve(tuple(high))
        out.append(str(solve(tuple(sorted(exponents)))))
    print('\n'.join(out))


if __name__ == "__main__":
    main()
```

## Complexity

- **Time:** $O(60 \cdot 2^{M} \cdot M)$ worst case per test case with memoisation, $M \le 15$
- **Space:** $O(60 \cdot 2^{M})$ worst case
- Auxiliary space excludes the buffered input and output.

## Edge cases

- Equal exponents cancel in pairs, so `2 5 5` gives 0.
- An exponent 0 is the constant polynomial 1 and is handled by the single-exponent rule ($2^0 = 1$).
- Exponents go up to about $2^{60}$, so nothing can be expanded explicitly.
- The memo is keyed by the sorted tuple of exponents; identical sub-problems appear often after the symmetric difference.

## Dry run

Exponents `{1, 3}`. The highest bit of 3 is 2.

- $H$: 3 has the bit, leaving 1, so $H = \{1\}$.
- $L$ together with $H$ by symmetric difference: 1 (from $L$) and 1 (from $H$) cancel, leaving the empty set.

$W = W(\emptyset) + W(\{1\}) = 0 + 2^{1} = 2$, matching $(1+x) + (1+x)^3 = 2 + 4x + 3x^2 + x^3$.

---

Same problem in rating order (#610 of 735): [../../by-rating/610-ODDBIN.md](../../by-rating/610-ODDBIN.md)
