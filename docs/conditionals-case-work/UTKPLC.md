[&larr; 113. Which Division](WHICHDIV.md) &middot; [Index](../../README.md) &middot; [129. Passing Marks &rarr;](PSGRADE.md)

# 123. Utkarsh and Placement tests

> CodeChef problem code [`UTKPLC`](https://www.codechef.com/problems/UTKPLC) &middot; difficulty **886** &middot; time limit **0.5s**

| | |
|---|---|
| **Topic** | Conditionals & Case Work |
| **Technique** | Ranking by a given priority order |
| **Time** | $O(1)$ per test case |
| **Space** | $O(1)$ |
| **Roadmap course** | 500 to 1000 difficulty rating (Level 1) |

## Question

Utkarsh is currently sitting for placements. He has applied to three companies named $A, B$, and $C$.

You know Utkarsh's order of preference among these $3$ companies, given to you as characters `first`, `second`, and `third` respectively (where `first` is the company he prefers most).

You also know that Utkarsh has received offers from exactly two of these three companies, given you as characters $x$ and $y$.

Utkarsh will always accept the offer from whichever company is highest on his preference list. Which company will he join?

**Input**

- The first line of input contains a single integer $T$, denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains three different space-separated characters: `first`, `second`, and `third`, denoting Utkarsh's order of preference among the three companies.
- The second line of each test case contains two space-separated characters $x$ and $y$, the companies from which Utkarsh has received offers.

**Output**

For each test case, print one line containing a single character, the company whose offer Utkarsh will accept.

The output is not case sensitive, so if the answer is $A$, both $a$ and $A$ will be accepted.

## Constraints

- $1 \leq T \leq 36$
- `first`, `second` and `third` are three different characters among $\{A, B, C\}$.
- $x$ and $y$ are two different characters among $\{A, B, C\}$.

**Subtasks**

**Subtask #1 (100 points):** Original constraints

## Sample

**Sample input**

```
2
A B C
A B
B C A
A C
```

**Sample output**

```
A
C
```

<details><summary>Explanation</summary>

**Test Case 1.** Utkarsh has received offers from $A$ and $B$. Of these two, he prefers company $A$ (first preference) over $B$ (second preference). Therefore Utkarsh will accept the offer of company $A$.

**Test Case 2.** Utkarsh has received offers from $A$ and $C$, where company $C$ is his second preference and company $A$ is his third preference. Utkarsh will accept the offer of company $C$.

</details>

## Approach

The preference order arrives as data rather than being fixed, so the solution builds the ranking at runtime: map the first-listed company to rank $0$, the second to $1$, the third to $2$. Utkarsh accepts whichever of his two offers has the **lower** rank.

With a dictionary from company letter to rank, the answer is `min(x, y, key=rank.get)` — one expression, no case analysis. Building the ranking from the input is what keeps this short; hard-coding `A > B > C` would fail sample case 2, where the stated order is `B C A` and the answer for offers `A C` is `C`.

Note that lower rank means *more* preferred, so the selection uses `min`, not `max`. Inverting that is the easy mistake, and sample case 1 would not catch it — there the preference order is `A B C` and the offers are `A B`, where `A` is both first-preferred and alphabetically first.

The constraints guarantee all three letters appear exactly once in the preference line and that the two offers are distinct, so every lookup succeeds and there is never a tie to break.

The input spans two lines per test case — three characters, then two — which the flat token read handles without caring about line boundaries.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        first, second, third, x, y = (c.decode() for c in data[1 + 5 * i:6 + 5 * i])
        # Preference order comes from the input, so build the ranking per case.
        rank = {first: 0, second: 1, third: 2}
        out.append(min(x, y, key=rank.get))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(1)$ per test case
- **Space:** $O(1)$

## Edge cases

- **The preference order comes from the input**, so the ranking has to be rebuilt for each test case. Hard-coding $A > B > C$ answers the first sample row correctly by luck and gets the second one wrong, where the order is $B > C > A$ and the answer is `C`.
- **$x$ and $y$ are guaranteed distinct**, so there is never a tie to break.
- **The answer may be any of the three preference levels**: in the second row the better of the two offers is only the input's *second* choice.
- `first`, `second` and `third` are guaranteed to be a permutation of $\{A, B, C\}$, so the ranking is always total and every offer has a rank.

## Dry run

| preference | offered | ranks | better | output |
|---|---|---|---|---|
| $A > B > C$ | $A, B$ | $0, 1$ | $A$ | `A` |
| $B > C > A$ | $A, C$ | $2, 1$ | $C$ | `C` |

The second row is the one that defeats a fixed alphabetical ranking.

> CodeChef tags: `Basic Programming Concepts`, `Algorithms`

---

Same problem in rating order (#124 of 486): [../../by-rating/124-UTKPLC.md](../../by-rating/124-UTKPLC.md)
