# 098. Equalizing Numbers

> [`EQLZING`](https://www.codechef.com/problems/EQLZING) &middot; difficulty **823** &middot; time limit **1s** &middot; 500 to 1000 difficulty rating (Level 1)

> _Edge cases and dry run for this problem are still to be written._

## Topic used

| | |
|---|---|
| **Topic** | Number Theory |
| **Technique** | Finding the invariant |
| **CodeChef tags** | `Mathematics`, `Algorithms`, `Constructive`, `Basic Math`, `ad-hoc` |
| **Complexity class** | Constant time $O(1)$ |
| **Time** | $O(1)$ per test case |
| **Space** | $O(1)$ |

## Question

Chef has two integers $A$ and $B$. In one operation he can choose any integer $d,$ and make one of the following two moves :
- Add $d$ to $A$ and subtract $d$ from $B$.
- Add $d$ to $B$ and subtract $d$ from $A$.

Chef is allowed to make as many operations as he wants. Can he make $A$ and $B$ **equal**?

**Input**

- First line will contain $T$, number of test cases. Then the test cases follow.
- Each test case contains of a single line of input, two integers $A, B$.

**Output**

For each test case, if Chef can make the two numbers equal print `YES` else print `NO`.

You may print each character of the string in uppercase or lowercase (for example, the strings `yEs`, `Yes`, `YeS`, and `YES` will all be treated as identical).

## Constraints

- $1 \leq T \leq 1000$
- $1 \leq A,B \leq 1000$

## Sample

**Sample input**

```
2
3 3
1 2
```

**Sample output**

```
Yes
No
```

<details><summary>Explanation</summary>

**Test case $1$:** Since $A$ and $B$ are already equal, Chef does not need any operations.

**Test case $2$:** It can be shown that $A$ and $B$ can never be made equal using any number of given operations.

</details>

## Approach

Both operations move the same $d$ from one number to the other. Whatever one gains, the other loses, so the **sum stays fixed**:

$$A + B = \text{constant}$$

That invariant settles the problem. If Chef can reach $A = B$, then each must equal half the total, so $A + B$ has to be even. Conversely, when $A + B$ is even the target is reachable in a single move: take $d = \frac{B - A}{2}$ and add it to $A$ while subtracting from $B$, landing both on the average. So the condition is exactly

$$A + B \equiv 0 \pmod 2$$

Looking for a quantity the operations cannot change is the standard opening move for "can this state be reached" problems, and it is usually faster than trying to construct a sequence of moves. Here the invariant immediately gives both directions of the proof — impossibility when the sum is odd, and an explicit one-move construction when it is even.

Note that $d$ is unrestricted: it may be negative, zero, or larger than either number, and the problem never requires the values to stay positive. That generality is what makes a single move always sufficient; a constraint keeping both numbers non-negative would make this a harder question.

Since $A$ and $B$ have the same parity exactly when their sum is even, `(a + b) % 2 == 0` and `a % 2 == b % 2` are interchangeable here. Sample case 1 has equal numbers already ($d = 0$ works); sample case 2 has an odd sum and is impossible.

## Solution

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        a, b = int(data[1 + 2 * i]), int(data[2 + 2 * i])
        # Every move preserves a + b, so the halves must be whole numbers.
        out.append("Yes" if (a + b) % 2 == 0 else "No")
    sys.stdout.write("\n".join(out) + "\n")


main()
```

---

Same problem grouped by topic: [../docs/number-theory/EQLZING.md](../docs/number-theory/EQLZING.md)
