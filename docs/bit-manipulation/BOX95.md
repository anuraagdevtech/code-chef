# 426. Boxes

> CodeChef problem code [`BOX95`](https://www.codechef.com/problems/BOX95) &middot; difficulty **1688** &middot; time limit **2.5s**

| | |
|---|---|
| **Topic** | Bit Manipulation |
| **Technique** | The top bit caps a box at two elements |
| **Time** | $O(N)$ per test case |
| **Space** | $O(1)$ |
| **Roadmap course** | 1600 to 1800 difficulty problems (Level 3) |

## Question

You are given an array $A$ of length $N$ such that:
- $2\times (A_1 \oplus A_2 \oplus \ldots \oplus A_N) \geq (A_1 | A_2 | \ldots | A_N)$, where $\oplus$ and $|$ denote the bitwise [xor](https://en.wikipedia.org/wiki/Bitwise_operation#XOR) and [or](https://en.wikipedia.org/wiki/Bitwise_operation#OR) operations respectively.

Your task is to perform the following operation until the array is empty:
 - Choose any element $A_i$ from the array.
 - Remove $A_i$ from the array.
 - Perform **one** of the following:
   - Use a new box and add $A_i$ to the box.
   - Select an existing box such that the XOR of all the elements in the box (before placing $A_i$) is **greater than or equal to** $A_i$ and add $A_i$ to the box.

Determine the **minimum** number of boxes required to empty the array $A$.

**Input**

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of two lines of input.
    - The first line of each test case contains one integer $N$ — the number of elements in $A$.
    - The second line contains $N$ integers $A_1,A_2,\ldots,A_N$, the elements of the array $A$.

**Output**

For each test case, output on a new line, the **minimum** number of boxes required to empty the array $A$.

## Constraints

- $1 \leq T \leq 10^5$
- $1 \leq N \leq 2\cdot 10^5$
- $1 \leq A_i \leq 10^{18}$
- The sum of $N$ over all test cases won't exceed $2\cdot 10^5$.

## Sample

**Sample input**

```
3
1
6
4
1 2 3 12
3
6 5 4
```

**Sample output**

```
1
1
2
```

<details><summary>Explanation</summary>

**Test case $1$:**
  - Choose $6$ from the array and delete it.
    - Add $6$ to a new box.

$A$ is empty now and we used one box.

**Test case $2$:**
  - Choose $12$ from the array and delete it.
    - Add $12$ to a new box. The XOR of the box becomes $12$.
  - Choose $3$ from the array and delete it.
    - Since the XOR of the box $12 \geq 3$, we can add $3$ to the box. The XOR of the box becomes $12\oplus3=15$.
  - Choose $2$ from the array and delete it.
    - Since the XOR of the box $15 \geq 2$, we can add $2$ to the box. The XOR of the box becomes $15\oplus2=13$.
  - Choose $1$ from the array and delete it.
    - Since the XOR of the box $13 \geq 1$, we can add $1$ to the box. The XOR of the box becomes $13\oplus1=12$.

$A$ is empty now and we used one box.

**Test case $3$:**
  - Choose $5$ from the array and delete it.
    - Add $5$ to a new box. The XOR of the box becomes $5$.
  - Choose $4$ from the array and delete it.
    - Since the XOR of the box $5 \geq 4$, we can add $4$ to the box. The XOR of the box becomes $5\oplus4=1$.
  - Choose $6$ from the array and delete it.
    - Add $6$ to a new box. The XOR of the second box is $6$.

$A$ is now empty and we used two boxes.

</details>

## Approach

Let $h$ be the highest set bit of the OR, and $k$ the number of elements having it. Everything turns on those $k$ elements.

**At most two per box.** To add an element carrying bit $h$, the box's running XOR must be at least that element, hence must itself carry bit $h$ — otherwise the XOR is below $2^h$ while the element is at or above it. The XOR's bit $h$ flips with each such insertion, so the first two are fine (the box starts at the first, and the XOR still carries $h$ for the second) but a third would face an XOR with bit $h$ cleared. So

$$\text{boxes} \geq \left\lceil \frac{k}{2} \right\rceil$$

**$k$ is odd.** This is what the guarantee $2Z \geq O$ buys, where $Z$ is the XOR and $O$ the OR. Bit $h$ of $Z$ is $k \bmod 2$. If $k$ were even, then $Z$'s bits lie in $O$ without bit $h$, so $Z \leq O - 2^h$ and $2Z \geq O$ would force $O \geq 2^{h+1}$ — contradicting $h$ being $O$'s top bit. So $k$ is odd and the bound is $(k+1)/2$.

**It is attained.** Seed one box with a top-bit element; its XOR stays at or above $2^h$ while only sub-$2^h$ elements are added, so that box absorbs *every* element without bit $h$. The remaining $k-1$ top-bit elements pair off, larger first, into $(k-1)/2$ boxes. Total $(k+1)/2$.

The samples bear this out: $[6]$ and $[1,2,3,12]$ each have a single top-bit element ($6$, and $12$ at bit $3$), so one box suffices — the latter swallowing $3, 2, 1$ in turn. But $[6,5,4]$ has all three elements carrying bit $2$, so $k = 3$ and two boxes are needed: $\{6,5\}$ and $\{4\}$.

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
        vals = [int(x) for x in data[pos + 1:pos + 1 + n]]
        pos += 1 + n
        top = 1 << (max(vals).bit_length() - 1)
        # Each box holds at most two elements carrying the top bit, and the
        # guarantee 2*XOR >= OR forces their count to be odd.
        k = sum(1 for v in vals if v & top)
        out.append(str((k + 1) // 2))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(N)$ per test case
- **Space:** $O(1)$

> CodeChef tags: `Mathematics`, `Bit Manipulation`, `Algorithms`
