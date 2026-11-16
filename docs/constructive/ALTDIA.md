[&larr; 682. Yet Another Crossover Episode](DIANE.md) &middot; [Index](../../README.md) &middot; [718. Tree Distances &rarr;](TDISTS.md)

# 698. Alternating Diameter

> CodeChef problem code [`ALTDIA`](https://www.codechef.com/problems/ALTDIA) &middot; difficulty **2300** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Constructive |
| **Technique** | A star with the minority-friendly colour in the centre |
| **Time** | $O(B + W)$ per test case |
| **Space** | $O(B + W)$ for the output |
| **Roadmap course** | 2000 to 2500 difficulty problems (Level 5) |

## Question

Chef stumbled upon $B$ black nodes and $W$ white nodes and now wants to construct a tree using them.

Chef is bamboozled by the total number of trees that can be constructed using these nodes. To reduce this count, Chef considered only those trees which have **at least** one diameter that has alternating colors i.e. a black node is followed by a white node and a white node is followed by a black node.

Help Chef in finding out the tree with the **minimum** possible diameter among all the trees that satisfies the above condition. If no tree satisfies the above conditions, print $-1$. If multiple trees satisfies the above condition, print any.

**Input**

- The first line contains a single integer $T$ - the number of test cases. Then the test cases follow.
- The first and only line of each test case contains two space separated integers $B, W$ representing the number of black and white nodes respectively.

**Output**

- If a tree can be constructed that fulfils all the requirements then
    - In the first line, output a string of length $B + W$ in which the $i^{th}$ character (1-based indexing) is either `W` or `B` denoting the colour of the $i^{th}$ node as black or white respectively.
    - In the following $B + W - 1$ lines, output two integers $U$ and $V$ denoting an edge between $U^{th}$ and $V^{th}$ node.
- If no tree fulfils the requirements print `-1` in a single line.

## Constraints

- $1 \leq T \leq 100$
- $0 \leq B, W \leq 1000$
- $1 \leq B + W \leq 1000$

## Sample

**Sample input**

```
3
1 1
0 2
1 2
```

**Sample output**

```
WB
2 1
-1
WBW
1 2
2 3
```

<details><summary>Explanation</summary>

**Test case $1$:** The tree has only one path between the nodes $1$ and $2$ which is the diameter and also alternating in color. The checker will handle multiple possible answers so you can also swap the colors of the node to achieve the same result.

**Test case $2$:** There is only one tree possible and its diameter would consist of all white nodes only. Therefore there is no tree which satisfies the given conditions.

</details>

## Approach

- One vertex: the diameter is that single vertex, trivially alternating. Print its colour and no edges.
- Only one colour and at least two vertices: any diameter has two adjacent vertices of the same colour, so the answer is $-1$.
- Two vertices of different colours: the single edge.
- Three or more vertices with both colours: a tree on at least three vertices has diameter at least 2, and a star achieves 2. Its diameters are the paths leaf - centre - leaf, so we need two leaves of one colour and a centre of the other. Some colour has at least two vertices; put a vertex of the *other* colour in the centre and everything else on the leaves.

In the output vertex 1 is the centre and every other vertex is joined to it.

## Solution (Python)

```python
import sys


def solve(tokens):
    black, white = (next(tokens), next(tokens))
    n = black + white
    if n == 1:
        return 'B' if black else 'W'
    if not black or not white:
        return '-1'
    if white >= 2:
        colors = 'B' * black + 'W' * white
    else:
        colors = 'W' + 'B' * black
    return colors + '\n' + '\n'.join(('1 ' + str(i) for i in range(2, n + 1)))


if __name__ == "__main__":
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    t = int(next(tokens))
    out = [solve(tokens) for _ in range(t)]
    sys.stdout.write('\n'.join(out))
```

## Complexity

- **Time:** $O(B + W)$ per test case
- **Space:** $O(B + W)$ for the output
- Auxiliary space excludes the buffered input and output.

## Edge cases

- $B + W = 1$ prints only the colour string.
- $B = 0$ or $W = 0$ with more than one vertex is impossible.
- When white has at least two vertices the centre is black; otherwise white is the centre and black supplies the two leaves.
- Several trees are optimal, so the output is validated by a checker.

## Dry run

`B = 1, W = 2`: white has two vertices, so the centre is black. Colours `BWW`, edges `1 2` and `1 3`. The diameter `2 - 1 - 3` reads W, B, W.

`B = 3, W = 1`: white cannot supply two leaves, so the white vertex is the centre: colours `WBBB`, edges `1 2`, `1 3`, `1 4`; the diameter B, W, B alternates.

> CodeChef tags: `Data Structures`, `Graphs`

---

Same problem in rating order (#661 of 735): [../../by-rating/661-ALTDIA.md](../../by-rating/661-ALTDIA.md)
