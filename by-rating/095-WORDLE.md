# 095. Wordle

> [`WORDLE`](https://www.codechef.com/problems/WORDLE) &middot; difficulty **804** &middot; time limit **1s** &middot; 500 to 1000 difficulty rating (Level 1)

## Topic used

| | |
|---|---|
| **Topic** | Strings |
| **Technique** | Position-wise comparison |
| **CodeChef tags** | `Data Structures`, `Basic Programming Concepts`, `String`, `Loops` |
| **Complexity class** | Constant time $O(1)$ |
| **Time** | $O(L)$ per test case with $L = 5$ |
| **Space** | $O(L)$ |

## Question

Chef invented a modified wordle.

There is a hidden word $S$ and a guess word $T$, both of length $5$.

Chef defines a string $M$ to determine the correctness of the guess word. For the $i^{th}$ index:
- If the guess at the $i^{th}$ index is correct, the $i^{th}$ character of $M$ is $\texttt{G}$.
- If the guess at the $i^{th}$ index is wrong, the $i^{th}$ character of $M$ is $\texttt{B}$.

Given the hidden word $S$ and guess $T$, determine string $M$.

**Input**

- First line will contain $T$, number of test cases. Then the test cases follow.
- Each test case contains of two lines of input.
- First line contains the string $S$ - the hidden word.
- Second line contains the string $T$ - the guess word.

**Output**

For each test case, print the value of string $M$.

You may print each character of the string in uppercase or lowercase (for example, the strings $\texttt{BgBgB}$, $\texttt{BGBGB}$, $\texttt{bgbGB}$ and $\texttt{bgbgb}$ will all be treated as identical).

## Constraints

- $1 \leq T \leq 1000$
- $|S| = |T| = 5$
- $S, T$ contain uppercase english alphabets only.

## Sample

**Sample input**

```
3
ABCDE
EDCBA
ROUND
RINGS
START
STUNT
```

**Sample output**

```
BBGBB
GBBBB
GGBBG
```

<details><summary>Explanation</summary>

**Test Case $1$:** Given string $S = \texttt{ABCDE}$ and $T = \texttt{EDCBA}$. The string $M$ is:
- Comparing the first indices, $\texttt{A} \neq \texttt{E}$, thus, $M[1] = \texttt{B}$.
- Comparing the second indices, $\texttt{B} \neq \texttt{D}$, thus, $M[2] = \texttt{B}$.
- Comparing the third indices, $\texttt{C} = \texttt{C}$, thus, $M[3] = \texttt{G}$.
- Comparing the fourth indices, $\texttt{D} \neq \texttt{B}$, thus, $M[4] = \texttt{B}$.
- Comparing the fifth indices, $\texttt{E} \neq \texttt{A}$, thus, $M[5] = \texttt{B}$.
Thus, $M = \texttt{BBGBB}$.

**Test Case $2$:** Given string $S = \texttt{ROUND}$ and $T = \texttt{RINGS}$. The string $M$ is:
- Comparing the first indices, $\texttt{R} = \texttt{R}$, thus, $M[1] = \texttt{G}$.
- Comparing the second indices, $\texttt{O} \neq \texttt{I}$, thus, $M[2] = \texttt{B}$.
- Comparing the third indices, $\texttt{U} \neq \texttt{N}$, thus, $M[3] = \texttt{B}$.
- Comparing the fourth indices, $\texttt{N} \neq \texttt{G}$, thus, $M[4] = \texttt{B}$.
- Comparing the fifth indices, $\texttt{D} \neq \texttt{S}$, thus, $M[5] = \texttt{B}$.
Thus, $M = \texttt{GBBBB}$.

</details>

## Approach

This is the simplified Wordle: each position is judged **only against the same position** in the hidden word. Character $i$ of the mask is `G` when $S_i = T_i$ and `B` otherwise.

`zip(s, t)` walks the two strings in lockstep, and a generator expression inside `"".join` builds the mask in one pass:

```python
"".join("G" if a == b else "B" for a, b in zip(s, t))
```

The thing to notice is what this problem deliberately leaves out. Real Wordle has a third state — a letter present in the word but in the wrong place — which requires counting letter multiplicities and is substantially trickier, because a repeated guess letter must not be credited more times than it occurs in the answer. Here there is no yellow, so no cross-position bookkeeping is needed at all and each index is independent.

Sample case 1 makes that concrete: `ABCDE` against `EDCBA` shares every letter, yet only the middle `C` sits in the right place, so the mask is `BBGBB` rather than all green. An implementation that checked membership with `in` instead of comparing positions would wrongly report five matches.

Both strings are guaranteed to be length $5$ and uppercase, so no validation or case folding is needed. Each test case spans two lines, read as two consecutive tokens.

## Solution

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        s = data[1 + 2 * i].decode()
        g = data[2 + 2 * i].decode()
        # Each index is judged on its own; there is no "right letter, wrong
        # place" state in this variant.
        out.append("".join("G" if a == b else "B" for a, b in zip(s, g)))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Edge cases

- **Nothing in common** (`ABCDE` against `EDCBA`): only the middle letter aligns, giving `BBGBB` — note that `A` and `E` both *appear* in the other word, yet score black, because this variant has no "right letter, wrong place" state.
- **Repeated letters** (`START` against `STUNT`): the `T` at index $1$ matches and the `T` at index $4$ matches, each judged on its own. Because there is no yellow state, duplicates need no tallying — the usual Wordle difficulty disappears.
- **Identical words**: all `G`.
- **No match anywhere**: all `B`.
- Both strings are exactly five characters, so no length handling is needed.

## Dry run

`START` against the guess `STUNT`, index by index:

| index | 0 | 1 | 2 | 3 | 4 |
|---|---|---|---|---|---|
| answer | `S` | `T` | `A` | `R` | `T` |
| guess | `S` | `T` | `U` | `N` | `T` |
| result | `G` | `G` | `B` | `B` | `G` |

Output `GGBBG`.

---

Same problem grouped by topic: [../docs/strings/WORDLE.md](../docs/strings/WORDLE.md)
