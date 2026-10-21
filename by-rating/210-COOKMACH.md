# 210. Cooking Machine

> [`COOKMACH`](https://www.codechef.com/problems/COOKMACH) &middot; difficulty **1329** &middot; time limit **1s** &middot; Level up from 1* to 2* (Level 2)

## Topic used

| | |
|---|---|
| **Topic** | Bit Manipulation |
| **Technique** | Halving and doubling toward a power of two |
| **Complexity class** | Polylogarithmic $O(\log^2 n)$ |
| **Time** | $O(\log A \cdot \log B)$ per test case |
| **Space** | $O(1)$ |

## Question

Chef is on a vacation these days, so his friend Chefza is trying to solve Chef's everyday tasks.

Today's task is to make a sweet roll. Rolls are made by a newly invented cooking machine. The machine is pretty universal - it can make lots of dishes and Chefza is thrilled about this.

To make a roll, Chefza has to set all the settings to specified integer values. There are lots of settings, each of them set to some initial value. The machine is pretty complex and there is a lot of cooking to be done today, so Chefza has decided to use only two quick ways to change the settings. In a unit of time, he can pick one setting (let's say its current value is **v**) and change it in one of the following ways.

- If **v** is even, change this setting to **v/2**. If **v** is odd, change it to **(v − 1)/2**.

- Change setting to **2 × v**

The receipt is given as a list of integer values the settings should be set to. It is guaranteed that each destination setting can be represented as an integer power of **2**.

Since Chefza has just changed his profession, he has a lot of other things to do. Please help him find the **minimum** number of operations needed to set up a particular setting of the machine. You can prove that it can be done in finite time.

**Input**

The first line of the input contains an integer **T** denoting the number of test cases. The description of **T** test cases follows.

The only line of each test case contains two integers **A** and **B** denoting the initial and desired values of the setting, respectively.

**Output**

For each test case, output a single line containing minimum number of operations Chefza has to perform in order to set up the machine.

**Constraints**

- **1** ≤ **T** ≤ **200**

- **1** ≤ **A** ≤ **10^7**

- **1** ≤ **B** ≤ **10^7**, and **B** is an integer power of **2**

**Subtasks**

- **Subtask #1 [40 points]: A ≤ 100 and B ≤ 100**

- **Subtask #2 [60 points]: No additional constraints**

## Constraints

- 1 ≤ T ≤ 200
- 1 ≤ A ≤ 10^7
- 1 ≤ B ≤ 10^7, and B is an integer power of 2

## Sample

**Sample input**

```
6
1 1
2 4
3 8
4 16
4 1
1 4
```

**Sample output**

```
0
1
4
2
2
2
```

<details><summary>Explanation</summary>

- In the first test case, you don't need to do anything.

- In the second test case, you need to multiply 2 by 2 and get 4. This is done in 1 operation.

- In the third test case, you need to obtain 1 from 3 and then multiply it by 2 three times to obtain 8. A total of 4 operations.

- In the fourth test case, multiply 4 by 2 twice.

- In the fifth test case, divide 4 by 2 twice.

- In the sixth test case, multiply 1 by 2 twice.

</details>

## Approach

The two moves are "halve, rounding down" and "double". Doubling only scales, so it can never remove a factor that halving has not already stripped — which means any optimal route **halves for a while, then doubles**. Interleaving the two would undo work.

So walk the halving chain from $A$: $A, \lfloor A/2 \rfloor, \lfloor A/4 \rfloor, \ldots$, recording the cost to reach each value $v$. From $v$, doubling reaches $B$ only when $B = v \cdot 2^m$ for some $m \geq 0$ — and since $B$ is guaranteed to be a power of two, that requires $v$ to be a power of two as well, with $v \leq B$. The total cost is the halving steps plus $m$, and the answer is the minimum over the chain.

The chain has at most about $24$ entries for $A \leq 10^7$, so this is effectively constant time.

The sample cases show both shapes. $A = 4, B = 16$ doubles twice with no halving. $A = 4, B = 1$ halves twice with no doubling. $A = 3, B = 8$ needs both: $3$ is not a power of two, so it must be halved to $1$ (one step, losing the odd bit) and then doubled three times — four moves in all.

That odd case is the one to understand. Halving $3$ gives $1$, not $1.5$: the rounding **discards information**, which is why $3$ can never reach $8$ in fewer moves. Values must be reduced to a power of two before doubling can help.

The chain must stop before reaching $0$, since $1$ halves to $0$ and $0$ doubles to itself — a dead end, and $B \geq 1$ is never $0$.

## Solution

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        a, b = int(data[1 + 2 * i]), int(data[2 + 2 * i])
        best = None
        v, steps = a, 0
        # Any optimal route halves first, then doubles: doubling cannot undo
        # the information that rounding down has already discarded.
        while v > 0:
            if v <= b and b % v == 0:
                q = b // v
                if q & (q - 1) == 0:          # q is a power of two
                    cost = steps + q.bit_length() - 1
                    if best is None or cost < best:
                        best = cost
            v //= 2
            steps += 1
        out.append(str(best))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Edge cases

- **$A = B$** (the first row): zero operations, found at $0$ halvings with a quotient of $1$.
- **$A > B$** (the fifth row, $4 \to 1$): only halving is used, and the doubling term contributes $0$.
- **$A < B$** (the second and sixth rows): no halving at all.
- **$A$ off the power-of-two chain** (the third row, $A = 3$ with $B = 8$): $3$ must be halved all the way down to $1$ before doubling, costing $1 + 3 = 4$. Halving first and doubling after is forced, because doubling cannot restore the bit that an earlier floor division discarded — so the search over "halve $k$ times, then double" covers every optimal route.
- **Halving reaches $1$ and then $0$**, so the `while v > 0` bound terminates and $v = 0$ is never tested as a candidate.
- **$B$ is guaranteed to be a power of two**, which makes `b % v == 0` already imply that $v$ and $b/v$ are powers of two — the explicit `q & (q - 1)` test is belt-and-braces, and $q \geq 1$ so it is never applied to zero.

## Dry run

Third sample: $A = 3$, $B = 8$.

| halvings | $v$ | $8 \bmod v$ | $q = 8/v$ | power of two? | cost |
|---:|---:|---:|---:|:---:|---:|
| 0 | 3 | 2 | — | — | — |
| 1 | 1 | 0 | 8 | yes | $1 + 3 = $ **4** |
| 2 | 0 | — | — | — | loop ends |

Output `4`: one halving $3 \to 1$, then three doublings $1 \to 2 \to 4 \to 8$.

---

Same problem grouped by topic: [../docs/bit-manipulation/COOKMACH.md](../docs/bit-manipulation/COOKMACH.md)
