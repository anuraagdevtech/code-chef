# 373. Say No To Drugs

> CodeChef problem code [`NODRUGS`](https://www.codechef.com/problems/NODRUGS) &middot; difficulty **1425** &middot; time limit **0.5s**

| | |
|---|---|
| **Topic** | Conditionals & Case Work |
| **Technique** | Monotone objective, so only an endpoint dose matters |
| **Time** | $O(N)$ per test case |
| **Space** | $O(1)$ |
| **Roadmap course** | Jump from 2* to 3* (Level 3) |

## Question

There are $N$ people participating in a race. The $N^{th}$ participant is your friend, so you want him to win. You are not a man of ethics, so you decided to inject some units of a Performance Enhancement Drug (don't ask where that came from) in your friend's body.

- From the charts, you came to know the speed of every player. Formally, for a player $i$, his speed is denoted by $S_i$.
- The change in speed with one unit of the drug is $K$ units. Note that $K$ can be negative, which means the drug has more side effects than benefits.
- Of course, there will be a drug test before the race, so your friend will be caught if the number of units of the drug in his blood is greater than or equal to $L$.

You need to determine whether you can help your friend to win the race (with or without drugs), without getting caught.

**Note:** A player wins the race if he has the maximum speed among all the participants. If there are more than one people with a maximal speed, they tie at first place, and **no one** wins!

**Input**

- First line will contain a single integer $T$, the number of test cases. Description of the test cases follows.
- First line of each test case will contain three space-separated integers, $N$ - the number of participants, $K$ - the change in speed with one unit of the drug, and $L$ - minimum units of the drug that can be detected in the drug test.
- Second line of each test case will contain $N$ space-separated integers $S_i$, the speeds of the participants.

**Output**

For each test case print "Yes" if you can help your friend to win the race, otherwise "No" in a single line.

## Constraints

- $1 \leq T \leq 200$
- $1 \leq N, L \leq 1000$
- $-1000 \le K \le 1000$
- $1 \leq S_i \leq 1000$

**Subtasks**

- 30 points : $1 \leq R \leq 10000$
- 70 points : $1 \leq R \leq 10^9$

## Sample

**Sample input**

```
3
4 2 2
2 1 3 2
4 2 2
2 1 4 2
3 -10 100
12 11 9
```

**Sample output**

```
Yes
No
No
```

<details><summary>Explanation</summary>

- In test case $1$, initial speeds are $\{2, 1, 3, 2\}$. You can inject $1$ unit of the drug into your friend's body, and increase his speed from $2$ to $4$. $4$ is the fastest speed, thus you helped your friend win the race. Hence, the answer is "Yes".
- In test case $2$, initial speeds are $\{2, 1, 4, 2\}$. You can inject $1$ unit of the drug into your friend's body, and increase his speed from $2$ to $4$. But you can not inject any more units of the drug, and with speed $4$ your friend can only tie at rank $1$ and not Win. Hence, the answer is "No".
- In test case $3$, initial speeds are $\{12, 11, 9\}$. Note that the impact of the drug in this case is negative, which means that the speed will only decrease if you inject it. So, there is no way you can help your friend to win. Hence, the answer is "No".

</details>

## Approach

The friend's final speed $S_N + uK$ is **monotone in the dose $u$**, so the best dose is always an endpoint of the legal range and there is nothing to search. The dose must stay strictly below $L$ to escape detection, so $u \in \{0, 1, \ldots, L-1\}$ — note the test catches $u \geq L$, which makes the usable maximum $L-1$, the classic off-by-one here.

With $m = \max(S_1, \ldots, S_{N-1})$, winning requires a **strict** maximum, since ties mean nobody wins:

$$S_N + uK > m$$

- $K > 0$: more is better, so take $u = L-1$.
- $K \leq 0$: the drug does not help, so take $u = 0$ and race clean. A negative $K$ is a pure liability.

So the whole problem is one comparison, with $\max(0, (L-1)K)$ as the best boost.

The first two samples are the same race one point apart: with $S_N = 2$, $K = 2$, $L = 2$ the single legal dose gives $4$, which beats a rival's $3$ but not a rival's $4$ — the second case failing precisely because equality is not a win.

The third sample has $K = -10$ and a generous $L = 100$, but every unit *lowers* the speed, so the honest dose of $0$ is optimal, and $9 < 12$ loses anyway.

The degenerate $N = 1$ case leaves the max over rivals empty; the friend is then the sole participant and wins outright, which the code handles by treating the rival maximum as $-\infty$.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n, k, l = int(data[pos]), int(data[pos + 1]), int(data[pos + 2])
        speeds = [int(x) for x in data[pos + 3:pos + 3 + n]]
        pos += 3 + n
        rival = max(speeds[:-1]) if n > 1 else float("-inf")
        # The dose is capped at L - 1, and a non-positive K is never worth using.
        boost = (l - 1) * k if k > 0 else 0
        out.append("Yes" if speeds[-1] + boost > rival else "No")
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(N)$ per test case
- **Space:** $O(1)$
