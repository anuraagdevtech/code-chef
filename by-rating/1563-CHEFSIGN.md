# 1563 &middot; Chef and Sign Sequences

> CodeChef problem code [`CHEFSIGN`](https://www.codechef.com/problems/CHEFSIGN) &middot; time limit **2s** &middot; 1400 to 1600 difficulty problems (Level 2)

## Topics used

| | |
|---|---|
| **Topic** | Strings |
| **Technique** | Run lengths scanned from both directions |
| **CodeChef tags** | `Data Structures`, `Arrays`, `Groupings`, `String`, `Substring` |
| **CodeChef category** | easy |
| **Time** | $O(|s|)$ per test case |
| **Space** | $O(|s|)$ |

Same write-up grouped by topic: [../docs/strings/CHEFSIGN.md](../docs/strings/CHEFSIGN.md)

## Question

Chef found a strange string yesterday - a string of signs **s**, where each sign is either a **'<'**, **'='** or a **'>'**. Let N be the length of this string. Chef wants to insert N + 1 positive integers into this sequence and make it valid. A valid sequence is a sequence where every sign is preceded and followed by an integer, and the signs are correct. That is, if a sign '<' is preceded by the integer *a* and followed by an integer *b*, then *a* should be less than *b*. Likewise for the other two signs as well.

Chef can take some positive integers in the range **[1, P]** and use a number in the range as many times as he wants.

Help Chef find the minimum possible **P** with which he can create a valid sequence.

**Input**

The first line of the input contains an integer **T** denoting the number of test cases. The description of **T** test cases follows.

The only line of each test case contains the string of signs **s**, where each sign is either **'<'**, **'='** or a **'>'**.

**Output**

For each test case, output a single line containing an integer corresponding to the minimum possible **P**.

**Constraints**

- 1 ≤ **T, |s|** ≤ 10^5

- 1 ≤ Sum of **|s|** over all test cases in a single test file ≤ 106

**Subtasks**

**Subtask #1 (30 points)**

- 1 ≤ **T, |s|** ≤ 103

- 1 ≤ Sum of **|s|** over all test cases in a single test file ≤ 104

**Subtask #2 (70 points)**

- Original constraints

## Constraints

- 1 ≤ T, |s| ≤ 10^5
- 1 ≤ Sum of |s| over all test cases in a single test file ≤ 106

## Sample

**Sample input**

```
4
<<<
<><
<=>
<=<
```

**Sample output**

```
4
2
2
3
```

<details><summary>Explanation</summary>

Here are some possible valid sequences which can be formed with the minimum **P** for each of the test cases:

```
1 < 2 < 3 < 4
1 < 2 > 1 < 2
1 < 2 = 2 > 1
1 < 2 = 2 < 3
```

</details>

## Approach

Each of the $N+1$ slots needs a value large enough to satisfy the chain of `<` signs reaching it from the left and the chain of `>` signs reaching it from the right. Both are computed by a linear sweep.

**Left pass.** $L_0 = 1$, and for each $i$:
- $s_{i-1} =$ `<` → $L_i = L_{i-1} + 1$ (must exceed the previous value)
- $s_{i-1} =$ `=` → $L_i = L_{i-1}$ (must equal it)
- $s_{i-1} =$ `>` → $L_i = 1$ (free to restart at the minimum)

**Right pass** is the mirror image, with `>` driving the increase.

A slot must satisfy both constraints at once, so its value is $\max(L_i, R_i)$, and the answer is the largest such value over all slots.

Taking the maximum is what couples the two passes. A slot sitting at the bottom of a `>` run *and* the start of a `<` run is pinned by whichever run is longer — neither pass alone sees that.

The `=` case is the one most easily mishandled: it propagates the running value **unchanged** rather than resetting it, so a long `<<=<` chain keeps climbing across the equals sign. Sample case 4, `<=<`, gives left values $1, 2, 2, 3$ and answer $3$ — the `=` holds the value flat but does not break the chain, so the final `<` still has to climb past it.

Sample case 3, `<=>`, peaks at $2$ because the `<` and `>` runs each have length one and the `=` merely ties the two middle slots together.

Sample case 1, `<<<`, is a pure ascent needing $1,2,3,4$.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        s = data[1 + i]
        n = len(s)
        left = [1] * (n + 1)
        for j in range(1, n + 1):
            ch = s[j - 1]
            if ch == 60:        # '<'
                left[j] = left[j - 1] + 1
            elif ch == 61:      # '='  propagates, it does not reset
                left[j] = left[j - 1]
        right = [1] * (n + 1)
        for j in range(n - 1, -1, -1):
            ch = s[j]
            if ch == 62:        # '>'
                right[j] = right[j + 1] + 1
            elif ch == 61:
                right[j] = right[j + 1]
        # Each slot must satisfy both directions at once.
        out.append(str(max(max(a, b) for a, b in zip(left, right))))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(|s|)$ per test case
- **Space:** $O(|s|)$
