# 096. Cars and Bikes

> [`TYRES`](https://www.codechef.com/problems/TYRES) &middot; difficulty **809** &middot; time limit **0.5s** &middot; 500 to 1000 difficulty rating (Level 1)

> _Edge cases and dry run for this problem are still to be written._

## Topic used

| | |
|---|---|
| **Topic** | Number Theory |
| **Technique** | Remainder modulo 4 |
| **CodeChef tags** | `Mathematics`, `Basic Math` |
| **Complexity class** | Constant time $O(1)$ |
| **Time** | $O(1)$ per test case |
| **Space** | $O(1)$ |

## Question

**Read problems statements in [Russian](https://www.codechef.com/download/translated/COOK133/russian/TYRES.pdf) and [Bengali](https://www.codechef.com/download/translated/COOK133/bengali/TYRES.pdf).**
Chef opened a company which manufactures cars and bikes. Each car requires $4$ tyres while each bike requires $2$ tyres. Chef has a total of $N$ tyres ($N$ is even). He wants to manufacture maximum number of cars from these tyres and then manufacture bikes from the remaining tyres.

Chef's friend went to Chef to purchase a bike. If Chef's company has manufactured even a single bike then Chef's friend will be able to purchase it.

Determine whether he will be able to purchase the bike or not.

**Input**

- The first line contains an integer $T$ denoting the number of test cases. The $T$ test cases then follow.
- The first line of each test case contains an integer $N$ denoting the number of tyres.

**Output**

For each test case, output `YES` or `NO` depending on whether Chef's friend will be able to purchase the bike or not. Output is case insensitive.

## Constraints

- $1 \leq T \leq 100$
- $2 \leq N \leq 1000$
- $N$ is even

**Subtasks**

- 30 points : $1 \leq R \leq 10000$
- 70 points : $1 \leq R \leq 10^9$

## Sample

**Sample input**

```
3
8
2
6
```

**Sample output**

```
NO
YES
YES
```

<details><summary>Explanation</summary>

- For the first test case Chef, will manufacture $2$ cars and will thus use all the $8$ tyres and thus could not manufacture any bike.

- For the second test case, Chef cannot manufacture any car since there are not enough tyres and will thus manufacture only a single bike which will be purchased by Chef's friend.

- For the third test case, Chef will manufacture $1$ car and thus use $4$ tyres. From the remaining $2$ tyres, Chef can manufacture a single bike which will be purchased by Chef's friend.

</details>

## Approach

Chef builds as many cars as possible first, each taking $4$ tyres, so $\lfloor N/4 \rfloor$ cars are made and $N \bmod 4$ tyres remain. Bikes take $2$ tyres each, so the friend can buy one exactly when the leftover is at least $2$.

Because $N$ is guaranteed **even**, the remainder $N \bmod 4$ is either $0$ or $2$ — never $1$ or $3$. So the whole question collapses to

$$N \equiv 2 \pmod 4$$

In words: an even number that is *not* a multiple of four leaves exactly two tyres over, which is precisely one bike. A multiple of four is consumed entirely by cars and leaves nothing.

The evenness guarantee is what makes this clean, and it is worth seeing why. Without it, $N = 7$ would leave $3$ tyres, still enough for one bike, and the test would have to be $N \bmod 4 \geq 2$. That more general form is also correct here, just redundant.

The samples cover both residues: $N = 8$ is $0 \bmod 4$ and yields no bike, while $N = 2$ and $N = 6$ are both $2 \bmod 4$ and yield one. Note $N = 2$ produces zero cars and a single bike — building cars first does not mean a car is always built.

## Solution

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        n = int(data[1 + i])
        # n is even, so the leftover after making cars is either 0 or 2 tyres.
        out.append("YES" if n % 4 == 2 else "NO")
    sys.stdout.write("\n".join(out) + "\n")


main()
```

---

Same problem grouped by topic: [../docs/number-theory/TYRES.md](../docs/number-theory/TYRES.md)
