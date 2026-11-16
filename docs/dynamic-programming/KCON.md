[&larr; 362. Dish Distribution](DISHDIS.md) &middot; [Index](../../README.md) &middot; [515. The Great Wall of Byteland &rarr;](BWALL.md)

# 503. K-Concatenation

> CodeChef problem code [`KCON`](https://www.codechef.com/problems/KCON) &middot; difficulty **1780** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Dynamic Programming |
| **Technique** | Kadane over two copies plus profitable middle copies |
| **Time** | $O(N)$ per test case |
| **Space** | $O(N)$ |
| **Roadmap course** | 1600 to 1800 difficulty problems (Level 3) |

## Question

You are given an array **A** with size **N** (indexed from 0) and an integer **K**. Let's define another array **B** with size **N** · **K** as the array that's formed by concatenating **K** copies of array **A**.

For example, if **A** = {1, 2} and **K** = 3, then **B** = {1, 2, 1, 2, 1, 2}.

You have to find the maximum subarray sum of the array **B**. Fomally, you should compute the maximum value of **B_i + B_i+1 + B_i+2 + ... + B_j**, where 0 ≤ **i** ≤ **j** < **N** · **K**.

**Input**

- The first line of the input contains a single integer **T** denoting the number of test cases. The description of **T** test cases follows.

- The first line of each test case contains two space-separated integers **N** and **K**.

- The second line contains **N** space-separated integers **A_0, A_1, ..., A_N-1**.

**Output**

For each test case, print a single line containing the maximum subarray sum of **B**.

**Constraints**

- 1 ≤ **T** ≤ 10

- 1 ≤ **N** ≤ 10^5

- 1 ≤ **K** ≤ 10^5

- -10^6 ≤ **A_i** ≤ 10^6 for each valid **i**

**Subtasks**

**Subtask #1 (18 points):** **N** · **K** ≤ 10^5

**Subtask #2 (82 points):** original constraints

## Constraints

- 1 ≤ T ≤ 10
- 1 ≤ N ≤ 10^5
- 1 ≤ K ≤ 10^5
- -10^6 ≤ A_i ≤ 10^6 for each valid i

## Sample

**Sample input**

```
2
2 3
1 2
3 2
1 -2 1
```

**Sample output**

```
9
2
```

<details><summary>Explanation</summary>

**Example case 1:** **B** = {1, 2, 1, 2, 1, 2} and the subarray with maximum sum is the whole {1, 2, 1, 2, 1, 2}. Hence, the answer is 9.

**Example case 2:** **B** = {1, -2, 1, 1, -2, 1} and the subarray with maximum sum is {1, 1}. Hence, the answer is 2.

</details>

## Approach

A subarray either lies inside one copy or crosses a copy boundary. Kadane over two copies covers every possible start and end fragment. If the total sum of one copy is positive, all $K-2$ middle copies improve a crossing subarray; otherwise including additional full copies cannot help.

For $K=1$, run Kadane once. For $K\ge2$, run it over two copies and add $\max(0,(K-2)\sum A)$. Initialise from an actual element because the subarray must be nonempty.

## Solution (Python)

```python
import sys


def main() -> None:
    tokens = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(tokens))):
        n, k = int(next(tokens)), int(next(tokens))
        a = [int(next(tokens)) for _ in range(n)]
        current = best = a[0]
        for i in range(1, n*min(k,2)):
            value = a[i%n]
            current = max(value, current+value)
            best = max(best, current)
        if k > 2:
            best += max(0,(k-2)*sum(a))
        out.append(str(best))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
```

## Complexity

- **Time:** $O(N)$ per test case
- **Space:** $O(N)$
- Auxiliary space excludes the buffered input and output.

## Edge cases

- All-negative arrays return their largest element, never zero.
- $K=1$ cannot use a cross-boundary subarray.
- A zero total needs no extra middle-copy contribution.

## Dry run

For `[1,2]`, `K=3`, Kadane over two copies gives 6, and one positive middle copy contributes 3, giving 9. For `[1,-2,1]`, two copies give 2 and total zero adds nothing.

> CodeChef tags: `Algorithms`, `Greedy`

---

Same problem in rating order (#504 of 735): [../../by-rating/504-KCON.md](../../by-rating/504-KCON.md)
