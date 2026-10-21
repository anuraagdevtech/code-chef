# 199. Snake Procession

> [`SNAKPROC`](https://www.codechef.com/problems/SNAKPROC) &middot; difficulty **1290** &middot; time limit **1s** &middot; Level up from 1* to 2* (Level 2)

> _Edge cases and dry run for this problem are still to be written._

## Topic used

| | |
|---|---|
| **Topic** | Strings |
| **Technique** | Single-pass state machine |
| **Complexity class** | Linear $O(n)$ |
| **Time** | $O(L)$ per report |
| **Space** | $O(1)$ |

## Question

The annual snake festival is upon us, and all the snakes of the kingdom have gathered to participate in the procession. Chef has been tasked with reporting on the procession, and for this he decides to first keep track of all the snakes. When he sees a snake first, it'll be its Head, and hence he will mark a 'H'. The snakes are long, and when he sees the snake finally slither away, he'll mark a 'T' to denote its tail. In the time in between, when the snake is moving past him, or the time between one snake and the next snake, he marks with '.'s.

Because the snakes come in a procession, and one by one, a valid report would be something like "..H..T...HTH....T.", or "...", or "HT", whereas "T...H..H.T", "H..T..H", "H..H..T..T" would be invalid reports (See explanations at the bottom).

Formally, a snake is represented by a 'H' followed by some (possibly zero) '.'s, and then a 'T'. A valid report is one such that it begins with a (possibly zero length) string of '.'s, and then some (possibly zero) snakes between which there can be some '.'s, and then finally ends with some (possibly zero) '.'s.

Chef had binged on the festival food and had been very drowsy. So his report might be invalid. You need to help him find out if his report is valid or not.

**Input**
- The first line contains a single integer, $R$, which denotes the number of reports to be checked. The description of each report follows after this.
- The first line of each report contains a single integer, $L$, the length of that report.
- The second line of each report contains a string of length $L$. The string contains only the characters '.', 'H', and 'T'.

**Output**
- For each report, output the string **Valid** or **Invalid** in a new line, depending on whether it was a valid report or not.

**Constraints**
- $1 \le R \le 500$
- $1 \le L \le 500$

## Constraints

- $1 \le R \le 500$
- $1 \le L \le 500$

## Sample

**Sample input**

```
6
18
..H..T...HTH....T.
3
...
10
H..H..T..T
2
HT
11
.T...H..H.T
7
H..T..H
```

**Sample output**

```
Valid
Valid
Invalid
Valid
Invalid
Invalid
```

<details><summary>Explanation</summary>

- "H..H..T..T" is invalid because the second snake starts before the first snake ends, which is not allowed.

- ".T...H..H.T" is invalid because it has a 'T' before a 'H'. A tail can come only after its head.

- "H..T..H" is invalid because the last 'H' does not have a corresponding 'T'.

</details>

## Approach

Snakes pass one at a time, so at any moment the report is either *between* snakes or *inside* one. That is a two-state machine, and a single boolean tracks it.

Scanning left to right:

- `.` — always fine, in either state.
- `H` — a head. Valid only when **outside** a snake; seeing one while already inside means two overlapping snakes. Switches to inside.
- `T` — a tail. Valid only when **inside** a snake; seeing one while outside means a tail with no head. Switches to outside.

After the scan the state must be **outside**, or a snake was left unterminated.

All three failure modes appear in the samples, which is why the final check is as necessary as the in-loop ones:

- `H..H..T..T` — a head while already inside (case 3).
- `.T...H..H.T` — a tail before any head (case 5).
- `H..T..H` — ends inside, with a trailing head never closed (case 6).

A solution checking only that the counts of `H` and `T` match would accept the first and third of those, since `H..H..T..T` has two of each. Order and nesting are what the state machine captures.

The empty-ish case `...` is valid: zero snakes is allowed, and the state never leaves *outside*. Likewise `HT` is a snake of zero length between head and tail.

The given $L$ is redundant for Python, since the string carries its own length, but the token must still be consumed.

## Solution

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    r = int(data[0])
    pos = 1
    out = []
    for _ in range(r):
        # data[pos] is L, which Python does not need.
        s = data[pos + 1]
        pos += 2
        inside = False
        valid = True
        for ch in s:
            if ch == 72:          # 'H'
                if inside:
                    valid = False
                    break
                inside = True
            elif ch == 84:        # 'T'
                if not inside:
                    valid = False
                    break
                inside = False
        # A snake left open at the end is also invalid.
        out.append("Valid" if valid and not inside else "Invalid")
    sys.stdout.write("\n".join(out) + "\n")


main()
```

---

Same problem grouped by topic: [../docs/strings/SNAKPROC.md](../docs/strings/SNAKPROC.md)
