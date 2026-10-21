# 1180 &middot; Play Piano

> CodeChef problem code [`PLAYPIAN`](https://www.codechef.com/problems/PLAYPIAN) &middot; time limit **1s** &middot; 500 to 1000 difficulty rating (Level 1)

## Topics used

| | |
|---|---|
| **Topic** | Strings |
| **Technique** | Validating fixed-size blocks |
| **CodeChef tags** | `Algorithms`, `Constructive`, `ad-hoc` |
| **CodeChef top tag** | `Ad Hoc` |
| **CodeChef category** | school |
| **Time** | $O(|s|)$ per test case |
| **Space** | $O(1)$ |

Same write-up grouped by topic: [../docs/strings/PLAYPIAN.md](../docs/strings/PLAYPIAN.md)

## Question

Two sisters, A and B, play the piano every day. During the day, they can play in any order. That is, A might play first and then B, or it could be B first and then A. But each one of them plays the piano exactly once per day. They maintain a common log, in which they write their name whenever they play.

You are given the entries of the log, but you're not sure if it has been tampered with or not. Your task is to figure out whether these entries could be valid or not.

### Input
- The first line of the input contains an integer $T$ denoting the number of test cases. The description of the test cases follows.
- The first line of each test case contains a string $s$ denoting the entries of the log.

### Output
- For each test case, output `yes` or `no` according to the answer to the problem.

### Constraints
- $1 \le T \le 500$
- $2 \le |s| \le 100$
- $|s|$ is even
- Each character of $s$ is either 'A' or 'B'

## Constraints

- $1 \le T \le 500$
- $2 \le |s| \le 100$
- $|s|$ is even
- Each character of $s$ is either 'A' or 'B'

## Sample

**Sample input**

```
4
AB
ABBA
ABAABB
AA
```

**Sample output**

```
yes
yes
no
no
```

<details><summary>Explanation</summary>

**Testcase 1**: There is only one day, and both A and B have played exactly once. So this is a valid log. Hence 'yes'.

**Testcase 2**: On the first day, A has played before B, and on the second day, B has played first. Hence, this is also a valid log.

**Testcase 3**: On the first day, A played before B, but on the second day, A seems to have played twice. This cannot happen, and hence this is 'no'.

</details>

## Approach

Each day both sisters play exactly once, in either order. So a valid log is a concatenation of two-character blocks, each of which is `AB` or `BA` — equivalently, each block contains one of each letter.

That gives a simple test: walk the string two characters at a time and require the pair to **differ**.

$$s_{2i} \neq s_{2i+1} \quad\text{for every } i$$

The constraint that $|s|$ is even is what guarantees the string splits cleanly into whole days, so no partial block needs handling.

The trap is checking a global property instead of the per-day one. Counting letters and requiring equal numbers of `A` and `B` is *necessary* but not *sufficient* — sample case 3, `ABAABB`, has three of each yet is invalid, because its second day reads `AA` and its third `BB`. Only the block-local check catches it.

Sample case 2, `ABBA`, shows that the order within a day may vary freely: `AB` then `BA` is perfectly legal, so the sisters need not alternate across days.

Sample case 4, `AA`, is the minimal failure — a single day with the same sister twice.

In Python this reads cleanly as `all(s[i] != s[i+1] for i in range(0, len(s), 2))`, which short-circuits on the first bad day.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        s = data[1 + i]
        # Each day is one block of two and must hold one of each sister.
        ok = all(s[j] != s[j + 1] for j in range(0, len(s), 2))
        out.append("yes" if ok else "no")
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(|s|)$ per test case
- **Space:** $O(1)$
