[&larr; 325. Minion Chef and Bananas](MINEAT.md) &middot; [Index](../../README.md) &middot; [327. Forest Gathering &rarr;](FORESTGA.md)

# 326. Stacks

> CodeChef problem code [`STACKS`](https://www.codechef.com/problems/STACKS) &middot; difficulty **1799** &middot; time limit **4s**

| | |
|---|---|
| **Topic** | Binary Search |
| **Technique** | Patience stacking with a sorted top list |
| **Time** | $O(N \log N)$ per test case |
| **Space** | $O(N)$ |
| **Roadmap course** | Jump from 2* to 3* (Level 3) |

## Question

As every other little boy, Mike has a favorite toy to play with. Mike's favorite toy is a set of **N** disks. The boy likes to compose his disks in stacks, but there's one very important rule: the disks in a single stack must be ordered by their radiuses in a **strictly** increasing order such that the top-most disk will have the smallest radius.

For example, a stack of disks with radii (5, 2, 1) is valid, while a stack of disks with radii (3, 4, 1) is not.

Little Mike has recently come up with the following algorithm after the order of disks are given:

- First, Mike initiates an empty set of disk stacks.

- Then, Mike processes the disks in the chosen order using the following pattern:
	- If there is at least one stack such that Mike can put the current disk on the top of the stack without making it invalid, then he chooses the stack with the smallest top disk radius **strictly** greater than the radius of the current disk, and puts the current disk on top of that stack.

- Otherwise, Mike makes a new stack containing only the current disk.

For example, let's assume that the order of the disk radii is (3, 4, 5, 1, 1, 2). Here's how the set of the top stack disks will appear during the algorithm's run:

- In the beginning of the algorithm, the set of disk stacks is empty. After processing the first disk, the set of top stack disks is {3}.

- We cannot put the second disk on the only stack that we have after processing the first disk, so we make a new stack. After processing the second disk, the set of top stack disks is {3, 4}.

- We cannot put the third disk on any of the available stacks, so we make a new stack. After processing the third disk, the set of top stack disks is {3, 4, 5}.

- The fourth disk has radius 1, so it can be easily put on any of the available stacks. According to the algorithm, we choose the stack with the top disk radius equal to 3. After processing the fourth disk, the set of top stack disks is {1, 4, 5}.

- The fifth disk has radius 1, so there are two stacks we can put it on. According to the algorithm, we choose the stack with the top disk radius equal to 4. After processing the fifth disk, the set of top stack disks is {1, 1, 5}.

- The sixth disk has radius 2, so there is only one stack we can put it on. The final set of top stack disks is {1, 1, 2}.

Mike is really excited about his new algorithm, but he has so many disks that it seems impossible to simulate the algorithm manually.

You are given an array **A** of **N** integers denoting the radii of Mike's disks. The disks are already ordered by Mike. Your task is to find the set of the stack top disk radii after the algorithm is done.

**Input**

The first line of the input contains an integer **T** denoting the number of test cases. The description of **T** test cases follows.

The first line of a test description contains a single integer **N**.

The second line of the description contains **N** integers denoting **A_1, ... , A_N**.

**Output**

For each test case, output a single line. The line should start with a positive integer **S** denoting the number of stacks after the algorithm is done. This should be followed by **S** integers on the same line denoting the stacks' top disk radii in **non-decreasing order**.

If there are multiple correct answers, you are allowed to output any of them.

**Constraints**

- 1 ≤ **T** ≤ 10

    - 1 ≤ **N** ≤ 10^5

    - 1 ≤ **A_i** ≤ 10^9

## Constraints

- 1 ≤ T ≤ 10
    - 1 ≤ N ≤ 10^5
    - 1 ≤ A_i ≤ 10^9

## Sample

**Sample input**

```
3
6
3 4 5 1 1 2
10
3 2 9 5 2 9 4 14 7 10
8
14 5 13 19 17 10 18 12
```

**Sample output**

```
3 1 1 2
5 2 2 4 7 10 
4 5 10 12 18
```

<details><summary>Explanation</summary>

**Test case $1$:** This case is already explained in the problem statement.

**Test case $2$:** After processing the first disk, the set of top stack disks are $[3]$. The second disk can be placed on the first stack. Thus, top stack disks are $[2]$. The next $3$ disks can be stacked together. Thus, the top stack disks are $[2, 2]$. The next two disks can be stacked together to get $[2, 2, 4]$. The next two disks can be stacked together to get $[2, 2, 4, 7]$. The last disk can be put on top of the fifth stack. The final stack top are $[2, 2, 4, 7, 10]$. Thus, $5$ stacks are needed.

**Test case $3$:** After processing the first disk, the set of top stack disks are $[14]$. The second disk can be placed on the first stack. Thus, top stack disks are $[5]$. The next disk can be placed on second stack to get $[5, 13]$. The next $2$ disks can be stacked together. Thus, the top stack disks are $[5, 13, 17]$. The next disk can be placed on second stack to get $[5, 10, 17]$. The next disk can be placed on fourth stack to get $[5, 10, 17, 18]$. The last disk can be put on top of the third stack. The final stack top are $[5, 10, 12, 18]$. Thus, $4$ stacks are needed.

</details>

## Approach

Mike's rule — place the disk on the stack whose top is the **smallest radius still strictly greater** than it, else start a new stack — is exactly the *patience sorting* deal, and it has a property that makes it cheap to simulate.

Keep the stack tops in a list sorted ascending. For a disk $d$:

- `bisect_right(tops, d)` gives the index of the first top strictly greater than $d$ — precisely the stack Mike chooses;
- if that index exists, overwrite it with $d$;
- otherwise append $d$ as a new stack.

**The list stays sorted automatically.** Replacing `tops[k]` with $d$ is safe because $d \geq \texttt{tops}[k-1]$ (everything before index $k$ is $\leq d$) and $d < \texttt{tops}[k] \leq \texttt{tops}[k+1]$. Appending is safe because $d$ exceeded every existing top. So no re-sorting is ever needed, and each disk costs one binary search.

That invariant is the whole trick — without it one would reach for a heap or a balanced multiset and work much harder.

Tracing the first sample $(3,4,5,1,1,2)$: the tops grow to $[3,4,5]$, then the first $1$ displaces the $3$, the second $1$ displaces the $4$, and the $2$ displaces the $5$, finishing at $[1,1,2]$ — three stacks.

The output is the **stack count first**, then the tops in ascending order, which is just the list's own order. That leading count is easy to miss from the statement.

Note `bisect_right` rather than `bisect_left` is required: the rule says *strictly* greater, so a top equal to $d$ must not be chosen.

## Solution (Python)

```python
import sys
from bisect import bisect_right


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n = int(data[pos])
        tops = []
        for v in data[pos + 1:pos + 1 + n]:
            d = int(v)
            # First top strictly greater than d; the list stays sorted after
            # the overwrite, so no re-sorting is ever needed.
            k = bisect_right(tops, d)
            if k == len(tops):
                tops.append(d)
            else:
                tops[k] = d
        pos += 1 + n
        out.append(" ".join(map(str, [len(tops)] + tops)))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(N \log N)$ per test case
- **Space:** $O(N)$

## Edge cases

- **Mike's rule is exactly a patience-stacking step**: the new disk goes on the stack whose top is the *smallest radius strictly greater* than it, which is the first top above the disk in sorted order — a `bisect_right`.
- **The list of tops stays sorted automatically.** Overwriting the found position with a smaller value keeps the order, because the replaced top was the first one above it and the one before it is at most the disk. So the list never needs re-sorting.
- **A disk larger than every top starts a new stack**, which the append handles when the search runs off the end.
- **Equal radii start new stacks**, because the rule demands a *strictly* greater top — the sample's two $1$s end up on separate stacks, which is why the answer has two tops of $1$.
- **The answer is the count followed by the final tops**, which the sorted list supplies directly.
- **A strictly increasing input** gives one stack per disk, since each is larger than every existing top.
- **$N \leq 10^5$** with one bisect per disk.

## Dry run

First sample: disks $3, 4, 5, 1, 1, 2$.

| disk | first top strictly greater | action | tops after |
|---:|---|---|---|
| 3 | none | new stack | $3$ |
| 4 | none | new stack | $3, 4$ |
| 5 | none | new stack | $3, 4, 5$ |
| 1 | $3$ | place on it | $1, 4, 5$ |
| 1 | $4$ | place on it | $1, 1, 5$ |
| 2 | $5$ | place on it | $1, 1, 2$ |

Output `3 1 1 2`.

---

Same problem in rating order (#462 of 486): [../../by-rating/462-STACKS.md](../../by-rating/462-STACKS.md)
