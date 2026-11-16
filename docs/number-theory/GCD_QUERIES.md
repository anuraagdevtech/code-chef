[&larr; 715. Chef and Riffles](RIFFLES.md) &middot; [Index](../../README.md) &middot; [731. Squarified &rarr;](SQUAR.md)

# 724. GCD Queries

> CodeChef problem code [`GCD_QUERIES`](https://www.codechef.com/problems/GCD_QUERIES) &middot; difficulty **2422** &middot; time limit **2.5s**

| | |
|---|---|
| **Topic** | Number Theory |
| **Technique** | One min-heap of sorted indices per prime, with lazy deletion |
| **Time** | $O(V \log \log V + (N + Q) \log V \log N)$ |
| **Space** | $O(V + N \log V)$ |
| **Roadmap course** | 2000 to 2500 difficulty problems (Level 5) |

## Question

You are given an array $A$ consisting of $N$ integers along with $Q$ queries.

For each query:
- $X$ : Given an integer $X$, print and **remove** the **minimum** element in the array $k$, such that $\texttt{gcd} (X, k) \gt 1$, where $\texttt{gcd}$ denotes the [greatest common divisor](https://en.wikipedia.org/wiki/Greatest_common_divisor).
If no value present in the array satisfies the condition, print and remove the **minimum** element of the array.

**Input**

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of multiple lines of input.
    - The first line of each test case consists of a single integer $N$ — the number of elements in the array.
    - The second line of each test case contains $N$ space-separated integers $A_1,A_2,\ldots,A_N$ — the elements of the array $A$.
    - The third line contains one integer $Q$, denoting the number of queries.
    - The next line contains $Q$ space-separated integers, where the $i^{th}$ integer is $X_i$, denoting the $i^{th}$ query.

**Output**

For each test case, print $Q$ space-separated integers denoting the answer to each query.

## Constraints

- $1 \leq T \leq 10^5$
- $1 \leq Q \leq N \leq 2 \cdot 10^5$
- $1 \leq A_i, X_i \leq 10^6$
- The sum of $N$ over all test cases won't exceed $2 \cdot 10^5$.
- The sum of $Q$ over all test cases won't exceed $2 \cdot 10^5$.

## Sample

**Sample input**

```
1
5
2 9 3 15 10
4
2 2 3 7
```

**Sample output**

```
2 10 3 9
```

<details><summary>Explanation</summary>

**Test case $1$:** The given array is $[2, 9, 3, 15, 10]$ and there are $4$ queries:
- Query $1$: Given $X = 2$. The elements $2$ and $10$ satisfy the condition. Since $2$ is smaller, we print and remove $2$ from array. The array becomes $A = [9, 3, 15, 10]$.
- Query $2$: Given $X = 2$. The element $10$ satisfies the condition. We print and remove $10$ from array. The array becomes $A = [9, 3, 15]$.
- Query $3$: Given $X = 3$. The elements $3$ and $9$ satisfy the condition. Since $3$ is smaller, we print and remove $3$ from array. The array becomes $A = [9, 15]$.
- Query $4$: Given $X = 7$. No element satisfies the condition, so we have to select $9$ since it is the smallest element present. We print and remove $9$ from array. The array becomes $A = [15]$.

</details>

## Approach

$\gcd(X, k) > 1$ exactly when $X$ and $k$ share a prime factor. Sort the array; then "the minimum element" means "the smallest sorted index", and ties between equal values do not matter.

For every prime $p$ keep a list of the sorted indices of the elements divisible by $p$. Indices are appended in increasing order, so each list is already a valid min-heap. A smallest-prime-factor sieve up to $10^6$ factorises any number into its distinct primes in $O(\log V)$.

For a query $X$, look at the heap of each prime factor of $X$: discard removed indices from its top, and take the smallest live top over all those heaps. If none of the heaps has a live element, fall back to the globally smallest live index, found with a pointer that only moves forward. Mark the chosen index as removed and print its value.

An element sits in several heaps; it is removed physically from each only when it reaches the top, so every heap entry is popped at most once.

## Solution (Python)

```python
import sys
import heapq


spf = list(range(1000001))
for i in range(2, 1001):
    if spf[i] == i:
        for j in range(i * i, 1000001, i):
            if spf[j] == j:
                spf[j] = i


def solve(tokens):
    n = next(tokens)
    values = sorted((next(tokens) for _ in range(n)))
    heaps = {}

    def factors(number):
        while number > 1:
            prime = spf[number]
            yield prime
            while number % prime == 0:
                number //= prime
    for i, number in enumerate(values):
        for prime in factors(number):
            heaps.setdefault(prime, []).append(i)
    alive = bytearray(b'\x01') * n
    first_alive = 0
    out = []
    q = next(tokens)
    for _ in range(q):
        number = next(tokens)
        best = n
        for prime in factors(number):
            heap = heaps.get(prime)
            if heap:
                while heap and (not alive[heap[0]]):
                    heapq.heappop(heap)
                if heap:
                    best = min(best, heap[0])
        if best == n:
            while not alive[first_alive]:
                first_alive += 1
            best = first_alive
        alive[best] = 0
        out.append(str(values[best]))
    return ' '.join(out)


if __name__ == "__main__":
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    t = int(next(tokens))
    out = [solve(tokens) for _ in range(t)]
    sys.stdout.write('\n'.join(out))
```

## Complexity

- **Time:** $O(V \log \log V + (N + Q) \log V \log N)$
- **Space:** $O(V + N \log V)$
- Auxiliary space excludes the buffered input and output.

## Edge cases

- $X = 1$ has no prime factors and always takes the global minimum.
- Elements equal to 1 are in no heap and can only be removed by the fallback.
- $Q \le N$, so the array never runs out.
- The sieve is shared by all test cases.

## Dry run

`A = [2, 9, 3, 15, 10]`, sorted `2 3 9 10 15`. Heaps: prime 2 -> `{2, 10}`, prime 3 -> `{3, 9, 15}`, prime 5 -> `{10, 15}`.

- `X = 2`: heap of 2 gives 2. Remove it.
- `X = 2`: heap of 2 now gives 10. Remove it.
- `X = 3`: heap of 3 gives 3.
- `X = 7`: no heap for 7, so the global minimum 9.

Output `2 10 3 9`.

> CodeChef tags: `Mathematics`, `Number Theory`, `Integer Factorisation`, `Divisors`

---

Same problem in rating order (#688 of 735): [../../by-rating/688-GCD_QUERIES.md](../../by-rating/688-GCD_QUERIES.md)
