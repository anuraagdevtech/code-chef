[&larr; 591. Chef and Rectangle Array](CHSQARR.md) &middot; [Index](../../README.md) &middot; [610. Appy Loves One &rarr;](HMAPPY1.md)

# 596. The Lost Arithmetic Sequences

> CodeChef problem code [`TAASEQ`](https://www.codechef.com/problems/TAASEQ) &middot; difficulty **2012** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Arrays |
| **Technique** | A constant number of removal candidates, each verified in linear time |
| **Time** | $O(N)$ per test case |
| **Space** | $O(N)$ |
| **Roadmap course** | Rise from 3* to 4* (Level 4) |

## Question

Jem couldn't even finish half of the homework exercises in "Advanced topics in algorithm" class. The teacher is really upset and gives him one final problem to solve - if he can't solve it, he is gonna fail the course.

Jem is given an array **A** consisting of **N** integers. The teacher asks him to remove exactly one number in the array to make the array become an arithmetic progressions.

Jem wanted to ask the teacher about the definition of arithmetic progressions but he remembered that he had heard this term in last week's lesson just before falling asleep. Now his life is in your hands again!

Anyways, we provide you the definition of arithmetic progression. Arithmetic progression is a sequence of numbers, where the difference between any two adjacent numbers is same.

**Input**

Input contains mutilpe test cases. The first line of the input contains a single integer **T** represents the number of tests. It is followed by T group of line represent the test cases.

Each test case consists of two lines where the first line contains a single integer **N**.

The second line contains **N** space separated integers denoting the array **A**.

**Output**

For each test case print out single integer which is the number you will remove from the array. If there is more than one solution take the smallest one. If there is no solution print out -1.

**Constraints**

- **1 ≤ T ≤ 10 **

- **2 ≤ N ≤ 10^5**

- **0 ≤ A_i ≤ 10^9**

## Constraints

- 1 ≤ T ≤ 10
- 2 ≤ N ≤ 10^5
- 0 ≤ A_i ≤ 10^9

## Sample

**Sample input**

```
3
2
3 4
4
1 5 3 4
6
2 4 6 7 8 10
```

**Sample output**

```
3
-1
7
```

<details><summary>Explanation</summary>

**test 1:** an array contain a single integer is considered to be an arithmetic progression so you can remove any number in the array. But note that we must print out the **smallest result** which is 3.

**test 2:** there is no solution since none of [1, 3, 4], [1, 5, 3], [1, 5, 4], [5, 3, 4] is an arithmetic progressions.

**test 3:** the only way to archive an airthmetic progressions is remove the number 7 which will give us [2, 4, 6, 8, 10].

</details>

## Approach

Either one of the first two elements is removed, or both stay and their difference $d$ is the common difference of the result. In the latter case scan for the first adjacent pair whose difference is not $d$: the removed element has to be one of those two, since otherwise that defect would survive. If no defect exists the array is already an arithmetic progression and only an end element can be removed.

That leaves at most five candidate positions - indices 0, 1, $N-1$ and the two around the first defect. For each, build the array without it and check directly that it is an arithmetic progression. Print the smallest value among the valid removals, or -1.

## Solution (Python)

```python
import sys


def main() -> None:
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    out = []
    for _ in range(next(tokens)):
        n = next(tokens)
        values = [next(tokens) for _ in range(n)]
        candidates = {0, 1, n - 1}
        if n > 2:
            step = values[1] - values[0]
            for i in range(2, n):
                if values[i] - values[i - 1] != step:
                    candidates.update((i - 1, i))
                    break
        valid = []
        for skip in candidates:
            rest = [x for i, x in enumerate(values) if i != skip]
            if len(rest) < 3 or all((rest[i] - rest[i - 1] == rest[1] - rest[0] for i in range(2, len(rest)))):
                valid.append(values[skip])
        out.append(str(min(valid, default=-1)))
    print('\n'.join(out))


if __name__ == "__main__":
    main()
```

## Complexity

- **Time:** $O(N)$ per test case
- **Space:** $O(N)$
- Auxiliary space excludes the buffered input and output.

## Edge cases

- Arrays of length at most 2 after removal are always arithmetic progressions.
- When several removals work the smallest removed value is required, not the first position.
- An array that is already a progression loses its first or last element - whichever is smaller.
- A constant array allows any removal; the candidates still contain its minimum.

## Dry run

`A = [2, 4, 6, 7, 8, 10]`. The first difference is 2 and the first pair that breaks it is (6, 7), so the candidates are indices 0, 1, 5, 2 and 3.

Removing index 3 (the 7) leaves `2 4 6 8 10`, a progression. Removing any other candidate leaves the pair 6, 7, 8 with difference 1 next to a difference of 2.

Answer 7.

---

Same problem in rating order (#574 of 735): [../../by-rating/574-TAASEQ.md](../../by-rating/574-TAASEQ.md)
