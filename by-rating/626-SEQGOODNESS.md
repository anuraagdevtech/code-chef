[&larr; 625. Minimize swaps](625-DIVBY3.md) &middot; [Index](README.md) &middot; [627. Minimum Operation &rarr;](627-MINIMUMOP.md)

# 626. Sum of Goodness

> [`SEQGOODNESS`](https://www.codechef.com/problems/SEQGOODNESS) &middot; difficulty **2167** &middot; time limit **1s** &middot; 2000 to 2500 difficulty problems (Level 5)

## Topic used

| | |
|---|---|
| **Topic** | Combinatorics |
| **Technique** | Each value contributes a difference of two binomial tails, maintained incrementally |
| **CodeChef tags** | `Algorithms`, `Mathematics`, `Number Theory`, `Modular Arithmetic`, `Sorting` |
| **Complexity class** | Linear $O(n)$ (one-off precomputation) |
| **Time** | $O(N)$ per test case after $O(\max N)$ precomputation |
| **Space** | $O(\max N)$ |

## Question

You are given an array $A = A_1, A_2, \ldots, A_N$ of size $N$.

Consider a subsequence $S = S_1, S_2, \ldots, S_M$ of $A$. Let us define the *Goodness* of subsequence $S$ as follows:

 - Sort the subsequence $S$ in non-decreasing order.
 - Then, the *Goodness* of subsequence $S$ is the number of indices such that $S_i = i,$ where
  $(1 \le i \le |S|).$

For example, suppose $A = [ 10, 3, 2, 5, 11, 3, 1, 12 ]$, and the subsequence is $S = [ 3, 2, 5, 3, 1 ]$. After sorting, $S = [ 1, 2, 3, 3, 5 ]$, and so the *Goodness*  of $S$ is $4$.

Consider all the $2^N - 1$ possible non-empty subsequences of array $A$, and find the sum of all their *Goodness*.

Since the answer can be large, output the answer modulo $10^9 + 7.$

**Note:** A sequence $S$ is a *subsequence* of array $A$ if $S$ can be obtained from $A$ by deletion of several (possibly, zero) elements. For example, $[3,1]$ is a subsequence of $[3,2,1]$ and $[4,3,1]$, but not a subsequence of $[1,3,3,7]$ and $[3,10,4]$.

**Input**

- The first line of input will contain a single integer $T$, denoting the number of test cases. Then the test cases follow.
- The first line of each test case contains an integer $N$ - the size of the array $A$.
- The second line of each test case contains $N$ space-separated integers, $A_1, A_2, A_3,..., A_N.$

**Output**

For each test case, output the answer modulo $10^9 + 7$.

## Constraints

- $1 \leq T \leq 10^5$
- $1 \leq N \leq 10^5$
- $1 \leq A_i \leq N $ for each $1 \leq i \leq N$.
- The sum of $N$ over all test cases does not exceed $2 \cdot 10^5$

## Sample

**Sample input**

```
4
2
1 2
5
3 2 5 5 3
4
1 1 2 1
6
6 4 5 2 3 1
```

**Sample output**

```
3
5
17
63
```

<details><summary>Explanation</summary>

**Testcase 1:** The given array is $[1, 2]$. There are 3 possible non-empty subsequences:
- $[1]$. The *Goodness* of this subsequence is $1$, since $S_1 = 1$.
- $[2]$. The *Goodness* of this subsequence is $0$.
- $[1, 2]$. The *Goodness* of this subsequence is $2$, since $S_1 = 1$ and $S_2 = 2$.

Thus the total sum is $1 + 0 + 2 = 3$, which is the answer.

</details>

## Approach

In the sorted subsequence, the positions holding the value $v$ form a contiguous block, and position $v$ lies in that block exactly when

$$\#\{\text{chosen} < v\} < v \le \#\{\text{chosen} \le v\}.$$

Every value contributes at most one to the goodness, so the total is the sum over $v$ of the number of subsequences satisfying this. Because "at least $v$ chosen below $v$" implies "at least $v$ chosen up to $v$", that number is the difference of two tail counts. With $c_v$ the number of array elements $\le v$,

$$\text{count}(v) = \#\{\text{subsets with} \ge v \text{ of the } c_v\} - \#\{\text{subsets with} \ge v \text{ of the } c_{v-1}\}.$$

Work with probabilities (divide by $2^N$) so the unrelated elements disappear. Let $T(m, t) = \Pr[\text{Bin}(m, \tfrac12) \ge t]$. It can be updated in $O(1)$ in both arguments:

- adding one element: $T(m+1, t) = T(m, t) + \binom{m}{t-1} / 2^{m+1}$;
- raising the threshold: $T(m, t+1) = T(m, t) - \binom{m}{t} / 2^{m}$.

Sweep $v$ upwards: add the elements equal to $v$ one at a time, record the increase of the tail (this is the difference above), then raise the threshold for the next value. Multiply the final sum by $2^N$.

## Solution

```python
import sys


def main() -> None:
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    out = []
    MOD = 10 ** 9 + 7
    mx = 100000
    fact = [1] * (mx + 1)
    inv_fact = [1] * (mx + 1)
    pow2 = [1] * (mx + 1)
    inv_pow2 = [1] * (mx + 1)
    half = (MOD + 1) // 2
    for i in range(1, mx + 1):
        fact[i] = fact[i - 1] * i % MOD
        pow2[i] = pow2[i - 1] * 2 % MOD
        inv_pow2[i] = inv_pow2[i - 1] * half % MOD
    inv_fact[mx] = pow(fact[mx], -1, MOD)
    for i in range(mx, 0, -1):
        inv_fact[i - 1] = inv_fact[i] * i % MOD

    def choose(n, k):
        return 0 if k < 0 or k > n else fact[n] * inv_fact[k] % MOD * inv_fact[n - k] % MOD
    for _ in range(next(tokens)):
        n = next(tokens)
        counts = [0] * (n + 1)
        for _ in range(n):
            counts[next(tokens)] += 1
        size = 0
        tail = 0
        total = 0
        for v in range(1, n + 1):
            old = tail
            for _ in range(counts[v]):
                tail = (tail + choose(size, v - 1) * inv_pow2[size + 1]) % MOD
                size += 1
            total = (total + tail - old) % MOD
            tail = (tail - choose(size, v) * inv_pow2[size]) % MOD
        out.append(str(total * pow2[n] % MOD))
    print('\n'.join(out))


if __name__ == "__main__":
    main()
```

## Edge cases

- Values larger than their own count can never sit at their index and add 0 automatically.
- Duplicates of $v$ are added one by one; each changes the tail.
- The empty subsequence has goodness 0, so including it does not matter.
- Inverse powers of two and factorials are precomputed once for all test cases.

## Dry run

`A = [1, 2]`.

- $v = 1$: tail $T(0, 1) = 0$. Add the element 1: $T(1, 1) = 0 + \binom{0}{0}/2 = 1/2$. Contribution $1/2$. Raise the threshold: $T(1, 2) = 1/2 - \binom{1}{1}/2 = 0$.
- $v = 2$: add the element 2: $T(2, 2) = 0 + \binom{1}{1}/4 = 1/4$. Contribution $1/4$.

Total $3/4$, times $2^2$ gives 3: `[1]` has goodness 1 and `[1, 2]` has goodness 2.

---

Same problem grouped by topic: [../docs/combinatorics/SEQGOODNESS.md](../docs/combinatorics/SEQGOODNESS.md)
