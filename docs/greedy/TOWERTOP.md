[&larr; 431. Maximum Median Matching](MEDMAXMATCH.md) &middot; [Index](../../README.md) &middot; [443. Buying Sweets &rarr;](BUYSWEET.md)

# 432. Building Towers

> CodeChef problem code [`TOWERTOP`](https://www.codechef.com/problems/TOWERTOP) &middot; difficulty **1693** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Greedy |
| **Technique** | Doubling to the first tower, then one per operation |
| **Time** | $O(1)$ per test case |
| **Space** | $O(1)$ |
| **Roadmap course** | 1600 to 1800 difficulty problems (Level 3) |

## Question

Chef is given a contract to build towers in Chefland which are made by stacking blocks one above the other. Initially, there is only $1$ block in the inventory and no tower has been built. Chef follows the following $2$ steps in each operation:

- Either build a new tower or update an existing tower that has been built in previous operations using **any** number of blocks currently present in the inventory. After this step, the size of the inventory reduces by the number of blocks used.
- Suppose the tower Chef updated or built has $B$ blocks **after the step**, Chef gets to add $B$ new blocks to the inventory as a reward.

Find the **maximum** number of towers of height $X$ that Chef can build in $M$ operations.

**Note:** Tower of height $X$ means that the tower consists of $X$ blocks placed one above the other.

**Input**

- First line will contain $T$, number of test cases. Then the test cases follow.
- Each test case contains a single line of input, two space separated integers $X, M$.

**Output**

For each test case, output a single integer, the maximum number of towers that Chef can build.

## Constraints

- $1 \leq T \leq 100$
- $1 \leq X \leq 10^9$
- $0 \leq M \leq 10^{17}$

## Sample

**Sample input**

```
4
2 1
2 2
2 3
53 7
```

**Sample output**

```
0
1
2
1
```

<details><summary>Explanation</summary>

**Test Cases $1$, $2$ and $3$:**
- Operation $1$:
    - Remove $1$ block from the inventory and build a new tower of height $1$ after which the inventory becomes empty.
    - Add $1$ block to the inventory after which the inventory has only $1$ block.
- Operation $2$:
    - Remove $1$ block from the inventory and update the tower of height $1$ to $1 + 1 = 2$ after which the inventory becomes empty.
    - Add $2$ blocks to the inventory after which the inventory has only $2$ blocks.
- Operation $3$:
    - Remove $2$ blocks from the inventory and build a new tower of height $2$ after which the inventory becomes empty.
    - Add $2$ blocks to the inventory after which the inventory has only $2$ blocks.

So after operation $1$, there is no tower of height $2$ built, after operation $2$, there is a single tower of height $2$ built and after operation $3$, $2$ towers of height $2$ are built.

**Test Case $4$:**
- Operation $1$:
    - Remove $1$ block from the inventory and build a new tower of height $1$ after which the inventory becomes empty.
    - Add $1$ block to the inventory after which the inventory has only $1$ block.
- Operation $2$:
    - Remove $1$ block from the inventory and update the tower of height $1$ to $1 + 1 = 2$ after which the inventory becomes empty.
    - Add $2$ blocks to the inventory after which the inventory has only $2$ blocks.
- Operation $3$:
    - Remove $2$ blocks from the inventory and update the tower of height $2$ to $2 + 2 = 4$ after which the inventory becomes empty.
    - Add $4$ blocks to the inventory after which the inventory has only $4$ blocks.
- Operation $4$:
    - Remove $4$ blocks from the inventory and update the tower of height $4$ to $4 + 4 = 8$ after which the inventory becomes empty.
    - Add $8$ blocks to the inventory after which the inventory has only $8$ blocks.
- Operation $5$:
    - Remove $8$ blocks from the inventory and update the tower of height $8$ to $8 + 8 = 16$ after which the inventory becomes empty.
    - Add $16$ blocks to the inventory after which the inventory has only $16$ blocks.
- Operation $6$:
    - Remove $16$ blocks from the inventory and update the tower of height $16$ to $16 + 16 = 32$ after which the inventory becomes empty.
    - Add $32$ blocks to the inventory after which the inventory has only $32$ blocks.
- Operation $7$:
    - Remove $21$ blocks from the inventory and update the tower of height $32$ to $32 + 21 = 53$ after which the inventory has $32 - 21 = 11$ blocks remaining.
    - Add $53$ blocks to the inventory after which the inventory has $53 + 11 = 64$ blocks in total.

So after $7^{th}$ operation we are able to achieve one tower of height $53$.

</details>

## Approach

Spending the whole inventory on one tower **doubles** it. If the tower has $h$ blocks and the inventory also holds $h$, adding all $h$ makes it $2h$ and the reward restores the inventory to $2h$. Starting from one block, operation $i$ leaves a tower of $2^{i-1}$ with $2^{i-1}$ in reserve, so the first tower of height $X$ needs

$$k = \min\{\,i : 2^{i-1} \geq X\,\}$$

operations — and the exact height $X$ is reachable at step $k$, because the inventory then holds $2^{k-2} \geq X - 2^{k-2}$, just enough to top up from $2^{k-2}$ to $X$.

The payoff is what the inventory looks like afterwards. Blocks spent plus the reward leave

$$2^{k-2} - (X - 2^{k-2}) + X = 2^{k-1} \;\geq\; X$$

so from then on **every operation builds a whole new tower**: spend $X$, get $X$ back, inventory unchanged. Hence

$$\text{answer} = \max(0,\ M - k + 1)$$

Doubling is optimal because the reward equals the tower's new size, so the inventory can never grow faster than by doubling, and the first tower cannot be finished sooner.

The samples trace this. For $X = 2$ we have $k = 2$: $M = 1$ gives $0$ (one operation only reaches height $1$), $M = 2$ gives $1$, and $M = 3$ gives $2$ — the third operation builds a second tower outright from the two banked blocks. For $X = 53$, $k = 7$ since $2^6 = 64 \geq 53$, so $M = 7$ yields exactly $1$: the tower grows $1, 2, 4, 8, 16, 32$ and then jumps to $53$.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        x, m = int(data[1 + 2 * i]), int(data[2 + 2 * i])
        # Doubling reaches 2^(k-1) after k operations; afterwards the inventory
        # stays at or above X, so each further operation is a whole tower.
        k = (x - 1).bit_length() + 1
        out.append(str(max(0, m - k + 1)))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(1)$ per test case
- **Space:** $O(1)$

## Edge cases

- **The inventory doubles while building the first tower.** Starting from one block, pouring everything into the same tower each turn gives heights $1, 2, 4, 8, \dots$ and refills the inventory to match — so reaching height $X$ takes $k = \lceil \log_2 X \rceil + 1$ operations.
- **After that, every operation yields a whole tower.** The inventory is then at least $X$, and spending $X$ blocks on a fresh tower refills it by $X$ — so it never drops below $X$ again.
- **Hence the answer is $M - k + 1$**: the first tower plus one per remaining operation.
- **Too few operations give $0$**, which the clamp handles — the first sample row has $M = 1$ against $k = 2$.
- **$X = 1$ makes $k = 1$**, since `(1-1).bit_length() + 1 = 1`: the very first operation already builds a tower of height $1$.
- **$X$ need not be a power of two.** For $X = 53$, seven operations reach height $64 \geq 53$, and the formula counts that as the one tower it is.
- **$M$ up to $10^{17}$** means the answer can be enormous, so no simulation is possible — but the arithmetic stays exact.

## Dry run

Fourth sample: $X = 53$, $M = 7$. Building one tower as fast as possible:

| operation | tower height after | inventory after |
|---:|---:|---:|
| 1 | 1 | 1 |
| 2 | 2 | 2 |
| 3 | 4 | 4 |
| 4 | 8 | 8 |
| 5 | 16 | 16 |
| 6 | 32 | 32 |
| 7 | 64 | 64 |

Seven operations produce exactly one tower of height at least $53$, so the output is `1`.

> CodeChef tags: `Algorithms`

---

Same problem in rating order (#403 of 486): [../../by-rating/403-TOWERTOP.md](../../by-rating/403-TOWERTOP.md)
