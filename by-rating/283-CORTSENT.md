# 283. Correct Sentence

> [`CORTSENT`](https://www.codechef.com/problems/CORTSENT) &middot; difficulty **1485** &middot; time limit **0.5s** &middot; 1400 to 1600 difficulty problems (Level 2)

## Topic used

| | |
|---|---|
| **Topic** | Strings |
| **Technique** | Per-word alphabet membership |
| **CodeChef tags** | `Data Structures`, `Algorithms`, `String`, `Implementation` |
| **Complexity class** | Linear $O(n)$ |
| **Time** | $O(\sum |S_i|)$ per test case |
| **Space** | $O(1)$ |

## Question

Chef knows about two languages spoken in Chefland, but he is not proficient in any of them. The first language contains lowercase English letters between 'a' and 'm' inclusive and the second language contains only uppercase English letters between 'N' and 'Z' inclusive.

Due to Chef's limited vocabulary, he sometimes mixes the languages when forming a sentence — each word of Chef's sentence contains only characters from one of the languages, but different words may come from different languages.

You are given a sentence as a sequence of $K$ words $S_1, S_2, \ldots, S_K$. Determine whether it could be a sentence formed by Chef, i.e. if it contains only the characters from the two given languages and each word contains only characters from a single language.

**Input**
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first and only line of each test case contains an integer $K$ followed by a space and $K$ space-separated strings $S_1, S_2, \ldots, S_K$.

**Output**
For each test case, print a single line containing the string `"YES"` if the given sentence can be formed by Chef or `"NO"` if it cannot.

You may print each character of the string in uppercase or lowercase (for example, the strings "yEs", "yes", "Yes" and "YES" will all be treated as identical).

**Constraints**
- $1 \le T \le 10^5$
- $1 \leq K \leq 10$
- $1 \leq |S_i| \leq 100$ for each valid $i$
- the sum of lengths of all the strings on the input does not exceed $10^5$
- each string contains only lowercase and uppercase English letters

## Constraints

- $1 \le T \le 10^5$
- $1 \leq K \leq 10$
- $1 \leq |S_i| \leq 100$ for each valid $i$
- the sum of lengths of all the strings on the input does not exceed $10^5$
- each string contains only lowercase and uppercase English letters

## Sample

**Sample input**

```
3
1 aN
2 ab NO
3 A N D
```

**Sample output**

```
NO
YES
NO
```

<details><summary>Explanation</summary>

**Example case 1:** A single word cannot contain characters from both languages.

**Example case 2:** This could be a sentence formed by Chef since each word contains only characters from a single language.

**Example case 3:** Letters 'A' and 'D' do not belong to either of the two languages.

</details>

## Approach

Two alphabets: the first is lowercase `a`–`m`, the second is uppercase `N`–`Z`. A sentence is valid when **each word** draws entirely from one of them — different words may use different alphabets, but no word may mix.

So for every word, check that all its characters lie in the first range, or that all lie in the second.

Two traps, and the samples target both.

**Mixing within a word is the forbidden thing**, not mixing within a sentence. Sample case 2, `ab NO`, uses both alphabets and is valid, because each individual word is pure. A solution demanding one alphabet per sentence would reject it.

**The ranges are restricted, not just by case.** Lowercase stops at `m` and uppercase starts at `N` — so a lowercase `z` and an uppercase `A` both belong to *neither* alphabet. Sample case 3, `A N D`, fails on exactly this: `N` is fine, but `A` and `D` are uppercase letters below `N` and belong to no language at all. Checking merely `islower()` or `isupper()` would wrongly accept it.

Sample case 1, `aN`, is the within-word mix.

Comparing characters against the range bounds directly is cheap; with the summed length bounded by $10^5$ and $T$ up to $10^5$, bulk input reading matters more than the check itself. Note the word count $K$ and the words all share **one line**, which the flat token read handles naturally.

## Solution

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        k = int(data[pos])
        words = data[pos + 1:pos + 1 + k]
        pos += 1 + k
        ok = True
        for word in words:
            # Lowercase stops at 'm' and uppercase starts at 'N', so letters
            # outside those ranges belong to neither language.
            lo = all(97 <= ch <= 109 for ch in word)       # a..m
            hi = all(78 <= ch <= 90 for ch in word)        # N..Z
            if not (lo or hi):
                ok = False
                break
        out.append("YES" if ok else "NO")
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Edge cases

- **The two alphabets are disjoint and incomplete**: lowercase `a`–`m` and uppercase `N`–`Z`. A letter outside both — `A` or `z`, say — belongs to neither language, which is what fails the third sample row on its lone `A`.
- **A word must sit entirely in one language.** `aN` mixes them and fails, even though each character is individually valid in some language.
- **Different words may use different languages**, as the second row does (`ab` then `NO`), so the test is per word rather than per sentence.
- **One bad word condemns the sentence**, and the loop breaks on the first failure.
- **A single-character word is still checked**, which is how the third row fails.
- **Bytes are compared as integer codes** against the four range bounds, avoiding a decode over up to $10^5$ characters.

## Dry run

| sentence | word | all in `a`–`m`? | all in `N`–`Z`? | verdict |
|---|---|:---:|:---:|---|
| `aN` | `aN` | no (`N`) | no (`a`) | `NO` |
| `ab NO` | `ab` | yes | — | continue |
| | `NO` | no | yes | `YES` |
| `A N D` | `A` | no | no (`A` < `N`) | `NO` |

---

Same problem grouped by topic: [../docs/strings/CORTSENT.md](../docs/strings/CORTSENT.md)
