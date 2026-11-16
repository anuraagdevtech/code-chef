[&larr; 562. Girl Friend and String Gift](562-CHGLSTGT.md) &middot; [Index](README.md) &middot; [564. The Uncountable Ways &rarr;](564-CNTWAYS.md)

# 563. Sereja and Commands

> [`SEACO`](https://www.codechef.com/problems/SEACO) &middot; difficulty **1990** &middot; time limit **1s** &middot; Rise from 3* to 4* (Level 4)

## Topic used

| | |
|---|---|
| **Topic** | Prefix Sums |
| **Technique** | Reverse sweep over commands with two difference arrays |
| **Complexity class** | Linear $O(n)$ |
| **Time** | $O(N + M)$ per test case |
| **Space** | $O(N + M)$ |

## Question

Sereja has an array **A** consisting of **n** integers. Initially, all the elements of array are zero.

Sereja writes down **m** commands on a piece of a paper. The commands are enumerated from **1** to **m**. These commands can be of the following two types of commands:

-  **l r (1 ≤ l ≤ r ≤ n)** — Increase all elements of the array by one, whose indices belongs to the range **[l, r]**

-  **l r (1 ≤ l ≤ r ≤ m)** — Execute all the commands whose indices are in the range **[l, r]**. It's guaranteed that **r** is strictly less than the enumeration/number of the current command.

Can you please help Sereja in executing all the commands written on this piece of paper.

**Input**

The first line of the input contains an integer **T** denoting the number of test cases. The description of **T** test cases follows.

The first line contains integers **n** and **m**. Next **m** lines contain Sereja's commands in the format, described in statement: **t**, **l**, **r**, where **t** - number of type (1 or 2).

**Output**

For each test case on different lines print an array **a**, after executing all the commands. The numbers have to be separated by spaces. As the numbers can be quite large, print them modulo **10^9 + 7**.

**Constraints**

- **1** ≤ **T** ≤ **3**

- **1** ≤ **n, m** ≤ **10^5**

**Subtasks**

- Subtask #**1** (20 points): 1 ≤ **n, m** ≤ 10

- Subtask #**2** (30 points): 1 ≤ **n, m** ≤ 1000

- Subtask #**3** (50 points): original constraints

## Constraints

- 1 ≤ T ≤ 3
- 1 ≤ n, m ≤ 10^5

## Sample

**Sample input**

```
3
5 5
1 1 2
1 4 5
2 1 2
2 1 3
2 3 4
1 2
1 1 1
1 1 1
10 10
1 1 10
2 1 1
2 1 2
2 1 3
2 1 4
2 1 5
2 1 6
2 1 7
2 1 8
2 1 9
```

**Sample output**

```
7 7 0 7 7
2
512 512 512 512 512 512 512 512 512 512
```

<details><summary>Explanation</summary>

**Example case 1.**.

After the first command, the resulting array is [1 1 0 0 0], after second [1 1 0 1 1].

On third command, we repeat the 1'st and the 2'nd command, so that resulting array is [2 2 0 2 2].

After fourth command, the array will looks like [4 4 0 4 4].

Last command will apply 3'rd and 4'th commands,
which by themselves will apply 1'st, 2'nd, 1'st, 2'nd, 3'rd(1'st, 2'nd), so resulting arrays is [7 7 0 7 7].

</details>

## Approach

A type-2 command can only refer to earlier commands, so how many times a command is executed depends only on later commands. Process the commands from last to first.

Let `count[i]` be the total number of executions of command $i$: one for itself plus one for every execution of a later type-2 command whose range contains $i$. Maintain those extra executions with a difference array over command indices; because we move right to left, an update for range $[l, r]$ is "add at $r$, cancel below $l$", and the running sum at $i$ is the pending extra count.

When command $i$ is of type 2, push `count[i]` onto its command range. When it is of type 1, add `count[i]` to the array range $[l, r]$ through a second, ordinary difference array. A final prefix sum produces the array. Everything is modulo $10^9 + 7$.

## Solution

```python
import sys


def main() -> None:
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    out = []
    MOD = 1000000007
    for _ in range(next(tokens)):
        n, m = (next(tokens), next(tokens))
        commands = [(next(tokens), next(tokens) - 1, next(tokens) - 1) for _ in range(m)]
        delta = [0] * (m + 1)
        diff = [0] * (n + 1)
        extra = 0
        for i in range(m - 1, -1, -1):
            extra = (extra + delta[i]) % MOD
            count = extra + 1
            kind, left, right = commands[i]
            if kind == 2:
                delta[right] = (delta[right] + count) % MOD
                delta[left - 1 if left else m] = (delta[left - 1 if left else m] - count) % MOD
            else:
                diff[left] += count
                diff[right + 1] -= count
        total = 0
        row = []
        for x in diff[:n]:
            total = (total + x) % MOD
            row.append(str(total))
        out.append(' '.join(row))
    print('\n'.join(out))


if __name__ == "__main__":
    main()
```

## Edge cases

- The counts grow exponentially (the third sample doubles nine times), so they must be reduced modulo $10^9 + 7$.
- A type-2 range starting at command 1 has no "below $l$" slot; a spare cell absorbs the cancellation.
- Type-2 commands only reference earlier indices, so the reverse order always has the final count ready.
- The subtraction in the difference array needs a non-negative modular result.

## Dry run

Sample 1, commands: (1) add `[1,2]`, (2) add `[4,5]`, (3) run 1-2, (4) run 1-3, (5) run 3-4.

Backwards: command 5 runs once and gives +1 to commands 3 and 4. Command 4 runs $1 + 1 = 2$ times and gives +2 to commands 1-3. Command 3 runs $1 + 1 + 2 = 4$ times and gives +4 to commands 1 and 2. Commands 2 and 1 therefore run $1 + 2 + 4 = 7$ times each.

Array: `7 7 0 7 7`.

---

Same problem grouped by topic: [../docs/prefix-sums/SEACO.md](../docs/prefix-sums/SEACO.md)
