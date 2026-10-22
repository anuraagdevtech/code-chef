# 239. Akash and Dinner

> CodeChef problem code [`CHEFDINE`](https://www.codechef.com/problems/CHEFDINE) &middot; difficulty **1438** &middot; time limit **2.5s**

| | |
|---|---|
| **Topic** | Greedy |
| **Technique** | Cheapest representative per group |
| **Time** | $O(N \log N)$ per test case |
| **Space** | $O(N)$ |
| **Roadmap course** | 1400 to 1600 difficulty problems (Level 2) |

## Question

Akash got his money from CodeChef today, so he decided to have dinner outside.
He went to a restaurant having $N$ items on the menu. The $i^{th}$ item on the menu belongs to the *category* $A_i$ and requires $B_i$ time to be cooked.

Akash wants to have a *complete meal*. Thus, his meal should have **at least** $K$ **distinct** *categories* of food.
The total time required to get all the food Akash orders, is the **sum** of the cooking time of all the items in the order.

Help Akash find the **minimum time** required to have a complete meal or tell if it is not possible to do so.

**Input**

- First line will contain $T$, the number of test cases. Then the test cases follow.
- Each test case contains three lines:
    - The first line of each test case contains two space-separated integers $N$ and $K$, denoting the number of dishes on the menu and the number of distinct categories in a complete meal.
    - The second line contains $N$ space-separated integers where the $i^{th}$ integer is $A_i$, denoting the category of the $i^{th}$ dish in the menu.
    - The third line contains $N$ space-separated integers where the $i^{th}$ integer is $B_i$, denoting the time required to cook the $i^{th}$ dish in the menu.

**Output**

For each test case, output in a single line, the **minimum time** required to have a complete meal.

If it is impossible to have a complete meal, print $-1$ instead.

## Constraints

- $1 \leq T \leq 100$
- $1 \leq N,K \leq 10^5$
- $1 \leq A_i \leq 10^5$
- $0 \leq B_i \leq 10^5$
- The sum of $N$ over all test cases won't exceed $10^5$.

## Sample

**Sample input**

```
4
3 1
1 2 3
2 1 3
8 3
1 3 2 2 4 1 3 5
3 3 0 1 2 4 1 4
1 1
5
1
5 3
1 1 2 2 1
1 1 0 3 5
```

**Sample output**

```
1
3
1
-1
```

<details><summary>Explanation</summary>

**Test case $1$:** Akash can choose dish with index $2$ having category $2$. The total time required to get the complete meal is $1$.

**Test case $2$:** Akash can choose dishes with index $3, 5,$ and $7$ from the menu.
- Dish $3$: The dish has category $2$ and requires time $0$.
- Dish $5$: The dish has category $4$ and requires time $2$.
- Dish $7$: The dish has category $3$ and requires time $1$.

Thus, there are $3$ distinct categories and the total time to get the meal is $0+2+1 = 3$. It can be shown that this is the minimum time to get the *complete meal*.

**Test case $3$:** Akash can choose the only available dish having category $5$. The total time required to get the complete meal is $1$.

**Test case $4$:** The total number of distinct categories available is $2$, which is less than $K$. Thus, it is impossible to have a *complete* meal.

</details>

## Approach

A complete meal needs at least $K$ **distinct** categories. Since ordering more dishes only adds time, the optimal meal takes exactly $K$ dishes, one from each of $K$ different categories.

Two greedy steps follow.

**Within a category, take the cheapest dish.** Any other choice from the same category costs at least as much and contributes the same category, so it is dominated.

**Across categories, take the $K$ cheapest representatives.** The per-category minima are independent, so sorting them and summing the smallest $K$ is optimal.

If fewer than $K$ distinct categories exist on the menu, no complete meal is possible and the answer is $-1$ — sample case 4, which has only two categories against $K = 3$.

Building the minima with a dictionary keyed by category is one pass; sorting the values and summing a prefix finishes it.

Sample case 2 is the one that exercises both steps. Category $1$ offers dishes costing $3$ and $4$, so its representative is $3$; category $2$ offers $0$ and $1$, giving $0$; category $3$ offers $3$ and $1$, giving $1$. With representatives $[3, 1, 0, 2, 4]$, the three cheapest sum to $0 + 1 + 2 = 3$.

Note that cooking times may be **zero** ($B_i \geq 0$), so a total of $0$ is legitimate and no positivity may be assumed. Taking the first dish seen per category rather than the minimum would answer $3 + 3 + 0 = 6$ here.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n, k = int(data[pos]), int(data[pos + 1])
        cats = data[pos + 2:pos + 2 + n]
        times = data[pos + 2 + n:pos + 2 + 2 * n]
        pos += 2 + 2 * n
        # Cheapest dish per category; times may legitimately be zero.
        best = {}
        for c, b in zip(cats, times):
            v = int(b)
            if c not in best or v < best[c]:
                best[c] = v
        if len(best) < k:
            out.append("-1")
        else:
            out.append(str(sum(sorted(best.values())[:k])))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(N \log N)$ per test case
- **Space:** $O(N)$

## Edge cases

- **A preparation time of zero is legal** ($B_i \geq 0$), so the per-category minimum must not use $0$ as an "unset" sentinel. The second row's answer depends on a genuine $0$.
- **Fewer than $K$ distinct categories** → $-1$. The fourth row has only two categories and needs three, even though it has five dishes.
- **Only the cheapest dish per category counts**, so a category full of slow dishes is represented by its one fast dish and nothing else — the second row's category $1$ offers $3$ and $4$ and contributes only $3$.
- **Exactly $K$ categories** → every one of them is used and the sort is a formality.
- **Category labels are compared as raw byte tokens**, which is safe because the input has no leading zeros, so each label has one spelling.
- **Sum of $N \leq 10^5$**: only the per-category minima are sorted, at most $\min(N, \text{distinct})$ values.

## Dry run

Second sample: $N = 8$, $K = 3$, categories $1,3,2,2,4,1,3,5$ with times $3,3,0,1,2,4,1,4$.

| category | times offered | cheapest |
|---:|---|---:|
| 1 | $3, 4$ | 3 |
| 2 | $0, 1$ | **0** |
| 3 | $3, 1$ | 1 |
| 4 | $2$ | 2 |
| 5 | $4$ | 4 |

Five categories available, so pick the three cheapest minima: $0 + 1 + 2 = $ `3`.

> CodeChef tags: `Algorithms`

---

Same problem in rating order (#248 of 486): [../../by-rating/248-CHEFDINE.md](../../by-rating/248-CHEFDINE.md)
