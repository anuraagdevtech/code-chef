# 949 &middot; Rearranging digits to get a multiple of 5

> CodeChef problem code [`DIGARR`](https://www.codechef.com/problems/DIGARR) &middot; time limit **1s** &middot; 500 to 1000 difficulty rating (Level 1)

## Topics used

| | |
|---|---|
| **Topic** | Strings |
| **Technique** | Divisibility decided by one digit |
| **CodeChef tags** | `Data Structures`, `String` |
| **CodeChef category** | school |
| **Time** | $O(D)$ per test case |
| **Space** | $O(1)$ |

Same write-up grouped by topic: [../docs/strings/DIGARR.md](../docs/strings/DIGARR.md)

## Question

Given a positive integer $N$, MoEngage wants you to determine if it is possible to rearrange the digits of $N$ (in decimal representation) and obtain a [multiple](https://en.wikipedia.org/wiki/Multiple_(mathematics)) of $5$.

For example, when $N = 108$, we can rearrange its digits to construct $180 = 36 \cdot 5$ which is a multiple of $5$.

**Input**

- The first line contains an integer $T$, the number of test cases. The description of the $T$ test cases follow.
- Each test case consists of two lines
- The first line contains a single integer $D$, the number of digits in $N$.
- The second line consists of a string of length $D$, the number $N$ (in decimal representation). It is guaranteed that the string does not contain leading zeroes and consists only of the characters $0, 1, \dots 9$.

**Output**

- For each test case, print $\texttt{Yes}$ if it is possible to rearrange the digits of $N$ so that it becomes a multiple $5$. Otherwise, print $\texttt{No}$.

You may print each character of the string in uppercase or lowercase (for example, the strings $\texttt{YeS}$, $\texttt{yEs}$, $\texttt{yes}$ and $\texttt{YES}$ will all be treated as identical).

## Constraints

- $1 \leq T \leq 1000$
- $1 \leq D \leq 1000$
- $1 \leq N \lt 10^{1000}$
- Sum of $D$ over all test cases $\leq 1000$.

**Subtasks**

- 30 points : $1 \leq R \leq 10000$
- 70 points : $1 \leq R \leq 10^9$

## Sample

**Sample input**

```
3
3
115
3
103
3
119
```

**Sample output**

```
Yes
Yes
No
```

<details><summary>Explanation</summary>

**Test Case $1$:** The given number is already divisible by $5$, therefore the answer is $\texttt{Yes}$.

**Test Case 2:** We can obtain $310 = 62 \cdot 5$ by rearranging the digits of $103$, so the answer is $\texttt{Yes}$.

**Test Case 3:** The only numbers that can be obtained by rearranging the digits of $119$ are $\{119, 191, 911\}$. None of these numbers are multiples of $5$, so the answer is $\texttt{No}$.

</details>

## Approach

A number is divisible by $5$ exactly when its **last digit** is $0$ or $5$. Since the digits may be rearranged freely, the question becomes simply: does $N$ contain a $0$ or a $5$ anywhere?

If it does, move that digit to the end and the result is a multiple of $5$. If it does not, no arrangement can end in $0$ or $5$, so the answer is `No`.

So the whole solution is `"0" in s or "5" in s` — a scan of the digit string, with no arithmetic at all. That matters here: $D$ reaches $1000$, so $N$ can be up to $10^{1000}$, far beyond any fixed-width integer. Python could parse it as a big integer, but there is no need — treating the input as **text** is both simpler and faster, and is the right instinct whenever a problem's bounds are given as a digit count rather than a value.

One subtlety deserves a mention: a valid number should not have leading zeros. If the chosen digit to move is a $0$, something non-zero must remain to lead. That is always possible, because the input is guaranteed to have no leading zeros and $N \geq 1$, so at least one non-zero digit exists — and moving a single $0$ to the back leaves it available to lead. The example $108 \to 180$ is exactly this.

Sample case 2 ($103$) relies on the $0$; case 1 ($115$) on the $5$; case 3 ($119$) has neither and fails.

The $D$ given on its own line is redundant for Python, since the string carries its own length, but the token must still be consumed.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        # data[pos] is D, which Python does not need.
        s = data[pos + 1]
        pos += 2
        # Divisible by 5 iff some digit can be moved to the last position.
        out.append("Yes" if b"0" in s or b"5" in s else "No")
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(D)$ per test case
- **Space:** $O(1)$
