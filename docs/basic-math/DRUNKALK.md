# 119. Drunk Alcoholic

> CodeChef problem code [`DRUNKALK`](https://www.codechef.com/problems/DRUNKALK) &middot; difficulty **874** &middot; time limit **0.5 - 1s**

| | |
|---|---|
| **Topic** | Basic Math |
| **Technique** | Net progress per cycle, with an odd remainder |
| **Time** | $O(1)$ per test case |
| **Space** | $O(1)$ |
| **Roadmap course** | 500 to 1000 difficulty rating (Level 1) |

## Question

Faizal is very sad after finding out that he is responsible for Sardar's death. He tries to drown his sorrows in alcohol and gets very drunk. Now he wants to return home but is unable to walk straight. For every $3$ steps forward, he ends up walking one step backward.

Formally, in the $1^{st}$ second he moves $3$ steps forward, in the $2^{nd}$ second he moves $1$ step backwards, in the $3^{rd}$ second he moves $3$ steps forward, in $4^{th}$ second $1$ step backwards, and so on.

How far from his initial position will Faizal be after $k$ seconds have passed?
Assume that Faizal's initial position is $0$.

**Input**

- The first line of input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains a single integer $k$, the number of seconds after which Faizal's position is to be calculated.

**Output**

- For each test case, output a single line containing one integer - Faizal's position after $k$ seconds.

## Constraints

- $1 \leq T \leq 100000$
- $0 \leq k \leq 100000$
- The sum of $k$ over all test cases does not exceed $1000000$

**Subtasks**

- 30 points : $1 \leq R \leq 10000$
- 70 points : $1 \leq R \leq 10^9$

## Sample

**Sample input**

```
3
5
11
23
```

**Sample output**

```
7
13
25
```

<details><summary>Explanation</summary>

**1st Test Case**
- Faizal walks $3$ steps forward in the $1^{st}$ second, ending up at $3$
- Faizal walks $1$ step backward in the $2^{nd}$ second, ending up at $2$
- Faizal walks $3$ steps forward in the $3^{rd}$ second, ending up at $5$
- Faizal walks $1$ step backward in the $4^{th}$ second, ending up at $4$
- Faizal walks $3$ steps forward in the $5^{th}$ second, ending up at $7$

</details>

## Approach

The walk repeats a two-second cycle: $+3$ forward, then $-1$ back, for a net gain of $2$ steps every $2$ seconds. So over complete cycles the position simply equals the elapsed time.

**$k$ even.** There are $k/2$ complete cycles, each worth $+2$:

$$\text{position} = \frac{k}{2} \cdot 2 = k$$

**$k$ odd.** There are $(k-1)/2$ complete cycles plus one final forward second:

$$(k - 1) + 3 = k + 2$$

So the answer is $k$ for even $k$ and $k + 2$ for odd $k$ — a pleasingly compact result that is easy to miss if one simulates without looking for the pattern.

The odd case is where the intuition slips. After an odd number of seconds Faizal has just taken a forward step and has not yet staggered back, so he is momentarily *ahead* of his steady-state position by $2$. Sample case 1 shows it: after $5$ seconds he is at $7$, not $5$.

The case $k = 0$ is inside the constraints and gives $0$ — even, so the formula handles it with no special guard.

The constraints are worth reading as a hint: $T$ reaches $10^5$ while the sum of $k$ is bounded by $10^6$, which is the setter signalling that per-test simulation would be acceptable but a closed form is better. Since the closed form is two lines, there is no reason to loop.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        k = int(data[1 + i])
        # +3 then -1 nets +2 per 2 seconds; an odd second ends mid-stagger.
        out.append(str(k if k % 2 == 0 else k + 2))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(1)$ per test case
- **Space:** $O(1)$

> CodeChef tags: `Special`, `Basic Programming Concepts`, `Algorithms`, `Constructive`
