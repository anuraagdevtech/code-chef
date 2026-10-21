# 479. The One Who Knocks!

> CodeChef problem code [`EOOPR`](https://www.codechef.com/problems/EOOPR) &middot; difficulty **1749** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Conditionals & Case Work |
| **Technique** | Reachability of a difference by odd and even steps |
| **Time** | $O(1)$ per test case |
| **Space** | $O(1)$ |
| **Roadmap course** | 1600 to 1800 difficulty problems (Level 3) |

## Question

*“I am not in danger, Skyler. I am the danger. A guy opens his door and gets shot, and you think that of me? No! I am the one who knocks!”*

Skyler fears Walter and ponders escaping to Colorado. Walter wants to clean his lab as soon as possible and then go back home to his wife.

In order clean his lab, he has to achieve cleaning level of lab as $Y$. The current cleaning level of the lab is $X$.

He must choose one positive **odd** integer $a$ and one positive **even** integer $b$. Note that, he cannot change $a$ or $b$ once he starts cleaning.

He can perform any one of the following operations for one round of cleaning:
  1. Replace $X$ with $X+a$.
  2. Replace $X$ with $X-b$.

Find minimum number of rounds (possibly zero) to make lab clean.

###Input:

- First line will contain $T$, number of test cases. $T$ testcases follow :
- Each test case contains two space separated integers $X, Y$.

###Output:
For each test case, output an integer denoting minimum number of rounds to clean the lab.
###Constraints
- $1 \leq T \leq 10^5$
- $ |X|,|Y| \leq 10^9$

## Constraints

- $1 \leq T \leq 10^5$
- $ |X|,|Y| \leq 10^9$

## Sample

**Sample input**

```
3
0 5
4 -5
0 10000001
```

**Sample output**

```
1
2
1
```

<details><summary>Explanation</summary>

- For the first testcase, you can convert $X$ to $Y$  by choosing $a=5$ and $b=2$.
It will cost minimum of $1$ cleaning round. You can select any other combination of $a, b$ satisfying above condition but will take minimum of $1$ cleaning round in any case.

- For the second testcase, you can convert $X$ to $Y$ by choosing $a=1$ and $b=10$. In first round they will replace $X$ to $X+a$ and then in second round replace to $X-b$. You can perform only one operation in one round.

</details>

## Approach

With $a$ a fixed positive **odd** step up and $b$ a fixed positive **even** step down, the reachable totals after a few rounds are $a$, $-b$, $2a$, $a - b$, $-2b$, $3a$, $2a - b$, and so on. Only $d = Y - X$ matters, so the answer is a short case analysis on its sign and parity.

- **$d = 0$:** nothing to do, $0$ rounds.
- **$d > 0$ odd:** one round, $a = d$.
- **$d < 0$ even:** one round, $b = -d$.
- **$d < 0$ odd:** one round is impossible ($a > 0$ and $-b$ is even), but two work: $a - b = d$ with $a = 1$ and $b = 1 - d$, which is even and at least $2$.
- **$d > 0$ even:** one round is impossible. Two rounds give $2a$, which is $d$ only when $a = d/2$ is **odd**, i.e. $d \equiv 2 \pmod 4$. So:
  - $d \equiv 2 \pmod 4$: two rounds.
  - $d \equiv 0 \pmod 4$: three rounds, via $2a - b$ — pick any odd $a \geq (d+2)/2$ and set $b = 2a - d$, which is even and positive.

So the answer is never more than $3$, and the only case needing three is a positive difference divisible by $4$ — because two "up" moves always land on $2 \times (\text{odd})$, which is $2$ mod $4$.

The samples: $0 \to 5$ is a positive odd difference, so one round. $4 \to -5$ is $-9$, negative and odd, so two. And $0 \to 10000001$ is again positive and odd, so one — size is irrelevant, since $a$ may be as large as needed.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        x, y = int(data[1 + 2 * i]), int(data[2 + 2 * i])
        d = y - x
        if d == 0:
            out.append("0")
        elif d < 0:
            out.append("1" if d % 2 == 0 else "2")
        elif d % 2:
            out.append("1")
        elif d % 4 == 2:
            out.append("2")               # 2a with a = d/2 odd
        else:
            out.append("3")               # 2a - b; two ups land on 2 mod 4
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(1)$ per test case
- **Space:** $O(1)$

> CodeChef tags: `Special`, `Basic Programming Concepts`, `Algorithms`, `Constructive`
