[&larr; 610. Appy Loves One](HMAPPY1.md) &middot; [Index](../../README.md) &middot; [626. Subarray Removal &rarr;](REMSUBARR.md)

# 613. Chef and Sub Array 

> CodeChef problem code [`CHEFSUBA`](https://www.codechef.com/problems/CHEFSUBA) &middot; difficulty **1908** &middot; time limit **0.5s**

| | |
|---|---|
| **Topic** | Arrays |
| **Technique** | Window sums on the doubled array, then a sliding maximum per rotation |
| **Time** | $O(N + P)$ |
| **Space** | $O(N)$ |
| **Roadmap course** | Rise from 3* to 4* (Level 4) |

## Question

Chef has a binary array **A** of length **N**. He also has a frame that can focus on at max **K** consecutive elements of the array.

Chef has a lovely dog which likes to do following two things.

- Shifting the array **A** to the right by one element (**N**-th element becomes 1_st, 1_st becomes 2_nd and so on)

- Asking Chef what is the maximal number of elements equal to 1, that can be captured by a frame (frame can capture **not more** than **K** consecutive elements of array).

Help Chef entertain his Dog!

**Input**

The first line of each test case contains three integers **N**, **K** and **P** denoting the number of elements in array **A**, size of a frame and the number of Dog's requests.

The second line contains **N** space-separated integers **A**_1, **A**_2, ..., **A_N** denoting the elements of array.

The third line contains string consisting of **P** characters, i-th character stands for dog's i-th question and equals **'!'** if  Dog shifts the array and **'?'** if dog asks what is the maximal number of ones captured by the frame.

**Output**

For each Dog's question output a single line containing an integer corresponding to the answer of the question.

**Constraints**

- 1 ≤ **N, K, P** ≤ 10^5

- 0 ≤ **A_i** ≤ 1

**Subtasks**

- **Subtask #1  (30 points)** **N, K, P** ≤ 10^3

- **Subtask #2 (70 points)** Original constraints.

## Constraints

- 1 ≤ N, K, P ≤ 10^5
- 0 ≤ A_i ≤ 1

## Sample

**Sample input**

```
5 3 4
1 0 0 1 1
?!!?
```

**Sample output**

```
2
3
```

<details><summary>Explanation</summary>

**Example case 1.**

For the first question , Chef can pick last **3** elements (or last two, no matter) for his frame,
and will have **2** elements equal **1**.

After first shift (exclamation mark) array will become: **1 1 0 0 1**.

After second shift (exclamation mark) array will become: **1 1 1 0 0**.

Now for the second question Chef can pick first **3** elements for his frame,
and will have **3** elements equal **1**.

</details>

## Approach

A shift just moves the start of a circular array. Double the array; after $s$ right shifts the current array is the length-$N$ window starting at $(-s) \bmod N$.

The values are 0 or 1, so the best frame always uses the full width $K$ (capped at $N$). Let `frame_sum[i]` be the number of ones in positions $i \dots i+K-1$ of the doubled array, from prefix sums. A frame fits inside the rotation starting at $t$ when its start lies in $[t, t + N - K]$, so the answer for that rotation is the maximum of `frame_sum` over a window of $N - K + 1$ consecutive starts - a sliding-window maximum with a monotone deque. All $N$ rotations are precomputed and each `?` is a lookup.

## Solution (Python)

```python
import sys
from collections import deque


def main() -> None:
    tokens = iter(sys.stdin.buffer.read().split())
    n, k, q = (int(next(tokens)) for _ in range(3))
    k = min(k, n)
    bits = [int(next(tokens)) for _ in range(n)]
    queries = next(tokens)
    bits += bits
    prefix = [0]
    for x in bits:
        prefix.append(prefix[-1] + x)
    frame_sum = [prefix[i + k] - prefix[i] for i in range(2 * n - k + 1)]
    width = n - k + 1
    window = deque()
    answers = []
    for i, x in enumerate(frame_sum):
        while window and frame_sum[window[-1]] <= x:
            window.pop()
        window.append(i)
        while window[0] <= i - width:
            window.popleft()
        if i >= width - 1:
            answers.append(frame_sum[window[0]])
    start = 0
    out = []
    for ch in queries:
        if ch == 33:
            start = (start - 1) % n
        else:
            out.append(str(answers[start]))
    print('\n'.join(out))


if __name__ == "__main__":
    main()
```

## Complexity

- **Time:** $O(N + P)$
- **Space:** $O(N)$
- Auxiliary space excludes the buffered input and output.

## Edge cases

- $K \ge N$: the frame sees the whole array, and the answer is the total number of ones.
- Frames may not wrap around the end of the current array - that is why the window of valid starts has length $N - K + 1$.
- Only the shift count modulo $N$ matters.
- The request string is read as bytes: 33 is `!`.

## Dry run

`A = [1, 0, 0, 1, 1]`, `K = 3`, requests `?!!?`.

Doubled array `1 0 0 1 1 1 0 0 1 1`, frame sums by start `1 1 2 3 2 1 1 2`.

- `?` with 0 shifts: valid starts are 0-2 with sums `1 1 2`, answer 2.
- two shifts later the rotation starts at 3 (`1 1 1 0 0`): starts 3-5 have sums `3 2 1`, answer 3.

---

Same problem in rating order (#551 of 735): [../../by-rating/551-CHEFSUBA.md](../../by-rating/551-CHEFSUBA.md)
