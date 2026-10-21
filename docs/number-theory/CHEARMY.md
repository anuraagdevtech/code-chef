# 395. Chef And The Hiring Event

> CodeChef problem code [`CHEARMY`](https://www.codechef.com/problems/CHEARMY) &middot; difficulty **1613** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Number Theory |
| **Technique** | Product expansion for parity, then base-5 indexing |
| **Time** | $O(\log K)$ per test case |
| **Space** | $O(1)$ |
| **Roadmap course** | 1600 to 1800 difficulty problems (Level 3) |

## Question

The Head Chef is receiving a lot of orders for cooking the best of the problems lately. For this, he organized an hiring event to hire some talented Chefs. He gave the following problem to test the skills of the participating Chefs. Can you solve this problem and be eligible for getting hired by Head Chef.

A non-negative number **n** is said to be *magical* if it satisfies the following property. Let **S** denote the multi-set of numbers corresponding to the non-empty subsequences of the digits of the number **n** in decimal representation. Please note that the numbers in the set **S** can have **leading zeros**. Let us take an element **s** of the multi-set **S**, **prod(s)** denotes the product of all the digits of number **s** in decimal representation.
The number **n** will be called magical if sum of **prod(s)** for all elements **s** in **S**, is even.

For example, consider a number 246, its all possible non-empty subsequence will be **S = {2, 4, 6, 24, 46, 26, 246}**. Products of digits of these subsequences will be **{prod(2) = 2, prod(4) = 4, prod(6) = 6, prod(24) = 8, prod(46) = 24, prod(26) = 12, prod(246) = 48**, i.e. **{2, 4, 6, 8, 24, 12, 48}**. Sum of all of these is 104, which is even. Hence 246 is a *magical* number.

Please note that multi-set **S** can contain repeated elements, e.g. if number is 55, then **S = {5, 5, 55}**. Products of digits of these subsequences will be **{prod(5) = 5, prod(5) = 5, prod(55) = 25}**, i.e. **{5, 5, 25}**. Sum of all of these is 35 which is odd. Hence 55 is not a
 *magical* number.

Consider a number 204, then **S = {2, 0, 4, 20, 04, 24, 204}**. Products of digits of these subsequences will be **{2, 0, 4, 0, 0, 8, 0}**. Sum of all these elements will be 14 which is even. So 204 is a *magical* number.

The task was to simply find the **K^th** *magical* number.

**Input**

- First line of the input contains an integer **T** denoting the number of test cases.

- Each of the next **T** lines contains a single integer **K**.

**Output**

For each test case, print a single integer corresponding to the **K^th** magical number.

**Constraints**

- **1** ≤ **T** ≤ **10^5**

- **1** ≤ **K** ≤ **10^12**.

**Subtasks**

**Subtask #1 : (20 points)**

- **1** ≤ **T** ≤ **100**

- **1** ≤ **K** ≤ **10^4**.

**Subtask 2 : (80 points) **
Original Constraints

## Constraints

- 1 ≤ T ≤ 10^5
- 1 ≤ K ≤ 10^12.

## Sample

**Sample input**

```
2
2
5
```

**Sample output**

```
2
8
```

<details><summary>Explanation</summary>

**Example case 1.**
2 is the 2^nd magical number, since it satisfies the property of the magical number. The first magical number will be of course 0.

</details>

## Approach

The sum over all non-empty subsequences has a closed form. Expanding the product $\prod_i (1 + d_i)$ generates exactly one term per subset of digits — the product of the chosen digits — so subtracting the empty term gives

$$\sum_{s \in S} \mathrm{prod}(s) = \prod_{i=1}^{m} (1 + d_i) \;-\; 1$$

That sum is even iff the product is odd iff **every factor $1 + d_i$ is odd** iff every digit $d_i$ is even. So the magical numbers are precisely those written with digits from $\{0, 2, 4, 6, 8\}$ — the whole subsequence machinery collapses to a digit test.

Checking the statement's examples: $246$ gives $3 \cdot 5 \cdot 7 - 1 = 104$, even; $55$ gives $6 \cdot 6 - 1 = 35$, odd; and $204$ gives $3 \cdot 1 \cdot 5 - 1 = 14$, even.

Listing them in order — $0, 2, 4, 6, 8, 20, 22, \ldots$ — reveals a **base-5 numbering**: the $K$-th magical number is $K-1$ written in base $5$ with each digit doubled. This works because the even digits are an ordered alphabet of size $5$, and the ordering of magical numbers by value matches the lexicographic ordering of their base-5 codes, including leading zeros.

So the answer is a base conversion: write $K - 1$ in base $5$, then map each digit $c \mapsto 2c$. With $K \leq 10^{12}$ that is about $18$ digits, so each query is a short loop and $T = 10^5$ is comfortable.

The samples confirm the indexing starts at $0$: $K = 2$ gives $K-1 = 1$, i.e. `1` in base $5$, so $2$; and $K = 5$ gives $4$, so $8$. $K = 6$ would give `10`, i.e. $20$.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for tok in data[1:1 + t]:
        k = int(tok) - 1              # the list starts at 0
        digits = []
        # Magical numbers use digits {0,2,4,6,8}, so base 5 with doubled digits.
        while True:
            digits.append(str(2 * (k % 5)))
            k //= 5
            if not k:
                break
        out.append("".join(reversed(digits)))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(\log K)$ per test case
- **Space:** $O(1)$

> CodeChef tags: `Mathematics`, `Algorithms`, `Constructive`
