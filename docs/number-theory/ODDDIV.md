[&larr; 563. Prime Tuples](PTUPLES.md) &middot; [Index](../../README.md) &middot; [565. Number of Factors &rarr;](NUMFACT.md)

# 564. Odd Divisors

> CodeChef problem code [`ODDDIV`](https://www.codechef.com/problems/ODDDIV) &middot; difficulty **1657** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Number Theory |
| **Technique** | Add every odd divisor to its multiples |
| **Time** | $O(V\log V+T)$ overall for $V=\max R$ |
| **Space** | $O(V+T)$ |
| **Roadmap course** | Rise from 3* to 4* (Level 4) |

## Question

Little Egor likes to play with positive integers and their divisors. Bigger the number to play with, more the fun! The boy asked you to come up with an algorithm, that could play the following game:

Let's define **f(n)** as the sum of all odd divisors of **n**. I.e. **f(10) = 1 + 5 = 6** and **f(21) = 1 + 3 + 7 + 21 = 32**. The game is to calculate **f(l) + f(l + 1) + ... + f(r - 1) + f(r)** for the given integers **l** and **r**.

Have fun! But be careful, the integers might be quite big.

**Input**

The first line of the input contains one integer **T** denoting the number of test cases.

The only line of the test case description contains two positive integers **l** and **r**.

**Output**

For each test case, output the required sum on a separate line.

**Constraints**

- **1 ≤ T ≤ 10**

- **1 ≤ l ≤ r ≤ 10^5**

## Constraints

- 1 ≤ T ≤ 10
- 1 ≤ l ≤ r ≤ 10^5

## Sample

**Sample input**

```
2
1 10
42 42
```

**Sample output**

```
45
32
```

<details><summary>Explanation</summary>

In the first example case, **f(1) + f(2) + ... + f(10) = 1 + 1 + 4 + 1 + 6 + 4 + 8 + 1 + 13 + 6 = 45**

In the second example case, **f(42) = 32**.

</details>

## Approach

For each odd positive integer $d$, add $d$ to every multiple of $d$. After this divisor sieve, entry $f[n]$ is exactly the sum of odd divisors of $n$. A prefix sum over $f$ answers each interval as `prefix[r]-prefix[l-1]`.

## Solution (Python)

```python
import sys


def main() -> None:
    values = list(map(int,sys.stdin.buffer.read().split()))
    queries = list(zip(values[1::2],values[2::2]))
    limit = max(r for _,r in queries)
    sums = [0]*(limit+1)
    for d in range(1,limit+1,2):
        for multiple in range(d,limit+1,d):
            sums[multiple] += d
    for n in range(1,limit+1):
        sums[n] += sums[n-1]
    sys.stdout.write('\n'.join(str(sums[r]-sums[l-1]) for l,r in queries)+'\n')

if __name__ == '__main__':
    main()
```

## Complexity

- **Time:** $O(V\log V+T)$ overall for $V=\max R$
- **Space:** $O(V+T)$
- Auxiliary space excludes the buffered input and output.

## Edge cases

- Include divisor one.
- Powers of two have odd-divisor sum one.
- The left endpoint may be one, using prefix entry zero.

## Dry run

For the singleton range `[42,42]`, odd divisors are `1,3,7,21`, summing to 32. For `[1,10]`, the prefix sum is 45.

---

Same problem in rating order (#401 of 735): [../../by-rating/401-ODDDIV.md](../../by-rating/401-ODDDIV.md)
