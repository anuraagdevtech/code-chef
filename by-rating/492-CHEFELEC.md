[&larr; 491. Distinct Elements](491-DISTELE.md) &middot; [Index](README.md) &middot; [493. Rectangles Counting &rarr;](493-RECTCNT.md)

# 492. Chefland and Electricity

> [`CHEFELEC`](https://www.codechef.com/problems/CHEFELEC) &middot; difficulty **1767** &middot; time limit **1s** &middot; 1600 to 1800 difficulty problems (Level 3)

## Topic used

| | |
|---|---|
| **Topic** | Greedy |
| **Technique** | Remove the largest gap between consecutive powered villages |
| **CodeChef tags** | `greedy` |
| **Complexity class** | Linear $O(n)$ |
| **Time** | $O(N)$ per test case |
| **Space** | $O(N)$ |

## Question

There are **n** villages in a Chefland. Some of the villages have electricity facilities, other doesn't. You can consider the villages arranged in line in the order **1** to **n** from left to right. i-th of village can be considered at **x_i** coordinates.

Chef decided that electricity should be provided to all the villages. So, he decides to buy some amount of electric wires to connect the villeges without electricity to some villages with electricity. As Chef does not want to spend too much amount of money on wires, can you find out minimum amount of length of wire Chef should buy.

**Input**

First line of the input contains an integer **T** denoting the number of test cases. **T** test cases follow.

First line of each test case contains an integer **n** denoting number of villages in Chefland.

Second line will contain a string of length **n** containing '0' or '1's only. If i-th character of the string is '1', then it denotes that i-th village has electricity.

Next line contains **n** space separated integers denoting the **x** coordinates of the villages in the order from village **1** to n

**Output**

For each test case, output a single line containing a integer corresponding to the minimum length of wire Chef needs to buy.

**Constraints**

- **1 ≤ T ≤ 10**

- It is guaranteed that there will be at least one village which will have electricity.

- **1 ≤ x_1 <  x_2 <  ... < x_n ≤ 10^9**

**Subtasks**

**Subtask #1 : 30 points**

- **1 ≤ N ≤ 1000**

**Subtask #2 : 70 points**

- **1 ≤ N ≤ 10^5**

## Constraints

- 1 ≤ T ≤ 10
- It is guaranteed that there will be at least one village which will have electricity.
- 1 ≤ x_1 <  x_2 <  ... < x_n ≤ 10^9

## Sample

**Sample input**

```
2
2
01
1 2
3
100
1 5 6
```

**Sample output**

```
1
5
```

<details><summary>Explanation</summary>

**In the first example**, first village does not have electricity. If we put a wire between village 1 and 2 of length 1, then both the villages will have electricity.

**In the second example**,
We can a draw a wire from first village to third village, passing through second village. Its total length will be 5. Now all the villages will have electricity. This is the minimum length of wire you will require.

</details>

## Approach

Connecting every consecutive village costs $x_{N-1}-x_0$. Before the first powered village and after the last, every gap is necessary. Between two consecutive powered villages, all interior villages can be supplied from either end. Exactly one gap may be omitted, and omitting the largest gap saves the most wire.

Scan adjacent gaps, tracking their maximum since the previous powered village. On reaching another powered village, subtract that maximum from the total.

## Solution

```python
import sys


def main() -> None:
    tokens = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(tokens))):
        n = int(next(tokens))
        s = next(tokens)
        x = [int(next(tokens)) for _ in range(n)]
        answer = x[-1]-x[0]
        seen = s[0] == 49
        largest = 0
        for i in range(1,n):
            if seen:
                largest = max(largest, x[i]-x[i-1])
            if s[i] == 49:
                if seen:
                    answer -= largest
                seen = True
                largest = 0
        out.append(str(answer))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
```

## Edge cases

- At least one powered village is guaranteed.
- With only one source, no gap can be removed.
- Adjacent powered villages need no wire between them.

## Dry run

For positions `[1,5,6]` and status `100`, every gap is needed, so the cost is `6-1=5`.

---

Same problem grouped by topic: [../docs/greedy/CHEFELEC.md](../docs/greedy/CHEFELEC.md)
