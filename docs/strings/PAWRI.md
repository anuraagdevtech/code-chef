[&larr; 153. Play Piano](PLAYPIAN.md) &middot; [Index](../../README.md) &middot; [186. Chef and the Wildcard Matching &rarr;](TWOSTR.md)

# 185. Pawri Meme

> CodeChef problem code [`PAWRI`](https://www.codechef.com/problems/PAWRI) &middot; difficulty **1182** &middot; time limit **2s**

| | |
|---|---|
| **Topic** | Strings |
| **Technique** | Substring replacement |
| **Time** | $O(|S|)$ per test case |
| **Space** | $O(|S|)$ |
| **Roadmap course** | Level up from 1* to 2* (Level 2) |

## Question

Lately, Chef has been inspired by the "pawri" meme. Therefore, he decided to take a string $S$ and change each of its substrings that spells "party" to "pawri". Find the resulting string.

**Input**
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first and only line of each test case contains a single string $S$.

**Output**
For each test case, print a single line containing the string after it is modified by Chef.

**Constraints**
- $1 \leq T \leq 10$
- $1 \leq |S| \leq 10^5$
- $S$ contains only lowercase English letters

## Constraints

- $1 \leq T \leq 10$
- $1 \leq |S| \leq 10^5$
- $S$ contains only lowercase English letters

## Sample

**Sample input**

```
3
part
partypartiparty
yemaihuyemericarhaiauryahapartyhorahihai
```

**Sample output**

```
part
pawripartipawri
yemaihuyemericarhaiauryahapawrihorahihai
```

<details><summary>Explanation</summary>

**Example case 1:** There is no substring "party" in the original string.

**Example case 2:** The original string has $2$ substrings "party".

**Example case 3:** There is only a single substring "party" in the original string.

</details>

## Approach

Replace every occurrence of `party` with `pawri`. Python's `str.replace` does exactly this, scanning once and substituting all occurrences:

```python
s.replace("party", "pawri")
```

Two properties make the built-in the right tool rather than a hand-rolled loop.

**It replaces all occurrences, not just the first.** Sample case 2, `partypartiparty`, contains two `party` substrings separated by a near-miss, and both must change. A `find`-and-splice written by hand often handles only the first.

**Replacements cannot cascade.** The pattern and its replacement have the same length and differ in the middle, and crucially `pawri` does not contain `party`, so newly written text can never form a fresh match. That means a single pass is sufficient and there is no risk of the substitution feeding on its own output — the kind of bug that turns repeated `replace` calls into an infinite loop or a wrong answer.

Sample case 1, `part`, is the near-miss: a prefix of the pattern but not the pattern, so the string is returned unchanged. Partial matches must not be rewritten.

With $|S|$ up to $10^5$ the single linear pass is comfortable; the C-implemented `replace` is substantially faster than any character-by-character Python loop.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        s = data[1 + i].decode()
        # "pawri" never contains "party", so one pass cannot cascade.
        out.append(s.replace("party", "pawri"))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(|S|)$ per test case
- **Space:** $O(|S|)$

## Edge cases

- **A partial match stays put**: `part` lacks the trailing `y`, so it is left alone. The whole five-character pattern must appear.
- **A near miss**: `parti` is not a match either, and the second sample row contains one between two real matches.
- **Adjacent occurrences** (`partyparty`): both are replaced in the one pass.
- **No cascading is possible**, because `pawri` does not contain `party` — so a single `replace` is correct and there is no need to loop until the string stabilises.
- **$|S|$ up to $10^5$ across ten cases**, so the replacement should be a single library call rather than a character loop.

## Dry run

| input | matches found | output |
|---|---|---|
| `part` | none | `part` |
| `partypartiparty` | positions $0$ and $10$ | `pawripartipawri` |

In the second row the middle `parti` is skipped, leaving it untouched between the two replacements.

---

Same problem in rating order (#176 of 486): [../../by-rating/176-PAWRI.md](../../by-rating/176-PAWRI.md)
