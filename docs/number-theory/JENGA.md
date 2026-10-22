[&larr; 30. Test Score](CHEFSCORE.md) &middot; [Index](../../README.md) &middot; [41. Mario and Transformation &rarr;](TRANSFORM.md)

# 31. Jenga Night

> CodeChef problem code [`JENGA`](https://www.codechef.com/problems/JENGA) &middot; difficulty **613** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Number Theory |
| **Technique** | Divisibility as an exact-fit condition |
| **Time** | $O(1)$ per test case |
| **Space** | $O(1)$ |
| **Roadmap course** | 500 to 1000 difficulty rating (Level 1) |

## Question

Chef hosts a party for his birthday. There are $N$ people at the party. All these $N$ people decide to play Jenga.

There are $X$ Jenga tiles available. In one round, all the players pick $1$ tile each and place it in the tower.
The game is *valid* if:
- All the players have a tile in each round;
- All the tiles are used at the end.

Given $N$ and $X$, find whether the game is *valid*.

**Input**

- First line will contain $T$, the number of test cases. Then the test cases follow.
- Each test case contains a single line of input, containing two space-separated integers $N$ and $X$ representing the number of people at the party and the number of available tiles respectively.

**Output**

For each test case, output in a single line $\texttt{YES}$ if the game is valid, else output $\texttt{NO}$.

You may print each character of the string in uppercase or lowercase (for example, the strings $\texttt{YeS}$, $\texttt{yEs}$, $\texttt{yes}$ and $\texttt{YES}$ will all be treated as identical).

## Constraints

- $1 \leq T \leq 10^4$
- $1 \leq N, X \leq 1000$

## Sample

**Sample input**

```
3
3 3
4 2
2 4
```

**Sample output**

```
YES
NO
YES
```

<details><summary>Explanation</summary>

**Test case $1$:** The game will last for $1$ round after which the tiles will finish.

**Test case $2$:** There are not enough Jenga tiles for everyone to place.

**Test case $3$:** The game will last for $2$ rounds as after round $2$ all Jenga tiles are used.

</details>

## Approach

Each round consumes exactly $N$ tiles, one per player. After $r$ complete rounds, $rN$ tiles have been placed. The two validity rules say that every round must be complete (so the count is always a whole multiple of $N$) and that no tiles may be left over (so that multiple must equal $X$).

Putting them together, the game is valid exactly when $X = rN$ for some non-negative integer $r$ — that is, when

$$X \equiv 0 \pmod N$$

So the whole problem is `x % n == 0`.

The reason both rules collapse into one test is worth seeing. "Every round complete" alone would allow leftovers; "all tiles used" alone would allow a final partial round. Requiring both is precisely the statement that $N$ divides $X$ exactly.

Note the asymmetry that makes sample case 3 surprising at first glance: $N = 2$ players with $X = 4$ tiles is valid because they play two full rounds. There is no requirement that the game last only one round, nor that $X \leq N$. Conversely case 2 has more players than tiles, so not even the first round completes.

Watch the argument order — the input is $N$ then $X$, and computing `n % x` instead would pass case 1 (where both are $3$) while failing the rest.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        n, x = int(data[1 + 2 * i]), int(data[2 + 2 * i])
        # Every round uses exactly n tiles and none may be left over.
        out.append("YES" if x % n == 0 else "NO")
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(1)$ per test case
- **Space:** $O(1)$

## Edge cases

- **Fewer tiles than one round needs** ($N = 4$, $X = 2$): $2 \bmod 4 = 2$, so `NO` — not even one round completes. The sample's second row covers it, and it is also the row that catches swapping the operands, since $4 \bmod 2 = 0$ would wrongly say `YES`.
- **Exactly one round's worth** ($N = X$): `YES`.
- **$N = 1$**: every $X$ is divisible by $1$, so always `YES`.
- **Largest inputs** ($N = X = 1000$): `YES`.
- The condition is an exact fit, not "enough tiles": leftovers are a failure, so divisibility is the whole test.

## Dry run

| $N$ (per round) | $X$ (tiles) | $X \bmod N$ | output |
|---:|---:|---:|---|
| 3 | 3 | 0 | `YES` |
| 4 | 2 | 2 | `NO` |
| 2 | 4 | 0 | `YES` |

Rows 2 and 3 are the same pair of numbers swapped, and they give opposite answers.

> CodeChef tags: `Mathematics`

---

Same problem in rating order (#38 of 486): [../../by-rating/038-JENGA.md](../../by-rating/038-JENGA.md)
