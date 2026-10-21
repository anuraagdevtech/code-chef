# 008. Chef And Operators

> [`CHOPRT`](https://www.codechef.com/problems/CHOPRT) &middot; difficulty **520** &middot; time limit **1s** &middot; 500 to 1000 difficulty rating (Level 1)

## Topic used

| | |
|---|---|
| **Topic** | Conditionals & Case Work |
| **Technique** | Three-way comparison |
| **CodeChef tags** | `Basic Programming Concepts`, `Conditional Statements` |
| **Complexity class** | Constant time $O(1)$ |
| **Time** | $O(1)$ per test case |
| **Space** | $O(1)$ |

## Question

Chef has just started Programming, he is in first year of Engineering. Chef is reading about Relational Operators.

Relational Operators are operators which check relationship between two values. Given two numerical values **A** and **B** you need to help chef in finding the relationship between them that is,

First one is greater than second or,
First one is less than second or,
First and second one are equal.
 

**Input**

First line contains an integer **T**, which denotes the number of testcases. Each of the **T** lines contain two integers **A** and **B**.

**Output**

For each line of input produce one line of output. This line contains any one of the relational operators

'<' , '>' , '='.

**Constraints**

1 ≤ **T** ≤ 10000
1 ≤ **A**, **B** ≤ 1000000001

## Constraints

- $1 \leq T \leq 10^4$
- $1 \leq A, B \leq 10^9 + 1$

## Sample

**Sample input**

```
3
10 20
20 10
10 10
```

**Sample output**

```
<
>
=
```

<details><summary>Explanation</summary>

In this example 1 as 10 is lesser than 20

</details>

## Approach

Print the relational operator describing how $A$ stands to $B$: `<` if $A$ is smaller, `>` if larger, `=` if equal. A three-branch comparison, with each outcome mapped to its symbol.

The three cases are mutually exclusive and exhaustive, so an `if / elif / else` covers the space exactly and the branch order carries no meaning. What *is* required is that the equality case get its own branch — collapsing it into one of the inequalities silently reports a strict relation for equal values.

Two practical notes for this particular problem. $A$ and $B$ reach $1000000001$, which is just past $2^{30}$ and over the $2{,}147{,}483{,}647$ ceiling of a signed 32-bit `int` only when summed — comparison itself is safe, but the bound is a hint that a C solution should use a wider type if it does any arithmetic. Python has no such concern.

With $T$ up to $10^4$, reading the whole stream at once and joining the output into a single write is worth doing; per-line `input()` and `print()` calls dominate the runtime in Python at this volume, even though the comparison itself is free.

The symbols must be printed bare, with no surrounding quotes — the problem statement quotes them only for clarity.

## Solution

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        a, b = int(data[1 + 2 * i]), int(data[2 + 2 * i])
        out.append("<" if a < b else ">" if a > b else "=")
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Edge cases

- **$A = B$**: must print `=`, so the chain needs all three branches and not just a two-way test. Sample case 3 covers it.
- **Both at the bound** $A = B = 10^9 + 1$: equal, so `=`. Note the limit is $10^9 + 1$, one past the usual $10^9$ — still inside 32-bit range, but it is a deliberate nudge past the round number.
- **Both minimal** ($A = B = 1$): `=`.
- Only the *sign* of $A - B$ matters, so no subtraction overflow is possible even in a fixed-width language; comparing directly avoids the question entirely.

## Dry run

| $A$ | $B$ | relation | output |
|---:|---:|---|---|
| 10 | 20 | $A < B$ | `<` |
| 20 | 10 | $A > B$ | `>` |
| 10 | 10 | equal | `=` |

The three sample rows exercise all three branches in turn.

---

Same problem grouped by topic: [../docs/conditionals-case-work/CHOPRT.md](../docs/conditionals-case-work/CHOPRT.md)
