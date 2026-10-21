# 1635 &middot; XOR with smallest element

> CodeChef problem code [`SMALLXOR`](https://www.codechef.com/problems/SMALLXOR) &middot; time limit **10s** &middot; 1600 to 1800 difficulty problems (Level 3)

## Topics used

| | |
|---|---|
| **Topic** | Heaps |
| **Technique** | Detecting the two-cycle that ends the process |
| **CodeChef tags** | `Special`, `Algorithms`, `Observation`, `Simulation` |
| **CodeChef category** | easy |
| **Time** | $O(N \log N)$ per test case |
| **Space** | $O(N)$ |

Same write-up grouped by topic: [../docs/heaps/SMALLXOR.md](../docs/heaps/SMALLXOR.md)

## Question

Chef has an array $A$ of length $N$ and an integer $X$.

In one operation, Chef does the following:
- Find the smallest element in the current array. Let this be $S$.
- Next, pick any **one** index $i$ such that $A_i = S$
- Finally, replace $A_i$ with $A_i \oplus X$

Here $\oplus$ denotes the [bitwise XOR](https://en.wikipedia.org/wiki/Bitwise_operation#XOR) operation.

For example, if $A = [1, 1, 2]$ and $X = 4$, then in one move Chef can turn the array into either $[5, 1, 2]$ or $[1, 5, 2]$.

Chef performs this operation **exactly** $Y$ times. Let $B$ be final array obtained.

Output the array $B$ in sorted order. Note that under this restriction, the output is unique.

**Input**

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of two lines of input.
    - The first line of each test case contains three space-separated integers $N$, $X$, and $Y$.
    - The second line contains $N$ space-separated integers denoting the array $A$.

**Output**

For each test case, output array $B$ in sorted order.

## Constraints

- $1 \leq T \leq 10^4$
- $1 \leq N \leq 10^5$
- $1 \leq Y \leq 10^9$
- $1 \leq A_i , X \leq 2^{30}$
- The sum of $N$ over all test cases won't exceed $10^5$.

## Sample

**Sample input**

```
3
1 6 99
9
3 7 44
1 2 3
5 20 6
5 10 15 20 25
```

**Sample output**

```
15 
3 5 6 
5 20 25 27 30
```

<details><summary>Explanation</summary>

**Test case $1$:** The array is initially $[9]$. Since there is only one element, it will be modified in each step. So,
- After the first operation, the array is $[15]$ (since $9 \oplus 6 = 15$)
- After the second operation, the array is $[9]$ (since $15 \oplus 6 = 9$)
- Continuing the above, it can be verified that after $99$ steps, the array is $[15]$.

**Test case $3$:** The sequence of steps is as follows:
- Initially, the array is $[5, 10, 15, 20, 25]$
- After operation $1$, it is $[17, 10, 15, 20, 25]$
- After operation $2$, it is $[17, 30, 15, 20, 25]$
- After operation $3$, it is $[17, 30, 27, 20, 25]$
- After operation $4$, it is $[5, 30, 27, 20, 25]$
- After operation $5$, it is $[17, 30, 27, 20, 25]$
- After operation $6$, it is $[5, 30, 27, 20, 25]$

Remember to print the output in sorted order.

</details>

## Approach

$Y$ reaches $10^9$, so the process cannot be simulated step by step — but it stabilises almost immediately.

Each value only ever alternates between $a$ and $a \oplus X$. These differ at $h$, the highest set bit of $X$, so the one with bit $h$ clear is the smaller; call it the element's **low** form and the other its **high** form.

Now watch the operation. If the global minimum is in low form, flipping it raises it. But if the global minimum is already in **high** form, flipping it gives its low form, which is smaller than the high value that was the minimum — so it is still the minimum, and the next operation flips it straight back. The process has entered a **two-cycle**, and every remaining operation just toggles that one element.

So the simulation only has to run until a popped element turns out to be in high form, which happens within $N+1$ steps because each earlier step promotes a distinct element from low to high and never revisits it. With $r$ operations left at that moment, the element's final value is

$$v \oplus \begin{cases} X & r \text{ odd} \\ 0 & r \text{ even}\end{cases}$$

A min-heap supplies the minimum at each step.

Sample 2 shows both phases: $[1,2,3]$ with $X = 7$ promotes $1 \to 6$, $2 \to 5$, $3 \to 4$, and then $4$ is in high form ($4 \oplus 7 = 3$), so the remaining $41$ operations — an odd count — leave it at $3$, giving `3 5 6`.

Sample 3 shows that elements can start in high form and be ignored entirely: $20$ and $25$ are both above their partners $0$ and $13$, so they are never touched, and the cycle forms on $5 \leftrightarrow 17$ after three promotions.

## Solution (Python)

```python
import heapq
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n, x, y = int(data[pos]), int(data[pos + 1]), int(data[pos + 2])
        heap = [int(v) for v in data[pos + 3:pos + 3 + n]]
        pos += 3 + n
        heapq.heapify(heap)
        for step in range(y):
            v = heap[0]
            flipped = v ^ x
            if flipped > v:
                heapq.heapreplace(heap, flipped)      # low form, so promote
            else:
                # High form: it stays the minimum and just toggles from here.
                left = y - step
                heapq.heapreplace(heap, flipped if left % 2 else v)
                break
        out.append(" ".join(map(str, sorted(heap))))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(N \log N)$ per test case
- **Space:** $O(N)$
