[&larr; 293. Yet Another Constructive Problem](ORANDCON.md) &middot; [Index](../../README.md) &middot; [313. Missing a Point &rarr;](PTMSSNG.md)

# 303. Consecutive Xor

> CodeChef problem code [`XOR2`](https://www.codechef.com/problems/XOR2) &middot; difficulty **1611** &middot; time limit **1.5s**

| | |
|---|---|
| **Topic** | Bit Manipulation |
| **Technique** | The total XOR is invariant |
| **Time** | $O(N)$ per test case |
| **Space** | $O(1)$ |
| **Roadmap course** | 1400 to 1600 difficulty problems (Level 2) |

## Question

Chef has an array $A$ of length $N$. He can perform the following operation on $A$:

**1)** Select an index $i$ $(1 \le i \le N - 1)$ and select an integer $X$ $(1 \le X \lt 2^{20})$. $\\$
**2)** Set $A_i := (A_i \oplus X)$ and $A_{i + 1} := (A_{i + 1} \oplus X)$. (Here, $\oplus$ denotes the [bitwise XOR operation](https://en.wikipedia.org/wiki/Bitwise_operation#XOR))

Determine if Chef can make all the elements of $A$ equal by applying the above operation any number of times (possibly zero).

**Input**

- The first line contains a single integer $T$ — the number of test cases. Then the test cases follow.
- The first line of each test case contains an integer $N$ — the size of the array $A$.
- The second line of each test case contains $N$ space-separated integers $A_1, A_2, \dots, A_N$ denoting the array $A$.

**Output**

For each test case, output `YES` if it is possible to make all the elements of $A$ equal by applying the given operation any number of times. Otherwise, output `NO`.

You may print each character of `YES` and `NO` in uppercase or lowercase (for example, `yes`, `yEs`, `Yes` will be considered identical).

## Constraints

- $1 \leq T \leq 10^5$
- $1 \leq N \leq 10^5$
- $0 \le A_i \lt 2^{20}$
- The sum of $N$ over all test cases won't exceed $2 \cdot 10^5$.

## Sample

**Sample input**

```
3
4
3 2 2 3
6
0 1 2 3 4 5
3
1 2 4
```

**Sample output**

```
YES
NO
YES
```

<details><summary>Explanation</summary>

**Test Case 1:** We can apply the following operation:
- $[3, 2, 2, 3] \xrightarrow{i = 2, X = 1} [3, 3, 3, 3]$

**Test Case 2:** It can be proved that we can not make all the elements of $A$ equal by applying the given operation.

**Test Case 3:** We can apply the following operations:
- $[1, 2, 4] \xrightarrow{i = 1, X = 6} [7, 4, 4] \xrightarrow{i = 2, X = 3} [7, 7, 7]$

</details>

## Approach

Each operation XORs the **same** $X$ into two neighbouring elements. In the XOR of the whole array those two contributions cancel, since $X \oplus X = 0$. So

$$A_1 \oplus A_2 \oplus \cdots \oplus A_N \;\text{ is invariant}$$

no matter how many operations are applied.

Now look at the target. If every element ends up equal to some $v$, the total XOR of the final array is $v$ when $N$ is **odd** (the copies cancel in pairs, leaving one) and $0$ when $N$ is **even** (they cancel completely).

- **$N$ odd.** The invariant imposes no obstruction — whatever the starting total $S$ is, the target value $v = S$ is consistent, and the operations are flexible enough to reach it. So the answer is always `YES`.
- **$N$ even.** The final total must be $0$, so the starting total must be $0$ too. The answer is `YES` exactly when $S = 0$.

Sample case 1, $[3,2,2,3]$, has even length and total $3 \oplus 2 \oplus 2 \oplus 3 = 0$ — `YES`. Sample case 2 has even length but total $1$, so no sequence of operations can ever fix it — `NO` regardless of effort.

Sample case 3, $[1,2,4]$, is odd-length and so succeeds even though its elements look entirely unrelated; the target is simply $1 \oplus 2 \oplus 4 = 7$.

Finding the conserved quantity is the whole solution — it decides both directions at once, and the answer is a single XOR fold plus a parity check.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n = int(data[pos])
        total = 0
        for v in data[pos + 1:pos + 1 + n]:
            total ^= int(v)
        pos += 1 + n
        # Operations preserve the total XOR; an even-length all-equal array
        # must have total 0.
        out.append("YES" if n % 2 or total == 0 else "NO")
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(N)$ per test case
- **Space:** $O(1)$

## Edge cases

- **The total XOR is invariant.** Each operation XORs two *adjacent* elements with the same $X$, so those two contributions cancel in the overall XOR — nothing any sequence of moves can change.
- **That settles the even case immediately**: if all $N$ elements end up equal to $v$ and $N$ is even, the total XOR is $0$, so a non-zero total makes it impossible.
- **An odd $N$ is always possible**, since the invariant then permits $v$ equal to the total XOR, and the operation is flexible enough to shuffle any XOR value along the array.
- **An odd $N$ needs no inspection of the values at all** (the third row, $1, 2, 4$, answers `YES` despite having a non-zero total).
- **An even $N$ with total $0$** is the other `YES` (the first row, $3,2,2,3$).
- **$X \geq 1$ is required** by the statement, but applying the same $X$ twice is a no-op, so the restriction never limits what is reachable.
- **Sum of $N \leq 2 \cdot 10^5$**: one XOR fold per case, with no array stored.

## Dry run

| $N$ | array | total XOR | parity of $N$ | output |
|---:|---|---:|---|---|
| 4 | $3,2,2,3$ | $0$ | even, total $0$ | `YES` |
| 6 | $0,1,2,3,4,5$ | $1$ | even, total $\neq 0$ | `NO` |
| 3 | $1,2,4$ | $7$ | **odd** | `YES` |

For the first row: XOR positions $2$ and $3$ with $1$ to get $3,3,3,3$.

> CodeChef tags: `Mathematics`, `Bit Manipulation`, `Algorithms`

---

Same problem in rating order (#351 of 486): [../../by-rating/351-XOR2.md](../../by-rating/351-XOR2.md)
