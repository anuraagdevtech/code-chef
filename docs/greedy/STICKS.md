# 203. Sticks

> CodeChef problem code [`STICKS`](https://www.codechef.com/problems/STICKS) &middot; difficulty **1261** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Greedy |
| **Technique** | Largest two pairs by frequency |
| **Time** | $O(N \log N)$ per test case |
| **Space** | $O(N)$ |
| **Roadmap course** | Level up from 1* to 2* (Level 2) |

## Question

Chef and his little brother are playing with sticks. They have total **N** sticks. Length of **i**-th stick is **A_i**.
Chef asks his brother to choose any four sticks and to make a rectangle with those sticks its sides. Chef warns his brother to not to break any of the sticks, he has to use sticks as a whole. Also, he wants that the rectangle formed should have the maximum possible area among all the rectangles that Chef's brother can make.

Chef's little brother takes this challenge up and overcomes it. Can you also do so? That is, you have to tell whether it is even possible to create a rectangle? If yes, then you have to tell the maximum possible area of rectangle.

**Input**

The first line contains a single integer **T** denoting the number of test-cases. **T** test cases follow.

The first line of each test case contains a single integer **N** denoting the number of sticks.

The second line of each test case contains **N** space-separated integers **A_1**, **A_2**, ..., **A_N** denoting the lengths of sticks.

**Output**

For each test case, output a single line containing an integer representing the maximum possible area for rectangle or -1 if it's impossible to form any rectangle using the available sticks.

**Constraints**

- **1** ≤ **T** ≤ **100**

- **1** ≤ **N** ≤ **10^3**

- **1** ≤ sum of **N**'s over all test-cases in a single test file ≤ **10^3**

- **1** ≤ **A_i** ≤ **10^3**

## Constraints

- 1 ≤ T ≤ 100
- 1 ≤ N ≤ 10^3
- 1 ≤ sum of N's over all test-cases in a single test file ≤ 10^3
- 1 ≤ A_i ≤ 10^3

## Sample

**Sample input**

```
2
5
1 2 3 1 2
4
1 2 2 3
```

**Sample output**

```
2
-1
```

<details><summary>Explanation</summary>

**Example case 1.** Chef's brother can choose sticks of lengths 1, 2, 1, 2. He can create a rectangle with area 1 * 2 = 2.

**Example case 2.** It's impossible to choose 4 sticks so that they form a rectangle.

</details>

## Approach

A rectangle needs two sticks of one length and two of another (a square being the case where both lengths coincide). So the question is which lengths are available **in pairs**, and the answer takes the two largest of those.

Count occurrences of each length. A length appearing $c$ times contributes $\lfloor c/2 \rfloor$ pairs — importantly, a length appearing four or more times supplies **both** sides on its own, forming a square. Collect all available pairs as a list of lengths, sort descending, and if at least two exist the answer is the product of the top two; otherwise $-1$.

The count-four case is the one most easily missed. With sticks $[5,5,5,5]$ the answer is $25$, not $-1$: one length yields two pairs. Treating each distinct length as contributing at most one pair would wrongly reject it.

Maximising the **area** rather than the perimeter is why the two largest pairs are taken: for a fixed choice of two available lengths $a \geq b$, the area is $ab$, and swapping in any larger available length only increases it. So the greedy is immediate — no comparison of candidate rectangles is needed.

Sample case 1, $[1,2,3,1,2]$, has pairs at lengths $1$ and $2$, giving $2 \times 1 = 2$. Sample case 2, $[1,2,2,3]$, has only a single pair and answers $-1$.

With $A_i \leq 10^3$ a frequency array would also work and would be marginally faster than a dictionary, but the sum of $N$ is only $10^3$ so either is comfortable.

## Solution (Python)

```python
import sys
from collections import Counter


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n = int(data[pos])
        counts = Counter(int(v) for v in data[pos + 1:pos + 1 + n])
        pos += 1 + n
        pairs = []
        for length, c in counts.items():
            # Four or more of a length supplies both sides, forming a square.
            pairs.extend([length] * (c // 2))
        pairs.sort(reverse=True)
        out.append(str(pairs[0] * pairs[1]) if len(pairs) >= 2 else "-1")
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(N \log N)$ per test case
- **Space:** $O(N)$

## Edge cases

- **Four sticks of one length form a square** without a special case: `c // 2` emits that length twice, and the two largest pair lengths then happen to be equal.
- **Exactly one pair available** (the second row, where only the $2$s pair up): $-1$, since a rectangle needs two pairs.
- **No pair at all** (every length appearing once): $-1$.
- **Odd leftovers are discarded** — a count of $3$ yields one pair and one unused stick, and a count of $5$ yields two pairs.
- **The two largest pairs give the largest area**, because the area is a product of two independently chosen positive lengths, so maximising each factor maximises the product.
- Sorting the pair lengths descending and taking the first two also handles the equal-pair case naturally, since both copies are adjacent.

## Dry run

First sample: $1, 2, 3, 1, 2$.

| length | count | pairs contributed |
|---:|---:|---|
| 1 | 2 | one pair of $1$ |
| 2 | 2 | one pair of $2$ |
| 3 | 1 | none |

Pair lengths sorted descending: $2, 1$ → area $2 \times 1 = $ `2`.

The second sample has counts $\{1{:}1, 2{:}2, 3{:}1\}$, so only one pair exists and the output is `-1`.

> CodeChef tags: `Algorithms`

---

Same problem in rating order (#191 of 486): [../../by-rating/191-STICKS.md](../../by-rating/191-STICKS.md)
