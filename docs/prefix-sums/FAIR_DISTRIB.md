[&larr; 456. Maximise Sum](MAXIMISESUM.md) &middot; [Index](../../README.md) &middot; [476. Copy and Paste &rarr;](NCOPIES.md)

# 471. Fair Distribution

> CodeChef problem code [`FAIR_DISTRIB`](https://www.codechef.com/problems/FAIR_DISTRIB) &middot; difficulty **1741** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Prefix Sums |
| **Technique** | Reparametrising by gaps turns it into suffix sums |
| **Time** | $O(N)$ per test case |
| **Space** | $O(1)$ |
| **Roadmap course** | 1600 to 1800 difficulty problems (Level 3) |

## Question

A mother bought a set of $N$ toys for her $2$ kids, Alice and Bob. She has already decided which toy goes to whom, however she has forgotten the monetary values of the toys. She only remembers that she ordered the toys in ascending order of their value. The prices are always non-negative.

A distribution is said to be *fair* when no matter what the actual values were, the difference between the values of the toys Alice got, and the toys Bob got, does not exceed the maximum value of any toy.

Formally, let $v_i$ be the value of $i$-th toy, and $S$ be a binary string such that $S_i = 1$ if the toy is to be given to Alice, and $S_i = 0$ if the toy is to be given to Bob.
Then, the distribution represented by $S$ is said to be *fair* if, for **all possible** arrays $v$ satisfying $0 \le v_1 \le v_2 \le .... \le v_N$,

$$
\left| \sum\limits_{i = 1}^{N} v_i \cdot [s_i = 1] - \sum\limits_{i = 1}^{N} v_i \cdot [s_i = 0] \right| \leq v_N
$$

where $[P]$ is $1$ iff $P$ is true, and $0$ otherwise.

You are given the binary string $S$ representing the distribution.
Print `YES` if the given distribution is *fair*, and `NO` otherwise.

**Input**

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of two lines of input.
    - The first line of each test case contains a single integer $N$, the number of toys.
    - The second line of each test case contains a binary string $S$ of length $N$.

**Output**

For each test case, output on a new line the answer: `YES` or `NO` depending on whether $S$ represents a fair distribution or not.

Each character of the output may be printed in either lowercase or uppercase, i.e, the strings `NO`, `no`, `nO`, and `No` will all be treated as equivalent.

## Constraints

- $1 \leq T \leq 10^4$
- $1 \leq N \leq 10^5$
- The sum of $N$ over all test cases won't exceed $3 \cdot 10^5$.
- $S$ is a binary string of length $N$.

**Subtasks**

- **Subtask 1 (10 points):** $1 \leq M \leq 10$
- **Subtask 2 (20 points):** The sum of $N$ across all test cases won't exceed $20$.
- **Subtask 3 (70 points):** No further constraints.

## Sample

**Sample input**

```
6
1
1
2
00
4
1010
4
1100
6
010101
5
00001
```

**Sample output**

```
YES
NO
YES
NO
YES
NO
```

<details><summary>Explanation</summary>

**Test case $1$:** The given formula reduces to $|v_1| \le v_1$, which is true since $v_1 \ge 0$.

**Test case $2$:** The distribution is not fair for $v_1 = v_2 = 1$, hence the answer is `NO`.
Note that the distribution is fair for $v_1 = v_2 = 0$, but we need to check if its fair for all possible $v$ satisfying the constraints.

**Test case $3$:** It can be proved that the distribution is always fair.

**Test case $4$:** The distribution is not fair for $v = [1, 2, 4, 8]$.

</details>

## Approach

Set $c_i = +1$ when $S_i = \texttt{1}$ and $-1$ otherwise, so the quantity to bound is $\bigl|\sum_i c_i v_i\bigr| \leq v_N$ for **every** non-decreasing non-negative $v$.

The quantifier over all $v$ is handled by changing variables to the gaps $d_j = v_j - v_{j-1} \geq 0$ (with $d_1 = v_1$), which range freely over the non-negative reals. Since $v_i = \sum_{j \leq i} d_j$, swapping the order of summation gives

$$\sum_i c_i v_i = \sum_j d_j \underbrace{\sum_{i \geq j} c_i}_{T_j}, \qquad v_N = \sum_j d_j$$

So the condition is $\bigl|\sum_j d_j T_j\bigr| \leq \sum_j d_j$ for all $d \geq 0$. Taking $d$ to be a single unit at position $j$ forces $|T_j| \leq 1$; conversely if every $|T_j| \leq 1$ then the triangle inequality gives the bound. Hence

$$\text{fair} \iff \bigl|T_j\bigr| \leq 1 \text{ for every suffix } j$$

a single right-to-left sweep. Note it is the **suffix** sums, not prefix sums, that matter — the gap at position $j$ raises every $v_i$ with $i \geq j$.

The samples show the mechanism. `1010` has suffix sums $0, -1, 0, -1$, all within range: fair. `1100` has the suffix sum $-2$ at $j = 3$, so making $v_3 = v_4$ large and $v_1 = v_2 = 0$ breaks the bound. `00` likewise has $T_1 = -2$. `00001` has $T_2 = -2$, so even a single toy for Alice at the end cannot rescue it. And `1` is fair because the only suffix sum is $1$.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        s = data[2 + 2 * i]
        # Each gap v_j - v_{j-1} weights the suffix sum from j onwards.
        run = 0
        ok = True
        for c in reversed(s):
            run += 1 if c == 0x31 else -1
            if run > 1 or run < -1:
                ok = False
                break
        out.append("YES" if ok else "NO")
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(N)$ per test case
- **Space:** $O(1)$

## Edge cases

- **Reparametrising by gaps is what makes this one scan.** Writing $v_i = \sum_{j \leq i} d_j$ with $d_j \geq 0$ turns the difference into $\sum_j d_j \cdot (\text{suffix sum of signs from } j)$, while the maximum value is $\sum_j d_j$.
- **So fairness means every suffix sum of signs lies in $[-1, 1]$.** Concentrating all the value in one gap shows each bound is necessary, and the triangle inequality shows they suffice.
- **The scan runs right to left**, accumulating $+1$ for Alice and $-1$ for Bob, and fails the moment the running total leaves the band.
- **A single toy** (the first row) has suffix sum $\pm 1$ and is always fair.
- **Two toys to the same kid** (the second row, `00`) gives a suffix sum of $-2$ and fails — even though the values are unknown, the adversary can make both toys expensive and equal.
- **Alternating assignments are fair** (the fifth row), since the running total never leaves $\{-1, 0, 1\}$.
- **Trailing imbalance is what the last row catches**: `00001` starts fine but accumulates $-2$ once the three leading zeros are reached.
- **The toys are given in ascending value order**, which is exactly what makes the gaps non-negative and the reparametrisation valid.

## Dry run

Last sample: $S = $ `00001`, scanned from the right.

| position | owner | running suffix sum |
|---:|---|---:|
| 5 | Alice | $+1$ |
| 4 | Bob | $0$ |
| 3 | Bob | $-1$ |
| 2 | Bob | **$-2$** |

The band is breached at position $2$, so `NO`. Concretely, with all five toys worth $1$ Bob holds $4$ against Alice's $1$, a difference of $3$ above the maximum value of $1$.

---

Same problem in rating order (#443 of 486): [../../by-rating/443-FAIR_DISTRIB.md](../../by-rating/443-FAIR_DISTRIB.md)
