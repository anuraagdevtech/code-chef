[&larr; 049. Chess Ratings](049-C_RATING.md) &middot; [Index](README.md) &middot; [051. Chef and Water Bottles &rarr;](051-CHEFBOTTLE.md)

# 050. Complementary Strand in a DNA

> [`DNASTRAND`](https://www.codechef.com/problems/DNASTRAND) &middot; difficulty **660** &middot; time limit **1s** &middot; 500 to 1000 difficulty rating (Level 1)

## Topic used

| | |
|---|---|
| **Topic** | Strings |
| **Technique** | Character-wise mapping with a translation table |
| **Complexity class** | Linear $O(n)$ |
| **Time** | $O(N)$ per test case |
| **Space** | $O(N)$ for the output string |

## Question

You are given the sequence of Nucleotides of one strand of DNA through a string $S$ of length $N$. $S$ contains the character $A, T, C,$ and $G$ only.

Chef knows that:
- $A$ is complementary to $T$.
- $T$ is complementary to $A$.
- $C$ is complementary to $G$.
- $G$ is complementary to $C$.

Using the string $S$, determine the sequence of the complementary strand of the DNA.

**Input**

- First line will contain $T$, number of test cases. Then the test cases follow.
- First line of each test case contains an integer $N$ - denoting the length of string $S$.
- Second line contains $N$ characters denoting the string $S$.

**Output**

For each test case, output the string containing $N$ characters - sequence of nucleotides of the complementary strand.

## Constraints

- $1 \leq T \leq 100$
- $1 \leq N \leq 100$
- $S$ contains `A`, `T`, `C`, and `G` only

## Sample

**Sample input**

```
4
4
ATCG
4
GTCC
5
AAAAA
3
TAC
```

**Sample output**

```
TAGC
CAGG
TTTTT
ATG
```

<details><summary>Explanation</summary>

**Test case $1$:** Based on the rules, the complements of `A`, `T`, `C`, and `G` are `T`, `A`, `G`, and `C` respectively. Thus, the complementary string of the given string `ATCG` is `TAGC`.

**Test case $2$:** Based on the rules, the complements of `G`, `T`, and `C` are `C`, `A`, and `G` respectively. Thus, the complementary string of the given string `GTCC` is `CAGG`.

**Test case $3$:** Based on the rules, the complement of `A` is `T`. Thus, the complementary string of the given string `AAAAA` is `TTTTT`.

**Test case $4$:** Based on the rules, the complements of `T`, `A`, and `C` are `A`, `T`, and `G` respectively. Thus, the complementary string of the given string `TAC` is `ATG`.

</details>

## Approach

Each nucleotide maps independently to its complement: `A` ↔ `T` and `C` ↔ `G`. Because no character's image depends on its neighbours, the whole answer is a position-by-position substitution.

Python has a built-in for exactly this. `str.maketrans("ATCG", "TAGC")` builds a translation table and `s.translate(table)` applies it in one C-level pass, which is both faster and less error-prone than a loop with an `if`/`elif` chain or a dictionary lookup per character.

The table is worth reading carefully — it is its own inverse. Position by position, `A`→`T`, `T`→`A`, `C`→`G`, `G`→`C`, so applying it twice returns the original strand, exactly as the biology implies.

A common slip is to build the complement with chained `replace` calls: `s.replace("A","T").replace("T","A")` destroys the data, because the second call also rewrites the `T`s the first one just produced, collapsing everything to `A`. A single simultaneous substitution avoids that entirely, which is the real reason `translate` is the right tool rather than merely a convenient one.

Note the problem gives $N$ on its own line before the string. It is redundant for Python, since the string carries its own length, but the token must still be consumed when walking the input.

## Solution

```python
import sys

# Applied in one pass, so A->T does not get undone by a later T->A.
COMPLEMENT = str.maketrans("ATCG", "TAGC")


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        # data[pos] is N, which Python does not need, but must be skipped.
        s = data[pos + 1].decode()
        pos += 2
        out.append(s.translate(COMPLEMENT))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Edge cases

- **`A` and `T` map to each other**, as do `C` and `G`, so sequential replacement is wrong: replacing every `A` with `T` and *then* every `T` with `A` turns the original `A`s back into `A`s. A single-pass translation table applies all four substitutions simultaneously, and the sample's first string `ATCG` exposes the bug at once.
- **A homogeneous strand** (`AAAAA`): becomes all `T`, confirming the mapping is per character and not positional.
- **$N = 1$**: a single base.
- **The length line must be consumed.** Python never needs $N$, but skipping to read it would desynchronise every later test case, so the parser advances past it deliberately.

## Dry run

The strand `ATCG`, one base at a time:

| base | `A` | `T` | `C` | `G` |
|---|---|---|---|---|
| complement | `T` | `A` | `G` | `C` |

So `ATCG` becomes `TAGC`. The other cases follow the same table: `GTCC` to `CAGG`, `AAAAA` to `TTTTT`, and `TAC` to `ATG`.

---

Same problem grouped by topic: [../docs/strings/DNASTRAND.md](../docs/strings/DNASTRAND.md)
