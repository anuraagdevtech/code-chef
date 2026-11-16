[&larr; 514. Prime Game](514-PRIGAME.md) &middot; [Index](README.md) &middot; [516. The Great Wall of Byteland &rarr;](516-BWALL.md)

# 515. String Reverse

> [`STR_REVERSE`](https://www.codechef.com/problems/STR_REVERSE) &middot; difficulty **1792** &middot; time limit **5s** &middot; 1600 to 1800 difficulty problems (Level 3)

## Topic used

| | |
|---|---|
| **Topic** | Strings |
| **Technique** | Keep the longest target prefix that is already a subsequence |
| **CodeChef tags** | `Data Structures`, `Algorithms`, `String`, `Greedy` |
| **Complexity class** | Linear $O(n)$ |
| **Time** | $O(|S|)$ per test case |
| **Space** | $O(1)$ auxiliary |

## Question

Chef has a string $S$ consisting only of English lowercase letters (`a` - `z`). However, Hitesh does not like it and wants it to be reversed.

Hitesh wonders what is the minimum number of operations required to reverse the string $S$ using the following operation:
- Select any $i$ such that $1 \le i \le \lvert S \rvert$ and remove $S_i$ from its original position and append it to the end of the string (i.e. shift any character to the end of the string).

For e.g. if $S =$ `abcde` and we apply operation on $i = 2$, then $S$ becomes `acdeb`.

Help Hitesh find the minimum number of operations required to reverse $S$.

It is guaranteed that it is possible to reverse the string in a finite number of operations.

**Input**

-   The first line of input contains a single integer  $T$, denoting the number of test cases. The description of  $T$  test cases follows.
-   Each test case consists of a single line containing the string S.

**Output**

For each test case, output the minimum number of operations required to reverse the string $S$.

## Constraints

- $1 \leq T \leq 10^3$
- $1  \leq \lvert S \rvert \leq 10^5$
- Sum of $\lvert S \rvert$ over all testcases does not exceed $2 \cdot 10^5$.

## Sample

**Sample input**

```
2
abdeba
codechef
```

**Sample output**

```
3
7
```

<details><summary>Explanation</summary>

- **Test case-1:** Following steps can be performed:
1.  $abdeba \to  abebad$
2.  $abebad \to abeadb$
3.  $abeadb \to  abedba$
- **Test case-2:** following steps can be performed:
1.  $codechef \to  codechfe$
2.  $codechfe \to codecfeh$
3.  $codecfeh \to codefehc$
4.  $codefehc \to  codfehce$
5.  $codfehce \to cofehced$
6.  $cofehced \to cfehcedo$
7.  $cfehcedo \to fehcedoc$

</details>

## Approach

Characters never moved keep their relative order and appear before all moved characters. Thus they must form a prefix of the target reversal. Conversely, keep any subsequence matching a target prefix and move all other characters to the end in target-suffix order.

Greedily match as much of the reversed target as a subsequence of the original string as possible. If $k$ characters are kept, exactly $|S|-k$ operations are necessary and sufficient. Access the reversed target by index without allocating another string.

## Solution

```python
import sys


def main() -> None:
    tokens = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(tokens))):
        s = next(tokens)
        n = len(s)
        matched = 0
        for char in s:
            if matched < n and char == s[n-1-matched]:
                matched += 1
        out.append(str(n-matched))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
```

## Edge cases

- A palindrome needs no moves.
- Repeated characters are matched greedily by position.
- A one-character string returns zero.

## Dry run

For `abdeba`, the target is `abedba`. The original string can keep target prefix `abe` as a subsequence, length three, so three moves suffice.

---

Same problem grouped by topic: [../docs/strings/STR_REVERSE.md](../docs/strings/STR_REVERSE.md)
