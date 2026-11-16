[&larr; 548. Ciel and Tomya](CIELTOMY.md) &middot; [Index](../../README.md) &middot; [552. Kingdom Unity &rarr;](KINGCON.md)

# 549. Petersen Graph

> CodeChef problem code [`PETERSEN`](https://www.codechef.com/problems/PETERSEN) &middot; difficulty **1894** &middot; time limit **1.5s**

| | |
|---|---|
| **Topic** | Graphs |
| **Technique** | Try the two starting vertices and follow unique letter transitions |
| **Time** | $O(|S|)$ per test case |
| **Space** | $O(|S|)$ |
| **Roadmap course** | Rise from 3* to 4* (Level 4) |

## Question

The following graph **G** is called a [Petersen graph](http://en.wikipedia.org/wiki/Petersen_graph) and its vertices have been numbered from **0** to **9**. Some letters have also been assigned to vertices of **G**, as can be seen from the following picture:

	<img src="//www.codechef.com//download/Petersen1tinysvg.png" width="300" alt="Petersen1tinysvg.png" />

	Let's consider a walk **W** in graph **G**, which consists of **L** vertices **W_1**, **W_2**, ..., **W_L**, such that **W_i** is connected with **W_i + 1** for 1 ≤ **i** < **L**. A string **S** of **L** letters **'A'-'E'** is realized by walk **W** if the sequence of letters written along **W** is equal to **S**. Vertices can be visited multiple times while walking along **W**.

For example, **S** = **'ABBECCD'** is realized by **W** = (0, 1, 6, 9, 7, 2, 3).

Your task is to determine whether there is a walk **W** which realizes a given string **S** in graph **G**, and if so, find the lexicographically least such walk.

**Input**

	The first line of the input contains one integer **T** denoting the number of testcases to process.

	The only line of each testcase contains one string **S**. It is guaranteed that **S** only consists of symbols **'A'-'E'**.

**Output**

	The output should contain exactly **T** lines, one line per each testcase in the order of their appearance. For each testcase, if there is no walk **W** which realizes **S**, then output **-1**. Otherwise, you should output the least lexicographical walk **W** which realizes **S**. Since all of the vertices are numbered from **0** to **9**, then it can be encoded as a string consisting of symbols **'0'-'9'** (see the "Examples" section for more details).

**Constraints**

1 ≤ **T** ≤ 8;

1 ≤ **|S|** ≤ 100000(10^5).

## Constraints

1 ≤ T ≤ 8;
1 ≤ |S| ≤ 100000(10^5).

## Sample

**Sample input**

```
2
AAB
AABE
```

**Sample output**

```
501
-1
```

## Approach

Vertices zero through four form the outer five-cycle; vertices five through nine form the inner star, and each outer vertex connects to its corresponding inner vertex. Both vertices with index congruent to $c$ modulo five carry letter $c$.

Each vertex has at most one neighbour with any requested letter. Hence the entire walk is forced once its starting vertex is fixed. Try the smaller starting vertex first; if its forced walk succeeds it is lexicographically smallest. Otherwise try the other start, and output minus one only if both fail.

## Solution (Python)

```python
import sys

TRANSITION = []
for u in range(10):
    if u < 5:
        neighbours = ((u-1)%5,(u+1)%5,u+5)
    else:
        i = u-5
        neighbours = ((i-2)%5+5,(i+2)%5+5,i)
    TRANSITION.append({v%5:v for v in neighbours})


def main() -> None:
    tokens = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(tokens))):
        s = next(tokens)
        first = s[0]-65
        answer = '-1'
        for start in (first,first+5):
            walk = [start]
            u = start
            for c in s[1:]:
                v = TRANSITION[u].get(c-65)
                if v is None:
                    break
                walk.append(v)
                u = v
            else:
                answer = ''.join(map(str,walk))
                break
        out.append(answer)
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
```

## Complexity

- **Time:** $O(|S|)$ per test case
- **Space:** $O(|S|)$
- Auxiliary space excludes the buffered input and output.

## Edge cases

- A one-letter string uses the smaller corresponding vertex.
- Repeated letters require crossing the spoke.
- A locally possible start may fail later, requiring the second start.

## Dry run

For `AAB`, starting at 0 forces `0->5`, but vertex 5 has no `B` neighbour. Starting at 5 forces `5->0->1`, so the least valid walk is `501`.

---

Same problem in rating order (#548 of 735): [../../by-rating/548-PETERSEN.md](../../by-rating/548-PETERSEN.md)
