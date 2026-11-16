[&larr; 507. Again XOR problem](KLXOR.md) &middot; [Index](../../README.md) &middot; [604. Little Elephant and Median &rarr;](MEDIAN.md)

# 598. Offer for Chef

> CodeChef problem code [`CHEFOFR`](https://www.codechef.com/problems/CHEFOFR) &middot; difficulty **2100** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Bit Manipulation |
| **Technique** | Greedy on answer bits with a partition DP over cluster counts |
| **Time** | $O(Q \cdot B \cdot P^2)$ with $P \le 50$ topped slices and $B$ bits in the total sweetness |
| **Space** | $O(P)$ big integers |
| **Roadmap course** | Rise from 3* to 4* (Level 4) |

## Question

Chef is very happy today because he got an offer from Gordon Ramsay himself to work for him in London. Chef wants to prepare a delicious cake for Gordon to impress him, but he does not know that Gordon Ramsay is not easy to impress.

Gordon cut Chef's cake into $N$ small slices (numbered $1$ through $N$), placed in a row in such a way that for each valid $i$, slices $i$ and $i+1$ are adjacent. Note that slices $N$ and $1$ are **not** adjacent. For each valid $i$, the $i$-th slice has *taste* $A_i$. Gordon wants to put special toppings on some slices and then ask Chef to group all slices into $K$ clusters in such a way that the slices in each cluster form a contiguous sequence and the *sweetness* of the cake is maximum possible.

For each valid $i$, let's denote the topping on the $i$-th slice by $t_i$ ($t_i = 0$ if there is no topping on this slice); the *sweetness* of this slice is $t_i \cdot A_i$, so the sweetness of a slice without any special topping is $0$.

The sweetness of a cluster is the total (summed up) sweetness of all slices in this cluster. Let's denote the sweetnesses of all clusters by $S_1, S_2, \ldots, S_K$. The sweetness of the whole cake is computed as $S_1 * S_2 * \ldots * S_K$, where the operation $*$ is defined in the following way: for any non-negative integers $x$ and $y$ such that $x \ge y$,
$$x * y = y * x = \sum_{n=0}^{\lfloor\log_2(x)\rfloor} 2^n\left(\left\lfloor\frac{x}{2^n}\right\rfloor \bmod 2\right)\left(\left\lfloor\frac{y}{2^n}\right\rfloor \bmod 2\right) \,.$$
It can be proven that this operation is associative, i.e. $(x * y) * z = x * (y * z)$.

You should answer $Q$ queries. In each query, you are given the toppings on all slices and the number of clusters $K$. Tell Chef the maximum possible sweetness of the cake!

**Input**
- The first line of the input contains a single integer $N$.
- The second line contains $N$ space-separated integers $A_1, A_2, \ldots, A_N$.
- The next line contains a single integer $Q$.
- For each query, two lines follow. The first of these lines contains a single integer $K$. The second line contains $N$ space-separated integers $t_1, t_2, \ldots, t_N$.

**Output**
Print a single line containing one integer — the maximum sweetness.

**Constraints**
- $1 \le Q \le 10$
- $1 \le N \le 10^5$
- $1 \le K \le 10^5$
- $1 \le A_i \le 10^{15}$ for each valid $i$
- $0 \le t_i \le 10$ for each valid $i$
- in each query, the number of slices with toppings does not exceed $50$

**Subtasks**
**Subtask #1 (100 points):** original constraints

## Constraints

- $1 \le Q \le 10$
- $1 \le N \le 10^5$
- $1 \le K \le 10^5$
- $1 \le A_i \le 10^{15}$ for each valid $i$
- $0 \le t_i \le 10$ for each valid $i$
- in each query, the number of slices with toppings does not exceed $50$

## Sample

**Sample input**

```
10
15 5 26 4 3 13 5 5 27 11
2
3
2 3 1 4 7 1 5 1 1 1
1
0 0 0 0 0 0 0 1 0 0
```

**Sample output**

```
33
5
```

<details><summary>Explanation</summary>

For the first query, Chef can choose clusters in the following way: cluster $1$ contains slices $1$ and $2$, cluster $2$ contains slices $3$ through $7$ and cluster $3$ contains slices $8$ through $10$. The sweetness of the cake is $(15 \cdot 2 + 5 \cdot 3) * (26 \cdot 1 + 4 \cdot 4 + 3 \cdot 7 + 13 \cdot 1 + 5 \cdot 5) * (5 \cdot 1 + 27 \cdot 1 + 11 \cdot 1) = 33$.

</details>

## Approach

Only slices with a topping matter - the statement guarantees there are few of them - and a slice with sweetness 0 can be attached to a neighbouring cluster without changing any sum. If $K$ exceeds the number of sweet slices some cluster has sweetness 0 and the AND is 0; if $K = 1$ the answer is the total.

Otherwise build the answer bit by bit from the top. Suppose the bits chosen so far form `ans`; try `mask = ans | bit`. The AND of all clusters contains `mask` exactly when every cluster sum contains `mask`, so the question is whether the positive values can be cut into exactly $K$ contiguous groups whose sums are all supersets of `mask`.

That is a partition DP over prefixes: `dp[r]` is a bitset of the possible numbers of groups for the first $r$ values, and `dp[r] |= dp[l] << 1` for every $l < r$ with `(prefix[r] - prefix[l]) & mask == mask`. Keep the bit if bit $K$ of `dp[m]` is set.

## Solution (Python)

```python
import sys


def main() -> None:
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    n = next(tokens)
    taste = [next(tokens) for _ in range(n)]
    out = []
    for _ in range(next(tokens)):
        k = next(tokens)
        values = []
        for x in taste:
            t = next(tokens)
            if t:
                values.append(t * x)
        if k > len(values):
            out.append('0')
            continue
        if k == 1:
            out.append(str(sum(values)))
            continue
        prefix = [0]
        for x in values:
            prefix.append(prefix[-1] + x)
        count = len(values)
        answer = 0
        for bit in range(prefix[-1].bit_length() - 1, -1, -1):
            mask = answer | 1 << bit
            reachable = [0] * (count + 1)
            reachable[0] = 1
            for right in range(1, count + 1):
                possibilities = 0
                for left in range(right):
                    if prefix[right] - prefix[left] & mask == mask:
                        possibilities |= reachable[left] << 1
                reachable[right] = possibilities
            if reachable[count] >> k & 1:
                answer = mask
        out.append(str(answer))
    print('\n'.join(out))


if __name__ == "__main__":
    main()
```

## Complexity

- **Time:** $O(Q \cdot B \cdot P^2)$ with $P \le 50$ topped slices and $B$ bits in the total sweetness
- **Space:** $O(P)$ big integers
- Auxiliary space excludes the buffered input and output.

## Edge cases

- Fewer than $K$ sweet slices: answer 0.
- $K = 1$: the single cluster is everything, no bit search needed.
- Clusters must be contiguous in the original row, which the compressed list preserves.
- Sums can be far larger than 32 bits, so the bit loop starts from the bit length of the total rather than a fixed 30.

## Dry run

First sample query: $K = 3$, sweetness values `30 15 26 16 21 13 25 5 27 11`.

Testing bits from the top, bit 5 (32) can be kept: the split `45 | 101 | 43` has all three sums containing 32. Lower bits are then tested against masks containing 32; only bit 0 survives, because 45, 101 and 43 are all odd, while no three-way split keeps 32 together with any of 16, 8, 4 or 2.

$45 \mathbin{\&} 101 \mathbin{\&} 43 = 33$.

---

Same problem in rating order (#607 of 735): [../../by-rating/607-CHEFOFR.md](../../by-rating/607-CHEFOFR.md)
