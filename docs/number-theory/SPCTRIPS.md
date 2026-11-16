[&larr; 565. Number of Factors](NUMFACT.md) &middot; [Index](../../README.md) &middot; [567. Levy Conjecture &rarr;](LEVY.md)

# 566. Special Triplets

> CodeChef problem code [`SPCTRIPS`](https://www.codechef.com/problems/SPCTRIPS) &middot; difficulty **1673** &middot; time limit **0.5s**

| | |
|---|---|
| **Topic** | Number Theory |
| **Technique** | Reduce scaled triples to divisor summatory counts |
| **Time** | $O(V\log V+T\sqrt V)$ overall for $V=\max N$ |
| **Space** | $O(V+T)$ |
| **Roadmap course** | Rise from 3* to 4* (Level 4) |

## Question

Gintoki has been very lazy recently and he hasn't made enough money to pay the rent this month. So the old landlady has given him a problem to solve instead, if he can solve this problem the rent will be waived.
The problem is as follows:

A triplet of integers $(A, B, C)$ is considered to be special if it satisfies the following properties for a given integer $N$ :

- $A \bmod B = C$
- $B \bmod C = 0$
- $1 \le A, B, C \le N$

**Example**: There are three special triplets for $N = 3$.
- $(1, 3, 1)$ is a special triplet, since $(1 \bmod 3) = 1$ and $(3 \bmod 1) = 0$.
- $(1, 2, 1)$ is a special triplet, since $(1 \bmod 2) = 1$ and $(2 \bmod 1) = 0$.
- $(3, 2, 1)$ is a special triplet, since $(3 \bmod 2) = 1$ and $(2 \bmod 1) = 0$.

The landlady gives Gintoki an integer $N$. Now Gintoki needs to find the number of special triplets. Can you help him to find the answer?

**Input**

- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first and only line of each test case contains a single integer $N$.

**Output**

- For each testcase, output in a single line the number of special triplets.

## Constraints

- $1 \leq T \leq 10$
- $2 \leq N \leq 10^5$

**Subtasks**

**Subtask #1 (5 points):** $2 \le N \le 10^3$

**Subtask #2 (20 points):** $2 \le N \le 10^4$

**Subtask #3 (75 points):**  Original constraints

## Sample

**Sample input**

```
3
3
4
5
```

**Sample output**

```
3
6
9
```

<details><summary>Explanation</summary>

**Test case $1$**: It is explained in the problem statement.

**Test case $2$**: The special triplets are $(1, 3, 1)$, $(1, 2, 1)$, $(3, 2, 1)$, $(1, 4, 1)$,  $(4, 3, 1)$, $(2, 4, 2)$. Hence the answer is $6$.

**Test case $3$**: The special triplets are $(1, 3, 1)$, $(1, 2, 1)$, $(3, 2, 1)$, $(1, 4, 1)$, $(4, 3, 1)$, $(1, 5, 1)$, $(5, 4, 1)$, $(5, 2, 1)$, $(2, 4, 2)$. Hence the answer is $9$.

</details>

## Approach

Fix $C$ and write $B=kC$ with $k\ge2$. The congruence $A\bmod B=C$ means $A=C+qB$. With $m=\lfloor N/C\rfloor$, there are $\lfloor(m-1)/k\rfloor+1$ choices for $A$. Summing over $k=2$ through $m$ simplifies to $D(m-1)=\sum_{j=1}^{m-1}\lfloor(m-1)/j\rfloor$.

Precompute $D$ as the prefix sum of ordinary divisor counts using a divisor sieve. The answer is $\sum_{C=1}^{\lfloor N/2\rfloor}D(\lfloor N/C\rfloor-1)$. Group consecutive $C$ values having the same quotient $N//C$, giving only square-root many groups per query.

## Solution (Python)

```python
import sys


def main() -> None:
    values = list(map(int,sys.stdin.buffer.read().split()))
    limit = max(values[1:])
    divisor_prefix = [0]*(limit+1)
    for d in range(1,limit+1):
        for multiple in range(d,limit+1,d):
            divisor_prefix[multiple] += 1
    for i in range(1,limit+1):
        divisor_prefix[i] += divisor_prefix[i-1]
    out = []
    for n in values[1:]:
        answer = 0
        left = 1
        end = n//2
        while left <= end:
            quotient = n//left
            right = min(end,n//quotient)
            answer += (right-left+1)*divisor_prefix[quotient-1]
            left = right+1
        out.append(str(answer))
    sys.stdout.write('\n'.join(out)+'\n')

if __name__ == '__main__':
    main()
```

## Complexity

- **Time:** $O(V\log V+T\sqrt V)$ overall for $V=\max N$
- **Space:** $O(V+T)$
- Auxiliary space excludes the buffered input and output.

## Edge cases

- $C$ is positive and strictly smaller than $B$.
- $A=C$ is valid when $A<B$; it corresponds to $q=0$.
- Triple counts are exact integers without a modulus.

## Dry run

For `N=4`, `C=1` contributes `D(3)=5` triples and `C=2` contributes `D(1)=1`, giving six.

---

Same problem in rating order (#410 of 735): [../../by-rating/410-SPCTRIPS.md](../../by-rating/410-SPCTRIPS.md)
