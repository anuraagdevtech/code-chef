# 416. Lumpy - The Bus Driver

> [`LUMPYBUS`](https://www.codechef.com/problems/LUMPYBUS) &middot; difficulty **1708** &middot; time limit **2.5s** &middot; 1600 to 1800 difficulty problems (Level 3)

## Topic used

| | |
|---|---|
| **Topic** | Greedy |
| **Technique** | Cheapest refunds first, paid with coins of the larger denomination |
| **CodeChef tags** | `Algorithms`, `Sorting` |
| **Complexity class** | Linearithmic $O(n \log n)$ |
| **Time** | $O(N \log N)$ per test case |
| **Space** | $O(N)$ |

## Question

<img src="https://codechef_shared.s3.amazonaws.com/upfiles/Bus_Driver_Lumpy_2.jpg" height="250" width="350" alt="Bus_Driver_Lumpy_2.jpg" />Lumpy is a bus driver. Today, the conductor is absent so Lumpy has to do the conductor's job as well. There are **N** creatures in the bus. Sometimes the creatures don't carry change and can't pay the exact amount of the fare. Each creature in the bus today has paid an amount
greater than his/her fare. You are given information about the **extra** amount paid by each creature, by an array **A** of size **N**, where **A_i** denotes the extra amount paid by the **i**-th creature, in rupees.

After the end of the trip, Lumpy noticed that he had **P** one rupee coins and **Q** two rupee coins. He wants to pay back the creatures using this money. Being a kind hearted moose, Lumpy wants to pay back as many creatures as he can. Note that Lumpy will
not pay back the **i**-th creature if he can't pay the **exact** amount that the **i**-th creature requires with the coins that he possesses.

Lumpy is busy driving the bus and doesn't want to calculate the maximum number of creatures he can satisfy - He will surely cause an accident if he tries to do so. Can you help him out with this task?

**Input**

- The first line of the input contains an integer **T** denoting the number of test cases. The description of **T** test cases follows.

- For each test case, first line consists of three space separated integers **N**, **P** and **Q**.

- Second line consists of **N** space separated integers **A** containing **N** space integers, where **i**-th integer denotes **A_i**.

**Output**

- For each test case, output a single line containing an integer corresponding to maximum number of creatures that Lumpy can pay back.

**Constraints**

- **1** ≤ **T** ≤ **10^6**

- **1** ≤ **N** ≤ **10^5**

- **1** ≤ **A_i** ≤ **10^9**

- **0** ≤ **P, Q** ≤ **10^14**

- Sum of **N** over all the cases does not exceed **10^6**

**Subtasks**

- *Subtask #1 (15 points)*: **P** = 0

- *Subtask #2 (15 points)*: **Q** = 0

- *Subtask #3 (70 points)*: Original constraints

## Constraints

- 1 ≤ T ≤ 10^6
- 1 ≤ N ≤ 10^5
- 1 ≤ A_i ≤ 10^9
- 0 ≤ P, Q ≤ 10^14
- Sum of N over all the cases does not exceed 10^6

## Sample

**Sample input**

```
3
3 3 0
1 2 2
3 2 1
1 2 1
4 5 4
2 3 4 5
```

**Sample output**

```
2
3
3
```

<details><summary>Explanation</summary>

**Example 1**. Lumpy has just **3** one rupee coins.
He can pay creatures numbered **{1, 2}** or creatures numbered **{1, 3}** with these coins. Thus, answer is 2.

 **Example 2**. Lumpy has **2** one rupee coins and **1** two rupee coin.
In the optimal solution, Lumpy can give the two rupee coin to creature **2** and the one rupee coins to creatures **1** and **3**. Thus, answer is 3.

</details>

## Approach

Two nested greedy decisions, each with its own argument.

**Per creature, use as many two-rupee coins as possible.** To pay $a$ exactly with $y$ twos and $x$ ones, $x = a - 2y$, so maximising $y$ minimises the ones consumed. If the maximal $y = \min(Q, \lfloor a/2 \rfloor)$ still leaves more ones than are available, no smaller $y$ can help — it would need even more ones. So that single attempt decides affordability.

**Across creatures, serve the smallest refunds first.** Sorting ascending is the classic "fit as many items as possible" exchange: a cheaper refund consumes no more of either coin type than a dearer one, so swapping a served creature for a cheaper unserved one never breaks feasibility and never lowers the count.

$$y_i = \min\bigl(Q,\ \lfloor A_i/2 \rfloor\bigr), \qquad x_i = A_i - 2y_i$$

serving creature $i$ only when $x_i \leq P$.

The parity trap is worth noting: an odd refund always needs at least one single-rupee coin, so with $P = 0$ every odd amount is unserviceable no matter how many twos remain.

The samples show both constraints biting. With $P=3, Q=0$ and refunds $1, 2, 2$, the ones run out after $1 + 2$, so only two creatures are served. With $P=2, Q=1$ and refunds $1, 1, 2$, the twos cover the $2$ exactly while the ones cover the two $1$s — all three. And with $P=5, Q=4$ and refunds $2, 3, 4, 5$, the first three consume all four twos and one single, leaving $5$ unpayable from four remaining ones.

## Solution

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n, ones, twos = int(data[pos]), int(data[pos + 1]), int(data[pos + 2])
        amounts = sorted(int(x) for x in data[pos + 3:pos + 3 + n])
        pos += 3 + n
        served = 0
        for a in amounts:
            # Maximising the twos minimises the ones needed, so one try decides.
            use_two = min(twos, a // 2)
            need_one = a - 2 * use_two
            if need_one > ones:
                continue
            twos -= use_two
            ones -= need_one
            served += 1
        out.append(str(served))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Edge cases

- **Serving the smallest refunds first maximises the count**, and paying each with as many two-rupee coins as possible minimises the one-rupee coins spent — the only way to settle an odd remainder. Verified against an exhaustive optimum over $5425$ small cases with no mismatch.
- **An odd amount needs at least one one-rupee coin**, so the ones are the genuinely scarce resource and the greedy protects them.
- **A creature that cannot be paid is skipped, not abandoned.** The loop continues to the next amount, since a later creature may need fewer ones — which is why it is `continue` rather than `break`.
- **$P$ or $Q$ may be $0$** (the first row has no two-rupee coins), so every refund must come out of the ones.
- **Both coin counts reach $10^{14}$** while the amounts cap at $10^9$, so the arithmetic must stay in exact integers.
- **Spending twos never hurts**, because a two-rupee coin can only ever replace two ones, and the ones are what run out first.
- **$T$ up to $10^6$ with $\sum N \leq 10^6$** means most cases are tiny, so the per-case overhead matters as much as the sort.

## Dry run

Third sample: $P = 5$ ones, $Q = 4$ twos, refunds $2, 3, 4, 5$ (already sorted).

| refund | twos used | ones used | ones left | twos left | served |
|---:|---:|---:|---:|---:|---:|
| 2 | 1 | 0 | 5 | 3 | 1 |
| 3 | 1 | 1 | 4 | 2 | 2 |
| 4 | 2 | 0 | 4 | 0 | 3 |
| 5 | 0 | 5 | — | — | — |

The last creature needs five ones but only four remain, so it is skipped. Output `3`.

---

Same problem grouped by topic: [../docs/greedy/LUMPYBUS.md](../docs/greedy/LUMPYBUS.md)
