[&larr; 318. ChefWatson uses Social Network](BOOKCHEF.md) &middot; [Index](../../README.md) &middot; [320. Pair Sort Version 3 &rarr;](PSORT3.md)

# 319. Remove One Element

> CodeChef problem code [`REMONE`](https://www.codechef.com/problems/REMONE) &middot; difficulty **1700** &middot; time limit **1.5s**

| | |
|---|---|
| **Topic** | Sorting |
| **Technique** | Two candidate offsets, verified by a merge |
| **Time** | $O(N \log N)$ per test case |
| **Space** | $O(N)$ |
| **Roadmap course** | Jump from 2* to 3* (Level 3) |

## Question

Alice has an array $A$ consisting of $N$ **distinct** integers. Bob takes exactly $N - 1$ elements from this array and adds a positive integer $X$ (i.e. $X \gt 0$) to each of these numbers and then shuffles them to form a new array $B$ of length $N - 1$.

You are given both arrays $A$ and $B$. You have to identify the value of $X$ chosen by Bob. If there are multiple possible values of $X$, print the **smallest** of them. It is guaranteed that for the given input, there exists at least one possible value of $X$.

**Note:** Since the input is large, prefer using fast input methods.

**Input**

- The first line of input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- Each test case contains $3$ lines of input.
- The first line contains an integer $N$ - the length of array $A$.
- The second line contains $N$ space-separated integers $A_1, A_2, \dots, A_N$, denoting the array $A$.
- The third line contains $N - 1$ space-separated integers $B_1, B_2, \dots, B_{N-1}$, denoting the array $B$.

**Output**

For each test case, output the value of $X$ chosen by Bob. In case there are multiple possible values of $X$, print the smallest of them.

## Constraints

- $1 \leq T \leq 7$
- $2 \leq N \leq 10^5$
- $1 \leq A_i \leq 10^9$
- $1 \leq B_i \leq 2 \cdot 10^9$
- $A_1, A_2, \dots, A_N$ are pairwise distinct.
- $B_1, B_2, \dots, B_{N-1}$ are pairwise distinct.
- Sum of $N$ over all test cases does not exceed $5 \cdot 10^5$.

## Sample

**Sample input**

```
3
4
1 4 3 8
15 8 11
2
4 8
10
2
2 4
3
```

**Sample output**

```
7
2
1
```

<details><summary>Explanation</summary>

**Test case $1$:** Bob takes the elements $\{1, 4, 8\}$ and adds $7$ to them to obtain a new sequence $\{8, 11, 15\}$. There is no other value of $X$ that can be added to the elements of $A$ to get $B$.

**Test case $3$:** There is only one option with Bob to consider, i.e. to take element $\{2\}$ and add $1$ to it to get array $B$. If he takes element $\{4\}$, he will have to add $-1$ which is not allowed.

</details>

## Approach

Sort both arrays. $B$ is $A$ with one element dropped and $X$ added to the rest, so sorting preserves the correspondence: $B_0$ must come from either $A_0$ or $A_1$ — the only two possibilities for "smallest surviving element", depending on whether $A_0$ was the one removed.

That gives just **two candidate offsets**:

$$X = B_0 - A_1 \qquad\text{or}\qquad X = B_0 - A_0$$

Since $A_1 > A_0$, the first is the smaller, so try it first and take the first that validates.

**Validation** is a two-pointer merge: walk $A$ and $B$ together, consuming a $B$ element whenever $A_i + X$ matches it and otherwise skipping that $A_i$. The candidate is valid when at most **one** skip occurs and all of $B$ is consumed.

The constraint $X > 0$ must also be checked — $B_0 - A_1$ can easily be zero or negative, as in sample case 3 where $A = [2,4]$ and $B = [3]$ give $3 - 4 = -1$, rejecting that candidate and leaving $X = 1$.

Sample case 1 shows the larger candidate winning: $A = [1,3,4,8]$ and $B = [8,11,15]$ reject $X = 5$ (which would need an $11$ that $A+5$ does not produce) and accept $X = 7$, dropping the $3$.

Sample case 2 takes the smaller candidate, $X = 2$, dropping the $4$ — and it is genuinely smaller than the alternative $X = 6$, which is why the order of trying matters for the "smallest $X$" requirement.

Values reach $2 \times 10^9$, so this needs **64-bit** arithmetic outside Python.

## Solution (Python)

```python
import sys


def works(a, b, x):
    """Can B be A shifted by x with exactly one element of A dropped?"""
    if x <= 0:
        return False
    i = j = skipped = 0
    while i < len(a) and j < len(b):
        if a[i] + x == b[j]:
            i += 1
            j += 1
        else:
            skipped += 1
            if skipped > 1:
                return False
            i += 1
    return j == len(b)


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n = int(data[pos])
        a = sorted(int(v) for v in data[pos + 1:pos + 1 + n])
        b = sorted(int(v) for v in data[pos + 1 + n:pos + 2 * n])
        pos += 2 * n
        # B[0] comes from A[0] or A[1]; the latter gives the smaller offset.
        for cand in (b[0] - a[1], b[0] - a[0]):
            if works(a, b, cand):
                out.append(str(cand))
                break
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(N \log N)$ per test case
- **Space:** $O(N)$

## Edge cases

- **Exactly one element of $A$ is dropped**, so after sorting both arrays, $B_1$ must come from either $A_1$ or $A_2$ — nothing further along, since at most one element before it can be missing.
- **Trying $A_2$ first yields the smaller $X$**, because $A_2 > A_1$ makes $B_1 - A_2 < B_1 - A_1$ — and the problem asks for the smallest. Checking $A_1$ first would return the larger offset whenever both work.
- **$X$ must be strictly positive**, which the guard enforces; $B_1 - A_2$ can easily come out negative or zero.
- **The candidate is verified by a merge**, allowing exactly one skip in $A$ — which rejects an offset that matches the first element by accident.
- **The merge must also confirm $B$ is exhausted**, hence the `j == len(b)` check; running out of $A$ early is a failure.
- **$N = 2$ leaves a single element in $B$** (the second and third rows), where both candidates are worth trying.
- **The values are pairwise distinct within each array**, so the sorted merge never faces ties.
- **$B_i$ can reach $2 \times 10^9$** while $A_i$ caps at $10^9$, so the offset can be as large as the values themselves.

## Dry run

First sample: $A = 1, 3, 4, 8$ and $B = 8, 11, 15$ (both sorted).

| candidate $X$ | from | merge |
|---:|---|---|
| $8 - 3 = 5$ | $A_2$ | $1{+}5 = 6 \neq 8$ (skip), $3{+}5 = 8$ ✓, $4{+}5 = 9 \neq 11$ → second skip, **fails** |
| $8 - 1 = 7$ | $A_1$ | $1{+}7 = 8$ ✓, $3{+}7 = 10 \neq 11$ (skip), $4{+}7 = 11$ ✓, $8{+}7 = 15$ ✓ → **works** |

Output `7`: Bob dropped the $3$.

---

Same problem in rating order (#407 of 486): [../../by-rating/407-REMONE.md](../../by-rating/407-REMONE.md)
