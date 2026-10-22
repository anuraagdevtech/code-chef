[&larr; 169. Motivation](169-IMDB.md) &middot; [Index](README.md) &middot; [171. Two Dishes &rarr;](171-TWODISH.md)

# 170. Studying Alphabet

> [`ALPHABET`](https://www.codechef.com/problems/ALPHABET) &middot; difficulty **1123** &middot; time limit **1s** &middot; Level up from 1* to 2* (Level 2)

## Topic used

| | |
|---|---|
| **Topic** | Sets |
| **Technique** | Subset containment |
| **Complexity class** | Linear $O(n)$ |
| **Time** | $O(|W|)$ per word |
| **Space** | $O(1)$ |

## Question

Not everyone probably knows that Chef has younger brother Jeff. Currently Jeff learns to read.

He knows some subset of the letter of Latin alphabet. In order to help Jeff to study, Chef gave him a book with the text consisting of **N** words. Jeff can read a word if it consists only of the letters he knows.

Now Chef is curious about which words his brother will be able to read, and which are not. Please help him!

**Input**

The first line of the input contains a lowercase Latin letter string **S**, consisting of the letters Jeff can read. Every letter will appear in **S** no more than once.

The second line of the input contains an integer **N** denoting the number of words in the book.

Each of the following **N** lines contains a single lowercase Latin letter string **W_i**, denoting the **i**^th word in the book.

**Output**

For each of the words, output <tt>"Yes"</tt> (without quotes) in case Jeff can read it, and <tt>"No"</tt> (without quotes) otherwise.

**Constraints**

- **1** ≤ **|S|** ≤ **26**

- **1** ≤ **N** ≤ **1000**

- **1** ≤ **|W_i|** ≤ **12**

- Each letter will appear in **S** no more than once.

- **S, W_i** consist only of lowercase Latin letters.

**Subtasks**

- **Subtask #1 (31 point)**: **|S|** = **1**, i.e. Jeff knows only one letter.

- **Subtask #2 (69 point)**	: no additional constraints

## Constraints

- 1 ≤ |S| ≤ 26
- 1 ≤ N ≤ 1000
- 1 ≤ |W_i| ≤ 12
- Each letter will appear in S no more than once.
- S, W_i consist only of lowercase Latin letters.

## Sample

**Sample input**

```
act
2
cat
dog
```

**Sample output**

```
Yes
No
```

<details><summary>Explanation</summary>

The first word can be read.

The second word contains the letters d, o and g that aren't known by Jeff.

</details>

## Approach

Jeff can read a word exactly when every letter in it is one he knows:

$$\text{set}(W_i) \subseteq \text{set}(S)$$

Building the known letters into a `set` once, outside the loop, makes each word a single subset test with $O(1)$ lookups per character. Rebuilding the set per word, or scanning the string `S` for each character, would turn a linear solution into a quadratic one for no reason.

Python spells the subset test directly as `set(w) <= known`, which reads exactly like the mathematics.

Two things do **not** matter, and noticing that avoids wasted work. Letter **repetition** is irrelevant — a word may use a known letter many times, which is why sets rather than counts are the right structure. And **order** is irrelevant too; sample case 1 has Jeff knowing `act` and reading `cat`, a different arrangement of the same letters.

The guarantee that each letter appears in $S$ at most once means $S$ is already effectively a set, so no deduplication is needed — though converting to a set does it for free.

Sample case 2, `dog`, fails on the very first letter, and the `<=` short-circuits there.

Note the input shape: there is **no $T$**. The first line is the known-letter string, the second is $N$, and then come $N$ words — each producing one `Yes` or `No`.

## Solution

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    # No test-case count: known letters, then the word count, then the words.
    known = set(data[0])
    n = int(data[1])
    # Repetition and order are irrelevant, so compare as sets.
    out = ["Yes" if set(data[2 + i]) <= known else "No" for i in range(n)]
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Edge cases

- **Repetition in the word is irrelevant**: `cat` and `catt` both need only $\{a, c, t\}$, which is why a set comparison is right and counting is not needed.
- **Order is irrelevant** too — `act` and `cat` are the same requirement.
- **One unknown letter is enough to fail**: `dog` shares nothing with $\{a,c,t\}$, but `cad` would fail just as surely on the single `d`.
- **All 26 letters known**: every word answers `Yes`.
- **Input shape**: no test-case count — the first token is the known-letters string, then the word count, then the words.

## Dry run

Known letters $\{a, c, t\}$.

| word | letters used | subset? | output |
|---|---|:---:|---|
| `cat` | $\{c, a, t\}$ | yes | `Yes` |
| `dog` | $\{d, o, g\}$ | no | `No` |

---

Same problem grouped by topic: [../docs/sets/ALPHABET.md](../docs/sets/ALPHABET.md)
