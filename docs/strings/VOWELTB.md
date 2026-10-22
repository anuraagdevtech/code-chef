[&larr; 99. The Block Game](PALL01.md) &middot; [Index](../../README.md) &middot; [142. World Chess Championship &rarr;](WCC.md)

# 105. Is it a VOWEL or CONSONANT

> CodeChef problem code [`VOWELTB`](https://www.codechef.com/problems/VOWELTB) &middot; difficulty **520** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Strings |
| **Technique** | Membership test against a small set |
| **Time** | $O(1)$ |
| **Space** | $O(1)$ |
| **Roadmap course** | 500 to 1000 difficulty rating (Level 1) |

## Question

Write a program to take a character $(C)$ as input and check whether the given character is a vowel or a consonant.

$NOTE:-$
Vowels are 'A', 'E', 'I', 'O', 'U'. Rest all alphabets are called consonants.

**Input**

- First line will contain the character $C$.

**Output**

Print "Vowel" if the given character is a vowel, otherwise print "Consonant".

## Constraints

- $C$ $will$ $be$ $an$ $upper$ $case$ $English$ $alphabet$

## Sample

**Sample input**

```
Z
```

**Sample output**

```
Consonant
```

## Approach

A single uppercase letter is given; print `Vowel` if it is one of `A`, `E`, `I`, `O`, `U` and `Consonant` otherwise.

The direct expression is `c in "AEIOU"`, or `c in {"A","E","I","O","U"}` with a set. For five elements the difference is immaterial — the substring scan is if anything faster at this size — but the set version is the one that stays $O(1)$ as the collection grows, and it states "membership" rather than "is a substring of". For single characters the two agree; for multi-character needles they would not, which is worth keeping in mind before reusing the idiom.

Either way this beats a five-way `or` chain, which is longer and easy to mistype.

The constraints promise an uppercase English letter, so there is no need to normalise case or reject digits and punctuation. If that guarantee were absent, `c.upper() in "AEIOU"` would be the defensive form.

There is **no $T$** here — the input is a single character on one line, one test case. The expected output is `Vowel` or `Consonant`, capitalised exactly as shown, with the sample's `Z` producing `Consonant`.

## Solution (Python)

```python
import sys

VOWELS = {"A", "E", "I", "O", "U"}


def main() -> None:
    # Single character, no test-case count.
    c = sys.stdin.buffer.read().split()[0].decode()
    print("Vowel" if c in VOWELS else "Consonant")


main()
```

## Complexity

- **Time:** $O(1)$
- **Space:** $O(1)$

## Edge cases

- **Each of the five vowels** `A E I O U`: all must print `Vowel`.
- **`Y`**: a consonant under this problem's definition, since the set is exactly those five letters.
- **`A` and `Z`**, the two ends of the alphabet: one of each class, confirming the test is membership and not a range comparison.
- **Input shape**: one character and no test-case count. Reading with `.split()` discards the trailing newline, which a raw `read()` would keep and turn into a two-character token.
- The input is guaranteed upper case, so no case folding is needed — but that guarantee is the only reason.

## Dry run

Input is the single character `Z`.

| step | value |
|---|---|
| token read | `"Z"` |
| in $\{A, E, I, O, U\}$? | no |
| output | `Consonant` |

> CodeChef tags: `Basic Programming Concepts`, `Algorithms`

---

Same problem in rating order (#12 of 486): [../../by-rating/012-VOWELTB.md](../../by-rating/012-VOWELTB.md)
