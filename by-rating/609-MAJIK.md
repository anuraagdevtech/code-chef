[&larr; 608. Non Zero Subarray Xor](608-SUBARRAYXOR.md) &middot; [Index](README.md) &middot; [610. Odd Binomial Coefficients &rarr;](610-ODDBIN.md)

# 609. Wishcraft

> [`MAJIK`](https://www.codechef.com/problems/MAJIK) &middot; difficulty **2105** &middot; time limit **1s** &middot; 2000 to 2500 difficulty problems (Level 5)

## Topic used

| | |
|---|---|
| **Topic** | Greedy |
| **Technique** | Keep the two extremes and absorb the largest absolute values into them |
| **CodeChef tags** | `greedy`, `sorting` |
| **Complexity class** | Linearithmic $O(n \log n)$ |
| **Time** | $O(N \log N)$ per test case |
| **Space** | $O(N)$ |

## Question

*Magic is really very simple, all you’ve got to do is want something and then let yourself have it.*

Chadda and his Wizard friend PSC were exploring the enchanted forest on Halloween, when Chadda stumbled upon an array $A$ of $N$ magical numbers which took him into a different world.

Chadda remembered that PSC gave him two integers $P$ and $Q$ for such a situation.
Using these integers, Chadda can modify the array $A$ as follows:
- **At most** $P$ times, perform the following operation:
    - Pick two elements $x$ and $y$ from $A$, delete them both from $A$, and insert $(x+y)$ into $A$.
This operation can be performed only if $A$ has at least two elements.
- **At most** $Q$ times, perform the following operation:
    - Pick two elements $x$ and $y$ from $A$, delete them both from $A$, and insert $(x-y)$ into $A$.
This operation can also be performed only if $A$ has at least two elements.

Note that each operation reduces the size of $A$ by one.
The two types of operations (addition and subtraction) can be performed in any order, as long as at most $P$ addition operations and $Q$ subtraction operations are made.

Let $B$ denote the final array obtained after performing some (possibly, zero) operations.
To return to his original world, Chadda has to find the **maximum possible** value of
$$
\max(B) - \min(B)
$$

across all possible final arrays $B$.
Can you help Chadda find this value?

**Input**

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of three lines of input.
  - The first line of each test case contains a single integer $N$ — the size of the array.
  - The second line contains two space-separated integers $P$ and $Q$ — the maximum number of addition and subtraction operations, respectively.
  - The third line contains $N$ space-separated integers $A_1, A_2, \ldots, A_N$: the elements of array $A$.

**Output**

For each test case, output on a new line the answer: the maximum possible value of $\max(B) - \min(B)$ across all possible final arrays $B$.

## Constraints

- $1 \leq T \leq 10^5$
- $1 \leq N \leq 10^5$
- $0 \leq P, Q \leq N - 1$
- $-10^9 \leq A_i \leq 10^9$
- The sum of $N$ over all test cases won't exceed $3 \cdot 10^5 $.

**Subtasks**

- **Subtask 1 (10 points):** $1 \leq M \leq 10$
- **Subtask 2 (20 points):** The sum of $N$ across all test cases won't exceed $20$.
- **Subtask 3 (70 points):** No further constraints.

## Sample

**Sample input**

```
3
2
0 0
5 1
6
1 2
8 -1 -4 2 6 -3
7
6 6
-2 -4 2 -2 -3 -1 -1
```

**Sample output**

```
4
23
15
```

<details><summary>Explanation</summary>

**Test case $1$:** $P = Q = 0$, so no operations can be performed at all.
The answer is just $\max([5, 1]) - \min([5, 1]) = 5-1 = 4$.

**Test case $2$:** The array is $A = [8, -1, -4, 2, 6, -3]$. The following sequence of operations can be performed:
- Choose $2$ and $-3$, remove them, and insert $2 - (-3) = 5$ into the array.
The elements are now $[8, -1, -4, 6, 5]$.
- Choose $8$ and $5$, remove them, and add $8+5 = 13$ to the array.
The elements are now $[13, -1, -4, 6]$.
- Choose $-4$ and $6$, remove them and add $(-4) - (6)$ to the array.
The elements are now $[13, -1, -10]$.

The difference between maximum and minimum for this array is $13 - (-10) = 23$.
With one addition and two subtraction operations available, it can be proved that this is the maximum attainable value.

**Test Case $3$:**: It can be proven that $15$ is the maximum attainable value.

</details>

## Approach

Each operation removes two elements and inserts one combination of them, so $P + Q$ operations can fold at most $P + Q$ other elements into the two elements that will end up as the maximum and the minimum.

Folding an element $x$ into an extreme can widen the gap by exactly $|x|$ and never by more: with the addition, a positive $x$ is added to the maximum and a negative $x$ to the minimum; with the other operation the roles are mirrored. So whichever kind of operation is still available, any leftover element can be used, and its contribution is its absolute value.

Start from the gap between the original maximum and minimum - those two are the best bases - and add the $P + Q$ largest absolute values among the remaining $N - 2$ elements.

## Solution

```python
import sys


def main() -> None:
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    out = []
    for _ in range(next(tokens)):
        n = next(tokens)
        merges = next(tokens)
        splits = next(tokens)
        values = sorted((next(tokens) for _ in range(n)))
        magnitudes = sorted((abs(x) for x in values[1:-1]), reverse=True)
        out.append(str(values[-1] - values[0] + sum(magnitudes[:merges + splits])))
    print('\n'.join(out))


if __name__ == "__main__":
    main()
```

## Edge cases

- $P = Q = 0$: the answer is simply max minus min.
- $N = 1$: there is nothing to combine and the answer is 0.
- At most $N - 2$ elements can be absorbed, so a surplus of operations is harmless.
- The gap can reach about $N \cdot 10^9$.

## Dry run

`A = [8, -1, -4, 2, 6, -3]`, `P = 1, Q = 2`.

Sorted: `-4 -3 -1 2 6 8`. Base gap $8 - (-4) = 12$. Absolute values of the middle elements, largest first: `6 3 2 1`; three operations take $6 + 3 + 2 = 11$.

Answer $12 + 11 = 23$.

---

Same problem grouped by topic: [../docs/greedy/MAJIK.md](../docs/greedy/MAJIK.md)
