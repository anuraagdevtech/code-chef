# 332. List of Lists

> [`LISTLIST`](https://www.codechef.com/problems/LISTLIST) &middot; difficulty **1567** &middot; time limit **1s** &middot; Jump from 2* to 3* (Level 3)

## Topic used

| | |
|---|---|
| **Topic** | Greedy |
| **Technique** | Counting how many singletons can survive |
| **Complexity class** | Linear $O(n)$ |
| **Time** | $O(N)$ per test case |
| **Space** | $O(N)$ |

## Question

You are given a positive integer $N$ and an array $A$ of size $N$. There are $N$ lists $L_1, L_2 \ldots L_N$. Initially, $L_i = [A_i]$.

You can perform the following operation any number of times as long as there are at least $2$ lists:

- Select $2$ (non-empty) lists $L_i$ and $L_j$ ($i \neq j$)
- Append $L_j$ to $L_i$ and remove the list $L_j$. Note that this means $L_j$ cannot be chosen in any future operation.

Find the minimum number of operations required to obtain a set of lists that satisfies the following conditions:

- The first element and last element of each list are equal.
- The first element of all the lists is the same.

Print $-1$ if it is not possible to achieve this via any sequence of operations.

**Input**

- The first line of input contains a single integer $T$, denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains an integer $N$.
- The second line of each test case contains $N$ space-separated integers $A_1, A_2, \ldots, A_N$.

**Output**

For each test case, print a single line containing one integer: the minimum number of operations required to obtain an array of lists that satisfies the given conditions.

Print $-1$ if it is impossible to achieve such an array of lists.

## Constraints

- $1 \leq T \leq 10^5$
- $1 \leq N \leq 2 \cdot 10^5$
- $1 \leq A_i \leq N$
- Sum of $N$ over all test cases doesn't exceed $2 \cdot 10^5$

**Subtasks**

**Subtask 1(100 points):** Original constraints

## Sample

**Sample input**

```
3
1
1
2
1 2
3
1 1 2
```

**Sample output**

```
0
-1
2
```

<details><summary>Explanation</summary>

**Test case $1$:** There is only one list $[1]$, and it trivially satisfies the condition so no operations are required.

**Test case $2$:** There are only $2$ ways to do an operation - either take list $[1]$ and append it to list $[2]$ or take list $[2]$ and append it to list $[1]$. In both cases, it is not possible to satisfy both given conditions at the same time. Hence, the answer is $-1$.

**Test case $3$:** Here is one possible order of operations:
- Select the $3$rd list $[2]$ and append it to the $1$st list $[1]$.
- Then, select the $2$nd list $[1]$ and append it to the $1$st list $[1, 2]$.

Finally, we are left with the single list $[1, 2, 1]$ which satisfies the given conditions. It can be verified that it is impossible to do this using less than $2$ operations.

</details>

## Approach

Appending keeps a list's **first** element and takes its **last** from whatever was appended, so every final list begins and ends with the common value $v$. Each merge reduces the number of lists by exactly one, so starting from $N$ lists and finishing with $f$ costs $N - f$ operations — minimising work means **maximising the number of final lists**.

Now count how $v$ is spent. A final list of length $1$ is just $[v]$ and uses one copy; a final list of length $\geq 2$ uses two, one at each end, and can hold any number of other values in its middle. So if $v$ occurs $c$ times and the other $N - c$ values are non-zero in number, they must all be buried inside lists, and one such list suffices:

$$f_{\max} = 1 + (c - 2) = c - 1$$

Adding a second non-singleton list would consume two more copies of $v$ to gain one list, a net loss — which is why one container is optimal rather than merely sufficient. So the cost is $N - c + 1$, minimised by choosing $v$ to be the **most frequent** value.

Two boundary cases fall outside that formula. If every element already equals $v$, each is already a valid list and the answer is $0$. And if the top frequency is $1$ while some other value exists, no container can be closed at both ends, so the answer is $-1$.

The samples are exactly these three cases: a single element needs nothing; $[1,2]$ has no repeated value to wrap the other, giving $-1$; and $[1,1,2]$ buries the $2$ between the two $1$s, which is $2$ merges into the single list $[1,2,1]$.

## Solution

```python
import sys
from collections import Counter


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n = int(data[pos])
        top = max(Counter(data[pos + 1:pos + 1 + n]).values())
        pos += 1 + n
        if top == n:
            out.append("0")          # every element is already a valid list
        elif top >= 2:
            # One list buries all the other values; the rest stay singletons.
            out.append(str(n - top + 1))
        else:
            out.append("-1")
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Edge cases

- **The two conditions pull in opposite directions.** Every list must start and end with the same value, *and* all lists must start with the same value — so one value $v$ is chosen, every list begins and ends with $v$, and everything else must be buried in the middle of some list.
- **That needs two copies of $v$**, one at each end of the list holding the foreign elements. So a value appearing only once can never serve, and an array of all-distinct values is impossible: `-1`.
- **All elements equal** → $0$ operations, since each singleton already starts and ends with the same value and they all agree.
- **The count $n - \text{top} + 1$** builds one list of $n - \text{top} + 2$ elements (a $v$, the $n - \text{top}$ others, another $v$), costing one merge fewer than its length, and leaves the remaining $\text{top} - 2$ copies as singletons.
- **Using fewer merges fails** even when the lists look plausible. For $[1,1,2]$, merging the two $1$s gives $[1,1]$ and $[2]$, whose first elements disagree — so the answer is $2$ and not $1$.
- **Only the most frequent value matters**, so a single `Counter` maximum decides everything.

## Dry run

Third sample: $A = 1, 1, 2$, so the most frequent value is $1$ with two copies.

| step | lists |
|---:|---|
| start | $[1]$, $[1]$, $[2]$ |
| merge $[2]$ into the first $[1]$ | $[1,2]$, $[1]$ |
| merge the remaining $[1]$ into it | $[1,2,1]$ |

One list, starting and ending with $1$. Output `2` $= n - \text{top} + 1 = 3 - 2 + 1$.

---

Same problem grouped by topic: [../docs/greedy/LISTLIST.md](../docs/greedy/LISTLIST.md)
