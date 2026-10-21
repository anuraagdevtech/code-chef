# 1566 &middot; Boring String

> CodeChef problem code [`BORSTR`](https://www.codechef.com/problems/BORSTR) &middot; time limit **1.5s** &middot; 1400 to 1600 difficulty problems (Level 2)

## Topics used

| | |
|---|---|
| **Topic** | Strings |
| **Technique** | Longest repeated run |
| **CodeChef tags** | `Data Structures`, `String` |
| **CodeChef category** | school |
| **Time** | $O(N)$ per test case |
| **Space** | $O(1)$ |

Same write-up grouped by topic: [../docs/strings/BORSTR.md](../docs/strings/BORSTR.md)

## Question

A string is called *boring* if all the characters of the string are **same**.

You are given a string $S$ of length $N$, consisting of lowercase english alphabets. Find the length of the longest *boring* substring of $S$ which occurs **more than once**.

Note that if there is no *boring* substring which occurs more than once in $S$, the answer will be $0$.

A substring is obtained by deleting some (possibly zero) elements from the beginning of the string and some (possibly zero) elements from the end of the string.

**Input**

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of two lines of input.
    - The first line of each test case contains an integer $N$, denoting the length of string $S$.
    - The next contains string $S$.

**Output**

For each test case, output on a new line, the length of the longest *boring* substring of $S$ which occurs **more than once**.

## Constraints

- $1 \leq T \leq 1000$
- $1 \lt N \leq 2\cdot 10^5$
- The sum of $N$ over all test cases won't exceed $5\cdot 10^5$.
- $S$ consists of lowercase english alphabets.

## Sample

**Sample input**

```
4
3
aaa
3
abc
5
bcaca
6
caabaa
```

**Sample output**

```
2
0
1
2
```

<details><summary>Explanation</summary>

**Test case $1$:** The length of the longest *boring* substring that occurs more than once is $2$. The *boring* substring of length $2$ occurring more than once is `aa`.

**Test case $2$:** There is no *boring* substring which occurs more than once. Thus, the answer is $0$.

**Test case $3$:** The length of the longest *boring* substring that occurs more than once is $1$. Some *boring* substrings of length $1$ occurring more than once are `c` and `a`.

**Test case $4$:** The length of the longest *boring* substring that occurs more than once is $2$. The *boring* substring of length $2$ occurring more than once is `aa`.

</details>

## Approach

A boring substring is a run of one repeated character, so for each letter only its **run lengths** matter.

Fix a letter with runs of lengths $r_1 \geq r_2 \geq \cdots$. A boring substring of that letter with length $m$ occurs $\max(0, r - m + 1)$ times inside a run of length $r$, and it must occur at least twice overall. There are exactly two ways to achieve that:

- **Twice inside the longest run**, which needs $r_1 - m + 1 \geq 2$, i.e. $m \leq r_1 - 1$;
- **Once in each of the two longest runs**, which needs $m \leq r_2$.

So the best length for that letter is $\max(r_1 - 1,\ r_2)$, and the answer is the maximum over all $26$ letters.

Both branches are genuinely needed. Sample case 1, `aaa`, has a single run of $3$: sliding a window of length $2$ gives two occurrences, so the answer is $2$ — the first branch. Sample case 4, `caabaa`, has two runs of `a` of length $2$ each: here $r_1 - 1 = 1$ but $r_2 = 2$, so the second branch wins with $2$.

Sample case 3, `bcaca`, has two runs of length $1$ for both `a` and `c`, giving $\max(0, 1) = 1$.

Sample case 2, `abc`, has every run at length $1$ with no repeats, so $\max(0, 0) = 0$ — the explicit "no answer" case.

Tracking only the two largest runs per letter keeps this to one pass and constant space, which matters at $\sum N = 5 \times 10^5$.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n = int(data[pos])
        s = data[pos + 1]
        pos += 2
        # Keep the two longest runs per letter; nothing else can matter.
        best1 = [0] * 26
        best2 = [0] * 26
        run_ch, run_len = -1, 0
        for ch in s + b"\x00":
            if ch == run_ch:
                run_len += 1
                continue
            if run_ch != -1:
                c = run_ch - 97
                if run_len > best1[c]:
                    best1[c], best2[c] = run_len, best1[c]
                elif run_len > best2[c]:
                    best2[c] = run_len
            run_ch, run_len = ch, 1
        # Twice inside the longest run, or once in each of the top two.
        out.append(str(max(max(b1 - 1, b2) for b1, b2 in zip(best1, best2))))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(N)$ per test case
- **Space:** $O(1)$
