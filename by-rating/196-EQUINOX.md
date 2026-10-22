[&larr; 195. Make them equal](195-MAKEEQUAL.md) &middot; [Index](README.md) &middot; [197. Even Splits &rarr;](197-EVENSPLIT.md)

# 196. Equinox Strings

> [`EQUINOX`](https://www.codechef.com/problems/EQUINOX) &middot; difficulty **1272** &middot; time limit **0.5s** &middot; Level up from 1* to 2* (Level 2)

## Topic used

| | |
|---|---|
| **Topic** | Strings |
| **Technique** | First-character membership test |
| **Complexity class** | Linear $O(n)$ |
| **Time** | $O(N)$ per test case |
| **Space** | $O(1)$ |

## Question

Sarthak and Anuradha are very good friends and are eager to participate in an event called *Equinox*. It is a game of words. In this game, $N$ strings $S_1,\ldots, S_N$ are given. For each string $S_i$, if it starts with one of the letters of the word “EQUINOX”, Sarthak gets $A$ points and if not, Anuradha gets $B$ points. The one who has more points at the end of the game wins. If they both the same number of points, the game is a draw..

Print the winner of the game, if any, otherwise print “DRAW”.

**Input**
- The first line contains an integer $T$, the number of test cases. Then the test cases follow.
- The first line of each test case contains three integers $N$, $A$, $B$.
- $N$ lines follow, each containing a string $S_{i}$.
- All strings are in UPPERCASE.

**Output**
- For each test case, print “SARTHAK” (case insensitive) if he has more points than Anuradha, print “ANURADHA” (case insensitive) if she has more points than Sarthak, otherwise print “DRAW” (case insensitive), without the quotes.

**Constraints**
- $1 \leq T \leq 100$
- $1 \leq N \leq 100$
- $1 \leq A$, $B \leq 10^{9}$
- $1 \leq \left|S_{i}\right| \leq 100$

**Subtasks**
**Subtask #1 (100 points):** original constraints

## Constraints

- $1 \leq T \leq 100$
- $1 \leq N \leq 100$
- $1 \leq A$, $B \leq 10^{9}$
- $1 \leq \left|S_{i}\right| \leq 100$

## Sample

**Sample input**

```
2
4 1 3
ABBBCDDE
EARTH
INDIA
UUUFFFDDD
2 5 7
SDHHD
XOXOXOXO
```

**Sample output**

```
DRAW
ANURADHA
```

<details><summary>Explanation</summary>

**Test case $1$:** The strings which start with one of the letters of the word `EQUINOX` are $\{$ `EARTH`, `INDIA`, `UUUFFFDDD` $\}$. Thus, Sarthak gets $1$ point for each of these strings. In total, Sarthak gets $3$ points.
On the other hand, there is one string that does not start with one of the letters of the word `EQUINOX`. Thus, Anuradha gets $3$ points for that string.
Finally, since both of them have equal points, the game results in `DRAW`.

**Test case $2$:** There is only one string that starts with one of the letters of the word `EQUINOX` which is `XOXOXOXO`. Thus, Sarthak gets $5$ point for this string.
There is one string that does not start with one of the letters of the word `EQUINOX`. Thus, Anuradha gets $7$ points for that string.
Finally, Anuradha has the higher score. So she is the winner.

</details>

## Approach

For each string, only its **first character** matters: if it is one of the letters of `EQUINOX`, Sarthak scores $A$, otherwise Anuradha scores $B$. Tally both and compare.

The letter set is $\{$`E`, `Q`, `U`, `I`, `N`, `O`, `X`$\}$ — the *distinct* letters of the word, which conveniently has no repeats. Holding it as a `set` makes each test $O(1)$.

The trap is treating this as a scoring race by *count* rather than by points. $A$ and $B$ differ, so the side with more strings need not lead. Sample case 2 shows it: Sarthak wins one string and Anuradha one, but at $5$ against $7$ points Anuradha takes it.

Sample case 1 is the draw, and worth tracing: `ABBBCDDE` starts with `A`, which is **not** in `EQUINOX` despite the string containing `E` later. Only the first character counts. So Anuradha scores $3$ once, while Sarthak scores $1$ three times from `EARTH`, `INDIA` and `UUUFFFDDD` — level at $3$ apiece.

That last string is a good check too: `U` is in the set, so the rest of the string is irrelevant.

All strings are uppercase by guarantee, so no case folding is needed. With $A, B$ up to $10^9$ and $N$ up to $100$, totals reach $10^{11}$ — past 32 bits, so a C solution would need a 64-bit accumulator.

## Solution

```python
import sys

EQUINOX = set(b"EQUINOX")


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n, a, b = int(data[pos]), int(data[pos + 1]), int(data[pos + 2])
        words = data[pos + 3:pos + 3 + n]
        pos += 3 + n
        sarthak = anuradha = 0
        for word in words:
            # Only the first character is consulted.
            if word[0] in EQUINOX:
                sarthak += a
            else:
                anuradha += b
        out.append("SARTHAK" if sarthak > anuradha
                   else "ANURADHA" if anuradha > sarthak else "DRAW")
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Edge cases

- **Only the first character is consulted.** `UUUFFFDDD` scores for Sarthak on its leading `U` even though most of it is not an equinox letter, and `ABBBCDDE` scores for Anuradha despite containing `C`, `D` and `E`.
- **A draw is possible and must be printed as `DRAW`** — the first case ties at $3$ each, and does so with *unequal* per-word values ($A = 1$ against $B = 3$), so the tie is in the totals, not in the word counts.
- **More words does not mean winning.** The second case gives each player one word, and the larger $B = 7$ beats $A = 5$.
- **`EQUINOX` has seven distinct letters** including `X`, which the second case's `XOXOXOXO` relies on — a set built from the literal word covers them all without hand-listing.
- **$A, B \leq 10^9$ with $N \leq 100$** puts the totals up to $10^{11}$, past 32-bit but native in Python.
- Bytes are compared throughout, so the first character is an integer code and the lookup set is built from the byte string.

## Dry run

First sample: $A = 1$, $B = 3$.

| word | first char | in `EQUINOX`? | Sarthak | Anuradha |
|---|---|:---:|---:|---:|
| `ABBBCDDE` | `A` | no | 0 | 3 |
| `EARTH` | `E` | yes | 1 | 3 |
| `INDIA` | `I` | yes | 2 | 3 |
| `UUUFFFDDD` | `U` | yes | **3** | **3** |

Equal totals, so `DRAW`.

---

Same problem grouped by topic: [../docs/strings/EQUINOX.md](../docs/strings/EQUINOX.md)
