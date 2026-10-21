# 422. Encrypt Value

> CodeChef problem code [`ENV`](https://www.codechef.com/problems/ENV) &middot; difficulty **1633** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Greedy |
| **Technique** | Choosing which elements to add rather than multiply |
| **Time** | $O(N)$ per test case |
| **Space** | $O(N)$ |
| **Roadmap course** | 1600 to 1800 difficulty problems (Level 3) |

## Question

You are given an array $A$ containing $N$ integers.

Consider the following process:
- Let $S = 0$ initially.
- For each $i$ from $1$ to $N$ **in order**, update $S$ to either $(S+A_i)$ or $(S\times A_i)$.
That is, either add $A_i$ to $S$ or multiply $S$ by $A_i$.

Before performing the process, you're allowed to freely rearrange the elements of $A$ as you like.
If you choose the rearrangement of $A$ and the sequence of operations optimally, what's the **maximum** possible value of $S$ that you can obtain?

This maximum value can be very large, so print it modulo $10^9 + 7$.

**Input**

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of two lines of input.
    - The first line of each test case contains a single integer $N$ — the number of elements in the array.
    - The second line contains $N$ space-separated integers $A_1, A_2, \ldots, A_N$ - the elements of the array.

**Output**

For each test case, output on a new line the maximum possible value of $S$, modulo $10^9 + 7$.

## Constraints

- $1 \leq T \leq 10^3$
- $1 \leq N \leq 2 \cdot 10^5$
- $1 \leq A_i \leq 10^9$
- The sum of $N$ over all test cases won't exceed $2 \cdot 10^5$.

**Subtasks**

- **Subtask 1 (10 points):** $1 \leq M \leq 10$
- **Subtask 2 (20 points):** The sum of $N$ across all test cases won't exceed $20$.
- **Subtask 3 (70 points):** No further constraints.

## Sample

**Sample input**

```
2
4
4 2 5 2
3
1 2 1
```

**Sample output**

```
80
4
```

<details><summary>Explanation</summary>

**Test case $1$:** Choose the rearrangement $A = [2, 2, 5, 4]$. Then,
- Add $A_1 = 2$ to $S$. Now, $S = 2$.
- Add $A_2 = 2$ to $S$. Now, $S = 4$.
- Multiply $S$ by $A_3 = 5$. Now, $S = 20$.
- Multiply $S$ by $A_4 = 4$. Now, $S = 80$.

This is the maximum value that can be obtained.

**Test case $2$:** Choose any rearrangement and sum up all the numbers to get $1+1+2 = 4$.
This is the maximum value that can be obtained.

</details>

## Approach

$S$ starts at $0$, so the first step must be an addition — multiplying would pin $S$ at $0$ forever. Beyond that, the best shape is clear: do all the additions first and then all the multiplications, giving

$$S = \Bigl(\sum_{x \in T} x\Bigr) \cdot \prod_{x \notin T} x$$

for the chosen non-empty added set $T$. An addition made after a multiplication contributes only its own value, so it is never better.

Now choose $T$. For values $\geq 2$ it never pays to add two of them: $a + b \leq ab$ whenever $a, b \geq 2$, so moving one back into the product is at least as good. And adding a *single* value $a$ gives $a \cdot (\Pi/a) = \Pi$ — the same total whichever one it is. So with no ones present the answer is simply the full product $\Pi$.

Ones are the interesting case, because multiplying by $1$ wastes an element while adding it gains $1$. Let $c$ be the number of ones and $\Pi'$ the product of the rest:

- $c = 0$: answer $\Pi'$.
- $c \geq 2$: add all the ones, multiply everything else: $c \cdot \Pi'$. Pulling a value $a$ out of the product to add it would give $\frac{(c+a)}{a}\Pi' \leq c\Pi'$ exactly when $c \geq \frac{a}{a-1}$, which holds for $c \geq 2$.
- $c = 1$: that inequality flips, so add the one *and* the smallest other value $a$, giving $(1+a) \cdot \Pi'/a$. The smallest $a$ maximises $1 + 1/a$.
- all ones: nothing can be multiplied usefully, so the answer is $N$.

The samples show two of these. $[4,2,5,2]$ has no ones, so the answer is $4 \cdot 2 \cdot 5 \cdot 2 = 80$. $[1,2,1]$ has $c = 2$, giving $2 \cdot 2 = 4$ — the same as adding everything, and better than the $3$ that multiplying by a one would waste.

The case analysis is exact, so the modulus is applied only at the end; comparisons are never made on reduced values.

## Solution (Python)

```python
import sys

MOD = 1_000_000_007


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n = int(data[pos])
        vals = [int(x) for x in data[pos + 1:pos + 1 + n]]
        pos += 1 + n
        others = [v for v in vals if v > 1]
        ones = n - len(others)
        if not others:
            out.append(str(ones % MOD))       # nothing is worth multiplying
            continue
        if ones >= 2:
            seed = ones                       # add every one, multiply the rest
        else:
            # With no ones, a * (product / a) is the full product either way;
            # with exactly one, adding the smallest factor too beats keeping it.
            smallest = min(others)
            others.remove(smallest)
            seed = ones + smallest
        prod = 1
        for v in others:
            prod = prod * v % MOD
        out.append(str(seed * prod % MOD))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(N)$ per test case
- **Space:** $O(N)$

> CodeChef tags: `Algorithms`
