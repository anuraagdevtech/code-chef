[&larr; 641. Max Range Queries](MAXREMOV.md) &middot; [Index](../../README.md) &middot; [668. Increase 2 consecutive characters &rarr;](CCD.md)

# 644. Angry Cyborg

> CodeChef problem code [`AGCY`](https://www.codechef.com/problems/AGCY) &middot; difficulty **2072** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Prefix Sums |
| **Technique** | Range updates of a linear function with two difference arrays |
| **Time** | $O(N + Q)$ per test case |
| **Space** | $O(N)$ |
| **Roadmap course** | 2000 to 2500 difficulty problems (Level 5) |

## Question

Cyborg Jenish is angry.

He has so much rage that he decided to go on a demolition spree for $Q$ days.

There are $N$ cities in his world numbered $1$ to $N$, in a row from left to right. That is the $i^{th}$ city from left side is city-$i$ where $1 \leq i \leq N$. The supreme leader of the world is VSM and there are infinite statues of VSM in each city.

On each day Jenish chooses two cities $L$ and $R$. He starts at city-$L$ and moves along the row towards right side till he reaches the city-$R$. In city-$L$ he destroys $1$ statue, in the next city (i.e. city-$L+1$) he destroys $2$ statues, and so on till city-$R$ where he destroys  $R-L+1$ statues. In other words, he destroys $i-L+1$ statues in the $i^{th}$ city ( $L\leq i\leq R$ ).

Find the total number of VSM statues he destroyed in each city after $Q$ days.

**Input:**
- The first line contains an integer $T$, denoting the number of test cases.
- The first line of each test case, contains two space-separated integers $N$ and $Q$ denoting the number of cities in his world and  the number of days he goes on a demolition spree respectively.
- The $i^{th}$ line of next $Q$ lines of each test case contains two space-separated integers $L$ and $R$ denoting the starting city and the ending city respectively on $i^{th}$ day.

**Output:**
- For each test case, output a single line containing $N$ space-separated integers.
- The $i^{th}$ integer should denote the total number of VSM statues destroyed by cyborg Jenish in the city-$i$ after $Q$ days.

**Constraints:**
- $1 \leq  T \leq 10^3$
- $ 1 \leq N \leq 10^5$
- $1 \leq Q \leq 10^5$
- $1\leq L \leq R \leq N$
- The sum of $N$ over all test cases is less than $10^{6}$
- The sum of $Q$ over all test cases is less than $10^{6}$

## Constraints

- $1 \leq  T \leq 10^3$
- $ 1 \leq N \leq 10^5$
- $1 \leq Q \leq 10^5$
- $1\leq L \leq R \leq N$
- The sum of $N$ over all test cases is less than $10^{6}$
- The sum of $Q$ over all test cases is less than $10^{6}$
**Sample Input:**
```
2
5 3
1 3
1 2
4 5
2 1
1 1
```
**Expected Output:**
```
2 4 3 1 2
1 0
```
**Explanation**
In the first test case, the cyborg does the following:
- Starts at city-1 and goes till city-3, hence destroys $1$ statue in city-1, $2$ in city-2, and $3$ in city-3.
- Starts at city-1 and goes till city-2, hence destroys $1$ statue in city-1 and $2$ in city-2.
- Starts at city-4 and goes till city-5, hence destroys $1$ statue in city-4 and $2$ in city-5.
- Hence he destroyed total $2$ statues in city-1, $4$ in city-2, $3$ in city-3, $1$ in city-4, and $2$ in city-5.

## Sample

**Sample input**

```
2
5 3
1 3
1 2
4 5
2 1
1 1
```

**Sample output**

```
2 4 3 1 2
1 0
```

<details><summary>Explanation</summary>

In the first test case, the cyborg does the following:
- Starts at city-1 and goes till city-3, hence destroys $1$ statue in city-1, $2$ in city-2, and $3$ in city-3.
- Starts at city-1 and goes till city-2, hence destroys $1$ statue in city-1 and $2$ in city-2.
- Starts at city-4 and goes till city-5, hence destroys $1$ statue in city-4 and $2$ in city-5.
- Hence he destroyed total $2$ statues in city-1, $4$ in city-2, $3$ in city-3, $1$ in city-4, and $2$ in city-5.

</details>

## Approach

A day with cities $L \dots R$ adds $i - L + 1$ statues to city $i$ for every $i$ in the range, which is the linear function $1 \cdot i + (1 - L)$.

Keep two difference arrays, one for the coefficient of $i$ and one for the constant term. A query adds 1 to the slope and $1 - L$ to the intercept on $[L, R]$, i.e. it touches four cells. After all queries a prefix sum over both arrays gives, for every city, the total slope $s_i$ and intercept $c_i$ of the ranges covering it, and the answer for the city is $s_i \cdot i + c_i$.

## Solution (Python)

```python
import sys


def main() -> None:
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    out = []
    for _ in range(next(tokens)):
        n = next(tokens)
        q = next(tokens)
        slope = [0] * (n + 2)
        intercept = [0] * (n + 2)
        for _ in range(q):
            left = next(tokens)
            right = next(tokens)
            slope[left] += 1
            slope[right + 1] -= 1
            intercept[left] += 1 - left
            intercept[right + 1] -= 1 - left
        active_slope = active_intercept = 0
        row = []
        for i in range(1, n + 1):
            active_slope += slope[i]
            active_intercept += intercept[i]
            row.append(str(active_slope * i + active_intercept))
        out.append(' '.join(row))
    print('\n'.join(out))


if __name__ == "__main__":
    main()
```

## Complexity

- **Time:** $O(N + Q)$ per test case
- **Space:** $O(N)$
- Auxiliary space excludes the buffered input and output.

## Edge cases

- A range of one city ($L = R$) destroys a single statue.
- The totals grow like $Q \cdot N$ and exceed 32 bits.
- The difference arrays need one extra cell for the update at $R + 1$.
- Cities not covered by any day print 0.

## Dry run

`N = 5`, days `[1,3] [1,2] [4,5]`.

Slope after prefix sums: `2 2 1 1 1`. Intercept: days 1 and 2 add 0 each, day 3 adds $1 - 4 = -3$ on cities 4-5: `0 0 0 -3 -3`.

Totals: $2 \cdot 1 = 2$, $2 \cdot 2 = 4$, $1 \cdot 3 = 3$, $4 - 3 = 1$, $5 - 3 = 2$.

Output `2 4 3 1 2`.

> CodeChef tags: `Mathematics`, `Sequences and Progression`, `Algorithms`, `Queries`

---

Same problem in rating order (#597 of 735): [../../by-rating/597-AGCY.md](../../by-rating/597-AGCY.md)
