[&larr; 175. Make them equal](MAKEEQUAL.md) &middot; [Index](../../README.md) &middot; [199. Maximise the Subsequence Sum &rarr;](SIGNFLIP.md)

# 187. Magical Doors

> CodeChef problem code [`MAGDOORS`](https://www.codechef.com/problems/MAGDOORS) &middot; difficulty **1355** &middot; time limit **1.5s**

| | |
|---|---|
| **Topic** | Greedy |
| **Technique** | Tracking a global flip as parity |
| **Time** | $O(|S|)$ per test case |
| **Space** | $O(1)$ |
| **Roadmap course** | Level up from 1* to 2* (Level 2) |

## Question

Chef wants to cross a hallway of $N$ doors. These $N$ doors are represented as a string. Each door is initially either open or close, represented by $1$ or $0$ respectively. Chef is required to go through all the doors one by one in the order that they appear, starting from the leftmost door and moving only rightwards at each step.

To make the journey easier, Chef has a magic wand, using which Chef can flip the status of all the doors at once.
Determine the minimum number of times Chef has to use this wand to cross the hallway of doors.

For example, the doors are $10011$. Chef will start from the left and enter the first door. After passing through that door, the magic wand is waved. This flips the string to $01100$. Now Chef passes through the next two doors in one go. Again, just before reaching the 4th door, the magic wand is waved. Now that the string is in its original state, Chef passes through the last two doors as well.
The minimum number of times the magic wand needed to be used here was $2$.

**Input**

- First line will contain $T$, number of testcases. Then the testcases follow.
- Each testcase contains of a single string $S$, representing the doors as given in the problem.

**Output**

For each test case, print a single line containing one integer denoting the minimum number of times the magic wand needs to be used.

## Constraints

- $1 \leq T \leq 10^5$
- $1 \leq |S| \leq 10^5$
- Sum of $|S|$ over all test cases $ \leq 2 \cdot 10^6 $

## Sample

**Sample input**

```
3
111
010
10011
```

**Sample output**

```
0
3
2
```

<details><summary>Explanation</summary>

- **Test Case $1$**: Since all the doors are already open, Chef doesn't need to use the magic wand at all.
- **Test Case $2$**: Chef will use the wand the first time to open door $1$. This operation makes the string "101". Chef again needs to use the wand to open door $2$, and then one last time to open door $3$. In total, Chef used the wand $3$ times.
- **Testcase $3$**: As explained in the problem statement above.

</details>

## Approach

Waving the wand flips **every** door at once, so the board is never partially modified — after $k$ waves, the door written as $S_i$ currently shows

$$S_i \oplus (k \bmod 2)$$

That is the key simplification: the entire history of wand use collapses into a single parity bit. There is no need to maintain a mutable copy of the string, which would be $O(n)$ work per wave and far too slow.

Walking left to right, Chef needs each door open when he reaches it. If the door's effective value is $0$, he has no choice but to wave — and because waving is the only tool, waving exactly then is forced, so the greedy is also optimal. Flipping earlier would only have to be undone.

So the algorithm is: hold a parity bit, and for each character, if `S[i] ^ parity == 0`, flip the parity and increment the counter.

Sample case 2, `010`, is the worst case: every door is closed when reached, so the wand is used three times — once per door. Sample case 1, `111`, never needs it. Sample case 3, `10011`, needs two waves, matching the statement's own walkthrough.

Note that a wave is counted even if it happens immediately before the first door, so the answer can equal the string length. With the sum of $|S|$ reaching $2 \times 10^6$, the $O(1)$-per-character pass and bulk input reading are both necessary.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        s = data[1 + i]
        waves = 0
        parity = 0
        for ch in s:
            # Effective state is the written digit flipped by the wave parity.
            if (ch - 48) ^ parity == 0:
                waves += 1
                parity ^= 1
        out.append(str(waves))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(|S|)$ per test case
- **Space:** $O(1)$

## Edge cases

- **A wave flips every door at once**, so a door's effective state is its written digit XOR the number of waves cast so far. Only the *parity* of that count matters, so the string is never mutated and the scan stays $O(|S|)$.
- **All doors already open** (`111`) → $0$ waves.
- **Alternating** (`010`) → every door needs a wave, giving $|S| = 3$: each wave opens the current door but closes the next one, which is the worst case.
- **The greedy is forced, not a choice.** A closed door must be opened to pass it, and the only way is a wave; so the count is determined and no search is needed.
- **A wave is cast only when standing at a closed door**, so after it the door is open and progress is guaranteed.
- **Sum of $|S|$ up to $2 \cdot 10^6$**: bytes are iterated as integer codes with `ch - 48`, with no decoding to `str`.

## Dry run

Third sample: `10011`.

| door | written | wave parity | effective | wave cast? | waves |
|---:|---:|---:|---:|:---:|---:|
| 1 | 1 | 0 | 1 | no | 0 |
| 2 | 0 | 0 | 0 | **yes** | 1 |
| 3 | 0 | 1 | 1 | no | 1 |
| 4 | 1 | 1 | 0 | **yes** | 2 |
| 5 | 1 | 0 | 1 | no | 2 |

Output `2`. Note door $3$ is open only because of the wave cast at door $2$.

---

Same problem in rating order (#216 of 486): [../../by-rating/216-MAGDOORS.md](../../by-rating/216-MAGDOORS.md)
