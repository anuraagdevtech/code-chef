# unrated &middot; Stable Quick Sort

> CodeChef problem code [`QCKSRT2`](https://www.codechef.com/problems/QCKSRT2) &middot; time limit **1s** &middot; Jump from 2* to 3* (Level 3)

## Topics used

| | |
|---|---|
| **Topic** | Sorting |
| **Technique** | Which pivot choices preserve stability |
| **CodeChef category** | main |
| **Time** | $O(n)$ |
| **Space** | $O(n)$ |

Same write-up grouped by topic: [../docs/sorting/QCKSRT2.md](../docs/sorting/QCKSRT2.md)

## Question

## Stable Quick Sort

<details>
<summary>
Recall the meaning of stable sort
</summary>

A sorting algorithm is stable, if the relative order of elements that are "equal" are maintained.

To demonstrate this, consider a list of pairs of integers, [(1, 2), (2, 3), (2, 1), (3, 2)]

If we want to sort this list such that tuples with lesser first elements occur first, but among tuples with the same first value, we are not bothered with the order of the second value, for example both (2, 3) and (2, 1) can occur in any order and are considered "equal" to each other.

If we run **any** stable sorting algorithm with the comparator defined as above, the relative order of the elements with the same first value will remain unchanged. For the above example, a stable sorting algorithm will not change the above array given, however an unstable sorting algorithm could print [(1, 2), (2, 1), (2, 3), (3, 2)] instead.

</details>

We know that the some implementations of quick sort are not stable, specifically the one given in the question [QCKSRT1](https://codechef.com/PEC2021F/problems/QCKSRT1) is not stable.

Here is an attempt at a modification of quick sort ([modified quick sort](https://pastebin.com/79VhLCXT)) that is intended to be stable.

Note that it is no longer "in-place", that is we create extra memory for copying the values of the array. (Not really relevant to this problem, just an interesting observation)

In the above code ([modified quick sort](https://pastebin.com/79VhLCXT)), the line for choosing the pivot is left blank. If we choose the pivot to be the first value of the array (i.e $arr[l]$), then the sorting algorithm will be stable, however if it is randomised, then it won't be.

You are to help fill the gap in the above algorithm while making it randomised.

Given an array $A$ (of size $n$), of pairs of integers, print (in increasing order) those indices (numbered from $0$ to $n-1$) that if chosen as a pivot for the above modified [quick sort](https://pastebin.com/79VhLCXT) algorithm, results in a stable sorting algorithm.

Note that the if the output of your program is a list of indices called $candidates$ then choosing the pivot as $arr[candidates[rand(0, len(candidates)-1)]]$ would result in a version of quick sort that is both randomised and stable.

You are given a [solution template](https://pastebin.com/mLg6vGmb), note that the input and output is taken care of in the template and you only need to correct the function $choose\_pivot$ in the above template.

### Input

Note that you can directly fill in the $choose\_pivot$ function given in the [solution template](https://pastebin.com/mLg6vGmb), so you do not have to worry about this section.

This is an explanation of how input is taken in the solution template.

There are two lines, the first line contains a single integer $n$, the size of the array.

The second line contains $2n$ space separated integers, the $2i^{th}$ and $(2i+1)^{th}$ numbers denote the $i^{th}$ tuple.

### Output

Note that you can directly fill in the $choose\_pivot$ function given in the [solution template](https://pastebin.com/mLg6vGmb), so you do not have to worry about this section.

This is an explanation of how output is done in the given solution template.

In the first line print $m$, the number of valid choices of indices for the pivot in the first iteration of quick sort of this array

In the second line print those indices (space separated) in increasing order.

### Constraints

$1 \leq n \leq 1000$

$-10^9 \leq $ every integer given $ \leq 10^9$

## Constraints

$1 \leq n \leq 1000$
$-10^9 \leq $ every integer given $ \leq 10^9$

## Sample

**Sample input**

```
4
1 2 2 3 2 1 3 2
```

**Sample output**

```
3
0 1 3
```

<details><summary>Explanation</summary>

The given array is $\{(1, 2), (2, 3), (2, 1), (3, 2)\}$

If we choose the index 2, then the partitioned array after the first iteration of quick sort becomes $\{(1, 2), (2, 1), (2, 3), (3, 2)\}$ which is affects the stability, since the order of $(2, 3)$ and $(2, 1)$ is changed.

</details>

## Approach

A sort is **stable** when elements comparing equal keep their original relative order. Here the pairs are compared on their first component only, so two pairs sharing a first component are "equal" and must not be reordered.

The modified quicksort partitions around the chosen pivot **element**, placing that element ahead of the others that tie with it. So picking a pivot that is **not the earliest** occurrence of its key drags it in front of equal elements that originally preceded it — breaking stability.

Hence a pivot index $i$ is safe exactly when no earlier index shares its first component:

$$\text{valid} \iff a_j \neq a_i \text{ for all } j < i$$

— that is, $i$ is the **first occurrence** of its key.

The sample makes this concrete. The pairs are $(1,2), (2,3), (2,1), (3,2)$ with keys $1, 2, 2, 3$. Index $2$ holds the *second* pair with key $2$, so choosing it pulls $(2,1)$ ahead of $(2,3)$ — exactly the reordering the explanation flags. Indices $0$, $1$ and $3$ are each the first sighting of their key, giving three valid choices: `0 1 3`.

Randomising over this restricted set is what reconciles the two goals: the pivot is still chosen at random (so the expected running time stays $O(n \log n)$), but only among choices that cannot disturb equal elements.

Tracking seen keys in a set makes this a single pass. Note that the second components are irrelevant throughout — they are the payload the stability requirement protects, not part of the comparison.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    n = int(data[0])                 # no test-case count
    # Pairs are compared on the first component only.
    keys = [data[1 + 2 * i] for i in range(n)]
    seen = set()
    valid = []
    for i, key in enumerate(keys):
        # Only the earliest occurrence of a key can be pivoted on without
        # pulling it ahead of equal elements that came before it.
        if key not in seen:
            seen.add(key)
            valid.append(i)
    sys.stdout.write(f"{len(valid)}\n" + " ".join(map(str, valid)) + "\n")


main()
```

## Complexity

- **Time:** $O(n)$
- **Space:** $O(n)$
