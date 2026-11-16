[&larr; 513. String Reverse](STR_REVERSE.md) &middot; [Index](../../README.md) &middot; [546. Lavanya Loves DFA &rarr;](ICM2006.md)

# 516. Digit Operation

> CodeChef problem code [`DIGITOP`](https://www.codechef.com/problems/DIGITOP) &middot; difficulty **1798** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Strings |
| **Technique** | Length invariance and global digit deficits |
| **Time** | $O(\sum |A_i|+\sum |B_i|)$ per test case |
| **Space** | $O(N)$ for the input arrays |
| **Roadmap course** | 1600 to 1800 difficulty problems (Level 3) |

## Question

You are given arrays $A$ and $B$, each consisting of $N$ **strings**, and a positive integer $K$.
For all $1\le i \le N$, both $A_i$ and $B_i$ consist of characters from $0$ to $9$ (both inclusive).

You can perform the following types of operations on array $A$:
- Type $1$: Choose two indices $i$ and $j$ $(i\neq j)$ and swap any character of $A_i$ with any character of $A_j$. The cost of this operation is $0$.
- Type $2$: Choose an index $i$ and replace **one** character of $A_i$ with any character from $0$ to $9$ (both inclusive). The cost of this operation is $1$.

For example, let $A = [24, 30, 51]$. A valid sequence of operations can be:
- Swap $4$ in $A_1 = 24$ with $0$ in $A_2 = 30$ to obtain $[20, 34, 51]$.
- Swap $0$ in $A_1 = 20$ with $5$ in $A_3 = 51$ to obtain $[25, 34, 01]$.
- Replace $0$ in $A_3 = 01$ with $1$ to obtain $[25, 34, 11]$.
The cost of the above sequence of operations is $1$.

Find whether we can convert the array $A$ to array $B$ using **any** (possibly zero) number of operations with cost $\le K$.

**Input**

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of multiple lines of input.
    - The first line of each test case contains two space-separated integers $N$ and $K$, the size of array and the maximum cost of operations.
    - The second line of each test case contains $N$ space-separated strings $A_1,A_2,\ldots,A_N$.
    - The third line of each test case contains $N$ space-separated strings $B_1,B_2,\ldots,B_N$.

**Output**

For each test case, print `YES` if it is possible to convert array $A$ to $B$ using **any** (possibly zero) number of operations with cost $\le K$. Else, print `NO`.

You may print each character of the string in uppercase or lowercase (for example, the strings `yEs`, `yes`, `Yes`, and `YES` will all be treated as identical).

## Constraints

- $1 \leq T \leq 1000$
- $2 \leq N \leq 10^5$
- $1 \leq K \leq 10^{18}$
- $1 \leq |A_i|, |B_i| \leq 19$
- $A_i$ and $B_i$ consist of characters from $0$ to $9$ (both inclusive).
- The sum of $N$ over all test cases won't exceed $10^5$.

## Sample

**Sample input**

```
3
2 2
1 9
9 1
2 2
1 11
11 1
4 1
22 13 12 89
28 98 21 31
```

**Sample output**

```
YES
NO
YES
```

<details><summary>Explanation</summary>

**Test case $1$**: We can use one operation of type $1$ to swap $1$ in $A_1$ with $9$ in $A_2$. Thus, $A$ becomes $[9,1]$, which is equal to $B$. We are able to do this with $0$ cost, which is $\le 2$.

**Test case $2$:** It is impossible to convert $A$ to $B$ with at most $2$ cost.

</details>

## Approach

Both operations preserve the length of every array entry. If any corresponding lengths differ, conversion is impossible.

Otherwise all digit positions can be permuted for free: swaps between different entries are allowed, and a third position in another nonempty entry lets us simulate a swap within an entry. There are at least two entries. Count all digits globally. Every missing target digit requires one paid replacement, and replacing surplus digits supplies all deficits. The minimum cost is the sum of positive target-minus-source frequency differences.

## Solution (Python)

```python
import sys
from collections import Counter


def main() -> None:
    tokens = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(tokens))):
        n, budget = int(next(tokens)), int(next(tokens))
        a = [next(tokens) for _ in range(n)]
        b = [next(tokens) for _ in range(n)]
        if any(len(x) != len(y) for x,y in zip(a,b)):
            out.append('NO')
            continue
        source = Counter(digit for word in a for digit in word)
        target = Counter(digit for word in b for digit in word)
        needed = sum(max(0, count-source[digit]) for digit,count in target.items())
        out.append('YES' if needed <= budget else 'NO')
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
```

## Complexity

- **Time:** $O(\sum |A_i|+\sum |B_i|)$ per test case
- **Space:** $O(N)$ for the input arrays
- Auxiliary space excludes the buffered input and output.

## Edge cases

- Equal total lengths do not replace the per-entry length check.
- Leading zeros are characters and must be retained.
- The guarantee $N\ge2$ is needed for free within-entry rearrangement.

## Dry run

In sample three, source digit counts lack one `8` and have one extra `2`. One replacement resolves the deficit, while free swaps arrange the digits, so budget one succeeds.

> CodeChef tags: `Data Structures`, `Arrays`, `Algorithms`

---

Same problem in rating order (#518 of 735): [../../by-rating/518-DIGITOP.md](../../by-rating/518-DIGITOP.md)
