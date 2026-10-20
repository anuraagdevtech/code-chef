# 241. Chef and Coins Game

> CodeChef problem code [`CHCOINSG`](https://www.codechef.com/problems/CHCOINSG) &middot; difficulty **1442** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Game Theory |
| **Technique** | Losing positions form a residue class |
| **Time** | $O(1)$ per test case |
| **Space** | $O(1)$ |
| **Roadmap course** | 1400 to 1600 difficulty problems (Level 2) |

## Question

Chef is playing a game with his friend Misha. They have a pile containg **N** coins. Players take alternate turns, removing some coins from the pile. On each turn, a player can remove either one coin or coins equal to some prime power (i.e. **p^x** coins, where **p** - prime number and **x** - positive integer). Game ends when the pile becomes empty. The player who can not make a move in his turn loses.

Chef plays first. Your task is to find out who will win the game, provided that both of the player play optimally.

**Input**

- The first line of the input contains an integer **T** denoting the number of test cases. The description of **T** test cases follows.

- The only line of each test case contains one integer **N**.

**Output**

- For each test case, output a single line containing one word - the name of the winner of the game. Print "Chef" (without quotes) if Chef wins the game, print "Misha" (without quotes) otherwise.

**Constraints**

- **1** ≤ **T** ≤ **1000**

- **1** ≤ **N** ≤ **10^9**

**Subtasks**

**Subtask #1 (20 points): **

- **1** ≤ **N** ≤ **10**

**Subtask #2 (30 points): **

- **1** ≤ **N** ≤ **10^4**

**Subtask #3 (50 points): **No additional constraints.

## Constraints

- 1 ≤ T ≤ 1000
- 1 ≤ N ≤ 10^9

## Sample

**Sample input**

```
2
1
8
```

**Sample output**

```
Chef
Chef
```

<details><summary>Explanation</summary>

**Example case 1.** Chef will remove the only coin from the pile and will win the game.

**Example case 2.** Chef will remove all 8 coins from the pile and win the game. Chef can remove 8 coins because 8 is a prime power, as 8 = 2^3.</p

</details>

## Approach

A move removes $1$ coin or $p^x$ coins for a prime $p$. The answer is that Chef loses exactly when $N$ is a **multiple of $6$**.

**No legal move is a multiple of 6.** A number divisible by $6$ has both $2$ and $3$ as prime factors, so it cannot be a prime power; and $1$ is not divisible by $6$ either. So from a multiple of $6$, every move lands on a non-multiple.

**Every non-multiple of 6 can reach a multiple of 6.** If $N \equiv r \pmod 6$ with $r \in \{1,2,3,4,5\}$, removing exactly $r$ coins works — because each of $1, 2, 3, 4, 5$ is legal: $1$ by the special rule, $2, 3, 5$ as primes, and $4 = 2^2$ as a prime power.

Those two facts make the multiples of $6$ precisely the losing positions. From one you must hand your opponent a winning position; from anything else you can hand them a losing one. Since $N = 0$ (no move available, so a loss) is a multiple of $6$, the induction is anchored.

So Chef wins iff $N \bmod 6 \neq 0$, which is $O(1)$ — essential at $N$ up to $10^9$, where computing Sprague–Grundy values directly is impossible.

The samples are both Chef wins: $N = 1$ removes the single coin, and $N = 8 = 2^3$ is itself a prime power, so Chef takes the whole pile at once. The first losing position is $N = 6$, which is neither $1$ nor a prime power and whose every move leaves a winning remainder.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        n = int(data[1 + i])
        # No prime power (and not 1) is divisible by 6, while any remainder
        # 1..5 is itself a legal move. So multiples of 6 are the losses.
        out.append("Misha" if n % 6 == 0 else "Chef")
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(1)$ per test case
- **Space:** $O(1)$

> CodeChef tags: `Algorithms`, `Observation`
