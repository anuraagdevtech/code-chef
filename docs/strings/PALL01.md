[&larr; 92. Wordle](WORDLE.md) &middot; [Index](../../README.md) &middot; [105. Is it a VOWEL or CONSONANT &rarr;](VOWELTB.md)

# 99. The Block Game

> CodeChef problem code [`PALL01`](https://www.codechef.com/problems/PALL01) &middot; difficulty **720** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Strings |
| **Technique** | Palindrome check by reversal |
| **Time** | $O(d)$ per test case, $d$ = number of digits |
| **Space** | $O(d)$ |
| **Roadmap course** | 500 to 1000 difficulty rating (Level 1) |

## Question

The citizens of Byteland regularly play a game. They have blocks each denoting some integer from 0 to 9. These are arranged together in a random manner without seeing to form different numbers keeping in mind that the first block is never a 0. Once they form a number they read in the reverse order to check if the number and its reverse is the same. If both are same then the player wins. We call such numbers *palindrome*.

Ash happens to see this game and wants to simulate the same in the computer. As the first step he wants to take an input from the user and check if the number is a palindrome and declare if the user wins or not. 

**Input**

The first line of the input contains T, the number of test cases. This is followed by T lines containing an integer N.

**Output**

For each input output "wins" if the number is a palindrome and "loses" if not, in a new line.

**Constraints**

1<=T<=20

1<=N<=20000

## Constraints

- $1 \leq T \leq 20$
- $1 \leq N \leq 20000$

## Sample

**Sample input**

```
3
331
666
343
```

**Sample output**

```
loses
wins
wins
```

## Approach

A number is a palindrome when it reads the same forwards and backwards. In Python the cleanest test converts to a string and compares against its reverse:

```python
s == s[::-1]
```

The slice `[::-1]` walks the string with step $-1$, producing the reversal, and the comparison is a single pass. For $N \leq 20000$ that is at most five characters.

The alternative avoids strings by reversing arithmetically — peel digits with `n % 10` and rebuild with `rev = rev * 10 + digit` — then compare `rev == n`. It is the version to use in a language without cheap string conversion, and it is the same routine as the Reverse The Number problem. Note the crucial difference between the two problems though: there, reversing `2300` had to yield `32` with leading zeros dropped; here, `n` has no leading zeros to begin with, so the two approaches agree.

A common misstep is to compare only half the string, or to use a two-pointer loop with an off-by-one in the midpoint. The slice sidesteps both; a middle character in an odd-length number compares against itself and is always equal, so no special case is needed.

Output is lowercase `wins` for a palindrome and `loses` otherwise — note that the winning case is the palindrome, which is easy to invert when skimming.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        s = data[1 + i]
        out.append("wins" if s == s[::-1] else "loses")
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(d)$ per test case, $d$ = number of digits
- **Space:** $O(d)$

## Edge cases

- **A single digit** ($N \leq 9$): trivially a palindrome, so `wins`.
- **Even length** ($N = 1221$): a palindrome with no middle digit, so the check must not assume an odd length.
- **A trailing zero** ($N = 100$): reversing gives `001`, which differs from `100`, so `loses`. Comparing the *strings* is what makes this right — the reversal has to preserve length.
- **Largest input** ($N = 20000$): five digits, `02002` reversed, so `loses`.
- Reversing the digit string is simpler and safer than rebuilding the number arithmetically, and at $N \leq 20000$ there is no performance reason to prefer the latter.

## Dry run

| $N$ | digits reversed | equal? | output |
|---:|---|:---:|---|
| 331 | `133` | no | `loses` |
| 666 | `666` | yes | `wins` |
| 343 | `343` | yes | `wins` |

> CodeChef tags: `Data Structures`, `Mathematics`, `Algorithms`

---

Same problem in rating order (#72 of 486): [../../by-rating/072-PALL01.md](../../by-rating/072-PALL01.md)
