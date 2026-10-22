# 318. ChefWatson uses Social Network

> CodeChef problem code [`BOOKCHEF`](https://www.codechef.com/problems/BOOKCHEF) &middot; difficulty **1610** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Sorting |
| **Technique** | Sorting on a composite key |
| **Time** | $O(M \log M)$ |
| **Space** | $O(N + M)$ |
| **Roadmap course** | Jump from 2* to 3* (Level 3) |

## Question

Chef Watson uses a social network called ChefBook, which has a new feed consisting of posts by his friends. Each post can be characterized by **f** - the identifier of the friend who created the post, **p** - the popularity of the post(which is pre-calculated by ChefBook platform using some machine learning algorithm) and **s** - the contents of the post which is a string of lower and uppercase English alphabets.

Also, Chef has some friends, which he has marked as *special*.

The algorithm used by ChefBook for determining the order of posts in news feed is as follows:

- Posts of *special* friends should be shown first, irrespective of popularity. Among all such posts the popular ones should be shown earlier.

- Among all other posts, popular posts should be shown earlier.

Given, a list of identifiers of Chef's *special* friends and a list of posts, you have to implement this algorithm for engineers of ChefBook and output the correct ordering of posts in the new feed.

**Input**

First line contains **N**, number of *special* friends of Chef and **M**, the number of posts. Next line contains **N** integers **A_1, A_2, ..., A_N** denoting the identifiers of *special* friends of Chef. Each of the next **M** lines contains a pair of integers and a string denoting **f**, **p** and **s**, identifier of the friend who created the post, the popularity of the post and the contents of the post, respectively.

**Output**

Output correct ordering of posts in news feed in **M** lines. Output only the contents of a post.

**Constraints**

- **1** ≤ **N, M** ≤ **10^3**

  - **1** ≤ **A_i, f, p** ≤  **10^5**

  - **1** ≤ **length(s)** ≤  **100**

  - It is guaranteed that no two posts have same popularity, but the same friend might make multiple posts.

## Constraints

- 1 ≤ N, M ≤ 10^3
  - 1 ≤ A_i, f, p ≤  10^5
  - 1 ≤ length(s) ≤  100

## Sample

**Sample input**

```
2 4
1 2
1 1 WhoDoesntLoveChefBook
2 2 WinterIsComing
3 10 TheseViolentDelightsHaveViolentEnds
4 3 ComeAtTheKingBestNotMiss
```

**Sample output**

```
WinterIsComing
WhoDoesntLoveChefBook
TheseViolentDelightsHaveViolentEnds
ComeAtTheKingBestNotMiss
```

<details><summary>Explanation</summary>

Friends $1$ and $2$ are special. Among them, friend $2$'s post has more popularity. Thus, the first two posts of the feed would be of friend $2$ and $1$ respectively.
From remaining friends, i.e., friends $3$ and $4$, friend $4$'s post has more popularity. Thus, it would be shown earlier in the feed.
The final ordering of posts is $2\rightarrow 1\rightarrow 4\rightarrow 3$.

</details>

## Approach

The ordering rule has two levels, which map directly onto a **tuple sort key**:

1. posts from *special* friends come first, regardless of popularity;
2. within each of those two groups, higher popularity comes first.

So sort by `(not special, -popularity)`. The first component is `False` (i.e. $0$) for special posts and `True` ($1$) otherwise, so special posts sort ahead; the negated popularity turns Python's ascending sort into a descending one on that field.

Expressing both levels in one key avoids a two-pass partition-and-merge, and makes the precedence explicit — the special flag dominates because it comes first in the tuple.

Membership of the special list is tested against a `set`, giving $O(1)$ lookups rather than an $O(N)$ scan per post.

The guarantee that **no two posts share a popularity** means the sort is fully determined, so no stability question arises and any correct implementation produces the same order.

In the sample, friends $1$ and $2$ are special. Their posts have popularities $1$ and $2$, so they lead with the more popular first — `WinterIsComing` then `WhoDoesntLoveChefBook`. The remaining posts follow by popularity, so the $10$-popularity post from friend $3$ beats the $3$-popularity post from friend $4$ — note it outranks both special posts on popularity yet still comes after them.

Only the contents are printed, not the identifiers. There is **no $T$**: the first line holds $N$ and $M$.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    n, m = int(data[0]), int(data[1])       # no test-case count
    special = set(data[2:2 + n])
    pos = 2 + n
    posts = []
    for _ in range(m):
        friend, popularity, text = data[pos], int(data[pos + 1]), data[pos + 2]
        pos += 3
        # Special first, then popularity descending.
        posts.append((friend not in special, -popularity, text))
    posts.sort()
    sys.stdout.write("\n".join(p[2].decode() for p in posts) + "\n")


main()
```

## Complexity

- **Time:** $O(M \log M)$
- **Space:** $O(N + M)$

## Edge cases

- **Two sort keys in one tuple.** `friend not in special` puts special friends first (since `False < True`), and `-popularity` orders each group most-popular first — so one `sort` does the whole algorithm.
- **A special friend's post outranks every non-special post** regardless of popularity, which is exactly what the sample shows: a post of popularity $1$ from a special friend beats one of popularity $10$ from another.
- **Within the special group popularity still rules**, so the two special posts come out as $2$ then $1$.
- **Negating the popularity is what gives a descending order** inside an ascending sort, avoiding a custom comparator.
- **No tie rule is specified** for equally popular posts in the same group, so the post text serves as a deterministic third key.
- **There is no test-case count**: the first line holds $N$ and $M$ together.
- **Friend ids are matched as raw byte tokens** against the special set, safe because the input has no leading zeros.

## Dry run

Special friends $\{1, 2\}$.

| post | friend | special? | popularity | sort key |
|---|---:|:---:|---:|---|
| `WhoDoesntLoveChefBook` | 1 | yes | 1 | $(\text{False}, -1)$ |
| `WinterIsComing` | 2 | yes | 2 | $(\text{False}, -2)$ |
| `TheseViolentDelights…` | 3 | no | 10 | $(\text{True}, -10)$ |
| `ComeAtTheKing…` | 4 | no | 3 | $(\text{True}, -3)$ |

Sorted: `WinterIsComing`, `WhoDoesntLoveChefBook`, `TheseViolentDelights…`, `ComeAtTheKing…`

---

Same problem in rating order (#347 of 486): [../../by-rating/347-BOOKCHEF.md](../../by-rating/347-BOOKCHEF.md)
