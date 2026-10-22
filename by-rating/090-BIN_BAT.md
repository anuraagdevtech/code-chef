[&larr; 089. Minimum number of Flips](089-MINFLIPS.md) &middot; [Index](README.md) &middot; [091. Best of Two &rarr;](091-DICEGAME2.md)

# 090. Binary Battles

> [`BIN_BAT`](https://www.codechef.com/problems/BIN_BAT) &middot; difficulty **786** &middot; time limit **1.5s** &middot; 500 to 1000 difficulty rating (Level 1)

## Topic used

| | |
|---|---|
| **Topic** | Basic Math |
| **Technique** | Tournament rounds, and separators between them |
| **CodeChef tags** | `Mathematics`, `Number Theory`, `Basic Math`, `Logarithm` |
| **Complexity class** | Constant time $O(1)$ |
| **Time** | $O(1)$ per test case |
| **Space** | $O(1)$ |

## Question

$N$ teams have come to participate in a competitive coding event called “Binary Battles”. It is a [single-elimination tournament](https://en.wikipedia.org/wiki/Single-elimination_tournament) consisting of several rounds.

**Note:** It is known that $N$ is a power of $2$.

In one round, each team will be paired up with and compete against one of the other teams. If there are $X$ teams before the start of a round, $\frac{X}{2}$ matches are held simultaneously during the round between $\frac{X}{2}$ pairs of teams. The winning team of each match will move on to the next round, while the losing team of each match will be eliminated. There are no ties involved. The next round will then take place in the same format between the remaining teams. The process will continue until only one team remains, which will be declared the overall winner.

The organizers want to find the total time the event will take to complete. It is given that each round spans $A$ minutes, and that there is a break of $B$ minutes between every two rounds (no break after the last round).

For example, consider a case when $N = 4$, $A = 10$ and $B = 5$. The first round will consist of two matches and will take $10$ minutes to complete. Two teams move on to round 2 and the other two get eliminated. Then there is a break of $5$ minutes. The two remaining teams compete in round 2, which lasts $10$ more minutes. The team that wins is declared the overall winner. Thus the total time taken is $10 + 5 + 10 = 25$ minutes.

Can you help the organizers determine how long the event will take to finish?

**Input**

- The first line of input will contain a single integer $T$, denoting the number of test cases. Then the test cases follow.
- The first and only line of each test case contains three space-separated integers $N$, $A$ and $B$ respectively — the number of teams, the duration of each round and the length of the breaks between rounds.

**Output**

For each test case, output on a new line the time taken in minutes for the whole event to finish.

## Constraints

- $1 \leq T \leq 10^5$
- $2 \leq N \leq 2^{20}$
- $1 \leq A \leq 100$
- $1 \leq B \leq 100$
- $N$ is a power of $2$.

## Sample

**Sample input**

```
4
4 10 5
16 30 5
32 45 15
1024 23 9
```

**Sample output**

```
25
135
285
311
```

<details><summary>Explanation</summary>

**Test case 1:** As explained above, the total time the competition will take is $10 + 5 + 10 = 25$ minutes.

**Test case 2:** $4$ rounds will take place. The total time it will take is $30 + 5 + 30 + 5 + 30 + 5 + 30 = 135$ minutes.

</details>

## Approach

Each round halves the field, so starting from $N$ teams the tournament runs

$$R = \log_2 N$$

rounds before one team remains. The problem guarantees $N$ is a power of two, so this is an exact integer.

Rounds take $A$ minutes each, and breaks of $B$ minutes sit **between** rounds with none after the last. That makes breaks separators, not round markers, so there are $R - 1$ of them:

$$R \cdot A + (R - 1) \cdot B$$

This is the same *$n$ items have $n-1$ gaps* structure as the gaming-breaks problem, and it is again the likeliest place to go wrong — charging $R$ breaks adds a phantom $B$ to every answer.

Computing $R$ deserves care. `math.log2(n)` returns a float, and for large powers of two the result can land a hair off an integer, so `int(math.log2(n))` may round down to $R - 1$. Since $N$ is a power of two, `n.bit_length() - 1` gives $\log_2 N$ exactly using pure integer arithmetic — `(1024).bit_length()` is $11$, so $R = 10$. That is the right habit whenever an exact integer logarithm is needed.

Checking sample 4: $N = 1024$ gives $R = 10$, so $10 \times 23 + 9 \times 9 = 230 + 81 = 311$.

With $T$ up to $10^5$, reading the whole input at once and emitting one joined write matters more here than the arithmetic does.

## Solution

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        n, a, b = map(int, data[1 + 3 * i:4 + 3 * i])
        # n is a power of two, so bit_length gives an exact log2.
        rounds = n.bit_length() - 1
        # Breaks sit between rounds, so there is one fewer of them.
        out.append(str(rounds * a + (rounds - 1) * b))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Edge cases

- **$N = 2$**: a single round and **zero** breaks, so the answer is just $A$. The $(\text{rounds} - 1)$ factor must not go negative or invent a break.
- **Breaks sit between rounds**, so there is always one fewer break than round — the usual separator-versus-group trap.
- **$N$ is guaranteed a power of two**, which is what makes `bit_length() - 1` an exact $\log_2$. For a non-power it would silently round and give the wrong round count.
- **Largest input** ($N = 2^{20}$): twenty rounds and nineteen breaks.

## Dry run

| $N$ | rounds $\log_2 N$ | breaks | play $\text{rounds} \cdot A$ | rest $(\text{rounds}-1) \cdot B$ | output |
|---:|---:|---:|---:|---:|---|
| 4 | 2 | 1 | 20 | 5 | `25` |
| 16 | 4 | 3 | 120 | 15 | `135` |
| 32 | 5 | 4 | 225 | 60 | `285` |
| 1024 | 10 | 9 | 230 | 81 | `311` |

---

Same problem grouped by topic: [../docs/basic-math/BIN_BAT.md](../docs/basic-math/BIN_BAT.md)
