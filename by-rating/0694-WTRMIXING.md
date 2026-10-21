# 694 &middot; Water Mixing

> CodeChef problem code [`WTRMIXING`](https://www.codechef.com/problems/WTRMIXING) &middot; time limit **1s** &middot; 500 to 1000 difficulty rating (Level 1)

## Topics used

| | |
|---|---|
| **Topic** | Conditionals & Case Work |
| **Technique** | Signed difference against one-sided supplies |
| **CodeChef tags** | `Mathematics`, `Basic Math` |
| **CodeChef category** | school |
| **Time** | $O(1)$ per test case |
| **Space** | $O(1)$ |

Same write-up grouped by topic: [../docs/conditionals-case-work/WTRMIXING.md](../docs/conditionals-case-work/WTRMIXING.md)

## Question

Chef is setting up a perfect bath for himself. He has $X$ litres of hot water and $Y$ litres of cold water.
The initial temperature of water in his bathtub is $A$ degrees. On mixing water, the temperature of the bathtub changes as following:

- The temperature rises by $1$ degree on mixing $1$ litre of hot water.
- The temperature drops by $1$ degree on mixing $1$ litre of cold water.

Determine whether he can set the temperature to $B$ degrees for a perfect bath.

**Input**

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of four space-separated integers $A, B, X,$ and $Y$ — the initial temperature of bathtub, the desired temperature of bathtub, the amount of hot water in litres, and the amount of cold water in litres respectively.

**Output**

For each test case, output on a new line, `YES` if Chef can get the desired temperature for his bath, and `NO` otherwise.

You may print each character of the string in uppercase or lowercase (for example, the strings `YES`, `yEs`, `yes`, and `yeS` will all be treated as identical).

## Constraints

- $1 \leq T \leq 2000$
- $20 \leq A, B \leq 40$
- $0 \leq X, Y \leq 20$

## Sample

**Sample input**

```
4
24 25 2 0
37 37 2 9
30 20 10 9
30 31 0 20
```

**Sample output**

```
YES
YES
NO
NO
```

<details><summary>Explanation</summary>

**Test case $1$:** The initial temperature of water is $24$ and the desired temperature is $25$. Chef has $2$ litres of hot water. He can add $1$ litre hot water in the tub and change the temperature to $24+1=25$ degrees.

**Test case $2$:** The initial temperature of water is $37$ and the desired temperature is also $37$. Thus, Chef does not need to add any more water in the bathtub.

**Test case $3$:** The initial temperature of water is $30$ and the desired temperature is $20$. Chef needs to add $10$ litres of cold water to reach the desired temperature. Since he only has $9$ litres of cold water, he cannot reach the desired temperature.

**Test case $4$:** The initial temperature of water is $30$ and the desired temperature is $31$. Chef needs to add $1$ litre of hot water to reach the desired temperature. Since he has no hot water, he cannot reach the desired temperature.

</details>

## Approach

Each litre of hot water raises the temperature by one degree and each litre of cold lowers it by one, so the reachable temperatures form the interval

$$[A - Y,\; A + X]$$

and the question is whether $B$ lies inside it.

The cleaner way to think about it is through the signed difference $d = B - A$, because its **sign** selects which supply is relevant:

- $d > 0$: the bath must warm up, needing $d$ litres of hot water, so the test is $d \leq X$. The cold supply is irrelevant.
- $d < 0$: it must cool, needing $|d|$ litres of cold, so the test is $|d| \leq Y$.
- $d = 0$: nothing to do, always `YES`.

The trap is treating the two supplies as interchangeable. They are not — hot water cannot cool a bath. Sample case 3 is exactly this: it needs to drop $10$ degrees and there are $10$ litres of *hot* water available but only $9$ of cold, so the answer is `NO` despite the totals looking sufficient. Sample case 4 is the mirror image, needing one degree of warming with no hot water at all.

The interval form `a - y <= b <= a + x` expresses the same rule in a single line without branching, and is the version used below.

Sample case 2 covers $d = 0$, where both supplies go unused.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        a, b, x, y = map(int, data[1 + 4 * i:5 + 4 * i])
        # Hot only warms and cold only cools: reachable range is [a - y, a + x].
        out.append("YES" if a - y <= b <= a + x else "NO")
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(1)$ per test case
- **Space:** $O(1)$
