---
topic: Sets
subtopic: Intersection and complement of a union
time: $O(M + K)$ per test case
space: $O(M + K)$
---
The two sequences are given as **membership lists**, so both questions are set operations once they are loaded into sets. Let $I$ be the ignored files and $T$ the tracked ones.

"Tracked **and** ignored" is the intersection:

$$|T \cap I|$$

"Untracked **and** unignored" means in neither list, which is the complement of the union:

$$N - |T \cup I|$$

The second one is where a careless solution goes wrong: counting $(N - M) + (N - K)$ double-counts, and subtracting $M + K$ from $N$ ignores the overlap. Taking the union first handles it correctly, because a file in both lists must be discounted only once.

Note the two counts are not complementary — the files that are tracked-but-unignored and ignored-but-untracked belong to neither answer. In the first sample $N = 7$ with $I = \{1,4,6,7\}$ and $T = \{1,2,3,4,6,7\}$: the intersection is all of $I$, giving $4$, and the union has size $6$, leaving exactly one file (number $5$) in neither, giving $1$.

Since the input guarantees both sequences are strictly increasing, there are no duplicates to worry about, and the raw tokens can be used as set elements directly without parsing them to integers.
