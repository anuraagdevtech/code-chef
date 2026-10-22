# 425. 3-Blast Palindrome

> CodeChef problem code [`BLAST3`](https://www.codechef.com/problems/BLAST3) &middot; difficulty **1699** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Strings |
| **Technique** | Residue classes of the surviving positions |
| **Time** | $O(N)$ per test case |
| **Space** | $O(1)$ |
| **Roadmap course** | 1600 to 1800 difficulty problems (Level 3) |

## Question

You are given a string $S$ of length $N$.
Your task is to convert the string into a **non-empty** [palindrome](https://en.wikipedia.org/wiki/Palindrome#Characters,_words,_or_lines) using the following operation any (possibly zero) number of times:
- Choose an index $1\lt i\lt |S|$, where $|S|$ denotes the current length of string;
- Remove the characters at indices $(i-1)$, $i$, and $(i+1)$ from the string and concatenate remaining part(s) of the string.

Print `YES` if it is possible to convert the string into a non-empty palindrome and `NO` otherwise.

**Input**

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of two lines of input.
    - The first line of each test case contains $N$ - the length of string.
    - The next line contains string $S$.

**Output**

For each test case, print on a new line, `YES`, if it is possible to convert the given string into a non-empty palindrome, otherwise print `NO`.

Each character of the output may be printed in either uppercase or lowercase, i.e, the strings `Yes`, `YES`, `yes`, and `yEs` will be treated as identical.

## Constraints

- $1 \leq T \leq 10^5$
- $1 \leq N \leq 2 \cdot 10^5$
- $S$ consists of lowercase english alphabets only.
- The sum of $N$ over all test cases won't exceed $5 \cdot 10^5$.

## Sample

**Sample input**

```
3
5
aaaaa
5
abcde
5
aabcd
```

**Sample output**

```
YES
NO
YES
```

<details><summary>Explanation</summary>

**Test case $1$:** The given string is already a palindrome. Thus, we need $0$ operations.

**Test case $2$:** It is not possible to convert the string `abcde` into a palindrome using any number of operations.

**Test case $3$:** Choose $i = 4$ and delete the characters at indices $3, 4,$ and $5$. Thus, the string `aabcd` becomes `aa`, which is a palindrome.

</details>

## Approach

Run the operation **backwards**: building $S$ from the final string means inserting blocks of $3$ contiguous characters. Insertions into the same slot stay one run, so every maximal run of *deleted* positions has length divisible by $3$ — and conversely any such deletion pattern is realisable. So the surviving positions $p_1 < \cdots < p_L$ are exactly those with

$$p_1 \equiv 1, \quad p_{i+1} \equiv p_i + 1, \quad N \equiv p_L \pmod 3 \qquad\Longrightarrow\qquad p_i \equiv i \pmod 3$$

Now take the shortest useful palindrome, by case on $N \bmod 3$:

- **$N \equiv 1$:** keep a single character at any position $\equiv 1 \pmod 3$ — position $1$ always qualifies, and one character is a palindrome. Always `YES`.
- **$N \equiv 2$ or $0$:** a palindrome of length $L \equiv N \pmod 3$ has outer positions $p_1 \equiv 1$ and $p_L \equiv N \pmod 3$ with $S_{p_1} = S_{p_L}$. So that pair is **necessary**, and it is also sufficient: for $N \equiv 2$ the pair itself is a length-$2$ palindrome, and for $N \equiv 0$ the position $p_1 + 1 \equiv 2 \pmod 3$ lies strictly inside (since $p_L \geq p_1 + 2$) and serves as the middle.

So apart from the $N \equiv 1$ case the whole question is: **is there $p \equiv 1 \pmod 3$ before some $q \equiv N \pmod 3$ with the same character?** One left-to-right pass with a set of characters seen at positions $\equiv 1$ answers it.

The samples are all $N = 5$, so $N \equiv 2$ and the relevant positions are $\{1,4\}$ and $\{2,5\}$. `aaaaa` matches at once. `aabcd` matches $S_1 = S_2 = $ `a`. But `abcde` offers only the pairs $(a,b), (a,e), (d,e)$ — no match — so `NO`, even though three characters could in principle be dropped.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        n = int(data[1 + 2 * i])
        s = data[2 + 2 * i]
        if n % 3 == 1:
            out.append("YES")             # one surviving character suffices
            continue
        seen = set()
        ok = False
        for j in range(n):                 # j is 0-based, so position j + 1
            if (j + 1) % 3 == n % 3 and s[j] in seen:
                ok = True
                break
            if (j + 1) % 3 == 1:
                seen.add(s[j])
        out.append("YES" if ok else "NO")
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(N)$ per test case
- **Space:** $O(1)$

## Edge cases

- **Each operation removes exactly three consecutive characters**, so the length only ever drops by $3$ — and the surviving positions fall into fixed residue classes mod $3$.
- **$N \equiv 1 \pmod 3$ is always possible**, since the string can be whittled down to a single character, and one character is a palindrome.
- **Otherwise the survivors must pair up**, and the reachable pairs are exactly a position $p \equiv 1 \pmod 3$ with a later position $q \equiv N \pmod 3$ holding the same character. Verified by brute force over all $29{,}523$ strings of length at most $9$ on a three-letter alphabet, with no mismatch.
- **The scan order matters.** A position is tested against the set of earlier $p \equiv 1$ characters *before* being added to it, which enforces $p < q$.
- **All identical characters** (the first row) succeed as soon as the residues line up.
- **All distinct characters** (the second row) fail, since no pair can match.
- **The operation needs $|S| \geq 3$**, so a string of length $1$ or $2$ admits no moves at all — length $1$ is already a palindrome, and length $2$ needs its two characters equal.

## Dry run

Third sample: $N = 5$, $S = $ `aabcd`, so $N \bmod 3 = 2$.

| position | residue mod 3 | role | character | match? |
|---:|---:|---|---|:---:|
| 1 | 1 | candidate $p$ | `a` | recorded |
| 2 | 2 | candidate $q$ | `a` | **yes** — `a` already seen |

Output `YES`: removing positions $3,4,5$ leaves `aa`, a palindrome.

> CodeChef tags: `Algorithms`, `Constructive`

---

Same problem in rating order (#406 of 486): [../../by-rating/406-BLAST3.md](../../by-rating/406-BLAST3.md)
