[&larr; 551. Brush Fire](FIRE.md) &middot; [Index](../../README.md) &middot; [614. Chef and Subarray Queries &rarr;](CSUBQ.md)

# 553. Robot Game

> CodeChef problem code [`TR2`](https://www.codechef.com/problems/TR2) &middot; difficulty **1754** &middot; time limit **0.61675s**

| | |
|---|---|
| **Topic** | Trees |
| **Technique** | Merge root-path tries and count supporting maps |
| **Time** | $O(\sum N_i+M)$ per test case |
| **Space** | $O(\sum N_i+M)$ |
| **Roadmap course** | Rise from 3* to 4* (Level 4) |

## Question

Byteland is a kingdom of islands. Alice has N maps of the different islands constituting Byteland. Map of each island consists of cities, connected by roads. Being Byteland, the road layout of each island has a binary tree structure. Each island has a capital, which is the root of the binary tree of its map.

Alice is bored and plays the following game:

She chooses k out of these N maps and places a robot on the capital city of each map. Every robot is controlled by a common control string. If the present character of the control string is L(R), then all the robots move to the left(right) subtree on their map. All the robots follow the same control string and move on their respective maps.

A control string is valid with respect to a given map if it corresponds to a valid path on that map. A control string is considered valid for a given set of k maps if it is valid for each of the k chosen maps.

For example in a complete binary tree of 3 nodes, control strings "L" and "R" are valid and "LL" is an example of an invalid control string.

Alice is interested in knowing the longest control
string which is valid for at least k maps, for each value of k. Can you find this for her?

**Input**

First line of input contains an integer t (t<=5), the number of test cases. Each test case starts with an integer M (1<=M<=100), the number of maps. Then M maps description follow.

The ith map description starts with an integer N (2<=N<=1000), the number of cities on the island. Each of the following N-1 lines contain two space separated integers u c v (1<=u,v<=N , c=L or R) which means a road between city u and city v on the ith island and if c is L(R) then v is in the left(right) subtree of u. The capital city of each island is the city with number 1.

**Output**

For each test case output M space separated integers, where the ith integer denotes the length of the longest valid control string she can obtain assuming she can choose i maps.

## Constraints

- 1 <= T <= 5.
- 1 <= M <= 100 maps per case.
- 2 <= N <= 1000 cities in each map.
- Each map is a binary tree rooted at city 1; edges are labelled L or R.

## Sample

**Sample input**

```
2
3
5
1 L 2
1 R 3
3 L 4
3 R 5
4
1 R 2
1 L 3
2 L 4
3
1 L 2
1 R 3
2
5
1 L 2
2 L 3
3 L 4
4 L 5
6
1 L 2
2 R 3
3 L 4
4 R 5
5 L 6
```

**Sample output**

```
2 2 1
5 1
```

## Approach

Each root-to-node path is a control string over `L` and `R`. Merge all maps into a common binary trie, counting how many maps contain each trie node. A map contains each root path at most once, so visiting its vertices increments exactly those support counts.

For every trie node of depth $d$ and count $c$, update the longest string supported by exactly that node count. A suffix maximum over counts then converts this to the longest string supported by at least $k$ maps for every $k$.

## Solution (Python)

```python
import sys


def main() -> None:
    tokens = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(tokens))):
        maps = int(next(tokens))
        left = [-1]
        right = [-1]
        count = [0]
        depth = [0]
        for _ in range(maps):
            n = int(next(tokens))
            children = [[] for _ in range(n)]
            for _ in range(n-1):
                u,side,v = int(next(tokens))-1,next(tokens),int(next(tokens))-1
                children[u].append((side,v))
            count[0] += 1
            stack = [(0,0)]
            while stack:
                u,node = stack.pop()
                for side,v in children[u]:
                    branch = left if side == b'L' else right
                    if branch[node] == -1:
                        branch[node] = len(count)
                        left.append(-1)
                        right.append(-1)
                        count.append(0)
                        depth.append(depth[node]+1)
                    target = branch[node]
                    count[target] += 1
                    stack.append((v,target))
        answer = [0]*(maps+1)
        for c,d in zip(count,depth):
            answer[c] = max(answer[c],d)
        for k in range(maps-1,0,-1):
            answer[k] = max(answer[k],answer[k+1])
        out.append(' '.join(map(str,answer[1:])))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
```

## Complexity

- **Time:** $O(\sum N_i+M)$ per test case
- **Space:** $O(\sum N_i+M)$
- Auxiliary space excludes the buffered input and output.

## Edge cases

- The capital is vertex one in every map.
- Input edges need not be in parent-first order; traverse after reading the map.
- An empty control string is always valid and has length zero.

## Dry run

In sample one, path `RL` exists in the first two maps, while only one-step paths are common to all three. The answers are `2 2 1`.

---

Same problem in rating order (#480 of 735): [../../by-rating/480-TR2.md](../../by-rating/480-TR2.md)
