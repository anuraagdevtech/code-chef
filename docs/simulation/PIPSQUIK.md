# 235. Full Barrier Alchemist

> CodeChef problem code [`PIPSQUIK`](https://www.codechef.com/problems/PIPSQUIK) &middot; difficulty **1426** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Simulation |
| **Technique** | Walking a sequence with a consumable resource |
| **Time** | $O(N)$ per test case |
| **Space** | $O(1)$ |
| **Roadmap course** | 1400 to 1600 difficulty problems (Level 2) |

## Question

Edward Elric is chasing after Scar. To stop Edward, Scar creates $N$ barriers in the way, numbered from $1$ to $N$.
Each barrier Scar created is either one of the following two types.
- Type 1 barrier - This barrier starts from a height $X$ above the ground and extends till the sky.
- Type 2 barrier - This barrier starts from the ground and extends up to height $X$ above the ground.

<img src="https://codechef_shared.s3.amazonaws.com/download/HYC/External_contest_images/DCOD2019/problem1.png" width="500" alt="problem1.png" />

The height of Edward is $H$ units and he has an alchemic life force of $L$ units. Moreover, he can duck by $Y_{1}$ units and jump by height $Y_{2}$ units (as explained in the figures). He starts crossing barriers in sequence, starting from barrier $1$ till the barrier $N$. Whenever he can't pass a barrier by ducking or jumping (considered passed even when the barrier just touches him), he uses Alchemy to break the barrier. However, this costs him a single unit of his alchemic life force.

If after breaking a barrier no life force is left, Edward gets completely exhausted, unable to pass that barrier.
How many barriers can Edward cross?

And remember never to call him a pipsqueak if his height is too short!

**Input:**
- The first line contains $T$, the number of test cases. Then the test cases follow.
- For each test case, the first line contains five integers $N$, $H$, $Y_{1}$, $Y_{2}$ and $L$.
- The i-th of the next $N$ lines contains two integers $t_{i}$ and $X_{i}$ for the $i^{th}$ barrier where $t_{i} = 1$ denotes a Type 1 Barrier and $t_{i} = 2$ denotes a Type 2 barrier.

**Output:**
For each test case print a single line containing the number of barriers Edward can pass.

**Constraints**
- $1 \leq T\leq 100$
- $1 \leq N\leq 10^{3}$
- $2 \leq H\leq 10^{3}$
- $1 \leq Y_{1} < H$
- $1 \leq Y_{2} \leq 10^{3}$
- $1 \leq L \leq N$
- $1 \leq t_{i} \leq 2$
- $1 \leq X_{i}\leq 10^{3}$

## Constraints

- $1 \leq T\leq 100$
- $1 \leq N\leq 10^{3}$
- $2 \leq H\leq 10^{3}$
- $1 \leq Y_{1} < H$
- $1 \leq Y_{2} \leq 10^{3}$
- $1 \leq L \leq N$
- $1 \leq t_{i} \leq 2$
- $1 \leq X_{i}\leq 10^{3}$

## Sample

**Sample input**

```
3
6 5 1 2 3
2 2
2 1
1 10
2 8
2 4
1 2
1 4 2 5 1
2 6
6 5 1 2 3
2 2
2 1
1 10
2 8
2 4
1 6
```

**Sample output**

```
5
0
6
```

<details><summary>Explanation</summary>

**Test Case 1:**

Given $N = 6$, $H = 5$, $Y_{1} = 1$, $Y_{2} = 2$ and $L = 3$.
He passes the first three barriers by either ducking or jumping. He uses alchemic life force for breaking $4^{th}$, $5^{th}$ and $6^{th}$ barriers because he cannot pass them by either jumping or ducking. He gets exhausted after breaking the $6^{th}$ barrier and is unable to pass it. So, in total he passes $5$ barriers.

</details>

## Approach

Each barrier is passed in one of three ways, tested in order.

- **Type 2** (ground up to height $X$): Edward jumps over it if $X \leq Y_2$.
- **Type 1** (height $X$ up to the sky): Edward ducks under it if $H - Y_1 \leq X$ — ducking lowers his effective height to $H - Y_1$.
- Otherwise he breaks it, spending one unit of life force.

The rule that decides this problem is the exhaustion clause: **if breaking a barrier leaves zero life force, he does not pass that barrier**. So the check is to decrement first and then test for zero, counting the barrier only if something remains.

Sample case 1 traces it exactly. The first three barriers are cleared by jumping, jumping and ducking. The fourth ($X=8$, too tall to jump) and fifth ($X=4$) are broken, dropping $L$ from $3$ to $1$. The sixth is a type-1 barrier at height $2$, below his ducked height of $4$, so he breaks it — and that takes $L$ to $0$, so he collapses on it. The answer is $5$, not $6$.

Sample case 3 is the same input with the last barrier raised to $X = 6$, which he can now duck under for free, so all $6$ are cleared. Sample case 2 is the minimal exhaustion case: one barrier, one life force, broken and he stops at $0$.

Note the "touching counts as passing" wording makes both comparisons **inclusive** — $X \leq Y_2$ and $H - Y_1 \leq X$. Using strict inequalities would fail sample case 1 on the very first barrier, where $X = 2$ equals $Y_2 = 2$.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n, h, y1, y2, life = (int(v) for v in data[pos:pos + 5])
        pos += 5
        ducked = h - y1
        passed = 0
        for i in range(n):
            kind, x = int(data[pos + 2 * i]), int(data[pos + 2 * i + 1])
            # Touching counts as passing, so both tests are inclusive.
            if (kind == 2 and x <= y2) or (kind == 1 and ducked <= x):
                passed += 1
                continue
            life -= 1
            if life == 0:
                break            # exhausted on this barrier, so it is not passed
            passed += 1
        pos += 2 * n
        out.append(str(passed))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(N)$ per test case
- **Space:** $O(1)$

## Edge cases

- **Touching counts as passing**, so both tests are inclusive. The first case's opening barrier is type $2$ at height $2$ with a jump of exactly $2$, and it is cleared.
- **The two barrier kinds compare in opposite directions.** A type $2$ barrier rises from the ground to $X$, so he needs $X \leq Y_2$; a type $1$ barrier hangs from $X$ upwards, so his ducked height $H - Y_1$ must satisfy $H - Y_1 \leq X$. Using one direction for both fails most cases.
- **A broken barrier is still passed — unless it drains the last life.** The statement is explicit: if no life force remains after the break, he cannot pass *that* barrier. So the loop breaks before incrementing, and the first case passes $5$ of $6$ despite breaking three.
- **Exhaustion on the very first barrier** (the second case: one life, one impassable barrier) → `0`.
- **Lives may survive to the end** (the third case finishes with one left and passes all six).
- **$H - Y_1$ is computed once**, since the ducked height never changes during a run.

## Dry run

First sample: $H = 5$, $Y_1 = 1$ (so ducked height $4$), $Y_2 = 2$, $L = 3$.

| barrier | type | $X$ | test | result | lives | passed |
|---:|---:|---:|---|---|---:|---:|
| 1 | 2 | 2 | $2 \leq 2$ | jump | 3 | 1 |
| 2 | 2 | 1 | $1 \leq 2$ | jump | 3 | 2 |
| 3 | 1 | 10 | $4 \leq 10$ | duck | 3 | 3 |
| 4 | 2 | 8 | $8 \leq 2$ fails | break | 2 | 4 |
| 5 | 2 | 4 | $4 \leq 2$ fails | break | 1 | 5 |
| 6 | 1 | 2 | $4 \leq 2$ fails | break, **exhausted** | 0 | 5 |

Output `5`.

> CodeChef tags: `Basic Programming Concepts`, `Algorithms`

---

Same problem in rating order (#244 of 486): [../../by-rating/244-PIPSQUIK.md](../../by-rating/244-PIPSQUIK.md)
