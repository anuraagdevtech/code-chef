[&larr; 22. Air Conditioner Temperature](ACTEMP.md) &middot; [Index](../../README.md) &middot; [55. Water Mixing &rarr;](WTRMIXING.md)

# 32. Bus  Seat Numbering

> CodeChef problem code [`SEATNUMBER`](https://www.codechef.com/problems/SEATNUMBER) &middot; difficulty **613** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Conditionals & Case Work |
| **Technique** | Decomposing an index into deck and position |
| **Time** | $O(1)$ per test case |
| **Space** | $O(1)$ |
| **Roadmap course** | 500 to 1000 difficulty rating (Level 1) |

## Question

There is a bus with 30 seats. The seats are numbered from 1 to 30, and the numbering is as depicted in this image.

 <img src="https://cdn.codechef.com/download/Contest+images/START91/DvCx7Fn.png" width="550">

As can be seen in the image, the bus is divided into two decks - The Lower deck, and the Upper deck, with 15 seats each. And some of the seats come as Single and some as Double. For example, Seats 1 and 2 are Double, whereas Seat 11 is a Single.

You will be given a Seat number, and your job is to classify it as one of these 4 types:
- Lower Single
- Lower Double
- Upper Single
- Upper Double

**Input**

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of a single line of input which contains a single integers $N$ — the seat number.

**Output**

For each test case, output on a new line, the type of seat.

## Constraints

- $1 \leq T \leq 100$
- $1 \leq N \leq 30$

## Sample

**Sample input**

```
5
6
28
16
13
10
```

**Sample output**

```
Lower Double
Upper Single
Upper Double
Lower Single
Lower Double
```

<details><summary>Explanation</summary>

**Testcase 1:** The seat number 6 is in the Lower deck, and it is a Double. Hence the output is "Lower Double".

**Testcase 2:** The seat number 28 is in the Upper deck, and it is a Single. Hence the output is "Upper Single".

**Testcase 3:** The seat number 16 is in the Upper deck, and it is a Double. Hence the output is "Upper Double".

**Testcase 4:** The seat number 13 is in the Lower deck, and it is a Single. Hence the output is "Lower Single".

**Testcase 5:** The seat number 10 is in the Lower deck, and it is a Double. Hence the output is "Lower Double".

</details>

## Approach

The answer has two independent halves — which deck, and single or double — so the clean approach is to compute each separately and join them, rather than enumerating all four combinations.

**Deck.** There are $30$ seats split into two decks of $15$. Seats $1$–$15$ are Lower and $16$–$30$ are Upper, so the test is `n <= 15`.

**Position within the deck.** Reduce the seat to its offset inside its own deck:

$$p = ((N - 1) \bmod 15) + 1$$

The $-1$ and $+1$ convert to and from zero-based indexing, which is what makes the modulo land in the range $1..15$ rather than $0..14$. Seat $16$ maps to $p = 1$, seat $28$ maps to $p = 13$.

**Single or double.** Within each deck the first $10$ seats form five double berths and the last $5$ are singles, so $p \leq 10$ is Double and $p \geq 11$ is Single. This matches every anchor the problem gives: seats $1$ and $2$ are Double, seat $11$ is Single, and the samples confirm $p = 6, 10$ Double against $p = 13$ Single — the latter twice, once as seat $13$ (Lower) and once as seat $28$ (Upper).

Because the two decks are numbered identically, computing $p$ once and reusing it for both decks avoids writing the seat layout twice. Combining two independent binary decisions this way turns four cases into two.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        n = int(data[1 + i])
        deck = "Lower" if n <= 15 else "Upper"
        # Offset inside the deck, 1..15; the layout repeats per deck.
        p = (n - 1) % 15 + 1
        kind = "Double" if p <= 10 else "Single"
        out.append(f"{deck} {kind}")
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(1)$ per test case
- **Space:** $O(1)$

## Edge cases

- **$N = 15$ then $N = 16$**, the deck boundary: $15$ is the last lower seat (position $15$, so Single) and $16$ is the first upper one (position $1$, so Double). The sample includes $16$, which is where the modulo has to be right.
- **The `(n - 1) % 15 + 1` form matters**: a plain `n % 15` sends seat $15$ to position $0$ and breaks both the deck's last seat and the Single test.
- **$N = 10$ then $N = 11$**, the berth boundary: position $10$ is still Double, $11$ is Single.
- **First and last seats**: $N = 1$ is Lower Double, $N = 30$ is Upper Single.

## Dry run

| $N$ | deck ($\leq 15$?) | position $(N-1)\bmod 15 + 1$ | berth ($\leq 10$?) | output |
|---:|---|---:|---|---|
| 6 | Lower | 6 | Double | `Lower Double` |
| 28 | Upper | 13 | Single | `Upper Single` |
| 16 | Upper | 1 | Double | `Upper Double` |
| 13 | Lower | 13 | Single | `Lower Single` |
| 10 | Lower | 10 | Double | `Lower Double` |

Row 3 wraps to position $1$; row 5 sits exactly on the Double limit.

> CodeChef tags: `Basic Programming Concepts`, `Algorithms`

---

Same problem in rating order (#39 of 486): [../../by-rating/039-SEATNUMBER.md](../../by-rating/039-SEATNUMBER.md)
