[&larr; 495. Broken Life](495-BRKNLIFE.md) &middot; [Index](README.md) &middot; [497. Lunchtime &rarr;](497-LUNCHTIM.md)

# 496. Triplets

> [`SUMQ`](https://www.codechef.com/problems/SUMQ) &middot; difficulty **1772** &middot; time limit **1.5s** &middot; 1600 to 1800 difficulty problems (Level 3)

## Topic used

| | |
|---|---|
| **Topic** | Prefix Sums |
| **Technique** | Factor a triplet sum into two prefix sums |
| **CodeChef tags** | `Algorithms`, `Simple Algos`, `Dynamic Programming`, `Prefix Sum`, `Suffix Sum` |
| **Complexity class** | Linearithmic $O(n \log n)$ |
| **Time** | $O(P\log P+Q\log Q+R\log R)$ per test case |
| **Space** | $O(P+Q+R)$ |

## Question

Given a triplet of integers (X , Y , Z), such that X ≤ Y and Y ≥ Z, we define f(X , Y , Z) to be (X + Y) * (Y + Z). If either X > Y or Y < Z, or both, then f(X , Y , Z) is defined to be 0.

You are provided three arrays ** A , B** and **C **  of any length (their lengths may or may not be equal).

Your task is to find the sum of f(X , Y , Z) over all triplets (X, Y , Z) where  ** X, Y** and **Z ** belong to ** A**, **B** and **C** respectively.

 Output your sum for each test case modulo **1000000007**.

**Input**

- The first line contains a single integer, **T**, which is the number of test cases. The description of each testcase follows:

- The first line of each testcase contains **3** integers: **p, q** and **r**. These denote the lengths of **A**,**B** and **C** respectively.

- The second line contains **p** integers, which are the elements of **A**

- The third line contains **q** integers, which are the elements of **B**

- The fourth line contains **r** integers, which are the elements of **C**

**Output**

 Output the required sum modulo ** 1000000007 ** for each test case in a new line.

**Constraints**

  - 1 ≤ **T** ≤ 10

  - 1 ≤ **p**, **q**, **r** ≤ 100000

  - 1 ≤ every array element ≤ 1000000000

**Subtasks  **

  - Subtask #1 (30 points): 1 ≤ **p**,**q**,**r**  ≤ 100

  - Subtask #2 (70 points): 1 ≤** p**,**q**,**r**  ≤ 100000

## Constraints

- 1 ≤ T ≤ 10
  - 1 ≤ p, q, r ≤ 100000
  - 1 ≤ every array element ≤ 1000000000

## Sample

**Sample input**

```
1 
3 1 3
1 2 3
5
4 5 6
```

**Sample output**

```
399
```

<details><summary>Explanation</summary>

As there is only one choice for Y which equals to 5, to get a non-zero function value,we can choose any element for X from the set { 1 , 2 , 3 } and for Z from the set { 4  , 5 }

So triplets which give non-zero function values are:

 { 1 , 5  , 4 } :  ( 1 + 5 ) * ( 5 + 4 )  = 54

{ 1 , 5  , 5 } :  ( 1 + 5 ) * ( 5 + 5 )  = 60

{ 2 , 5  , 4 } :  ( 2 + 5 ) * ( 5 + 4 )  = 63

{ 2 , 5  , 5 } :  ( 2 + 5 ) * ( 5 + 5 )  = 70

{ 3 , 5  , 4 } :  ( 3 + 5 ) * ( 5 + 4 )  = 72

{ 3 , 5  , 5 } :  ( 3 + 5 ) * ( 5 + 5 )  = 80

Final answer : 54 + 60 + 63 + 70 + 72 + 80  = 399

</details>

## Approach

For fixed $Y$, eligible values satisfy $X\le Y$ and $Z\le Y$. The double sum factors into $(\sum X+Y\cdot\#X)(\sum Z+Y\cdot\#Z)$.

Sort all three arrays. Sweep $B$ in ascending order while adding eligible elements of $A$ and $C$ to running counts and sums. Each array element enters at most once, so after sorting the sweep is linear.

## Solution

```python
import sys


def main() -> None:
    tokens = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(tokens))):
        p, q, r = (int(next(tokens)) for _ in range(3))
        a = sorted(int(next(tokens)) for _ in range(p))
        b = sorted(int(next(tokens)) for _ in range(q))
        c = sorted(int(next(tokens)) for _ in range(r))
        i = j = sa = sc = answer = 0
        mod = 1000000007
        for y in b:
            while i < p and a[i] <= y:
                sa += a[i]
                i += 1
            while j < r and c[j] <= y:
                sc += c[j]
                j += 1
            answer = (answer + ((sa+i*y)%mod)*((sc+j*y)%mod)) % mod
        out.append(str(answer))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
```

## Edge cases

- Use non-strict comparisons, including values equal to $Y$.
- If either eligible prefix is empty, the contribution is zero.
- Repeated elements count separately.

## Dry run

For the sample `Y=5`, eligible `A=[1,2,3]` and `C=[4,5]`. Their factors are `6+3*5=21` and `9+2*5=19`; product `399`.

---

Same problem grouped by topic: [../docs/prefix-sums/SUMQ.md](../docs/prefix-sums/SUMQ.md)
