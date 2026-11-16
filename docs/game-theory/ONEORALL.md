[&larr; 635. Gold Mining](GOLMINE.md) &middot; [Index](../../README.md)

# 722. One or All

> CodeChef problem code [`ONEORALL`](https://www.codechef.com/problems/ONEORALL) &middot; difficulty **2420** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Game Theory |
| **Technique** | Parity of the total, plus the parity of the minimum when N is even |
| **Time** | $O(N)$ per test case |
| **Space** | $O(N)$ |
| **Roadmap course** | 2000 to 2500 difficulty problems (Level 5) |

## Question

Chef and Chefina are playing a game. There are $N$ piles where $i^{th}$ pile contains $A_i$ stones.

The players take alternate turns with **Chef starting the game**. In his/her turn, a player can make **one** of the following type of move:

- Type $1$: Choose **any** non-empty pile and remove $1$ stone from that pile.
- Type $2$: Remove $1$ stone each from **all** the $N$ piles. This move can be done only if **all** the $N$ piles contain at least $1$ stone.

The player who cannot make a move loses the game.

Determine the winner of the game if both players play optimally.

**Input**

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of multiple lines of input.
    - The first line of each test case contains a single integer $N$ denoting the number of piles.
    - The next line contains $N$ space-separated integers $A_1, A_2, A_3, \dots, A_N$ denoting the number of stones in each pile initially.

**Output**

For each test case, output `CHEF` if Chef wins the game, `CHEFINA` otherwise.

You may print each character in uppercase or lowercase. For example, the strings `CHEF`, `chef`, `Chef`,  and `cHEf` are all considered the same.

## Constraints

- $1 \leq T \leq 5000$
- $1 \leq N \leq 10^5$
- $1 \leq A_i \leq 10^9$
- The sum of $N$ over all test cases won't exceed $5\cdot 10^5$.

## Sample

**Sample input**

```
3
4
1 1 1 1
3
1 2 3
1
15
```

**Sample output**

```
CHEF
CHEFINA
CHEF
```

<details><summary>Explanation</summary>

**Test case $1$:** Chef can make a move of type $2$ and remove $1$ stone each from all the piles.
Thus, Chefina has no valid move to make and she loses.

**Test case $2$:** Consider the following sequence of moves:
- Chef removes $1$ stone each from all piles. Thus the remaining stones are $[0, 1, 2]$.
- Chefina removes $1$ stone from pile $2$. Thus the remaining stones are $[0, 0, 2]$.
- Chef removes $1$ stone from pile $3$. Thus the remaining stones are $[0, 0, 1]$.
- Chefina removes $1$ stone from pile $3$. Thus the remaining stones are $[0, 0, 0]$.

Thus, Chef has no valid move to make and he loses.

</details>

## Approach

**$N$ odd.** A type-1 move removes 1 stone and a type-2 move removes $N$ stones, an odd number. Every move flips the parity of the total, the game ends at total 0, and so the number of moves has the parity of the initial total: the first player wins exactly when the total is odd.

**$N$ even.** Now a type-2 move keeps the parity of the total but flips the parity of the minimum. Claim: the losing positions are exactly those where both the total and the minimum are even.

- From such a position every move leaves the set: a type-1 move makes the total odd; a type-2 move (possible only if the minimum is at least 2) keeps the total even but makes the minimum odd.
- From any other position there is a move into the set. If the minimum is odd and the total even, take one from every pile. If the total is odd and the minimum is even, take one stone from a pile that is larger than the minimum - one exists, since $N$ equal even piles would have an even total. If both are odd, take one stone from a minimum pile, making both even.

The terminal position (all piles empty) has total 0 and minimum 0 and is losing, consistent with the claim. So for even $N$ Chef wins unless the total and the minimum are both even.

## Solution (Python)

```python
import sys


def solve(tokens):
    n = next(tokens)
    piles = [next(tokens) for _ in range(n)]
    win = sum(piles) % 2 == 1 if n % 2 else min(piles) % 2 == 1 or sum(piles) % 2 == 1
    return 'CHEF' if win else 'CHEFINA'


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

- $N = 1$: the two move types coincide and Chef wins exactly when the pile is odd.
- All piles equal to 1 with even $N$: one type-2 move wins immediately.
- Only two parities are needed; the actual sizes are irrelevant.
- The total can reach $10^{14}$.

## Dry run

- `[1, 1, 1, 1]`: $N$ even, minimum 1 is odd - CHEF (he removes one from every pile).
- `[1, 2, 3]`: $N$ odd, total 6 is even - CHEFINA.
- `[15]`: $N$ odd, total 15 is odd - CHEF.

> CodeChef tags: `Algorithms`, `Constructive`

---

Same problem in rating order (#686 of 735): [../../by-rating/686-ONEORALL.md](../../by-rating/686-ONEORALL.md)
