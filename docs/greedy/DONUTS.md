# 391. Chain of Doughnuts

> CodeChef problem code [`DONUTS`](https://www.codechef.com/problems/DONUTS) &middot; difficulty **1611** &middot; time limit **2s**

| | |
|---|---|
| **Topic** | Greedy |
| **Technique** | Trading sacrificed chains against links needed |
| **Time** | $O(M \log M)$ per test case |
| **Space** | $O(M)$ |
| **Roadmap course** | 1600 to 1800 difficulty problems (Level 3) |

## Question

There is new delicious item in Chef's menu - a doughnut chain. Doughnuts connected successively in line forming a chain.

<img src="https://s3.amazonaws.com/codechef_shared/download/SEPT15/DONUT1.jpg" />

*Chain of 3 doughnuts*

Chef has received an urgent order for making a chain of **N** doughnuts. He noticed that there are exactly **N** cooked doughnuts in the kitchen, some of which are already connected in chains. The only thing he needs to do is connect them in one chain.

He can cut one doughnut (from any position in a chain) into two halves and then use this cut doughnut to link two different chains.

Help Chef determine the minimum number of cuts needed to complete the order.

**Input**

- The first line of the input contains an integer **T** denoting the number of test cases.

- The first line of each test case contains two integer **N** and **M** denoting the size of order and number of cooked chains respectively.

- The second line contains **M** space-separated integers **A_1**, **A_2**, ..., **A_M** denoting the size of the chains.

*It is guaranteed that **N** is equal to the sum of all **A_i**'s over **1<=i*<=M**.

**Output**

For each test case, output a single line containing an integer corresponding to the number of cuts needed Chef to make the order.

**Constraints and Subtasks**

- **1** ≤ **T** ≤ **200**

- **1** ≤ **N** ≤ **2*10^9**

- **1** ≤ **A_i** ≤ **10^5**

**Subtask 1: 10 points**

- **1** ≤ **M** ≤ **2*10^4**

- **A_i = 1**

**Subtask 2: 30 points**

- **1** ≤ **M** ≤ **100**

**Subtask 3: 60 points**

- **1** ≤ **M** ≤ **2*10^4**

## Constraints

- $1 \leq T \leq 200$
- $1 \leq N \leq 2 \cdot 10^9$
- $1 \leq M \leq 2 \cdot 10^4$
- $1 \leq A_i \leq 10^5$
- $N$ is guaranteed to equal $\sum_{i=1}^{M} A_i$

## Sample

**Sample input**

```
2
11 3
4 3 4
6 3
3 2 1
```

**Sample output**

```
2
1
```

<details><summary>Explanation</summary>

**Example 1:** We could cut 2 doughnut from any "chain" and use them to connect chains to the one.
 For example, let's cut it from the first chain. After this we will have chains of sizes 2, 3, 4 and two doughnuts that have been cut. So we could connect the first chain with second and second with third using these two doughnuts.

**Example 2:** We cut doughnut from the last "chain" and connect the first two chains.

<img src="https://s3.amazonaws.com/codechef_shared/download/SEPT15/DONUT2.png" />

*Image for second example. Yellow doughnut has been cut.*

</details>

## Approach

Each cut doughnut becomes one **link**, and joining $p$ separate pieces into a single chain takes $p - 1$ links. So the cost depends on how many pieces survive, and the only lever is how many chains are consumed entirely for link material.

Suppose the $d$ **smallest** chains are sacrificed, supplying $\mathrm{pre}[d] = A_1 + \cdots + A_d$ cuts (sorted ascending). Then $M - d$ pieces remain and need $M - d - 1$ links. Whichever of the two numbers is larger is the number of cuts:

$$\text{cost}(d) = \max\bigl(\mathrm{pre}[d],\ M - d - 1\bigr)$$

If the sacrifice falls short, the shortfall is taken a doughnut at a time from the end of a surviving chain, which shortens it without splitting it. If the sacrifice overshoots, the surplus cuts are made later, from inside the partly-assembled chain. Sacrificing the smallest chains is optimal because $\mathrm{pre}[d]$ is what we pay and it is minimised by taking the cheapest chains first.

As $d$ grows, $\mathrm{pre}[d]$ rises and $M - d - 1$ falls, so the cost is a V shape and the minimum sits at their crossover; with $M \leq 2 \times 10^4$ a direct scan over $d$ is simplest.

The two samples land on either side of that crossover. For chains $4, 3, 4$ nothing is worth sacrificing: $d = 0$ needs $M - 1 = 2$ links, taken from the end of a chain, while sacrificing the $3$-chain would already cost $3$. For chains $3, 2, 1$ the singleton is nearly free — sacrificing it costs $1$ cut and leaves just two pieces, needing exactly $1$ link, so the answer is $1$ rather than $2$.

Note $N$ reaches $2 \times 10^9$ but never enters the computation; only the chain sizes and their count matter.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        m = int(data[pos + 1])
        chains = sorted(int(x) for x in data[pos + 2:pos + 2 + m])
        pos += 2 + m
        # Sacrificing the d cheapest chains supplies pre[d] links but leaves
        # M - d pieces still needing M - d - 1.
        best = m - 1
        used = 0
        for d in range(1, m):
            used += chains[d - 1]
            cost = used if used > m - d - 1 else m - d - 1
            if cost < best:
                best = cost
        out.append(str(best))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(M \log M)$ per test case
- **Space:** $O(M)$
