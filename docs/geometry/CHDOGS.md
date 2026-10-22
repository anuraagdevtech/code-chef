[&larr; 247. Triangle Classification](TRIANGCL.md) &middot; [Index](../../README.md) &middot; [383. Polygon Relationship &rarr;](POLYREL.md)

# 252. Chef and Three Dogs

> CodeChef problem code [`CHDOGS`](https://www.codechef.com/problems/CHDOGS) &middot; difficulty **1473** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Geometry |
| **Technique** | Pursuit curve by relative closing speed |
| **Time** | $O(1)$ per test case |
| **Space** | $O(1)$ |
| **Roadmap course** | 1400 to 1600 difficulty problems (Level 2) |

## Question

Chef has three dogs sitting at the vertices of an equilateral triangle. The length of each side of the triangle equals to **s** meters. Chef gives the command "Start!" and each dog starts to run with constant speed **v** meters per second. At each moment, each dog is running towards the dog just right to him (in counter-clockwise direction). Therefore, their trajectories are forming some spirals that converging to one point as illustrated below.

<img src="https://s3.amazonaws.com/codechef_shared/download/upload/mice3.gif" style="width:150px;height:130px;" alt="mice3.gif" />

How long does it takes dogs to meet each other after the command "Start!"?

**Input**

The first line of the input contains an integer **T** denoting the number of test cases. The description of **T** test cases follows.

The only line of each test case contains two space-separated integers **s** and **v**.

**Output**

For each test case, output a single line containing a real number corresponding to the answer of the problem. The answer will be considered correct if its absolute or relative error does not exceed 10^-6.

**Constraints**

- **1** ≤ **T** ≤ **10**

- **1** ≤ **s, v** ≤ **10^9**

**Subtasks**

- Subtask #1 (40 points): **1** ≤ **s, v** ≤ **10**

- Subtask #2 (60 points): **original constraints**

## Constraints

- 1 ≤ T ≤ 10
- 1 ≤ s, v ≤ 10^9

## Sample

**Sample input**

```
2
2 5
1 1000000000
```

**Sample output**

```
0.266667
0.0000001
```

<details><summary>Explanation</summary>

Due to the triangle being very small, but the dogs running extremely fast, they will meet after less than 1e-6 seconds. Thus, due to remark about absolute or relative error in the output section, any answer within [0, 1e-6] will be considered correct.

</details>

## Approach

This is the classic **three-dog (or mice) pursuit problem**. By symmetry the configuration stays an equilateral triangle at every instant — it merely shrinks and rotates — so the whole spiral can be analysed without touching the trajectory itself.

Consider one dog chasing its target. The chaser moves at speed $v$ straight toward the target, closing the gap at rate $v$. Meanwhile the target also moves at speed $v$, but along a direction making a $120°$ angle with the line joining them, so its motion changes the separation at rate $v\cos 120° = -v/2$ — it recedes at only half speed.

The net closing rate is therefore constant:

$$v - v\cos 120° = v\left(1 + \tfrac{1}{2}\right) = \tfrac{3}{2}v$$

Starting from separation $s$, the dogs meet after

$$t = \frac{s}{\tfrac{3}{2}v} = \frac{2s}{3v}$$

The spiral paths never need to be integrated — reducing the chase to a one-dimensional closing rate is the entire trick, and it works because the symmetry keeps that angle fixed at $120°$ forever.

Checking the first sample: $s=2, v=5$ gives $4/15 = 0.2666\overline{6}$.

The answer is judged with a tolerance of $10^{-6}$ absolute **or** relative, not by exact text. The second sample makes that visible: $s=1, v=10^9$ gives roughly $6.7 \times 10^{-10}$, and the published expected output is written as `0.0000001` — a different numeral entirely, but well inside the absolute tolerance. The repository therefore checks this one numerically rather than by string comparison.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        s, v = int(data[1 + 2 * i]), int(data[2 + 2 * i])
        # Symmetry keeps the chase angle at 120 degrees, so the gap closes at
        # a constant v - v*cos(120) = 1.5v.
        out.append(f"{2 * s / (3 * v):.9f}")
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(1)$ per test case
- **Space:** $O(1)$

## Edge cases

- **The symmetry is what makes this constant.** Three dogs at the corners of an equilateral triangle, each chasing the next, keep the configuration equilateral forever — so the chase angle stays at $120^\circ$ and the closing speed never changes.
- **The closing rate is $v - v\cos 120^\circ = 1.5v$**, giving a meeting time of $s / 1.5v = 2s/(3v)$ — no integration of the pursuit curve is needed.
- **The answer can be minute.** With $s = 1$ and $v = 10^9$ it is about $6.7 \times 10^{-10}$, so plenty of decimal places must be printed rather than a default six.
- **The sample's second answer is $10^{-7}$ while this prints $6.7 \times 10^{-10}$**, and both are accepted: the checker allows an absolute error of $10^{-6}$, and at this magnitude everything under the tolerance passes. That is why this problem needs a special judge rather than exact matching.
- **The division must be floating point** — integer division would floor to $0$ for every case where $2s < 3v$.
- **$s, v$ up to $10^9$** put the answer anywhere from $\sim\!10^{-9}$ to $\sim\!6.7 \times 10^8$.

## Dry run

| $s$ | $v$ | $2s/(3v)$ | printed |
|---:|---:|---|---|
| 2 | 5 | $4/15$ | `0.266666667` |
| 1 | $10^9$ | $2/(3 \times 10^9)$ | `0.000000001` |

Each dog's velocity has a component $v\cos 120^\circ = -v/2$ along the line to its target, so the gap of $s$ shrinks at $1.5v$ throughout.

> CodeChef tags: `Mathematics`, `Basic Math`

---

Same problem in rating order (#271 of 486): [../../by-rating/271-CHDOGS.md](../../by-rating/271-CHDOGS.md)
