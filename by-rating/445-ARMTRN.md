# 445. Army Training

> [`ARMTRN`](https://www.codechef.com/problems/ARMTRN) &middot; difficulty **1742** &middot; time limit **1.5s** &middot; 1600 to 1800 difficulty problems (Level 3)

## Topic used

| | |
|---|---|
| **Topic** | Sorting |
| **Technique** | Sorted split maximising a product of two sums |
| **CodeChef tags** | `Algorithms`, `Sorting` |
| **Complexity class** | Linearithmic $O(n \log n)$ |
| **Time** | $O(N \log N)$ per test case |
| **Space** | $O(N)$ |

## Question

Chef is a high-ranked army officer and he has been given the job to train the army.

The army consists of $N$ soldiers where each soldier has $3$ parameters:
- *Attack points*: $A_i$ where $(0\lt A_i \lt 1000)$;
- *Defense points*: $(1000-A_i)$;
- *Soldier type*: `ATTACK` or `DEFENSE`.

For the whole army:
- *Attack value* of the army is defined as the **sum** of *attack points* of all `ATTACK` type soldiers.
- *Defense value* of the army is defined as the **sum** of *defense points* of all `DEFENSE` type soldiers.
- *Rating* of the army is defined as the **product** of *Attack value* and *Defense value* of the army.

Assign the *soldier type* to each of the soldiers to **maximize** the *rating* of the army. Print the maximum *rating*.

**NOTE:** The output may exceed the range of a $32$-bit integer.
Remember to use $64$-bit data types, such as `long long` in `C++`.

**Input**

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of multiple lines of input.
    - The first line of each test case contains an integer $N$ — the number of soldiers in the army.
    - The next line contains the array $A$ — where $A_{i}$ denotes the *attack points* of the $i^{th}$ soldier.

**Output**

For each test case, output on a new line the **maximum** possible *rating* that can be achieved.

## Constraints

- $1 \leq T \leq 100$
- $2 \leq N \leq 1000$
- $0 \lt A_{i} \lt 1000$
- Sum of $N$ over all test cases does not exceed $2000$.

## Sample

**Sample input**

```
4
2
500 500
3
500 500 500
4
100 800 300 500
4
300 700 800 200
```

**Sample output**

```
250000
500000
2080000
2250000
```

<details><summary>Explanation</summary>

**Test case $1$:** Soldier $1$ should be used for `ATTACK` while soldier $2$ should be used for `DEFENSE`. Thus, the *attack value* as well as the *defense value* equals $500$. The *rating* $=500\cdot 500 = 250000$. It can be proven that this is the maximum possible *rating* that we can achieve for the given army.

**Test case $2$:**
- Soldier $1$ and $2$ should be used for `ATTACK`. So, *attack value* $=500+500=1000$
- Soldier $3$ should be used for `DEFENSE`. So, *defense value* $=(1000-500)=500$

So, *rating* $=1000 \cdot 500=500000$. This is the maximum possible *rating* that we can achieve for the given army.

**Test case $3$:**
- Soldier $2$ and $4$ should be used for `ATTACK`. So, *attack value* $=800+500=1300$
- Soldier $1$ and $3$ should be used for `DEFENSE`. So, *defense value* $=(1000-100)+(1000-300)=1600$

So, *rating* $=1300 \cdot 1600=2080000$. This is the maximum possible *rating* that we can achieve for the given army.

**Test case $4$:**
- Soldier $2$ and $3$ should be used for `ATTACK`. So, *attack value* $=700+800=1500$
- Soldier $1$ and $4$ should be used for `DEFENSE`. So, *defense value* $=(1000-300)+(1000-200)=1500$

So, *rating* $=1500 \cdot 1500=2250000$. This is the maximum possible *rating* that we can achieve for the given army.

</details>

## Approach

Defense points are $1000 - A_i$, so a soldier is valuable on attack exactly when $A_i$ is large and valuable on defense exactly when $A_i$ is small. That means the optimal assignment, **for any fixed number $k$ of attackers**, puts the $k$ largest $A_i$ on attack:

$$\text{atk}(k) = \sum_{i<k} A_{(i)}, \qquad \text{def}(k) = 1000(N-k) - \Bigl(\textstyle\sum_i A_i - \text{atk}(k)\Bigr)$$

with $A$ sorted descending. Both halves of the product improve under the same ordering — the attack sum wants the big values and the defense sum wants the rest to be small — so there is no tension and the split is always a prefix of the sorted array.

That leaves only $N+1$ candidates, scanned with a running prefix sum:

$$\text{answer} = \max_{0 \leq k \leq N}\ \text{atk}(k) \cdot \text{def}(k)$$

The product is not monotone in $k$, so every split has to be tried: the attack sum rises while the defense sum falls, and with $A_i < 1000$ the balance point depends on the values. Note $k = 0$ and $k = N$ both give a product of $0$, so the optimum is always interior — an army of all attackers has no defense at all.

The samples bear this out. Three soldiers at $500$ each tie at $k = 1$ and $k = 2$ with $500 \cdot 1000 = 500000$. For $[800,500,300,100]$ the best is $k = 2$: $1300 \cdot 1600 = 2080000$, beating $k=1$'s $1680000$. And for $[800,700,300,200]$, $k = 2$ gives the perfectly balanced $1500 \cdot 1500$.

## Solution

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n = int(data[pos])
        a = sorted((int(x) for x in data[pos + 1:pos + 1 + n]), reverse=True)
        pos += 1 + n
        total = sum(a)
        best = 0
        attack = 0
        for k in range(n + 1):
            if k:
                attack += a[k - 1]
            # The remaining soldiers defend, each worth 1000 - A_i.
            defend = 1000 * (n - k) - (total - attack)
            best = max(best, attack * defend)
        out.append(str(best))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Edge cases

- **Sorting descending by attack makes every optimal split a prefix.** The attackers should be the soldiers with the highest attack points — which, since defense is $1000 - A_i$, are also the ones with the lowest defense — so trying each prefix size covers every candidate.
- **The defense value is $1000(n-k) - (\text{total} - \text{attack})$**, not a stored sum: each defender contributes $1000 - A_i$, so the group's value is $1000$ per defender minus their attack points.
- **Both extremes must be allowed**, so $k$ ranges over $0 \dots n$ — and both give a rating of $0$, which is why they are never optimal but still need including for correctness.
- **A balanced split is usually best**, since the rating is a product: the third sample peaks at $k = 2$ with $1300 \times 1600$.
- **Equal attack values** (the first two rows) make several splits tie, which the running maximum handles.
- **$0 < A_i < 1000$ strictly**, so no soldier has zero attack or zero defense.
- **$N \leq 1000$ with $\sum N \leq 2000$**, so the linear scan over split points is trivially affordable.

## Dry run

Third sample: $A = 100, 800, 300, 500$, sorted descending to $800, 500, 300, 100$ with a total of $1700$.

| $k$ | attack value | defenders | defense value | rating |
|---:|---:|---:|---:|---:|
| 0 | 0 | 4 | $4000 - 1700 = 2300$ | 0 |
| 1 | 800 | 3 | $3000 - 900 = 2100$ | 1680000 |
| 2 | 1300 | 2 | $2000 - 400 = 1600$ | **2080000** |
| 3 | 1600 | 1 | $1000 - 100 = 900$ | 1440000 |
| 4 | 1700 | 0 | 0 | 0 |

Output `2080000`.

---

Same problem grouped by topic: [../docs/sorting/ARMTRN.md](../docs/sorting/ARMTRN.md)
