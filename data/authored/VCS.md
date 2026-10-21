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

## Edge cases

- **Files in both lists must not be double-counted.** In the second row $M = K = 2$ and $N = 4$, so $N - M - K$ gives $0$, but file $4$ appears in both lists and the true answer is $1$. The union, not the sum, is what must be subtracted.
- **A file can be in neither list**: file $5$ in the first row and files $1$ and $2$ in the second.
- **A file can be in both**, which is what the first number counts — the first row has all four ignored files also tracked.
- **Both lists are strictly increasing**, so neither contains an internal duplicate and the sets can be built straight from the tokens.
- Comparing the raw byte tokens is safe here because the input has no leading zeros, so each number has exactly one spelling.

## Dry run

Second sample: $N = 4$, ignored $\{1, 4\}$, tracked $\{3, 4\}$.

| file | ignored? | tracked? | counted as |
|---:|:---:|:---:|---|
| 1 | yes | no | — |
| 2 | no | no | **untracked and not ignored** |
| 3 | no | yes | — |
| 4 | yes | yes | **both** |

Output `1 1`. Note $N - M - K = 0$ would be wrong, because file $4$ is subtracted twice.
