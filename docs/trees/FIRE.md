[&larr; 550. Rendezvous](TR1.md) &middot; [Index](../../README.md) &middot; [553. Robot Game &rarr;](TR2.md)

# 551. Brush Fire

> CodeChef problem code [`FIRE`](https://www.codechef.com/problems/FIRE) &middot; difficulty **1761** &middot; time limit **0.794s**

| | |
|---|---|
| **Topic** | Trees |
| **Technique** | Follow one burning branch while shielding its sibling |
| **Time** | $O(N)$ per test case |
| **Space** | $O(N)$ |
| **Roadmap course** | Rise from 3* to 4* (Level 4) |

## Question

Help! A brush fire has started near your house and you are the only one who can help extinguish it. The only tool you have at your disposal is a single fireproof barrier that can protect one bush at a time, provided the bush has not yet caught fire already. For simplicity, we will assume the flames spread according to the following discrete time model.

Initially, a single bush, say *s*, is on fire. You choose a bush, say *k*, to save. The flames then leap from *s* to every bush near *s* with the exception of bush *k* if it was near *s*. Say these new burning bushes form a set *B*. Bush *s* is then reduced to ashes and will never burn again. Now that the bushes in *B* are on fire, you may move the protective barrier from bush *k* to some other bush *k'*. The flames leap from bushes in *B* to every bush that has not yet burned (*i.e.* not *s* or in *B*) and is close enough to some bush in *B* except, perhaps, bush *k'*. Say this new set of burning bushes is *B'*.
The bushes in set *B* are reduced to ashes and will never burn again. Now, you may move the protective barrier from *k'* to another bush to protect it from the flames that will spread from bushes in *B'* and so on. This process repeats until there are no more bushes on fire.

The bushes are arranged in a peculiar manner. Before the fire started, each bush was close enough to spread a fire to at most three other bushes. Moreover, the bush that was initially on fire is actually close enough to only at most two other bushes. It is understood that for any two bushes A and B, if bush A is close enough to bush B then bush B is also close enough to bush A. Finally, the graph underlying the "close enough" relation has no cycles.

For whatever reason, some of the bushes hold some sentimental value to you. For this reason, you want to save all of these bushes.

**Input**

The first line of the input contains a single integer T ≤ 40 indicating the number of test cases that will follow. Each test case begins with three integers *n*, *s*, and *t* satisfying 1 ≤ *n* ≤ 10,000 and both *s* and *t* are between 1 and *n*. Here, *n* is the number of bushes (indexed from 1 to *n*), *s* is the index of the bush that is initially on fire, and *t* is the number of bushes you want to save.

Following this, there are *n* lines describing the "close enough" relation. The *i*'th line starts with an integer 0 ≤ *c_i* ≤ 3 meaning bush *i* is close enough to *c_i* other bushes. The remaining *c_i* integers on this line are the indices of the bushes that bush *i* is close to. As mentioned earlier, the input will be such that if bush *i* is close enough to bush *j*, then bush *j* is also close enough to bush *i*. Finally, we also guarantee that *c_s* ≤ 2.

The last line of input for each test case consists of *t* distinct integers between 1 and *n*. These correspond to indices of bushes you want to save.

Test cases are separated by a single blank line (including a blank line preceding the first test case).

**Output**

For each test case, you are to output a single line consisting of either "yes" or "no", depending on whether or not it is possible to save all of the indicated bushes.

## Constraints

- 1 <= T <= 40.
- 1 <= N <= 10000.
- The undirected graph is a forest.
- Every vertex has degree at most three, and the initial burning vertex has degree at most two.
- The target set contains between one and N distinct vertices.

## Sample

**Sample input**

```
3

3 1 2
2 2 3
1 1
1 1
2 3

3 1 1
2 2 3
1 1
1 1
2

7 1 3
2 2 3
3 1 4 5
3 1 6 7
1 2
1 2
1 3
1 3
4 5 7
```

**Sample output**

```
no
yes
yes
```

## Approach

Root the fire's component at the initial burning bush. The degree bounds give every vertex at most two children. An initial shield anywhere below a child can be moved up to that child without saving fewer marked bushes, so an optimal first shield may protect an entire child subtree. That subtree remains safe after its parent burns out; only the other child can continue burning.

A marked burning vertex is failure. An unmarked vertex with zero or one child is success because its only possible continuation can be shielded. With two children, choose which child to shield and recurse into the other. A reverse-order boolean DP therefore uses `safe[u] = not marked[u] and (child_count < 2 or any(safe[child]))`.

## Solution (Python)

```python
import sys


def main() -> None:
    tokens = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(tokens))):
        n,root,t = (int(next(tokens)) for _ in range(3))
        root -= 1
        graph = []
        for _ in range(n):
            degree = int(next(tokens))
            graph.append([int(next(tokens))-1 for _ in range(degree)])
        marked = {int(next(tokens))-1 for _ in range(t)}
        parent = [-2]*n
        parent[root] = -1
        order = [root]
        for u in order:
            for v in graph[u]:
                if parent[v] == -2:
                    parent[v] = u
                    order.append(v)
        safe = [False]*n
        for u in reversed(order):
            children = [v for v in graph[u] if parent[v] == u]
            safe[u] = u not in marked and (len(children) < 2 or any(safe[v] for v in children))
        out.append('yes' if safe[root] else 'no')
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
```

## Complexity

- **Time:** $O(N)$ per test case
- **Space:** $O(N)$
- Auxiliary space excludes the buffered input and output.

## Edge cases

- The initially burning bush cannot be saved.
- Unmarked bushes may be sacrificed.
- Disconnected components never reached by the fire are already safe.
- Input contains blank lines, handled by tokenisation.

## Dry run

In sample three, shield subtree 2 while bush 1 burns. Fire reaches 3; then shield marked bush 7 and allow unmarked leaf 6 to burn. All marked bushes are saved.

---

Same problem in rating order (#488 of 735): [../../by-rating/488-FIRE.md](../../by-rating/488-FIRE.md)
