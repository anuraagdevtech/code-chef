# 178. Chef and Feedback

> [`ERROR`](https://www.codechef.com/problems/ERROR) &middot; difficulty **1199** &middot; time limit **1s** &middot; Level up from 1* to 2* (Level 2)

## Topic used

| | |
|---|---|
| **Topic** | Strings |
| **Technique** | Substring search |
| **Complexity class** | Linear $O(n)$ |
| **Time** | $O(|S|)$ per test case |
| **Space** | $O(1)$ |

## Question

Lots of geeky customers visit our chef's restaurant everyday. So, when asked to fill the feedback form, these customers represent the feedback using a binary string (i.e a string that contains only characters **'0'** and **'1'**.

Now since chef is not that great in deciphering binary strings, he has decided the following criteria to classify the feedback as **Good** or **Bad** :

If the string contains the substring **"010"** or **"101"**, then the feedback is **Good**, else it is **Bad**. Note that, to be **Good** it is not necessary to have both of them as substring.

 So given some binary strings, you need to output whether according to the chef, the strings are **Good** or **Bad**.

**Input**

 The first line contains an integer **T** denoting the number of feedbacks. Each of the next **T** lines contains a string composed of only **'0' ** and **'1'**.

**Output**

 For every test case, print in a single line **Good** or **Bad** as per the Chef's method of classification.

**Constraints**

- ** 1 **≤  **T** ≤ **  100 **

- ** 1 ** ≤ ** |S| **  ≤ ** 10^5**

Sum of length of all strings in one test file will not exceed **6*10^6**.

## Constraints

-  1 ≤  T ≤   100
-  1  ≤  |S|   ≤  10^5
Sum of length of all strings in one test file will not exceed 6*10^6.

## Sample

**Sample input**

```
2
11111110
10101010101010
```

**Sample output**

```
Bad
Good
```

<details><summary>Explanation</summary>

**Example case 1.**

The string doesn't contain **010** or **101** as substrings.

**Example case 2.**

The string contains both **010** and **101** as substrings.

</details>

## Approach

The feedback is `Good` when the string contains `010` **or** `101` as a substring, and `Bad` otherwise. In Python that is directly

```python
"010" in s or "101" in s
```

The `in` operator on strings performs substring search — not character membership — and short-circuits on the first match.

What these two patterns actually detect is worth naming: a string is `Good` exactly when it contains a character that differs from **both** of its neighbours, i.e. an alternation of length three. A string with no such position must be a run of blocks each at least two long, like `11111110`.

That is sample case 1, which is `Bad` despite containing both digits — having a `0` and a `1` is not enough, they must alternate. A solution checking merely that both characters appear would wrongly call it `Good`.

Sample case 2 is a perfect alternation and matches immediately at position $0$.

Note that the two patterns must be searched as substrings, in order, not as a set of characters. And only one of them is needed, as the statement says explicitly.

With the summed length reaching $6 \times 10^6$, the C-implemented substring search plus bulk input reading matter; a Python-level sliding window over every triple would be far slower for the same result.

## Solution

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        s = data[1 + i]
        # Either pattern marks a character differing from both neighbours.
        out.append("Good" if b"010" in s or b"101" in s else "Bad")
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Edge cases

- **The endpoints can never qualify.** `11111110` ends in a single $0$, but that $0$ has only one neighbour, so no character differs from *both* of its neighbours — hence `Bad`. Scanning for "a character unlike the one before it" would wrongly accept this.
- **Both patterns must be tested.** `0010` contains only `010` and `1101` only `101`, so checking one pattern misses half the valid strings.
- **$|S| \leq 2$**: there is no interior position at all, so the answer is always `Bad`.
- **Sum of lengths up to $6 \times 10^6$**: the substring search must be the library's C-level scan rather than a Python loop over indices, and the input is kept as bytes to avoid decoding six megabytes.

## Dry run

| $S$ | contains `010`? | contains `101`? | output |
|---|:---:|:---:|---|
| `11111110` | no | no | `Bad` |
| `10101010101010` | yes | yes | `Good` |

In the first string every character matches at least one neighbour; the trailing $0$ has no right neighbour to differ from.

---

Same problem grouped by topic: [../docs/strings/ERROR.md](../docs/strings/ERROR.md)
