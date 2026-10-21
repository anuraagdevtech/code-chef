# 189. Chef and the Wildcard Matching

> [`TWOSTR`](https://www.codechef.com/problems/TWOSTR) &middot; difficulty **1254** &middot; time limit **1s** &middot; Level up from 1* to 2* (Level 2)

## Topic used

| | |
|---|---|
| **Topic** | Strings |
| **Technique** | Wildcard matching, position by position |
| **Complexity class** | Linear $O(n)$ |
| **Time** | $O(|X|)$ per test case |
| **Space** | $O(1)$ |

## Question

Chef wants to implement wildcard pattern matching supporting only the wildcard '?'. The wildcard character '?' can be substituted by any single lower case English letter for matching. He has two strings **X** and **Y** of equal length, made up of lower case letters and the character '?'. He wants to know whether the strings **X** and **Y** can be matched or not.

**Input**

The first line of input contain an integer **T** denoting the number of test cases. Each test case consists of two lines, the first line contains the string **X** and the second contains the string **Y**.

**Output**

For each test case, output a single line with the word **Yes** if the strings can be matched, otherwise output **No**.

**Constraints**

- **1** ≤ **T** ≤ **50**

- Both **X** and **Y** have equal length and the length is between 1 and 10.

- Both **X** and **Y** consist of lower case letters and the character '?'.

## Constraints

- 1 ≤ T ≤ 50
- Both X and Y have equal length and the length is between 1 and 10.
- Both X and Y consist of lower case letters and the character '?'.

## Sample

**Sample input**

```
2
s?or?
sco??
stor?
sco??
```

**Sample output**

```
Yes
No
```

<details><summary>Explanation</summary>

**Test case $1$:** One of the possible ways to match both the strings is $\texttt{score}$. This can be done by:
- Replace $1^{st}$ and $2^{nd}$ $\texttt{?}$ of string $X$ by characters $\texttt{c}$ and $\texttt{e}$ respectively.
- Replace $1^{st}$ and $2^{nd}$ $\texttt{?}$ of string $Y$ by characters $\texttt{r}$ and $\texttt{e}$ respectively.

**Test case $2$:** There exists no way to fill the $\texttt{?}$ such that the strings become equal. Thus, the answer is `No`.

</details>

## Approach

The strings are the same length and `?` stands for any single lowercase letter. Because the wildcard matches exactly one character — never zero, never many — the comparison stays **positional**: index $i$ of $X$ is matched against index $i$ of $Y$, with no alignment to work out.

Position $i$ matches when

$$X_i = \texttt{?} \quad\text{or}\quad Y_i = \texttt{?} \quad\text{or}\quad X_i = Y_i$$

and the strings match when every position does — `all(...)` over `zip(x, y)`.

The detail easy to miss is that **both** strings may contain wildcards, not just one. A `?` in either position is enough, so the test is symmetric. Sample case 1 relies on it: `s?or?` against `sco??` matches at index $1$ because $X$ has the wildcard, and at index $4$ because *both* do.

Sample case 2 fails at index $1$, where `t` meets `c` — two concrete and different letters, which no wildcard can reconcile.

It is worth noting what makes this far simpler than general wildcard matching. The `*` wildcard, which matches any *number* of characters, breaks the positional correspondence and needs dynamic programming or a two-pointer algorithm with backtracking. With only `?` and equal lengths, a single linear scan suffices.

Strictly, two `?`s matching each other means some letter could fill both — true, since any letter works. So the symmetric rule is correct, not merely convenient.

## Solution

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        x = data[1 + 2 * i].decode()
        y = data[2 + 2 * i].decode()
        # '?' matches exactly one character, and may appear in either string.
        ok = all(a == "?" or b == "?" or a == b for a, b in zip(x, y))
        out.append("Yes" if ok else "No")
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Edge cases

- **A `?` in either string matches**, so the test is a three-way disjunction rather than substituting one string's wildcards into the other.
- **Both strings may hold `?` in the same position** — the final column of the first sample row — and that still matches, since any single letter satisfies both.
- **Equal lengths are guaranteed**, so `zip` never silently truncates a longer string.
- **One mismatched letter fails the pair.** The second row differs only at index $1$ (`t` against `c`) and every other column matches.
- **Length can be $1$**, giving a single column to compare.
- Only lowercase letters and `?` appear, so no case folding is needed.

## Dry run

| index | X | Y | verdict |
|---:|---|---|---|
| 0 | `s` | `s` | equal |
| 1 | `?` | `c` | wildcard in X |
| 2 | `o` | `o` | equal |
| 3 | `r` | `?` | wildcard in Y |
| 4 | `?` | `?` | wildcard in both |

All five columns pass, so `s?or?` against `sco??` is `Yes`. Replacing index $1$ with a literal `t` fails immediately against `c`, giving the second row's `No`.

---

Same problem grouped by topic: [../docs/strings/TWOSTR.md](../docs/strings/TWOSTR.md)
