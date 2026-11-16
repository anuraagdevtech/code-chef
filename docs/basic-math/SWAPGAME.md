[&larr; 665. Minimize swaps](DIVBY3.md) &middot; [Index](../../README.md)

# 706. Make that Array!

> CodeChef problem code [`SWAPGAME`](https://www.codechef.com/problems/SWAPGAME) &middot; difficulty **2323** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Basic Math |
| **Technique** | A potential function makes the score independent of the moves |
| **Time** | $O(N)$ per test case |
| **Space** | $O(N)$ |
| **Roadmap course** | 2000 to 2500 difficulty problems (Level 5) |

## Question

Chef is given two arrays $A$ and $B$, each having $N$ elements.

In one move, Chef can choose an index $i$ $(1 \leq i \leq N-1$), get $(A_i - A_{i+1})$ points, and then swap $A_i$ and $A_{i+1}$.

**For example:** If Chef has the array - $[10, 7,5]$ and Chef chooses index $1$ during his move, he will get $10 - 7 = 3$ points and the new array will become $[7 , 10 ,5]$

Can you help Chef in finding the maximum number of points he can get while converting the array $A$ into array $B$?

$\textbf{Note:}$ It is guaranteed in the input that there exists a sequence of moves which can convert array $A$ into $B$.

**Input**

- The first line of input contains a single integer $T$, denoting the number of testcases. The description of the $T$ testcases follows.
- The first line of each test case contains a single integer $N$ denoting the number of elements in $A$ and $B$.
- The second line of each test case contains $N$ space separated integers $A_1, A_2,..., A_N$.
- The third line of each test case contains $N$ space separated integers $B_1, B_2,..., B_N$.

**Output**

For each test case, print a single line containing one integer, which is the maximum number of points that Chef can get while converting the array $A$ into array $B$

## Constraints

- $1 \leq T \leq 5 \cdot 10^4$
- $2 \leq N \leq 5 \cdot 10^5$
- $1 \leq A_i \leq 10^5$
- $1 \leq B_i \leq 10^5$
- The sum of $N$ over all test cases does not exceed $5 \cdot 10^5$

## Sample

**Sample input**

```
3
2
1 2
2 1
3
3 2 1
1 2 3
3
1 2 3
1 2 3
```

**Sample output**

```
-1
4
0
```

<details><summary>Explanation</summary>

**Test Case $1$:** Chef can choose $i = 1$ in the first move, get $1 - 2 = -1$ points and swap $A_1$ and $A_2$. After this move, $A$ is converted into $B$. We can prove that there exists no other sequence of moves which can result in higher score while converting $A$ into $B$.

**Test Case $2$:** One possible sequence of moves is the following:
- Choose $i = 2$. Total points $= 1$, and $A$ will become $[3, 1, 2]$.
- Choose $i = 1$. Total points $= 1 + 2$, and $A$ will become $[1, 3, 2]$.
- Choose $i = 2$. Total points $= 1 + 2 + 1$, and $A$ will become $[1, 2, 3]$.

There are other possible sequences of moves which can result in total $4$ points, but no such sequence exists which can result in more than $4$ points, and simultaneously convert $A$ into $B$.

</details>

## Approach

Define the potential $\Phi = \sum_i i \cdot A_i$. Swapping $A_i$ and $A_{i+1}$ changes it by

$$\bigl(i A_{i+1} + (i+1) A_i\bigr) - \bigl(i A_i + (i+1) A_{i+1}\bigr) = A_i - A_{i+1},$$

which is exactly the number of points the move earns. So the total score of any sequence of moves equals $\Phi(\text{final}) - \Phi(\text{initial})$, no matter which moves are made or in what order.

The final array must be $B$, and it is guaranteed to be reachable, so every valid sequence scores

$$\sum_i i \cdot (B_i - A_i),$$

and that is both the maximum and the only possible value.

## Solution (Python)

```python
import sys


def solve(tokens):
    n = next(tokens)
    source = [next(tokens) for _ in range(n)]
    target = [next(tokens) for _ in range(n)]
    return str(sum((i * (y - x) for i, (x, y) in enumerate(zip(source, target)))))


if __name__ == "__main__":
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    t = int(next(tokens))
    out = [solve(tokens) for _ in range(t)]
    sys.stdout.write('\n'.join(out))
```

## Complexity

- **Time:** $O(N)$ per test case
- **Space:** $O(N)$
- Auxiliary space excludes the buffered input and output.

## Edge cases

- $A = B$: the answer is 0, even though detours are possible - they earn nothing in total.
- The answer can be negative.
- Whether indices start at 0 or 1 does not matter, because both arrays have the same sum.
- Values up to $10^5$ and $N$ up to $5 \cdot 10^5$ give totals beyond 32 bits.

## Dry run

`A = [3, 2, 1]`, `B = [1, 2, 3]`.

With 0-based weights: $0 \cdot (1 - 3) + 1 \cdot (2 - 2) + 2 \cdot (3 - 1) = 4$.

Check with actual moves: swap (3, 2) for 1 point, (3, 1) for 2 points, (2, 1) for 1 point - 4 points and the array is `1 2 3`.

> CodeChef tags: `Algorithms`, `Constructive`

---

Same problem in rating order (#670 of 735): [../../by-rating/670-SWAPGAME.md](../../by-rating/670-SWAPGAME.md)
