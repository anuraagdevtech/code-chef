[&larr; 483. Digit Removal](DIGITREM.md) &middot; [Index](../../README.md) &middot; [491. Little Elephant and Bamboo &rarr;](LEBAMBOO.md)

# 490. Racing

> CodeChef problem code [`RACINGEN`](https://www.codechef.com/problems/RACINGEN) &middot; difficulty **1759** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Basic Math |
| **Technique** | Energy balance gives the shortest completion time |
| **Time** | $O(1)$ per test case |
| **Space** | $O(1)$ |
| **Roadmap course** | 1600 to 1800 difficulty problems (Level 3) |

## Question

Ann is going to take part in a race. At the start, she has $X$ units of energy. For each subsequent **second**, she can decide to run or to rest (she must perform the chosen action during the whole second). If she runs, she loses one unit of energy during that second and if she rests, she gains one unit of energy during that second. However, if Ann decides to rest when she has $X$ units of energy, she does not gain any extra energy. Naturally, she cannot decide to run if she has $0$ units of energy.

Ann needs to run for $R$ **minutes** to reach the goal and she needs to reach it within $M$ **minutes**. Is Ann able to finish the race on time?

**Input**
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first and only line of each test case contains three space-separated integers $X$, $R$ and $M$.

**Output**
For each test case, print a single line containing the string `"YES"` if Ann is able to finish the race or `"NO"` otherwise (without quotes).

**Constraints**
- $1 \le T \le 10^5$
- $1 \le X,R,M \le 10^9$

**Subtasks**
**Subtask #1 (100 points):** original constraints

## Constraints

- $1 \le T \le 10^5$
- $1 \le X,R,M \le 10^9$

## Sample

**Sample input**

```
2
60 3 5
60 3 4
```

**Sample output**

```
YES
NO
```

<details><summary>Explanation</summary>

**Example case 1:** Ann can run during the first, third and fifth minute. There are other possible solutions.

**Example case 2:** It is not possible for Ann to finish the race within four minutes.

</details>

## Approach

Convert both durations to seconds. For $r$ running seconds, the initial $X$ energy pays for the first $X$ runs; any remaining run requires a resting second beforehand. Hence the least elapsed time is $r+\max(0,r-X)$.

This lower bound is attainable by running until energy is exhausted, then alternating rest and run. Compare it to the deadline.

## Solution (Python)

```python
import sys


def main() -> None:
    tokens = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(tokens))):
        x, r, m = (int(next(tokens)) for _ in range(3))
        r *= 60
        out.append('YES' if r + max(0, r-x) <= 60*m else 'NO')
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
```

## Complexity

- **Time:** $O(1)$ per test case
- **Space:** $O(1)$
- Auxiliary space excludes the buffered input and output.

## Edge cases

- Energy is in seconds, while the input durations are in minutes.
- No rest is needed when $X\geq60R$.
- Finishing exactly at the deadline is allowed.

## Dry run

With `X=60, R=3`, running needs `180` seconds and resting needs `120`, totaling `300`. A five-minute deadline succeeds; four minutes fails.

> CodeChef tags: `Algorithms`, `Constructive`

---

Same problem in rating order (#487 of 735): [../../by-rating/487-RACINGEN.md](../../by-rating/487-RACINGEN.md)
