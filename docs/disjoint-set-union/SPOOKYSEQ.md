[&larr; 543. Home Delivery](HDELIVER.md) &middot; [Index](../../README.md) &middot; [707. Ancient Berland Roads &rarr;](ABROADS.md)

# 699. Spooky Sequences

> CodeChef problem code [`SPOOKYSEQ`](https://www.codechef.com/problems/SPOOKYSEQ) &middot; difficulty **2304** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Disjoint Set Union |
| **Technique** | Interleave the components, then permute equal strengths inside each |
| **Time** | $O((N + M)\,\alpha(N))$ per test case after factorial precomputation |
| **Space** | $O(N + M)$ |
| **Roadmap course** | 2000 to 2500 difficulty problems (Level 5) |

## Question

*“I am not a witch. I’m your wife.”
\- Valerie, The Princess Bride*

Once upon a time, in a distant land, a mischievous witch spied on a group of people who were enjoying their time together.

Enveloped by a dark desire, she resolved to put an end to their merry gatherings and kill all $N$ people.

There are $N$ people, and the witch knows that the $i$-th of them has a strength of $A_i$.
The witch also knows of $M$ friendships, each between two people.
Friendship is transitive, that is, if $X$ and $Y$ are friends and $Y$ and $Z$ are friends, then $X$ and $Z$ are also friends.

The witch wants to kill all these people in a particular sequence known as a *spooky sequence*.

A sequence $S$ is called a *spooky sequence* if it satisfies the following properties:
- $S$ contains $N$ **distinct** integers, each between $1$ and $N$.
That is, $S$ is a linear order of the $N$ people.
- For any $1 \leq i \lt j \leq N$, if $S_i$ and $S_j$ are **friends**, then $A_{S_i} \leq A_{S_j}$ should hold.
That is, for any two friends, one with *strictly* higher strength cannot appear earlier in the sequence than the other.

Find the total number of *spooky sequences*. The answer can be large, so print it modulo $10^9 + 7$.

**Input**

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of multiple lines of input.
    - The first line of each test case contains two space-separated integers $N$ and $M$ — the number of people and number of friendships, respectively.
    - The next $M$ lines describe the friendships. The $i$-th of these $M$ lines contains two space-separated integers $u_i$ and $v_i$, denoting a friendship between $u_i$ and $v_i$.
    - The last line contains $N$ space-separated integers $A_1, A_2,\ldots, A_N$ — the strengths of the people.

**Output**

For each test case, output on a new line the number of *spooky sequences*, modulo $10^9 + 7$.

## Constraints

- $1 \leq T \leq 2 \cdot 10^4$
- $1 \leq N \leq 2 \cdot 10^5$
- $0 \leq M \leq \min(2 \cdot 10^5,N\cdot(N-1)/2)$
- $1 \leq u_i, v_i \leq N$
- $u_i \neq v_i$ for each $1 \leq i \leq M$.
- Each unordered pair $(u_i, v_i)$ appears at most once in a testcase.
- $1 \leq A_i \leq 10^9$
- The sum of $N$  over all test cases won't exceed $2 \cdot 10^5$.
- The sum of $M$  over all test cases won't exceed $2 \cdot 10^5$.

**Subtasks**

- **Subtask 1 (10 points):** $1 \leq M \leq 10$
- **Subtask 2 (20 points):** The sum of $N$ across all test cases won't exceed $20$.
- **Subtask 3 (70 points):** No further constraints.

## Sample

**Sample input**

```
2
5 5
1 2
2 3
3 4
4 2
3 1
10 12 15 20 15
5 2
2 3
4 5
6 4 4 3 1
```

**Sample output**

```
5
60
```

<details><summary>Explanation</summary>

**Test case $1$:** Each pair among $\{1, 2, 3, 4\}$ are friends, while $5$ is not friends with anyone else. Taking into account the strength condition for the group of $4$, there are five spooky sequences:
$[5, 1, 2, 3, 4]$
$[1, 5, 2, 3, 4]$
$[1, 2, 5, 3, 4]$
$[1, 2, 3, 5, 4]$
$[1, 2, 3, 4, 5]$

**Test case $2$:** $2$ and $3$ are friends, $4$ and $5$ are friends, and $1$ is not a friend of anyone else.
So, in any ordering:
- $A_2 = A_3$, so the order of $2$ and $3$ doesn't matter (even though they are friends).
- $4$ should appear after $5$, since $A_4\gt A_5$.
- There are no further constraints.

It can be verified that there are $60$ sequences satisfying this.

</details>

## Approach

Friendship is transitive, so the people fall into groups of friends - the connected components of the friendship graph, found with a disjoint-set union. Within one group the order is dictated by strength, while different groups do not constrain each other.

Count the sequences in two stages.

- Choose which positions of the sequence belong to which group: a multinomial coefficient $N! / \prod_g (\text{size}_g)!$.
- Inside a group the members appear in the order of their strengths, which fixes everything except the relative order of members with equal strength; each set of $z$ members sharing a group and a strength can be arranged in $z!$ ways.

The answer is the product of these factors modulo $10^9 + 7$. A Counter over (component root, strength) gives the sizes of the equal-strength sets.

## Solution (Python)

```python
import sys
from collections import Counter


P = 1000000007
fact = [1] * 200001
for i in range(1, 200001):
    fact[i] = fact[i - 1] * i % P
inv_fact = [1] * 200001
inv_fact[-1] = pow(fact[-1], P - 2, P)
for i in range(200000, 0, -1):
    inv_fact[i - 1] = inv_fact[i] * i % P


def solve(tokens):
    n, m = (next(tokens), next(tokens))
    parent = list(range(n))
    size = [1] * n

    def root(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    for _ in range(m):
        u, v = (root(next(tokens) - 1), root(next(tokens) - 1))
        if u != v:
            if size[u] < size[v]:
                u, v = (v, u)
            parent[v] = u
            size[u] += size[v]
    equal_groups = Counter(((root(i), next(tokens)) for i in range(n)))
    MOD = 1000000007
    answer = fact[n]
    for i in range(n):
        if parent[i] == i:
            answer = answer * inv_fact[size[i]] % MOD
    for count in equal_groups.values():
        answer = answer * fact[count] % MOD
    return str(answer)


if __name__ == "__main__":
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    t = int(next(tokens))
    out = [solve(tokens) for _ in range(t)]
    sys.stdout.write('\n'.join(out))
```

## Complexity

- **Time:** $O((N + M)\,\alpha(N))$ per test case after factorial precomputation
- **Space:** $O(N + M)$
- Auxiliary space excludes the buffered input and output.

## Edge cases

- No friendships: every person is a separate group and all $N!$ orders are counted.
- One group with distinct strengths: exactly one sequence.
- Equal strengths in different groups do not interact.
- Factorials are precomputed once up to the maximum $N$.

## Dry run

Second sample: friendships `2-3` and `4-5`, strengths `6 4 4 3 1`.

Groups: `{1}`, `{2, 3}`, `{4, 5}`. Interleavings: $5! / (1! \, 2! \, 2!) = 30$.

In `{2, 3}` both strengths are 4, so the two can swap: factor $2!$. In `{4, 5}` the strengths differ: factor 1.

Answer $30 \cdot 2 = 60$.

---

Same problem in rating order (#663 of 735): [../../by-rating/663-SPOOKYSEQ.md](../../by-rating/663-SPOOKYSEQ.md)
