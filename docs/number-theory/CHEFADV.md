# 248. Chef and Adventures

> CodeChef problem code [`CHEFADV`](https://www.codechef.com/problems/CHEFADV) &middot; difficulty **1462** &middot; time limit **0.5s**

| | |
|---|---|
| **Topic** | Number Theory |
| **Technique** | Divisibility with an optional one-off offset |
| **Time** | $O(1)$ per test case |
| **Space** | $O(1)$ |
| **Roadmap course** | 1400 to 1600 difficulty problems (Level 2) |

## Question

Mysterious Chefland... Recently, Chef realised that Discuss, the educational system of Chefland, is out of date. Therefore, he is trying to find ways to update the infrastructure in the country. One possible way is to move all materials from Discuss to Discourse.

Chef will have access to Discourse if his *knowledge* and *power* become exactly equal to $N$ and $M$ respectively. Initially, he has power $1$ and knowledge $1$.

Chef can perform actions of the following types to improve his skills:
- solve a problem — increase his knowledge by $X$
- do a push-up — increase his power by $Y$
- install ShareChat to keep in touch with friends — increase both knowledge and power by $1$

Chef can only install ShareChat at most once. The remaining actions may be performed any number of times and the actions may be performed in any order.

Help Chef find out whether it is possible to move from Discuss to Discourse.

### Input
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first and only line of each test case contains four space-separated integers $N$, $M$, $X$ and $Y$.

### Output
For each test case, print a single line containing the string `"Chefirnemo"` if it is possible to reach the required knowledge and power or `"Pofik"` if it is impossible.

### Constraints
- $1 \le T \le 1,000$
- $1 \le N, M, X, Y \le 10^9$

### Subtasks
**Subtask #1 (30 points):** $1 \le N, M, X, Y \le 100$

**Subtask #2 (70 points):** original constraints

## Constraints

- $1 \le T \le 1,000$
- $1 \le N, M, X, Y \le 10^9$

## Sample

**Sample input**

```
5
2 2 1 2
11 10 5 9
11 11 5 9
12 11 5 9
1 2 1 100
```

**Sample output**

```
Chefirnemo
Chefirnemo
Pofik
Chefirnemo
Pofik
```

<details><summary>Explanation</summary>

**Example case 2:** We add $Y=9$ once to the power to get power $10$. We add $X=5$ twice to the knowledge to get knowledge $11$.

**Example case 3:** We can see that it is impossible to reach power $M=11$ no matter which or how many operations we do. Note that the ShareChat operation will increase both knowledge and power by $1$, and hence it will still be impossible to attain the given values of knowledge and power at the same time.

**Example case 4:** We can reach knowledge $11$ and power $10$ like in example case 2, the only difference is that we also use the ShareChat operation to increase both by $1$.

</details>

## Approach

Knowledge and power both start at $1$ and are raised independently — knowledge by multiples of $X$, power by multiples of $Y$. The only coupling is ShareChat, which adds $1$ to **both** and may be used at most once.

So there are exactly two scenarios, and the answer is yes if either works.

**Without ShareChat:** knowledge must climb from $1$ to $N$ in steps of $X$, so $X \mid (N-1)$; likewise $Y \mid (M-1)$.

**With ShareChat:** both targets lose an extra $1$, so $X \mid (N-2)$ and $Y \mid (M-2)$ — and both $N$ and $M$ must be at least $2$, since the install alone already carries them past $1$.

Checking both and OR-ing them is the whole solution. Treating ShareChat as optional-per-skill would be wrong: it raises *both* counters or neither, so the two divisibility tests in the second scenario must be applied together.

Sample case 3 shows the coupling biting. With $N = M = 11$, $X = 5$, $Y = 9$: without ShareChat, knowledge works ($10$ is a multiple of $5$) but power does not ($10$ is not a multiple of $9$). With ShareChat, power works ($9$ is a multiple of $9$) but knowledge does not ($9$ is not a multiple of $5$). Neither scenario succeeds in both coordinates, so `Pofik` — even though each coordinate is individually reachable in *some* scenario.

Sample case 5 is the non-negativity guard: $N = 1$ makes $N - 2$ negative, so the ShareChat branch is unavailable and only the first test applies.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        n, m, x, y = map(int, data[1 + 4 * i:5 + 4 * i])
        plain = (n - 1) % x == 0 and (m - 1) % y == 0
        # ShareChat raises both counters or neither, so both tests apply.
        boosted = n >= 2 and m >= 2 and (n - 2) % x == 0 and (m - 2) % y == 0
        out.append("Chefirnemo" if plain or boosted else "Pofik")
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(1)$ per test case
- **Space:** $O(1)$

> CodeChef tags: `Mathematics`, `Modular Arithmetic`, `Algebra`, `Basic Math`
