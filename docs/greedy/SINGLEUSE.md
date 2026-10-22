[&larr; 66. A or B](AORB.md) &middot; [Index](../../README.md) &middot; [104. Smallest Numbers of Notes &rarr;](FLOW005.md)

# 82. Single-use Attack

> CodeChef problem code [`SINGLEUSE`](https://www.codechef.com/problems/SINGLEUSE) &middot; difficulty **777** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Greedy |
| **Technique** | Comparing both strategies explicitly |
| **Time** | $O(1)$ per test case |
| **Space** | $O(1)$ |
| **Roadmap course** | 500 to 1000 difficulty rating (Level 1) |

## Question

Chef is playing a video game, and is now fighting the final boss.

The boss has $H$ health points. Each attack of Chef reduces the health of the boss by $X$.
Chef also has a special attack that can be used **at most once**, and will decrease the health of the boss by $Y$.

Chef wins when the health of the boss is $\leq 0$.
What is the **minimum** number of attacks needed by Chef to win?

**Input**

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- The first and only line of each test case will contain three space-separated integers $H, X, Y$ — the parameters described in the statement.

**Output**

For each test case, output on a new line the minimum number of attacks needed by Chef to win.

## Constraints

- $1 \leq T \leq 1000$
- $1 \leq X \lt Y \leq H \leq 100$

## Sample

**Sample input**

```
4
100 25 40
100 29 45
46 1 2
78 15 78
```

**Sample output**

```
4
3
45
1
```

<details><summary>Explanation</summary>

**Test case $1$:** Chef can attack the boss $4$ times normally. This results in $25 + 25 + 25 + 25 = 100$ damage, which is enough to defeat the boss.

**Test case $2$:** Chef can attack the boss $2$ times normally, then use the special attack. This results in $29 + 29 + 45 = 103$ damage, which is enough to defeat the boss.

**Test case $3$:** Chef can proceed as follows:
- First, use the special attack. This leaves the boss with $46 - 2 = 44$ health.
- Then, use $44$ normal attacks to defeat the boss, since each one does $1$ damage.

This takes a total of $44 + 1 = 45$ attacks.

**Test case $4$:** Chef can use the special attack to immediately bring the health of the boss to zero, hence only needing one attack.

</details>

## Approach

The special attack may be used **at most once**, so there are exactly two strategies and the answer is the cheaper one.

**Never use it.** Plain attacks deal $X$ each, so the boss falls in $\lceil H/X \rceil$ hits.

**Use it once.** The special removes $Y$ immediately, leaving $\max(0, H - Y)$ health for plain attacks:

$$1 + \left\lceil \frac{\max(0, H - Y)}{X} \right\rceil$$

The clamp matters because $Y$ may finish the boss outright — sample case 4 has $Y = H = 78$, so the special alone wins in a single attack and the remaining health must not go negative.

It is tempting to assume that since $X < Y$ the special is always worth using, making the second branch the answer. That is wrong, and sample case 1 shows why: $H = 100, X = 25, Y = 40$ costs $4$ attacks either way, because the special's extra damage is wasted inside a hit that would have been spent anyway. The special helps only when it removes enough to save a whole plain attack — a *rounding* effect, not a raw-damage one. Sample case 3 is the extreme: with $X = 1$ and $Y = 2$ the special saves exactly one hit out of $46$.

So compute both and take the minimum. With only two options, evaluating both is simpler and safer than deriving the condition under which the special pays off.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        h, x, y = map(int, data[1 + 3 * i:4 + 3 * i])
        plain = (h + x - 1) // x
        rest = max(0, h - y)                       # the special may finish it
        with_special = 1 + (rest + x - 1) // x
        # The special only helps when it saves a whole plain attack.
        out.append(str(min(plain, with_special)))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(1)$ per test case
- **Space:** $O(1)$

## Edge cases

- **The special attack finishes the job alone** ($H = 78$, $Y = 78$): one attack. The `max(0, H - Y)` clamp is what allows this — without it the remaining health goes negative and the ceiling division gives a nonsense extra attack.
- **The special saves nothing** ($H = 100$, $X = 25$, $Y = 40$): both routes cost $4$, so using it is optional. A solution that *always* fires the special happens to get this row right, but the comparison is what makes it right in general.
- **$X < Y$ is guaranteed**, so the special always hits harder — and yet it may still not reduce the attack count, because what matters is whether it saves a whole plain attack rather than how much damage it does.
- **The weakest possible plain attack** ($X = 1$, $H = 46$): $45$ attacks with the special, $46$ without.
- Both strategies are evaluated and the smaller taken, since "hits harder" does not imply "finishes sooner".

## Dry run

| $H$ | $X$ | $Y$ | plain only $\lceil H/X \rceil$ | with special $1 + \lceil (H-Y)^+/X \rceil$ | output |
|---:|---:|---:|---:|---:|---|
| 100 | 25 | 40 | 4 | $1 + \lceil 60/25 \rceil = 4$ | `4` |
| 100 | 29 | 45 | 4 | $1 + \lceil 55/29 \rceil = 3$ | `3` |
| 46 | 1 | 2 | 46 | $1 + 44 = 45$ | `45` |
| 78 | 15 | 78 | 6 | $1 + 0 = 1$ | `1` |

Row 1 is the tie, row 4 the one-shot kill.

> CodeChef tags: `Mathematics`

---

Same problem in rating order (#87 of 486): [../../by-rating/087-SINGLEUSE.md](../../by-rating/087-SINGLEUSE.md)
