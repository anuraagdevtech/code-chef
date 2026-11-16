[Index](../../README.md) &middot; [543. Home Delivery &rarr;](HDELIVER.md)

# 523. Queries with Bags

> CodeChef problem code [`DSUBAGS`](https://www.codechef.com/problems/DSUBAGS) &middot; difficulty **unrated** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Disjoint Set Union |
| **Technique** | Path compression and union by size |
| **Time** | $O((N+Q)\alpha(N))$ overall |
| **Space** | $O(N)$ |
| **Roadmap course** | Rise from 3* to 4* (Level 4) |

## Question

There are $N$ bags and $N$ magic cards which manufactured by $DSU$ $Company$
daily. Each bag and card has assigned a number between $1$ to $N$. Initially $i^{th}$ card
is in the $i^{th}$ bag. Now manager wants to club some card together.

Manager is really busy right now he needs your help to perform this task.

You have $Q$ queries to perform.

Each query can be among $3$ $Types$ :

- $Type$-$1$. $Query$ - $1$ $A$ $B$

Magic card with number $A$ and $B$ are merge into single bag if they belong to two
different bags. Its independent which bag to choose, our goal is to add both the cards with number $A$ and $B$ in the same bag.

$NOTE$ - If you merging two magic cards $A$ and $B$ together then all other card which are already merge with card $A$ and $B$ will all be in a single bag after this query.

- $Type$-$2$. $Query$ - $2$ $A$ $B$

You need to check if two magic cards with number $A$ and $B$ belongs to same bag
or not.

- $Type$-$3$. $Query$ - $3$

This query use to check how many distinct bags remained till now.

**Input**

- The first line contains two space separated integer $N$ and $Q$.
- Next $Q$ line contains $3$ space separated integer for $Type$-$1$ and $Type$-$2$ query
and single integer for $Type$-$3$ query as shown in problem description.

**Output**

- For $Type$-$2$ query print **"YES"** if both magic cards belong to same bag else print **"NO"** without quotes.
- For $Type$-$3$ query print a single integer that denotes number of bags remained till now.

## Constraints

- $1 \leq N, Q \leq 10^5$
- $1 \leq A, B \leq N$ $(A \neq B)$

**Subtasks**

- 30 points : $1 \leq N, Q \leq 10^3$
- 70 points : $Original$ $Constraints$

## Sample

**Sample input**

```
3 8
2 1 2
3
1 1 2
3
2 1 2
1 2 3
3
2 1 3
```

**Sample output**

```
NO
3
2
YES
1
YES
```

<details><summary>Explanation</summary>

- $1^{st}$ query will give ans $NO$ as card with number 1 and 2 belong to different bags.
- $2^{nd}$ query will check no of distinct bags which are $3$ as we did not perform any merge yet.
- $3^{rd}$ query will perform merge of two cards with number 1 and 2 into one bag.
- $4^{th}$ query will check no of distinct bags which are $2$ now.
- $5^{th}$ query will give ans $YES$ as card with number 1 and 2 belong to same bags.
- $6^{th}$ query will perform merge of two cards with number 2 and 3 into one bag.
- $7^{th}$ query will check no of distinct bags which is $1$. (All magic cards is in the same bag).
- $8^{th}$ query will give ans $YES$ as card with number 1 and 3 belong to same bag.

</details>

## Approach

A DSU component represents one bag of merged cards. Store parent pointers and component sizes. Find representatives with path compression and attach the smaller component to the larger during a merge.

Maintain the number of components, decreasing it only for merges between distinct representatives. Connectivity queries compare representatives; type-three queries read the maintained count.

## Solution (Python)

```python
import sys


def main() -> None:
    tokens = iter(sys.stdin.buffer.read().split())
    n,q = int(next(tokens)),int(next(tokens))
    parent = list(range(n))
    size = [1]*n
    components = n
    def find(u):
        while parent[u] != u:
            parent[u] = parent[parent[u]]
            u = parent[u]
        return u
    out = []
    for _ in range(q):
        kind = int(next(tokens))
        if kind == 3:
            out.append(str(components))
            continue
        u,v = find(int(next(tokens))-1),find(int(next(tokens))-1)
        if kind == 2:
            out.append('YES' if u == v else 'NO')
        elif u != v:
            if size[u] < size[v]:
                u,v = v,u
            parent[v] = u
            size[u] += size[v]
            components -= 1
    sys.stdout.write('\n'.join(out)+'\n')

if __name__ == '__main__':
    main()
```

## Complexity

- **Time:** $O((N+Q)\alpha(N))$ overall
- **Space:** $O(N)$
- Auxiliary space excludes the buffered input and output.

## Edge cases

- Repeating a merge does not decrease the bag count.
- The input has one case, without a test-count prefix.
- A card is always connected to itself.

## Dry run

The sample starts with three components. Merging 1 and 2 changes the count to two; merging 2 and 3 changes it to one. Connectivity of 1 and 3 then returns `YES`.

---

Same problem in rating order (#724 of 735): [../../by-rating/724-DSUBAGS.md](../../by-rating/724-DSUBAGS.md)
