# 347. XOR-ORED

> CodeChef problem code [`XORORED`](https://www.codechef.com/problems/XORORED) &middot; difficulty **1621** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Bit Manipulation |
| **Technique** | Choosing X bit by bit against an OR |
| **Time** | $O(N)$ per test case |
| **Space** | $O(1)$ |
| **Roadmap course** | Jump from 2* to 3* (Level 3) |

## Question

Given an array $A$ of $N$ non-negative integers, you can choose any non-negative integer $X$ and replace every element $A_i$ with $(A_i\oplus X)$ Here, $\oplus$ denotes the [bitwise XOR operation](https://en.wikipedia.org/wiki/Bitwise_operation#XOR).

Using the above operation exactly once, your goal is to **minimize** the bitwise OR of the new array. In other words, find $X$ such that $(A_1\oplus X)\lor \cdots \lor (A_N \oplus X)$ is minimized, where $\lor$ denotes the [bitwise OR operation](https://en.wikipedia.org/wiki/Bitwise_operation#OR).

Find the value of $X$ and the minimum possible bitwise OR of the new array.

**Input**

- The first line contains a single integer $T$ - the number of test cases. Then $T$ test cases follow.
- The first line of each test case contains a single integer $N$ - the length of the array.
- The next line contains $N$ integers $A_1,\ldots, A_N$.

**Output**

For each test case, print two integers: $X$ and the minimum possible bitwise OR of the new array.

If there are multiple values of $X$ that achieve the minimum bitwise OR, print any of them.

## Constraints

- $1 \leq T \leq 5000$
- $ 1 \leq N \leq 100 $
- $ 0 \leq  A_i \leq 10^9 $

**Subtasks**

- 30 points : $1 \leq R \leq 10000$
- 70 points : $1 \leq R \leq 10^9$

## Sample

**Sample input**

```
1
2
4 6
```

**Sample output**

```
6 2
```

<details><summary>Explanation</summary>

Here, if we take $X=6$, then our expression would become $(4\oplus 6) \lor (6\oplus 6) = 2\lor 0 = 2$, which is the minimum possible.

</details>

## Approach

XOR acts on each bit separately and OR is also computed per bit, so bit $b$ of the answer depends only on bit $b$ of the array and of $X$. Three cases:

- **Every $A_i$ has the bit set.** Choose $X$'s bit $1$: all of them flip to $0$, so the OR bit is $0$.
- **No $A_i$ has it.** Choose $X$'s bit $0$: they stay $0$, so the OR bit is $0$.
- **Mixed.** Either choice leaves at least one element with the bit set, so the OR bit is $1$ no matter what.

So the uniform bits are all clearable and the mixed bits are all unavoidable. "All set" is exactly a bit of the AND, and "at least one set" exactly a bit of the OR, so with

$$\mathcal{A} = A_1 \,\&\, \cdots \,\&\, A_N, \qquad \mathcal{O} = A_1 \mid \cdots \mid A_N$$

taking $X = \mathcal{A}$ achieves the minimum, which is

$$\mathcal{O} \oplus \mathcal{A} \;=\; \mathcal{O} \;\&\; \neg\mathcal{A}$$

(the XOR equals the AND-NOT because $\mathcal{A} \subseteq \mathcal{O}$ as bit sets). Both reduce in a single pass, so no bit loop is needed.

$X$ is **not unique**: its bits on the mixed positions are free, since they change nothing. The sample $[4, 6]$ has $\mathcal{A} = 4$ and $\mathcal{O} = 6$, so the minimum is $2$; our $X = 4$ gives $\{0, 2\}$ and the sample's $X = 6$ gives $\{2, 0\}$ — different arrays, same OR, both accepted by the judge.

Note $X$ may freely exceed the array values; here it is bounded by $\mathcal{A} \leq \max A_i$ anyway.

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
        both, either = -1, 0
        for tok in data[pos + 1:pos + 1 + n]:
            v = int(tok)
            both &= v
            either |= v
        pos += 1 + n
        # Bits set in every element can be cleared; mixed bits cannot.
        out.append(f"{both} {either ^ both}")
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(N)$ per test case
- **Space:** $O(1)$
