[Index](../../README.md) &middot; [603. Random decreasing function &rarr;](RDF.md)

# 514. A Plus B Again!

> CodeChef problem code [`TAAPLUSB`](https://www.codechef.com/problems/TAAPLUSB) &middot; difficulty **1796** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Probability |
| **Technique** | Sum the carry probabilities as a geometric series |
| **Time** | $O(1)$ per test case |
| **Space** | $O(1)$ |
| **Roadmap course** | 1600 to 1800 difficulty problems (Level 3) |

## Question

Have you ever implemented a program adding two big integers that cannot be represented by the primitive data type of your programming language? The algorithm is just simulation of the column addition method that we have been taught in elementary school. Sometimes we forget the carry and the result is incorrect.

 In this problem, you need to evaluate the expected value of the number of times we have non-zero carry when adding two non-negative integers that contain **at most N** digits each. Note that we are adding the numbers in their **base 10** representation.

For example, the following table shows the number of carries when adding some pairs of numbers:

**A**
		**B**
		**Number of carries**
	20
		4
		0
	111
		119
		1
	123
		923
		1
	1235
		98765
		5

**Input**

The first line of the input contains an integer **T** denoting the number of test cases. The description of **T** test cases follows.
Each test case has a single line containing an integer **N**.

**Output**

For each test case, output a single line containing the required expected value.
Your answer will be accepted if the error is less than 10 ^-6.

**Constraints**

- **1** ≤ **T** ≤ **100,000(10^5)**

- **1** ≤ **N** ≤ **100,000(10^5)**

## Constraints

- 1 ≤ T ≤ 100,000(10^5)
- 1 ≤ N ≤ 100,000(10^5)

## Sample

**Sample input**

```
3
1
2
3
```

**Sample output**

```
0.45
0.945
1.4445
```

<details><summary>Explanation</summary>

**Example case 1.**
We have 10*10 = 100 cases of adding two 1-digit number.
The carry appears when adding 1 and 9, 2 and 9, 3 and 9 ... and so on,
there are 45 cases in total and in each case, the carry appears exactly once.

</details>

## Approach

Pad both uniformly chosen numbers to $N$ digits with leading zeros. Without an incoming carry, 45 of the 100 digit pairs generate a carry; with one, 55 do. Hence $p_i=0.45+0.1p_{i-1}$ with $p_0=0$, so $p_i=(1-10^{-i})/2$.

Linearity of expectation gives $\sum_{i=1}^N p_i=N/2-(1-10^{-N})/18$. Evaluate this closed form. Once $N$ is large, the correction $10^{-N}$ is below floating-point relevance.

## Solution (Python)

```python
import sys


def main() -> None:
    tokens = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(tokens))):
        n = int(next(tokens))
        answer = n/2 - (1 - 10.0**(-n))/18
        out.append(f'{answer:.10f}')
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
```

## Complexity

- **Time:** $O(1)$ per test case
- **Space:** $O(1)$
- Auxiliary space excludes the buffered input and output.

## Edge cases

- Leading zeros are allowed when representing numbers with at most $N$ digits.
- Include the carry from the most significant input digit.
- Print enough decimal places for the error tolerance.

## Dry run

For `N=2`, carry probabilities are `0.45` and `0.495`; their sum is `0.945`.

> CodeChef tags: `Algorithms`, `Dynamic Programming`

---

Same problem in rating order (#517 of 735): [../../by-rating/517-TAAPLUSB.md](../../by-rating/517-TAAPLUSB.md)
