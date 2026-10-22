# 54. It is My Serve

> CodeChef problem code [`MYSERVE`](https://www.codechef.com/problems/MYSERVE) &middot; difficulty **691** &middot; time limit **0.5s**

| | |
|---|---|
| **Topic** | Number Theory |
| **Technique** | Block index parity via modulo |
| **Time** | $O(1)$ per test case |
| **Space** | $O(1)$ |
| **Roadmap course** | 500 to 1000 difficulty rating (Level 1) |

## Question

Alice and Bob are playing a game of table tennis where irrespective of the point scored, every player makes $2$ consecutive serves before the service changes. Alice makes the first serve of the match. Therefore the first $2$ serves will be made by Alice, then the next $2$ serves will be made by Bob and so on.

Let's consider the following example match for more clarity:
- Alice makes the $1^{st}$ serve.
- Let us assume, Bob wins this point. (Score is $0$ for Alice and $1$ for Bob)
- Alice makes the $2^{nd}$ serve.
- Let us assume, Alice wins this point. (Score is $1$ for Alice and $1$ for Bob)
- Bob makes the $3^{rd}$ serve.
- Let us assume, Alice wins this point. (Score is $2$ for Alice and $1$ for Bob)
- Bob makes the $4^{th}$ serve.
- Let us assume, Alice wins this point. (Score is $3$ for Alice and $1$ for Bob)
- Alice makes the $5^{th}$ serve.
- And the game continues $\ldots$

After the score reaches $P$ and $Q$ for Alice and Bob respectively, both the players forgot whose serve it is. Help them determine whose service it is.

**Input**

- The first line contains a single integer $T$ — the number of test cases. Then the test cases follow.
- The first line of each test case contains two integers $P$ and $Q$ — the score of Alice and Bob respectively.

**Output**

For each test case, determine which player's (`Alice` or `Bob`) serve it is.

You may print each character of `Alice` and `Bob` in uppercase or lowercase (for example, `Bob`, `BOB`, `boB` will be considered identical).

## Constraints

- $1 \leq T \leq 200$
- $0 \le P, Q \le 10$

## Sample

**Sample input**

```
4
0 0
0 2
2 2
4 7
```

**Sample output**

```
Alice
Bob
Alice
Bob
```

<details><summary>Explanation</summary>

- **Test Case 1:** Since no points have been scored yet, this is the first serve of the match. Alice makes the $1^{st}$ serve of the match.
- **Test Case 2:** Two points have been scored yet. Thus, it is the third serve of the match. Bob makes the $3^{rd}$ serve of the match.
- **Test Case 3:** Four points have been scored yet. Thus, it is the fifth serve of the match. Alice makes the $5^{th}$ serve of the match.
- **Test Case 4:** Eleven points have been scored yet. Thus, it is the twelfth serve of the match. Bob makes the $12^{th}$ serve of the match.

</details>

## Approach

The scores themselves are a distraction. Serving rotates on a fixed schedule that depends only on **how many points have been played**, not on who won them. That total is

$$n = P + Q$$

Serves come in blocks of two: serves $1,2$ belong to Alice, serves $3,4$ to Bob, serves $5,6$ to Alice again. The next serve to be played is serve number $n + 1$, which sits in block

$$\left\lfloor \frac{n}{2} \right\rfloor$$

counting blocks from zero. Alice owns the even-numbered blocks and Bob the odd ones, so the server is Alice when $\lfloor n/2 \rfloor$ is even and Bob otherwise.

Two steps, each easy to get subtly wrong. Dividing by $2$ collapses each pair of serves into one block; taking that result modulo $2$ asks whose turn the block is. Doing only one of them — testing `n % 2` or `n % 4` directly — gets half the cases right and looks plausible.

Equivalently the whole thing is `(n // 2) % 2`, which is just bit $1$ of $n$. Working through the samples: $n = 0$ gives block $0$, Alice; $n = 2$ gives block $1$, Bob; $n = 4$ gives block $2$, Alice; $n = 11$ gives block $5$, Bob.

Note $P = Q = 0$ is a valid input — the match has not started and Alice serves first.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        p, q = int(data[1 + 2 * i]), int(data[2 + 2 * i])
        # Serves run in blocks of 2; Alice owns the even-numbered blocks.
        out.append("Alice" if ((p + q) // 2) % 2 == 0 else "Bob")
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(1)$ per test case
- **Space:** $O(1)$

## Edge cases

- **The very first serve** ($0$&ndash;$0$): block $0$, so Alice.
- **The switch after two points**: a total of $1$ is still block $0$ (Alice), a total of $2$ is block $1$ (Bob). The sample's second row sits just past the change.
- **Only the total matters**, not how it splits: $0$&ndash;$2$, $1$&ndash;$1$ and $2$&ndash;$0$ all give block $1$, so Bob serves in all three.
- **Largest total** ($10 + 10 = 20$): block $10$, which is even, so Alice.
- Dividing by two to get the block index and then testing *its* parity is the whole trick; testing the parity of the total itself gives a different, wrong pattern.

## Dry run

| $P$ | $Q$ | total | block $\lfloor \text{total}/2 \rfloor$ | block parity | output |
|---:|---:|---:|---:|---|---|
| 0 | 0 | 0 | 0 | even | `Alice` |
| 0 | 2 | 2 | 1 | odd | `Bob` |
| 2 | 2 | 4 | 2 | even | `Alice` |
| 4 | 7 | 11 | 5 | odd | `Bob` |

Row 4 has an odd total, which still lands inside block $5$.

> CodeChef tags: `Mathematics`

---

Same problem in rating order (#58 of 486): [../../by-rating/058-MYSERVE.md](../../by-rating/058-MYSERVE.md)
