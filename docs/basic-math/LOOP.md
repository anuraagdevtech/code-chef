# 102. Circular Track

> CodeChef problem code [`LOOP`](https://www.codechef.com/problems/LOOP) &middot; difficulty **838** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Basic Math |
| **Technique** | Distance on a circle |
| **Time** | $O(1)$ per test case |
| **Space** | $O(1)$ |
| **Roadmap course** | 500 to 1000 difficulty rating (Level 1) |

## Question

There is a circular track of length $M$ consisting of $M$ checkpoints and $M$ **bidirectional** roads such that each road has a length of $1$ unit.

![](https://s3.amazonaws.com/codechef_shared/download/Images/START38/START38.png)

Chef is currently at checkpoint $A$ and wants to reach checkpoint $B$. Find the **minimum** length of the road he needs to travel.

**Input**

- First line will contain $T$, the number of test cases. Then the test cases follow.
- Each test case contains a single line of input, three integers $A, B,$ and $M$ - the initial checkpoint, the final checkpoint, and the total number of checkpoints respectively.

**Output**

For each test case, output the **minimum** length Chef needs to travel.

## Constraints

- $1 \leq T \leq 1000$
- $2 \leq M \leq 10^9$
- $1 \leq A, B \leq M$
- $A \neq B$

## Sample

**Sample input**

```
4
1 3 100
1 98 100
40 30 50
2 1 2
```

**Sample output**

```
2
3
10
1
```

<details><summary>Explanation</summary>

**Test Case $1$:** Chef can go from $1$ to $3$ as: $1 \rightarrow 2$ and then $2 \rightarrow 3$. Thus, total length travelled is $2$ units.

**Test Case $2$:** Chef can go from $1$ to $98$ as: $98 \leftarrow 99 \leftarrow 100 \leftarrow 1$. Thus, minimum distance travelled is $3$ units.

**Test Case $3$:** Chef can go from $40$ to $30$ as: $30 \leftarrow 31 \leftarrow 32 \leftarrow \dots \leftarrow 39 \leftarrow 40$. Thus, minimum distance travelled is $10$ units.

**Test Case $4$:** Chef can go from $2$ to $1$ as: $1 \leftarrow 2$. Thus, minimum distance travelled is $1$ unit.

</details>

## Approach

The track is a cycle of $M$ checkpoints joined by unit-length roads, and the roads are **bidirectional** — so Chef may walk either way around. The two routes between $A$ and $B$ partition the whole loop, so their lengths sum to $M$:

$$d = |A - B|, \qquad \text{answer} = \min(d,\; M - d)$$

Bidirectionality is the hinge. On a one-way track the answer would be $(B - A) \bmod M$, direction-dependent and often much larger. Sample case 2 shows the difference starkly: from checkpoint $1$ to $98$ on a $100$-track, the forward walk is $97$ but going backwards is only $3$.

The `min` also means the answer never exceeds $\lfloor M/2 \rfloor$ — the furthest two points on a cycle are diametrically opposite.

Sample case 4 is the tightest case: $M = 2$, so the two checkpoints are adjacent both ways and $d = M - d = 1$. The `min` is indifferent, which is correct — both routes are one road long.

The absolute value handles $B < A$ without a branch, as in sample case 3 where the walk runs from $40$ down to $30$. And since $A \neq B$ is guaranteed, the answer is always at least $1$.

With $M$ up to $10^9$ the arithmetic is trivial for Python, and no modular reduction is needed because $A$ and $B$ already lie in $[1, M]$.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        a, b, m = map(int, data[1 + 3 * i:4 + 3 * i])
        d = abs(a - b)
        # Roads are bidirectional, so the two arcs sum to m.
        out.append(str(min(d, m - d)))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(1)$ per test case
- **Space:** $O(1)$

## Edge cases

- **The long way round is shorter** ($A = 1$, $B = 98$, $M = 100$): going backwards costs $3$ against $97$ forwards. Returning $|A - B|$ alone fails here, and the sample's second row is exactly this.
- **Exactly antipodal** ($A = 2$, $B = 1$, $M = 2$): both arcs measure $1$, so the tie is harmless.
- **$A \neq B$ is guaranteed**, so the distance is never zero.
- **Largest track** ($M = 10^9$): no overflow, and the two arcs always sum to $M$.
- Roads are bidirectional, which is the fact that makes the answer a minimum of two arcs rather than one directed distance.

## Dry run

| $A$ | $B$ | $M$ | one way $|A-B|$ | the other $M - d$ | output |
|---:|---:|---:|---:|---:|---|
| 1 | 3 | 100 | 2 | 98 | `2` |
| 1 | 98 | 100 | 97 | 3 | `3` |
| 40 | 30 | 50 | 10 | 40 | `10` |
| 2 | 1 | 2 | 1 | 1 | `1` |

Row 2 takes the back route; row 4 is the tie.

> CodeChef tags: `Mathematics`, `Algorithms`

---

Same problem in rating order (#104 of 486): [../../by-rating/104-LOOP.md](../../by-rating/104-LOOP.md)
