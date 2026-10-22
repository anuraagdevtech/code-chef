# 464. Crushed Apples and a Balance Scale

> CodeChef problem code [`APP_BAL_SCA`](https://www.codechef.com/problems/APP_BAL_SCA) &middot; difficulty **1736** &middot; time limit **1.5s**

| | |
|---|---|
| **Topic** | Number Theory |
| **Technique** | Halving only reaches the odd part |
| **Time** | $O(\log M)$ per test case |
| **Space** | $O(1)$ |
| **Roadmap course** | 1600 to 1800 difficulty problems (Level 3) |

## Question

You are preparing for meals ahead of your busy night at Restaurant Deep Dishes. An essential ingredient is apples.

In your inventory, you have $M$ kilograms of crushed apples. Head Chef Sandeep needs exactly $N$ kilograms of crushed apples, but Chef Pal has lost the weighing machine. Instead, all that is left is a balance pan with two scales. You do not have any measuring weights with you either.

So you can only place some crushed apples on both sides of the balance, and the balance will tell you whether or not they are of equal weight. You don't get any more information from it.\
And peculiarly, it gives out an error if both sides are not integers. You don't know if they are equal or not in this case.

In other words, this is what you can do:
- You can take a known weight of apples and divide into two equal parts using the balance, if the two halves have integer weights.
- You can take crushed apples of a known integer weight and get another portion of crushed apples that weighs the same, using the balance. Of course you cannot do this if are exceeding the available $M$ kilograms.
- And of course, even without using the balance, you can combine together known weights to get a heavier known weight.

Chef Pal is asking for your help. Under these constraints, is it possible to get exactly $N$ kilograms of crushed apples? Note that when you start out, the only weight that you know is that the entire crushed apples weights $M$ kilograms.

**Input**

- The first line of the input contains one integer $T$, the number of test cases. The test cases follow.
- The only line of each testcase contains two integers $M$ and $N$, the kilograms of apples you have, and the kilograms of apples that you need to make, respectively.

**Output**

- For each test case, if it is possible to use the balance scale to get exactly $N$ kilograms from $M$ kilograms, output *YES*.
- If it is not possible, output *NO*.

Note: You can output the answer in any case (upper or lower). For example, the strings *yEs*, *yes*, *Yes*, and *YES* will be recognized as positive responses.

## Constraints

- $1 \leq T \leq 2 \cdot 10^{5}$
- $1 \leq M \leq 10^{18}$
- $1 \leq N \leq 10^{18}$

## Sample

**Sample input**

```
4
2 1
1 1
5 1
4 9
```

**Sample output**

```
YES
YES
NO
NO
```

<details><summary>Explanation</summary>

**Testcase 1:** You can take the $2$ kilograms of crushed apples, halve it to get two portions of $1$ kilogram each. And so you've got the $1$ kilogram needed. So the answer is "YES".

</details>

## Approach

The balance offers exactly three moves: halve a known weight when both halves are integers, duplicate a known weight, and add known weights together. None of them can produce a finer division than repeated halving, so the **smallest** weight reachable from $M$ is

$$q = \frac{M}{2^{\nu_2(M)}}$$

the odd part of $M$, obtained by halving as long as the result stays an integer. Everything reachable is a sum of pieces of size $q$ or multiples of it, so every achievable weight is a multiple of $q$. And duplication is capped by the stock on hand, so nothing above $M$ is reachable.

Conversely every multiple of $q$ up to $M$ *is* reachable: halve $M$ all the way down to $2^{\nu_2(M)}$ pieces of size $q$, then combine as many as needed. So

$$\text{answer} = \text{YES} \iff N \leq M \text{ and } q \mid N$$

The point is that the balance can only bisect, never trisect — which is why an odd $M$ is completely rigid: $q = M$, and the only reachable weight is $M$ itself.

The samples show all three failure-free and failure cases. $M = 2, N = 1$: one halving gives $1$. $M = N = 1$: nothing to do. $M = 5, N = 1$: $5$ is odd, so $q = 5$ and only $5$ is reachable — `NO`. And $M = 4, N = 9$ asks for more apples than exist.

With $M$ up to $10^{18}$ the halving loop runs at most $60$ times, so $T = 2 \times 10^5$ is comfortable.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        m, n = int(data[1 + 2 * i]), int(data[2 + 2 * i])
        # The balance only bisects, so the finest piece is M's odd part.
        unit = m
        while unit % 2 == 0:
            unit //= 2
        out.append("YES" if n <= m and n % unit == 0 else "NO")
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(\log M)$ per test case
- **Space:** $O(1)$

## Edge cases

- **A balance with no weights can only bisect**, so from $M$ the reachable amounts are sums of $M/2^j$ pieces — that is, $M p / 2^j$ for integers $p, j$.
- **So $N$ is reachable iff the odd part of $M$ divides $N$**, since the powers of two can always be supplied by halving far enough while the odd factor can never be split.
- **$N$ must also not exceed $M$**, which is the other half of the test — the fourth row has $N = 9$ against $M = 4$ and fails on size alone.
- **The third row fails on the odd part**: $M = 5$ is already odd, so every reachable amount is a multiple of $5$ and $N = 1$ is out of reach.
- **$M$ a power of two makes the odd part $1$**, so every $N \leq M$ works — the first row, where $2$ halves into $1$ and $1$.
- **$M = N$ always works** with no weighing at all.
- **$M, N$ up to $10^{18}$**: the odd part is found by at most $60$ halvings, and the arithmetic stays exact.

## Dry run

| $M$ | odd part of $M$ | $N$ | $N \leq M$? | odd part divides $N$? | output |
|---:|---:|---:|:---:|:---:|---|
| 2 | 1 | 1 | yes | yes | `YES` |
| 1 | 1 | 1 | yes | yes | `YES` |
| 5 | 5 | 1 | yes | **no** | `NO` |
| 4 | 1 | 9 | **no** | yes | `NO` |

For the first row: balance $2$ kg into two piles of $1$ kg each.

---

Same problem in rating order (#436 of 486): [../../by-rating/436-APP_BAL_SCA.md](../../by-rating/436-APP_BAL_SCA.md)
