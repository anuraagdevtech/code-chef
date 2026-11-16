[&larr; 591. No Palindrome](591-NOPALINDROME.md) &middot; [Index](README.md) &middot; [593. Max Range Queries &rarr;](593-MAXREMOV.md)

# 592. Strategy for the World Cup

> [`WORLDCUP`](https://www.codechef.com/problems/WORLDCUP) &middot; difficulty **2055** &middot; time limit **1s** &middot; Rise from 3* to 4* (Level 4)

## Topic used

| | |
|---|---|
| **Topic** | Combinatorics |
| **Technique** | Multinomial over sixes, fours and the rest, with a prefix of binomials for wickets |
| **Complexity class** | Linear $O(n)$ |
| **Time** | $O(B_{\max} + T \cdot B)$ |
| **Space** | $O(B_{\max})$ |

## Question

Captain Dehatti from Bawanian village is making strategy to win the Fake Cricket World Cup organised in his village.

He want his team to score runs only in 4's and 6's because he believes that scoring any runs by running will make them tired.

He also wants that the team does not loose more than  **L** wickets.

He now wonders in how many ways his team can score exactly **R** runs in **B** balls. Ofcourse, he assumes that the opponent bowling is awesome and will not concede any extra runs.

Formally, He wonders how many ways can his team score exactly **R** runs in **B** balls, given that each ball can result in 4, 6, 0 , or W(wicket wont add anything to score). Atmost **L** wicktes are allowed [i.e. Atmost **L** 'W' can be there in B balls ].

**Note:** His batting order is fixed i.e. After each wicket , next player to come is fixed.

**Input**

First line contains **T**, the number of test cases.

Each test case contains 3 space separated integers, **R, B and L**

**Output**

For each test cases output the number of ways modulo 1e9+7 (i.e. 1000000007)

**Constraints**

- **1 ≤ T ≤ 25000**

- **0 ≤ R ≤ 10^9**

- **1 ≤ B ≤ 300**

- **0 ≤ L ≤ 9**

```
Note that the answer to R = 0 , B = 2 , W =1 is 3  [ 00 , 0W , W0 ]
```

## Constraints

- 1 ≤ T ≤ 25000
- 0 ≤ R ≤ 10^9
- 1 ≤ B ≤ 300
- 0 ≤ L ≤ 9

## Sample

**Sample input**

```
6
10 2 9
6 2 9
6 1 9
4 1 9
5 1 9
10 3 9
```

**Sample output**

```
2
4
1
1
0
12
```

<details><summary>Explanation</summary>

Explanation for the sample input 1:

All possible ways to face 2 deliveries:

00
04
06
0W
W0
W4
W6
WW
40
44
46
4W
60
64
66
6W

Only possible ways to win the match are 46 and 64. Hence answer is 2.

You need to consider all sample space i.e. 4^B

</details>

## Approach

Fix the number of sixes $s$. Then the fours are forced: $f = (R - 6s) / 4$ must be a non-negative integer. The remaining $n = B - s - f$ balls score nothing and each is either a dot ball or a wicket, with at most $L$ wickets.

The balls are ordered, so the number of ways is

$$\frac{B!}{s! \, f! \, n!} \cdot \sum_{w=0}^{\min(L, n)} \binom{n}{w}.$$

Factorials and inverse factorials modulo $10^9 + 7$ give the multinomial; the inner sum depends only on $(n, L)$ with $L \le 9$, so it is tabulated once for every $n$ as a running prefix of binomials. Sum over all feasible $s$.

## Solution

```python
import sys


def main() -> None:
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    cases = [(next(tokens), next(tokens), next(tokens)) for _ in range(next(tokens))]
    MOD = 1000000007
    most_balls = max((balls for runs, balls, wickets in cases), default=0)
    fact = [1] * (most_balls + 1)
    for i in range(1, most_balls + 1):
        fact[i] = fact[i - 1] * i % MOD
    inv_fact = [1] * (most_balls + 1)
    inv_fact[most_balls] = pow(fact[most_balls], MOD - 2, MOD)
    for i in range(most_balls, 0, -1):
        inv_fact[i - 1] = inv_fact[i] * i % MOD
    dot_ways = [[0] * 10 for _ in range(most_balls + 1)]
    for n in range(most_balls + 1):
        s = 0
        for wickets in range(10):
            if wickets <= n:
                s = (s + fact[n] * inv_fact[wickets] % MOD * inv_fact[n - wickets]) % MOD
            dot_ways[n][wickets] = s
    out = []
    for runs, balls, wickets in cases:
        total = 0
        if runs % 2 == 0 and runs <= 6 * balls:
            for six in range(min(balls, runs // 6) + 1):
                left = runs - 6 * six
                if left % 4:
                    continue
                four = left // 4
                n = balls - six - four
                if n >= 0:
                    total = (total + fact[balls] * inv_fact[six] % MOD * inv_fact[four] % MOD * inv_fact[n] % MOD * dot_ways[n][wickets]) % MOD
        out.append(str(total))
    print('\n'.join(out))


if __name__ == "__main__":
    main()
```

## Edge cases

- Odd $R$ or $R > 6B$ is impossible: answer 0.
- $R = 0$ is valid - every ball is a dot or a wicket.
- When $L$ exceeds the number of non-scoring balls, the prefix simply stops growing at $n$.
- The batting order is fixed, so wickets are indistinguishable apart from the ball they fall on.

## Dry run

`R = 6, B = 2, L = 9`.

- $s = 0$: $f = 6/4$ is not an integer - skip.
- $s = 1$: $f = 0$, $n = 1$. Arrangements $2! / (1! \, 0! \, 1!) = 2$; the one non-scoring ball is a dot or a wicket, $\binom{1}{0} + \binom{1}{1} = 2$.

Answer $2 \cdot 2 = 4$: `60`, `6W`, `06`, `W6`.

---

Same problem grouped by topic: [../docs/combinatorics/WORLDCUP.md](../docs/combinatorics/WORLDCUP.md)
