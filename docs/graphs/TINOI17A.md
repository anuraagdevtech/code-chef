[&larr; 525. Cricket Match](CRIMCH.md) &middot; [Index](../../README.md) &middot; [530. Moving Segments &rarr;](SEGDIR.md)

# 528. Fence - INOI 2017

> CodeChef problem code [`TINOI17A`](https://www.codechef.com/problems/TINOI17A) &middot; difficulty **unrated** &middot; time limit **3s**

| | |
|---|---|
| **Topic** | Graphs |
| **Technique** | Sparse flood fill with exposed-side counting |
| **Time** | $O(N)$ expected overall |
| **Space** | $O(N)$ |
| **Roadmap course** | Rise from 3* to 4* (Level 4) |

## Question

**INOI 2017, Problem 1, Fence**

 You have a rectangular farm which consists of **R*C** fields arranged in a grid
consisting of **R** rows and **C** columns. Each field is a **1 x 1** square.
Some of these fields have been planted with potatoes while the others lie
uncultivated. We say that two fields are adjacent if one lies immediately to the left
or to the right or above or below the other. (Note that two fields which touch each other at just one corner are not considered adjacent). If two fields are adjacent
then we say we may walk from one to the other. A **patch** is a collection
of all the cultivated fields such that one may walk from any field in the patch to any other field in the same patch only
via cultivated fields. There are no uncultivated fields in a patch. That is, all the cultivated fields in the farm can be partitioned into patches, and you can walk from one cultivated field to another cultivated field, if and only if, both of them belong to the same patch.

To prevent wild animals from destroying the cultivated fields you plan to
enclose each patch within fences constructed all along the boundaries of the patch. Wild animals infest the uncultivated fields, and also beyond the **R*C** farm. We need to ensure that the fences protect all the boundaries of each patch, so that the wild animals cannot get to any cultivated field without crossing a fence.

Clearly, the length of the fence needed for each patch may differ.
If your patch consists of just a single field then the fence will be
of length 4. If it consists of two adjacent fields then the fence
will be length 6.

Your task is to output the maximum length of fence needed to enclose a patch, among all the patches in your farm.
The input to your program will be a description of the positions of all the
cultivated fields in your farm.

**(X,Y)** refers to the field on the **X^th** row and **Y^th** column. So, **(1,1)** refers to the top-left corner field, and **(R,C)** refers to the bottom-right corner.

**Input**

- The first line contains three space separated integers, **R, C** and **N**, which are the number of rows, number of columns and the number of cultivated fields, respectively.

- The next **N** lines contain two space separated integers, **X_i** and **Y_i**, which signify that **(X_i, Y_i)** is a cultivated field.

**Output**

- A single integer which is the maximum length of fence needed for any patch.

**Constraints**

For all test cases you may assume that:

-
**0 ≤ Number of cultivated fields = N ≤ 100000**

- **1 ≤ X_i ≤ R**

- **1 ≤ Y_i ≤ C**

**Subtask 1**: For 15% of the score,

-
**1 ≤ R,C ≤ 20**

**Subtask 2**: For further 45% of the score,

-
**1 ≤ R,C ≤ 2500**

**Subtask 3**: For 40% of the score,

-
**1 ≤ R,C ≤ 1000000**

**Example**

```
**Input:**

**Output:**
```

**Explanation**

## Constraints

For all test cases you may assume that:
-
0 ≤ Number of cultivated fields = N ≤ 100000
- 1 ≤ X_i ≤ R
- 1 ≤ Y_i ≤ C

## Sample

**Sample input**

```
4 4 9
1 4
2 1
2 2
2 3
4 3
4 1
4 2
3 1
3 3
```

**Sample output**

```
16
```

<details><summary>Explanation</summary>

The input corresponds to the figure

```
<tt>
		. . . x
		x x x .
		x . x .
		x x x .
</tt>
```

'<tt>x</tt>' corresponds to a cultivated field, and '<tt>.</tt>' corresponds to an uncultivated field.

There are two patches. One patch, which includes only the (1,4) field needs a fence of length 4. The other patch, which has 8 fields in it, needs fence of length 16. A length of 12 to cover its outer boundary, and length 4 to cover its inner boundary.

Maximum(4,16) = 16. Hence, the answer is 16.

Note:

You may download the problem statements PDF and test cases zipped files here: http://pd.codechef.com/com/inoi/problems.zip. Please feel free to use them during the contest.

Password for the PDF and test cases zip files: DPtrumpsGreedy2017

</details>

## Approach

Store cultivated cells in a set rather than allocate the possibly enormous farm grid. Flood-fill each four-neighbour component. For every visited cell, count one fence unit for each of its four neighbours absent from the cultivated set.

Sum these exposed sides within each component and return the largest component perimeter. Keep membership and visited status separate, so already-visited cultivated neighbours never get counted as exposed.

## Solution (Python)

```python
import sys


def main() -> None:
    tokens = iter(map(int,sys.stdin.buffer.read().split()))
    rows,cols,n = next(tokens),next(tokens),next(tokens)
    cells = {(next(tokens),next(tokens)) for _ in range(n)}
    visited = set()
    answer = 0
    for start in cells:
        if start in visited:
            continue
        visited.add(start)
        stack = [start]
        perimeter = 0
        while stack:
            r,c = stack.pop()
            for v in ((r-1,c),(r+1,c),(r,c-1),(r,c+1)):
                if v not in cells:
                    perimeter += 1
                elif v not in visited:
                    visited.add(v)
                    stack.append(v)
        answer = max(answer,perimeter)
    print(answer)

if __name__ == '__main__':
    main()
```

## Complexity

- **Time:** $O(N)$ expected overall
- **Space:** $O(N)$
- Auxiliary space excludes the buffered input and output.

## Edge cases

- No cultivated fields gives perimeter zero.
- Diagonal contact does not connect patches.
- Boundaries around internal uncultivated holes also need fencing.

## Dry run

The sample has an isolated cell of perimeter 4 and a connected eight-cell ring. The ring has outer perimeter 12 and inner perimeter 4, giving maximum 16.

---

Same problem in rating order (#735 of 735): [../../by-rating/735-TINOI17A.md](../../by-rating/735-TINOI17A.md)
