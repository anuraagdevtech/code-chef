[&larr; 488. Brush Fire](488-FIRE.md) &middot; [Index](README.md) &middot; [490. Modular Equation &rarr;](490-MODEQ.md)

# 489. Little Elephant and Bamboo

> [`LEBAMBOO`](https://www.codechef.com/problems/LEBAMBOO) &middot; difficulty **1761** &middot; time limit **1.88586s** &middot; 1600 to 1800 difficulty problems (Level 3)

## Topic used

| | |
|---|---|
| **Topic** | Basic Math |
| **Technique** | Solve the linear equations for operation counts |
| **CodeChef tags** | `Mathematics`, `Basic Math` |
| **Complexity class** | Linear $O(n)$ |
| **Time** | $O(N)$ per test case |
| **Space** | $O(N)$ |

## Question

**Problem Statement**

Little Elephant from Zoo of Lviv likes bamboo very much. He currently has **n** stems of bamboo, **H_i** - height of **i-th** stem of bamboo (0-based numeration).

Today inspector Andrii from World Bamboo Association is visiting the plantation. He doesn't like current situation. He wants the height of **i-th** stem to be **D_i**, for each **i** from **0** to **n-1**, inclusive.

Little Elephant is going to buy some special substance. One bottle of such substance he can use to single stem of bamboo. After using substance for stem **i**, the height of **i-th** stem is decrased by **1** and the height of **j-th** stem is increased by **1** for each **j** not equal to **i**. Note that it is possible for some of the stems to have negative height, but after all transformations all stems should have positive height.

Substance is very expensive. Help Little Elephant and find the minimal number of bottles of substance required for changing current plantation to one that inspector wants. If it's impossible, print **-1**.

**Input**

First line contain single integer **T** - the number of test cases. **T** test cases follow. First line of each test case contains single integer **n** - the number of stems in the plantation. Second line contains **n** integers separated by single space - starting plantation. Next line of each test case contains **n** integers - plantation that inspector Andrii requires.

**Output**

In **T** lines print **T** integers - the answers for the corresponding test cases.

**Constraints**

1 <= **T** <= 50

1 <= **n** <= 50

1 <= **H_i, D_i** <= 50

## Constraints

1 <= T <= 50
1 <= n <= 50
1 <= H_i, D_i <= 50

## Sample

**Sample input**

```
3
1
1
2
2
1 2
2 1
3
3 2 2
4 5 3
```

**Sample output**

```
-1
1
5
```

## Approach

Let $d_i=D_i-H_i$, let $m$ be the total number of bottles, and let $x_i$ bottles be applied to stem $i$. Each bottle raises all stems by one except its selected stem, which instead decreases by one, so $d_i=m-2x_i$.

For $N>2$, summing gives $m=\sum d_i/(N-2)$. This uniquely determines the answer: require a nonnegative integer $m$ and nonnegative integer $x_i=(m-d_i)/2$ for every stem. For $N=2$, the sum must stay unchanged and the minimum is $|d_0|$. For $N=1$, only decreases are possible.

## Solution

```python
import sys


def main() -> None:
    tokens = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(tokens))):
        n = int(next(tokens))
        h = [int(next(tokens)) for _ in range(n)]
        d = [int(next(tokens))-v for v in h]
        if n == 1:
            answer = -d[0] if d[0] <= 0 else -1
        elif n == 2:
            answer = abs(d[0]) if sum(d) == 0 else -1
        else:
            total = sum(d)
            m, remainder = divmod(total, n-2)
            answer = m if remainder == 0 and m >= 0 and all(m >= x and (m-x)%2 == 0 for x in d) else -1
        out.append(str(answer))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
```

## Edge cases

- Treat $N=1$ and $N=2$ separately.
- A nonnegative total alone does not ensure parity or individual feasibility.
- Intermediate negative heights are explicitly allowed.

## Dry run

For `[3,2,2]` to `[4,5,3]`, differences are `[1,3,1]`. The total is `m=5`; operation counts are `[2,1,2]`, summing to five.

---

Same problem grouped by topic: [../docs/basic-math/LEBAMBOO.md](../docs/basic-math/LEBAMBOO.md)
