# 428. Bitwise Equation

> CodeChef problem code [`BITEQU`](https://www.codechef.com/problems/BITEQU) &middot; difficulty **1679** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Constructive |
| **Technique** | Neutralising the AND to reduce to one XOR |
| **Time** | $O(1)$ per test case |
| **Space** | $O(1)$ |
| **Roadmap course** | 1600 to 1800 difficulty problems (Level 3) |

## Question

Given an integer $N$, find four **positive** **distinct** integers $a$, $b$, $c$ and $d$ such that:
- $1 \leq a, b, c, d \leq 10^{18}$
- $((a\mathbin{\&}b)\mathbin{|}c)\oplus d = N$

Here $\mathbin{\&}$, $\mathbin{|}$, and $\oplus$ represent [bitwise AND, OR and XOR](https://en.wikipedia.org/wiki/Bitwise_operation), respectively.

If there are multiple answers, print **any** of them. If no answer exists, print $-1$.

**Input**

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of one line of input, containing a single integer $N$.

**Output**

For each test case, output $-1$ if there is no way to find four distinct integers to satisfy the equation.

Otherwise, print on a new line **any** four space-separated integers $a$, $b$, $c$ and $d$ that satisfy the conditions.

## Constraints

- $1 \leq T \leq 10^4$
- $0 \leq N \lt 2^{32}$

## Sample

**Sample input**

```
3
1
2
3221225472
```

**Sample output**

```
1 4 3 2
2 4 3 1
920426639 955944413 754668683 4244364431
```

<details><summary>Explanation</summary>

**Test case $1$:** We have $a = 1$, $b = 4$, $c = 3$, $d = 2$ and $((a\mathbin{\&}b)\mathbin{|}c)\oplus d = (0 \mathbin{|}3) \oplus 2 = 3 \oplus 2 = 1.$

**Test case $2$:** We have $a = 2$, $b = 4$, $c = 3$, $d = 1$ and $((a\mathbin{\&}b)\mathbin{|}c)\oplus d = (0 \mathbin{|}3) \oplus 1 = 3 \oplus 1 = 2.$

**Test case $3$:** Note that the value of $N$ might exceed the limit of signed a $32$-bit integer, use unsigned $32$-bit integers or $64$-bit integers instead.

</details>

## Approach

The equation has three operators, but one of them can be switched off. Pick $a$ and $b$ with **disjoint bits**, so $a \mathbin{\&} b = 0$ and the whole left side collapses to

$$c \oplus d = N$$

Choosing $a = 2^{58}$ and $b = 2^{59}$ does it: both are under $10^{18}$, they share no bit, and they are far above anything $N$ can reach ($N < 2^{32}$), so they cannot collide with $c$ or $d$.

Then set $c = 2^{33}$ and $d = 2^{33} \oplus N = 2^{33} + N$. Both are positive, both differ from each other whenever $N \neq 0$, and both stay below $2^{34}$. All four values are distinct and in range, so the answer is never $-1$.

The one exception is $N = 0$, where $c \oplus d = 0$ forces $c = d$. There the AND must do some work: $a = 12$, $b = 10$ gives $a \mathbin{\&} b = 8$, and with $c = 1$ the left side is $(8 \mathbin{|} 1) \oplus 9 = 9 \oplus 9 = 0$, with $12, 10, 1, 9$ all distinct.

So a solution exists for every $N$ in range, and the distinctness requirement — the real constraint here — is handled by keeping the two "padding" values in a bit range nothing else touches.

Any answer is accepted. For $N = 1$ we print $2^{58}, 2^{59}, 2^{33}, 2^{33}{+}1$ where the sample prints the far tidier `1 4 3 2`; both satisfy the equation. The sample's third line, with $N = 3221225472 = 2^{31} + 2^{30}$, shows that the intended solutions were found by randomised search — which is unnecessary once the AND is zeroed out.

## Solution (Python)

```python
import sys

PAD_A = 1 << 58          # disjoint bits, so a & b == 0
PAD_B = 1 << 59
HIGH = 1 << 33           # above every possible N, so c != d and both are free


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for tok in data[1:1 + t]:
        n = int(tok)
        if n:
            out.append(f"{PAD_A} {PAD_B} {HIGH} {HIGH ^ n}")
        else:
            # c ^ d = 0 would need c == d, so let the AND carry the value.
            out.append("12 10 1 9")
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(1)$ per test case
- **Space:** $O(1)$

> CodeChef tags: `Advanced Algorithms`, `Mathematics`, `Bit Manipulation`
