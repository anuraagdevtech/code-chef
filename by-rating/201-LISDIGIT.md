[&larr; 200. Points and Lines](200-POLIN.md) &middot; [Index](README.md) &middot; [202. Hard Cash &rarr;](202-CASH.md)

# 201. Digit Longest Increasing Subsequences 2

> [`LISDIGIT`](https://www.codechef.com/problems/LISDIGIT) &middot; difficulty **1297** &middot; time limit **3s** &middot; Jump from 2* to 3* (Level 3)

## Topic used

| | |
|---|---|
| **Topic** | Constructive |
| **Technique** | Using the LIS value itself as the digit |
| **Complexity class** | Linear $O(n)$ |
| **Time** | $O(n)$ per test case |
| **Space** | $O(n)$ |

## Question

Recently Chef learned about [Longest Increasing Subsequence](https://en.wikipedia.org/wiki/Longest_increasing_subsequence). To be precise, he means longest **strictly** increasing subsequence, when he talks of longest increasing subsequence.  To check his understanding, he took his favorite **n**-digit number and for each of its **n** digits, he computed the length of the longest increasing subsequence of digits ending with that digit. Then he stored these lengths in an array named **LIS**.

For example, let us say that Chef's favourite **4**-digit number is **1531**, then the **LIS** array would be **[1, 2, 2, 1]**. The length of longest increasing subsequence ending at first digit is **1** (the digit **1** itself) and at the second digit is **2** (**[1, 5]**), at third digit is also **2** (**[1, 3]**), and at the **4**th digit is **1** (the digit **1** itself).

Now Chef wants to give you a challenge. He has a valid **LIS** array with him, and wants you to find any **n**-digit number having exactly the same **LIS** array? You are guaranteed that Chef's **LIS** array is valid, i.e. there exists at least one **n**-digit number corresponding to the given **LIS** array.

**Input**

The first line of the input contains an integer **T** denoting the number of test cases.

For each test case, the first line contains an integer **n** denoting the number of digits in Chef's favourite number.

The second line will contain **n** space separated integers denoting **LIS** array, i.e. **LIS_1, LIS_2, ..., LIS_n**.

**Output**

For each test case, output a single **n**-digit number (without leading zeroes) having exactly the given **LIS** array. If there are multiple **n**-digit numbers satisfying this requirement, any of them will be accepted.

**Constraints**

- **1** ≤ **T** ≤ **30 000**

    - **1** ≤ **n** ≤ **9**

    - It is guaranteed that at least one **n**-digit number having the given **LIS** array exists

## Constraints

- 1 ≤ T ≤ 30 000
    - 1 ≤ n ≤ 9
    - It is guaranteed that at least one n-digit number having the given LIS array exists

## Sample

**Sample input**

```
5
1 
1
2 
1 2
2 
1 1
4
1 2 2 1
7 
1 2 2 1 3 2 4
```

**Sample output**

```
7
36
54
1531
1730418
```

<details><summary>Explanation</summary>

**Example case 1.** All one-digit numbers have the same **LIS** array, so any answer from **0** to **9** will be accepted.

**Example cases 2 & 3.** For a two digit number we always have **LIS_1 = 1**, but the value of **LIS_2** depends on whether the first digit is strictly less than the second one. If this is the case (like for number **36**), **LIS_2 = 2**, otherwise (like for numbers **54** or **77**) the values of **LIS_2** is **1**.

**Example case 4.** This has already been explained in the problem statement.

**Example case 5.** **7**-digit number **1730418** has **LIS** array **[1, 2, 2, 1, 3, 2, 4]**:

index
        LIS
        length
    1
        <font color="#578fb2">**1**</font>730418
        1
    2
        <font color="#578fb2">**17**</font>30418
        2
    3
        <font color="#578fb2">**1**</font>7<font color="#578fb2">**3**</font>0418
        2
    4
        173<font color="#578fb2">**0**</font>418
        1
    5
        <font color="#578fb2">**1**</font>7<font color="#578fb2">**3**</font>0<font color="#578fb2">**4**</font>18
        3
    6
        173<font color="#578fb2">**0**</font>4<font color="#578fb2">**1**</font>8
        2
    7
        <font color="#578fb2">**1**</font>7<font color="#578fb2">**3**</font>0<font color="#578fb2">**4**</font>1<font color="#578fb2">**8**</font>
        4

</details>

## Approach

The inverse problem looks harder than the forward one, but there is a construction so short it needs no search: **use the LIS value as the digit**.

$$d_i = \mathrm{LIS}_i$$

Why it works comes from the defining recurrence of the LIS array over any sequence $d$:

$$\mathrm{LIS}(i) = 1 + \max\{\mathrm{LIS}(j) : j < i,\ d_j < d_i\}$$

(with the max taken as $0$ when the set is empty). Suppose by induction that the array produced by $d = \mathrm{LIS}$ matches $\mathrm{LIS}$ at all earlier positions. Then the set above is $\{\mathrm{LIS}_j : j < i,\ \mathrm{LIS}_j < \mathrm{LIS}_i\}$, and its maximum is exactly $\mathrm{LIS}_i - 1$ — because a **valid** LIS array always has some earlier position with value $\mathrm{LIS}_i - 1$ (the predecessor of $i$ on its own increasing subsequence), and by definition no earlier value can sit strictly between $\mathrm{LIS}_i - 1$ and $\mathrm{LIS}_i$. So the recurrence returns $\mathrm{LIS}_i$, as required.

Two side conditions fall out for free. Every $\mathrm{LIS}_i \geq 1$, so no digit is $0$ and there is never a leading zero; and $n \leq 9$ bounds $\mathrm{LIS}_i \leq 9$, so every value is a legal single digit. That bound on $n$ is exactly what makes the identity construction work — for $n \geq 11$ an LIS array could demand a value of $10$.

Many answers are accepted. For $[1,2,2,1,3,2,4]$ we print `1221324` where the sample prints `1730418`; both have that LIS array. For $[1,1]$ we print `11` — equal digits are correct here, since the LIS must be *strictly* increasing so the second digit cannot extend the first.

## Solution

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n = int(data[pos])
        # The LIS value doubles as the digit: >= 1 so no leading zero, and
        # <= 9 because n <= 9.
        out.append(b"".join(data[pos + 1:pos + 1 + n]).decode())
        pos += 1 + n
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Edge cases

- **Using the LIS value as the digit is self-consistent.** Reading the array as digits, a strictly increasing run ending at position $i$ is a strictly increasing run of integers finishing at $L_i$ and starting at $1$ or more, so it has at most $L_i$ terms; and a chain with values $1, 2, \ldots, L_i$ genuinely exists, so exactly $L_i$ is achieved.
- **No leading zero**, because every $L_i \geq 1$; and **no digit above $9$**, because $n \leq 9$ bounds any increasing subsequence.
- **$L_i$ is the LIS length *ending at* position $i$**, not of the prefix — in `1 2 2 1` the value drops back to $1$ at the last position, which a prefix reading could never do.
- **Repeated values are fine**: the two $2$s in that array both have $L = 2$, because strict increase stops the second $2$ from extending a chain through the first.
- **This answer differs from the sample's.** The sample prints `1531` where this prints `1221`; a special judge checks the resulting LIS array rather than the exact digits, so both are accepted.
- **Existence is guaranteed** by the statement, so no feasibility check is needed.

## Dry run

Last sample: $L = 1, 2, 2, 1, 3, 2, 4$, so the number is `1221324`.

| position | digit | longest strictly increasing run ending here | length |
|---:|---:|---|---:|
| 1 | 1 | $1$ | 1 |
| 2 | 2 | $1, 2$ | 2 |
| 3 | 2 | $1, 2$ | 2 |
| 4 | 1 | $1$ | 1 |
| 5 | 3 | $1, 2, 3$ | 3 |
| 6 | 2 | $1, 2$ | 2 |
| 7 | 4 | $1, 2, 3, 4$ | 4 |

The lengths reproduce the input array exactly.

---

Same problem grouped by topic: [../docs/constructive/LISDIGIT.md](../docs/constructive/LISDIGIT.md)
