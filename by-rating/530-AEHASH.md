[&larr; 529. Ultimate Fencing](529-KEEPOUT.md) &middot; [Index](README.md) &middot; [531. Maximal Score Path &rarr;](531-RG_01.md)

# 530. A-E Hash Function

> [`AEHASH`](https://www.codechef.com/problems/AEHASH) &middot; difficulty **1832** &middot; time limit **0.5s** &middot; Rise from 3* to 4* (Level 4)

## Topic used

| | |
|---|---|
| **Topic** | Dynamic Programming |
| **Technique** | Memoised hash distributions per (length, number of A) with a max-convolution |
| **Complexity class** | Cubic or higher polynomial $O(n^3)$ and above |
| **Time** | $O(N \cdot A^2 \cdot H)$ in the worst case over all states, $H$ the largest hash value |
| **Space** | $O(N \cdot A \cdot H)$ for the memo table |

## Question

Chef Ash and Chef Elsh invented a new hash function! Their hash function will map a binary string consisting of characters 'A' and 'E' into an integer called the hash value of the string.

The pseudocode of the hash function is as below. hash(S) is the hash value of a binary string S. |S| denotes the length of S.

```
function hash(S):
	result = number of characters 'A' in S
	if |S| > 1:
		(S1, S2) = split(S)
		result = result + max(hash(S1), hash(S2))
	end if
	return result
end function
```

The function split in the above pseudocode takes a binary string S as the parameter and returns a pair of binary strings (S1, S2) such that:

- |S1| <= |S2|.

- The difference of |S1| and |S2| is at most 1.

- The concatenation of S1 and S2 (in that order) is S.

For example, split("AAAEE") returns ("AA", "AEE"), whereas split("AEAEAE") returns ("AEA", "EAE").

You doubt that this hash function have good distribution of different hash values. So, you wonder how many different binary strings consisting of A 'A' characters and E 'E' characters that have hash value of V.

**Input**

The first line contains a single integer T, the number of test cases. T test cases follow. Each testcase consists of a single line consisting of three integers A, E, and V.

**Output**

For each test case, output a single line consisting the number of different binary strings satisfying the rule, modulo 1000000007.

**Constraints**

- 1 ≤ T ≤ 1000

- 0 ≤ A ≤ 50

- 0 ≤ E ≤ 50

- 0 ≤ V ≤ 1000

## Constraints

- 1 ≤ T ≤ 1000
- 0 ≤ A ≤ 50
- 0 ≤ E ≤ 50
- 0 ≤ V ≤ 1000

## Sample

**Sample input**

```
4
0 0 0
1 0 1
3 2 6
4 2 8
```

**Sample output**

```
1
1
3
4
```

<details><summary>Explanation</summary>

For the last test case, the solutions are:
- AAEAAE

- AEAAAE

- AAEAEA

- AEAAEA

</details>

## Approach

The split depends only on the length, so the multiset of hash values of all strings with a given length $n$ and a given number $a$ of `A`s is a function of $(n, a)$ alone. Let `distribution(n, a)[v]` be the number of such strings with hash $v$.

For $n \le 1$ the hash equals $a$. Otherwise the left half has length $\lfloor n/2 \rfloor$; enumerate how many `A`s, $x$, go there. The hash is $a + \max(h_1, h_2)$, so we need the number of pairs (left string, right string) whose maximum hash is exactly $v$:

$$\#\{\max = v\} = f_v \cdot G_v + g_v \cdot F_{v-1},$$

with $F, G$ the running prefix sums of the two distributions. Only $O(\log N)$ distinct lengths ever appear, so the memo table is small and is shared by all test cases.

## Solution

```python
import sys
from functools import lru_cache


def main() -> None:
    MOD = 1000000007

    @lru_cache(None)
    def distribution(n, count_a):
        if count_a < 0 or count_a > n:
            return ()
        if n <= 1:
            return (1,) if count_a == 0 else (0, 1)
        left = n // 2
        right = n - left
        result = [0] * (count_a * (n.bit_length() + 1) + 1)
        for x in range(max(0, count_a - right), min(count_a, left) + 1):
            f = distribution(left, x)
            g = distribution(right, count_a - x)
            sf = sg = 0
            for v in range(max(len(f), len(g))):
                fv = f[v] if v < len(f) else 0
                gv = g[v] if v < len(g) else 0
                sg = (sg + gv) % MOD
                result[count_a + v] = (result[count_a + v] + fv * sg + gv * sf) % MOD
                sf = (sf + fv) % MOD
        while result and result[-1] == 0:
            result.pop()
        return tuple(result)
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    out = []
    for _ in range(next(tokens)):
        count_a, count_e, v = (next(tokens), next(tokens), next(tokens))
        table = distribution(count_a + count_e, count_a)
        out.append(str(table[v] if v < len(table) else 0))
    print('\n'.join(out))


if __name__ == "__main__":
    main()
```

## Edge cases

- Requests with $V$ larger than any achievable hash, or with impossible counts, answer 0.
- The single-character and empty strings are base cases: hash 1 for `A`, 0 otherwise.
- In the max-count formula the tie $h_1 = h_2 = v$ must be counted once - one side uses the inclusive prefix sum, the other the exclusive one.
- Counts are taken modulo $10^9 + 7$.

## Dry run

`A = 1, E = 1, V = 2`. Length 2 splits into two single characters.

- `AE`: halves hash to 1 and 0, so the hash is $1 + \max(1, 0) = 2$.
- `EA`: halves hash to 0 and 1, so the hash is again 2.

`distribution(2, 1) = [0, 0, 2]`, so the answer is 2.

---

Same problem grouped by topic: [../docs/dynamic-programming/AEHASH.md](../docs/dynamic-programming/AEHASH.md)
