[&larr; 268. Gcd of Subarrays](GCDSUBARRAYS.md) &middot; [Index](../../README.md) &middot; [284. Prefix Permutation &rarr;](PREFPERM.md)

# 271. Palindrome Pain

> CodeChef problem code [`PALINPAIN`](https://www.codechef.com/problems/PALINPAIN) &middot; difficulty **1506** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Constructive |
| **Technique** | Counting distinct palindrome halves |
| **Time** | $O(X + Y)$ per test case |
| **Space** | $O(X + Y)$ |
| **Roadmap course** | 1400 to 1600 difficulty problems (Level 2) |

## Question

You are given two integers $X$ and $Y$. You need to construct two different strings $S_1$ and $S_2$ consisting of only the characters $‘a’$ and $‘b’$, such that the following conditions are satisfied:

1. Both $S_1$ and $S_2$ are [palindromes](https://en.wikipedia.org/wiki/Palindrome).
2. Both $S_1$ and $S_2$ should contain exactly $X$ occurrences of $\texttt{a}$ and $Y$ occurrences of $\texttt{b}$.

If there are multiple possible answers, you may print **any** of them. If it is not possible to construct two distinct strings satisfying the conditions, print $-1$ instead.

**Input**

- The first line of input will contain a single integer $T$, denoting the number of test cases. Then the test cases follow.
- Each test case consists of a single line of input containing two space-separated integers $X, Y$.

**Output**

For each test case:
- If it is not possible to construct two distinct strings satisfying the conditions, print $-1$
- Otherwise, print two lines — the first should contain the string $S_1$ and the second should contain $S_2$
- If there are multiple possible answers, you may print any of them.

## Constraints

- $1 \leq T \leq 1000$
- $1 \leq X,Y \leq 10^3$

## Sample

**Sample input**

```
2
2 4
3 3
```

**Sample output**

```
abbbba
babbab
-1
```

<details><summary>Explanation</summary>

**Test case $1$:** The three palindromes containing $2$ $\texttt{a}$-s and $4$ $\texttt{b}$-s are $\texttt{abbbba}, \texttt{babbab},$ and $\texttt{bbaabb}$. Printing any two of these is a valid answer.

**Test case $2$:** There are no palindromes containing $3$ each of $\texttt{a}$ and $\texttt{b}$.

</details>

## Approach

A palindrome is determined entirely by its **first half** (plus a middle character when the length is odd), since the second half is forced as the mirror image. So counting distinct palindromes with given letter counts means counting distinct halves.

Two conditions must hold.

**A palindrome must exist at all.** At most one letter count may be odd, so $X$ and $Y$ cannot both be odd — sample case 2, $X = Y = 3$, fails here and prints $-1$.

**Two *different* palindromes must exist.** The half contains $\lfloor X/2 \rfloor$ `a`s and $\lfloor Y/2 \rfloor$ `b`s, and there is more than one arrangement exactly when **both** are at least $1$ — that is, when $X \geq 2$ and $Y \geq 2$. With $X = 1$, say, every half is all `b`s and the palindrome is unique, so the answer is $-1$ even though a palindrome exists.

When both conditions hold, build two halves that differ: one with the `a`s first, and one starting with a `b` before the remaining letters. Each is completed by the middle character (`a` if $X$ is odd, `b` if $Y$ is odd, nothing if both are even) and the reversed half.

Sample case 1, $X=2, Y=4$: the half holds one `a` and two `b`s, so `abb` and `bab` are two distinct halves, giving `abbbba` and `babbab` — exactly the published answer, though **any** valid pair is accepted and this is judged by a checker.

Note that both counts being even is fine and both being odd is fatal; exactly one odd simply places that letter in the centre.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        x, y = int(data[1 + 2 * i]), int(data[2 + 2 * i])
        # Two odd counts admit no palindrome; fewer than two of either letter
        # admits only one.
        if (x % 2 and y % 2) or x < 2 or y < 2:
            out.append("-1")
            continue
        ha, hb = x // 2, y // 2
        middle = "a" if x % 2 else ("b" if y % 2 else "")
        h1 = "a" * ha + "b" * hb
        h2 = "b" + "a" * ha + "b" * (hb - 1)
        out.append(h1 + middle + h1[::-1])
        out.append(h2 + middle + h2[::-1])
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(X + Y)$ per test case
- **Space:** $O(X + Y)$

## Edge cases

- **Both counts odd → no palindrome at all.** A palindrome admits at most one character with an odd count, so $X$ and $Y$ both odd is hopeless — the second sample row, $3$ and $3$.
- **Fewer than two of either letter → only one palindrome exists.** With $X = 1$ and $Y = 4$ the lone `a` must sit at the centre and the `b`s are forced symmetric, giving `bbabb` and nothing else — so two *distinct* strings are impossible.
- **The second palindrome moves a `b` to the front of the half**, which changes the half and hence the whole string while preserving both letter counts: the half $a^{h_a} b^{h_b}$ becomes $b\,a^{h_a} b^{h_b - 1}$.
- **The two halves genuinely differ**, because the first starts with `a` (possible since $X \geq 2$ gives $h_a \geq 1$) and the second starts with `b`.
- **One odd count is fine** and that letter takes the centre position, which the `middle` string handles for either letter.
- **Both counts even** leaves the centre empty, as in the first sample row.
- **Two lines of output per solvable case**, one per string, and a single `-1` otherwise.

## Dry run

First sample: $X = 2$, $Y = 4$ — both even, both at least $2$.

| | half | centre | full palindrome |
|---|---|---|---|
| $S_1$ | `abb` | — | `abbbba` |
| $S_2$ | `bab` | — | `babbab` |

Each contains two `a`s and four `b`s, both read the same forwards and backwards, and they differ.

> CodeChef tags: `Data Structures`, `Algorithms`

---

Same problem in rating order (#299 of 486): [../../by-rating/299-PALINPAIN.md](../../by-rating/299-PALINPAIN.md)
