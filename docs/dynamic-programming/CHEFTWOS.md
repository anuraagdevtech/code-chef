[&larr; 590. Little Elephant and Mouses](LEMOUSE.md) &middot; [Index](../../README.md) &middot; [600. A-E Hash Function &rarr;](AEHASH.md)

# 592. Chef and Two String

> CodeChef problem code [`CHEFTWOS`](https://www.codechef.com/problems/CHEFTWOS) &middot; difficulty **2233** &middot; time limit **1.5s**

| | |
|---|---|
| **Topic** | Dynamic Programming |
| **Technique** | Three-state automaton for good strings, run on both strings at once |
| **Time** | $O(N)$ per test case |
| **Space** | $O(1)$ - at most nine states |
| **Roadmap course** | Rise from 3* to 4* (Level 4) |

## Question

Chef's loves his dog so much! Once his dog created two strings **a** and **b** each of length **n** consisting of digits **1** and **2**, and even a problem about them!

Chef's Dog will tell by barking if a string **x** (also containing only digits **1** and **2** and with length **N**) is **good** or not by performing the following actions.

- It starts at first digit of the string, i.e. at **i = 1**.

- It can move from digit **i** to either **i - 1** or **i + 1** if **x_i** equals **1** and the corresponding digits exist.

- It can move from digit **i** to either **i - 2** or **i + 2** if **x_i** equals **2** and the corresponding digits exist.

- It **must** visit each digit **exactly** once.

- It **must** finish at the last digit (**X_N**).

Chef's dog wants to make both the strings **a** and **b** *good* by choosing some subset **S** (possibly empty) of indices of set **{1, 2, ..., n}** and swapping each index **i ϵ S** between string **a** and **b**, i.e. swapping **a_i** and **b_i**. Can you find how many such subsets **S** exist out there? As the answer could be large, output it modulo **10^9 + 7**.

**Input**

The first line of the input contains an integer **T** denoting the number of test cases. The description of **T** test cases follows.

The first line contains string **a**.

The second line contains string **b**.

**Output**

For each test case, output a single line containing answer of the problem.

**Constraints**

- **1** ≤ **T** ≤ **20**

- **1** ≤ **|a| = |b|** ≤ **10^5**

- **'1'** ≤ **a_i, b_i** ≤ **'2'**

**Subtasks**

- Subtask #1 (30 points) **|a|, |b|** ≤  10

- Subtask #2 (70 points) **original constraints**

## Constraints

- 1 ≤ T ≤ 20
- 1 ≤ |a| = |b| ≤ 10^5
- '1' ≤ a_i, b_i ≤ '2'

## Sample

**Sample input**

```
2
1111
2211
222
111
```

**Sample output**

```
8
0
```

<details><summary>Explanation</summary>

**Test case 1.**
Possible subsets are:
**{}**, **{1, 2}**, **{1, 2, 3}**, **{1, 2, 4}**, **{1, 2, 3, 4}**, **{3}**, **{4}**, **{3, 4}**.

**Test case 2.** There are no possible sets **S** which can make both the strings good.

</details>

## Approach

First characterise a good string. Reading left to right, a `1` simply steps forward. A `2` at position $i$ jumps to $i+2$; position $i+1$ is then still unvisited and can only be picked up by going $i \to i+2 \to i+1 \to i+3$, which forces the pattern `2 2 1` on positions $i, i+1, i+2$. So everything before the final character must be a concatenation of the blocks `1` and `221`; the last character itself is never used for a move, so it may be either digit.

That is a three-state automaton: state 0 between blocks, state 1 after the first `2`, state 2 after `22` (only `1` allowed next). Run a DP over pairs of states, one per string. At each position there are two choices - keep or swap - which feed the characters to the two automata in either order. After the first $N-1$ positions both automata must be in state 0, and the last position contributes a free factor of 2.

## Solution (Python)

```python
import sys


def main() -> None:
    tokens = iter(sys.stdin.buffer.read().split())
    out = []
    MOD = 1000000007
    transition = ({49: 0, 50: 1}, {50: 2}, {49: 0})
    for _ in range(int(next(tokens))):
        first, second = (next(tokens), next(tokens))
        ways = {(0, 0): 1}
        for x, y in zip(first[:-1], second[:-1]):
            next_ways = {}
            for (u, v), count in ways.items():
                for c, d in ((x, y), (y, x)):
                    if c in transition[u] and d in transition[v]:
                        state = (transition[u][c], transition[v][d])
                        next_ways[state] = (next_ways.get(state, 0) + count) % MOD
            ways = next_ways
        out.append(str(ways.get((0, 0), 0) * 2 % MOD))
    print('\n'.join(out))


if __name__ == "__main__":
    main()
```

## Complexity

- **Time:** $O(N)$ per test case
- **Space:** $O(1)$ - at most nine states
- Auxiliary space excludes the buffered input and output.

## Edge cases

- $N = 1$: the walk is already finished, so both subsets (swap or not) work and the answer is 2.
- When $a_i = b_i$ both choices lead to the same state pair and are counted twice, as they should be - they are different subsets.
- A block `221` cut off by the end of the prefix leaves a non-zero state and is rejected.
- Characters arrive as bytes, hence the keys 49 and 50 in the transition table.

## Dry run

`a = 1111`, `b = 2211`.

Positions 1-2 offer (1,2) and (1,2). The second string needs `22` there to start a `221` block, so the two positions must be either both kept or both swapped - 2 ways; the mixed choices die because a lone `2` is followed by a `1`.

Position 3 is (1,1): both choices keep both automata valid and bring them back to state 0 - 4 ways. The last position doubles it.

Answer 8.

---

Same problem in rating order (#644 of 735): [../../by-rating/644-CHEFTWOS.md](../../by-rating/644-CHEFTWOS.md)
