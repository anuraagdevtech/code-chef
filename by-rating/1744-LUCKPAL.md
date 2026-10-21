# 1744 &middot; Lucky Palin

> CodeChef problem code [`LUCKPAL`](https://www.codechef.com/problems/LUCKPAL) &middot; time limit **0.5s** &middot; 1600 to 1800 difficulty problems (Level 3)

## Topics used

| | |
|---|---|
| **Topic** | Strings |
| **Technique** | Placing a block and its mirror, costed in O(1) |
| **CodeChef tags** | `Data Structures`, `Special`, `Basic Programming Concepts`, `Algorithms`, `String`, `Case work`, `Loops`, `Conditional Statements`, `Greedy` |
| **CodeChef category** | easy |
| **Time** | $O(|S|)$ per test case for the cost scan, plus $O(|S|)$ per tied placement |
| **Space** | $O(|S|)$ |

Same write-up grouped by topic: [../docs/strings/LUCKPAL.md](../docs/strings/LUCKPAL.md)

## Question

Chef Palin, as his name suggests, is always very interested in palindromic strings. Recently, he made a pretty interesting discovery on palindromes and that made him feel really Lucky. He came across something known as Lucky Palindromes. He defines a string as being a lucky palindrome if it is a palindrome containing the string "lucky" as a substring. As always, now he wants to turn every string he comes across into a lucky palindrome. Being a chef, he is a man of patience and creativity, so he knows the operation of replacing any character of the string with any other character very well and he can perform this action infinitely many times. He wants you to write a program that can help him convert a given string to a lucky palindrome using the minimum number of operations and if several such lucky palindromes are possible, then output the lexicographically smallest one.

**Input**

The first line contains a single integer T <= 100 the number of testcases. The following T lines each contain a string of length <= 1000 and only containing characters 'a'-'z'.

**Output**

For each line of testcase, your program should output on a single line, the required lucky palindrome along with the minimum number of operations, both separated by a single space. If there is no lucky palindrome possible, then just output "unlucky" in a single line.

## Constraints

- $1 \leq T \leq 100$
- $1 \leq |S| \leq 1000$
- $S$ contains only the characters 'a'–'z'

## Sample

**Sample input**

```
3
laubcdkey
luckycodechef
aaaaaaaa
```

**Sample output**

```
luckykcul 8
luckycocykcul 6
unlucky
```

## Approach

The target is a palindrome of the same length containing `lucky`. Placing `lucky` at position $p$ forces, by the palindrome condition, its reverse `ykcul` at the mirrored position $q = |S| - p - 4$ (0-indexed $q = |S|-5-p$). So a placement is a **pair of forced blocks**, and it is only legal when they do not contradict each other.

Checking the overlaps settles which $p$ are legal. With the two blocks $\delta$ apart, the shared characters must agree; working through $\delta = 0, 1, 2, 3$ gives a clash every time (`lucky` against `ykcul`), while $\delta = 4$ agrees on the single shared letter (`y`, or `l` the other way round) and $\delta \geq 5$ is disjoint. So

$$\text{legal} \iff |p - q| \geq 4$$

which is empty exactly when $|S| < 9$ — hence `unlucky` for the sample's eight `a`s. The shortest lucky palindrome is `luckykcul`, of length $9$.

Everything outside the blocks splits into mirror pairs $(i, |S|-1-i)$, and those pairs are **the same for every placement**: a pair whose two characters already agree is kept as is at no cost, and a disagreeing pair costs one change and takes the smaller of the two letters, which is both cheapest and lexicographically best. An unforced centre keeps its own character.

That makes each placement's cost $O(1)$: ten character comparisons for the blocks, minus the double-counted shared position when $|p-q| = 4$, plus a prefix-sum lookup for the untouched mirror pairs. One pass finds the minimum cost; a second builds the string only for the tied placements and keeps the smallest.

`laubcdkey` ties at $8$ between `luckykcul` and `ykculucky`, and the lexicographic rule picks the former. `luckycodechef` costs $6$: the prefix `lucky` is free, the mirror `ykcul` costs $5$, and the pair $(\texttt{c}, \texttt{d})$ costs one more, resolving to `c`.

## Solution (Python)

```python
import sys

LUCKY = b"lucky"
YKCUL = b"ykcul"


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for s in data[1:1 + t]:
        n = len(s)
        half = n // 2
        # Cost of keeping each mirror pair as it is.
        mism = [0] * (half + 1)
        for i in range(half):
            mism[i + 1] = mism[i] + (s[i] != s[n - 1 - i])
        total_pairs = mism[half]

        best_cost = None
        winners = []
        for p in range(n - 4):
            q = n - 5 - p
            if abs(p - q) < 4:        # the two forced blocks would clash
                continue
            cost = sum(s[p + k] != LUCKY[k] for k in range(5))
            cost += sum(s[q + k] != YKCUL[k] for k in range(5))
            if abs(p - q) == 4:       # one position is forced by both blocks
                shared = max(p, q)
                cost -= s[shared] != LUCKY[shared - p]
            lo = min(p, q)
            top = min(lo + 4, half - 1)
            cost += total_pairs - (mism[top + 1] - mism[lo] if top >= lo else 0)
            if best_cost is None or cost < best_cost:
                best_cost, winners = cost, [p]
            elif cost == best_cost:
                winners.append(p)

        if best_cost is None:
            out.append("unlucky")
            continue
        answer = None
        for p in winners:
            q = n - 5 - p
            r = [None] * n
            for k in range(5):
                r[p + k] = LUCKY[k]
                r[q + k] = YKCUL[k]
            for i in range(half):
                if r[i] is None:
                    # Equal pair costs nothing; otherwise take the smaller letter.
                    r[i] = r[n - 1 - i] = min(s[i], s[n - 1 - i])
            if n % 2 and r[half] is None:
                r[half] = s[half]
            word = bytes(r).decode()
            if answer is None or word < answer:
                answer = word
        out.append(f"{answer} {best_cost}")
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(|S|)$ per test case for the cost scan, plus $O(|S|)$ per tied placement
- **Space:** $O(|S|)$
