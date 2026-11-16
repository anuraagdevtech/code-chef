[&larr; 690. Adjacent Flips](690-ADJFLIP.md) &middot; [Index](README.md) &middot; [692. Balanced Suffix &rarr;](692-BALSUFF.md)

# 691. Max Shift After XOR

> [`MAXCYCSHIFT`](https://www.codechef.com/problems/MAXCYCSHIFT) &middot; difficulty **2444** &middot; time limit **1.5s** &middot; 2000 to 2500 difficulty problems (Level 5)

## Topic used

| | |
|---|---|
| **Topic** | Hashing |
| **Technique** | Sliding window over the prefix xors of the doubled array |
| **CodeChef tags** | `Mathematics`, `Bit Manipulation`, `Algorithms`, `Simple Algos`, `Bitwise Operation`, `Two pointers`, `Prefix Sum` |
| **Complexity class** | Linear $O(n)$ |
| **Time** | $O(N)$ expected per test case |
| **Space** | $O(N)$ |

## Question

You are given an array $A$, consisting of $N$ integers.

Consider the following definitions:
- *Prefix xor array* of an array $A$ is defined as the array $B$ such that $B_i = A_1 \oplus \ldots \oplus A_i$, where $\oplus$ denotes [bitwise XOR operation](https://en.wikipedia.org/wiki/Bitwise_operation#XOR).
In other words, $B=[A_1, A_1 \oplus A_2, \ldots, A_1 \oplus A_2 \ldots \oplus A_N]$
- The *value* of an array $A$ is the number of *distinct* values in array $B$. For example, for array $A=[1, 2, 3, 0]$, we have $B=[1, 3, 0, 0]$. The array $B$ has $3$ distinct values, thus, the value of array $A$ is $3$.
- One right shift on the array $A$ is a transformation that changes the array $A=[A_1, A_2 \ldots, A_N]$ to $A^{'}=[A_N, A_1, \ldots, A_{N-1}]$.

Calculate the **maximum** *value* of the array $A$ you can get, by performing any (possibly zero) number of right shifts on the array $A$.

**Input**

- The first line of input contains $T$ $-$ the number of test cases you need to solve.
- The first line of each test case contains one integer $N$ $-$ the size of the array.
- The second line of each test case contains $N$ space-separated integers $A_1, \ldots, A_N$ $-$ the elements of the array $A$.

**Output**

For each test case, output on a new line the maximum value of an array $A$ you can achieve after performing any (possibly zero) number of right shifts on the array.

## Constraints

- $1 \leq T \leq 10^5$
- $2 \leq N \leq 2 \cdot 10^5$
- $0 \le A_i \le 2^{60} - 1$
- Sum of $N$ over all test cases doesn't exceed $2 \cdot 10^5$.

**Subtasks**

- **Subtask 1 (20 points):** Sum of $N$ over all test cases doesn't exceed $2000$.
- **Subtask 2 (80 points):** Original constraints.

## Sample

**Sample input**

```
3
2
0 0
6
1 1 1 2 2 2
4
1 2 2 8
```

**Sample output**

```
1
4
4
```

<details><summary>Explanation</summary>

**Test case $1$:** Perform zero right shifts on $A=[0,0]$. Thus, $B= [0, 0\oplus0]=[0,0]$. Thus, the *value* of array $A$ is $1$.

**Test case $2$:** Perform two right shifts on $A = [1, 1, 1, 2, 2, 2]$. Thus, $A$ becomes $[2, 2, 1, 1, 1, 2]$. The array $B = [2, 0, 1, 0, 1, 3]$. Thus, the *value* of $A$ is $4$. It can be shown that the value of $A$ cannot exceed $4$.

**Test case $3$:** Perform three right shifts on $A = [1, 2, 2, 8]$. Thus, $A$ becomes $[2, 2, 8, 1]$. The array $B = [2, 2\oplus 2, 2\oplus 2\oplus 8, 2\oplus 2\oplus 8\oplus 1] = [2, 0, 8, 9]$. Thus, the *value* of $A$ is $4$. It can be shown that the value of $A$ cannot exceed $4$.

</details>

## Approach

Write the array twice and let $P$ be the prefix-xor array of the doubled array, $P_0 = 0$. The rotation that starts at position $i$ has prefix xors

$$P_{i+1} \oplus P_i,\; P_{i+2} \oplus P_i,\; \dots,\; P_{i+N} \oplus P_i .$$

Xor with the fixed value $P_i$ is a bijection, so the number of distinct values among them equals the number of distinct values in the window $P_{i+1}, \dots, P_{i+N}$.

So the answer is the maximum number of distinct values in a window of length $N$ sliding over $P_1, \dots, P_{2N-1}$. Maintain a frequency table of the window: when it moves by one, decrement the outgoing value (deleting it when it reaches zero) and increment the incoming one; the number of keys is the current count. Every right shift is one of these $N$ rotations.

## Solution

```python
import sys
from collections import Counter


def solve(tokens):
    n = next(tokens)
    values = [next(tokens) for _ in range(n)]
    prefix = [0]
    for value in values + values:
        prefix.append(prefix[-1] ^ value)
    window = Counter(prefix[1:n + 1])
    best = len(window)
    for i in range(1, n):
        value = prefix[i]
        window[value] -= 1
        if not window[value]:
            del window[value]
        value = prefix[i + n]
        window[value] += 1
        best = max(best, len(window))
    return str(best)


if __name__ == "__main__":
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    t = int(next(tokens))
    out = [solve(tokens) for _ in range(t)]
    sys.stdout.write('\n'.join(out))
```

## Edge cases

- All elements 0: every prefix xor is 0 and the answer is 1.
- Values go up to $2^{60}$, so a hash map is used rather than an array.
- Only $N$ different rotations exist.
- The common xor constant can be ignored entirely.

## Dry run

`A = [1, 2, 2, 8]`. Doubled prefix xors $P_1 \dots P_8$: `1 3 1 9 8 10 8 0`.

- window $P_1..P_4$ = `1 3 1 9`: 3 distinct
- window $P_2..P_5$ = `3 1 9 8`: 4 distinct

Four is the maximum possible for $N = 4$. Answer 4.

---

Same problem grouped by topic: [../docs/hashing/MAXCYCSHIFT.md](../docs/hashing/MAXCYCSHIFT.md)
