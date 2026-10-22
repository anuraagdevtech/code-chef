# 195. Password

> CodeChef problem code [`PASSWD`](https://www.codechef.com/problems/PASSWD) &middot; difficulty **1470** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Strings |
| **Technique** | Several predicates, one with a positional restriction |
| **Time** | $O(|S|)$ per test case |
| **Space** | $O(1)$ |
| **Roadmap course** | Level up from 1* to 2* (Level 2) |

## Question

Chef is planning to setup a secure password for his Codechef account. For a password to be secure the following conditions should be satisfied:

1) Password must contain at least one lower case letter $[a-z]$;

2) Password must contain at least one upper case letter [A−Z] strictly inside (first or the last character won’t be considered)

3) Password must contain at least one digit $[0-9]$ strictly inside;

4) Password must contain at least one special character from the set $\{$ '@', '\#', '%', '&', '?' $\}$ strictly inside;

5) Password must be at least $10$ characters in length, but it can be longer.

Chef has generated several strings and now wants you to check whether the passwords are secure based on the above criteria. Please help Chef in doing so.

**Input**
- First line will contain $T$, number of testcases. Then the testcases follow.
- Each testcase contains of a single line of input, string $S$.

**Output**
For each testcase, output in a single line "YES" if the password is secure and "NO" if it is not.

**Constraints**
- $1 \leq |S| \leq 20$
- All the characters in $S$ are one of the following: lower case letters $[a-z]$, upper case letters $[A-Z]$, digits $[0-9]$, special characters from the set $\{$ '@', '\#', '%', '&', '?' $\}$
- Sum of length of strings over all tests is atmost $10^6$

## Constraints

- $1 \leq |S| \leq 20$
- All the characters in $S$ are one of the following: lower case letters $[a-z]$, upper case letters $[A-Z]$, digits $[0-9]$, special characters from the set $\{$ '@', '\#', '%', '&', '?' $\}$
- Sum of length of strings over all tests is atmost $10^6$

## Sample

**Sample input**

```
3
#cookOff#P1
U@code4CHEFINA
gR3@tPWD
```

**Sample output**

```
NO
YES
NO
```

<details><summary>Explanation</summary>

**Example case 1:** Condition $3$ is not satisfied, because the only digit is not strictly inside.

**Example case 2:** All conditions are satisfied.

**Example case 3:** Condition $5$ is not satisfied, because the length of this string is 8.

</details>

## Approach

Five conditions must all hold, and the one that makes this more than a checklist is **where** each character is allowed to count.

- **Lowercase** — anywhere in the string.
- **Uppercase**, **digit**, **special** — each must appear *strictly inside*, meaning the first and last characters do not count.
- **Length** at least $10$.

So the interior is the slice `s[1:-1]`, and three of the four character tests run against that slice while the lowercase test runs against the whole string. Taking the interior once and reusing it keeps the four tests symmetrical and avoids repeating the index arithmetic.

Sample case 1, `#cookOff#P1`, is built precisely on this distinction. It is long enough, has lowercase letters, has an uppercase `O` inside and a special `#` inside — but its only digit is the final `1`, which sits on the boundary and therefore does not count. The answer is `NO`.

Sample case 3, `gR3@tPWD`, satisfies every character rule inside but is only $8$ characters long, failing the length check alone.

Sample case 2 passes all five.

The length check should come first in practice: for a string shorter than $3$ the interior slice is empty, and while that merely makes the other tests false rather than erroring, checking the cheap condition first is the clearer order.

The special set is exactly $\{$ `@`, `#`, `%`, `&`, `?` $\}$ — five characters, no more.

## Solution (Python)

```python
import sys

SPECIAL = set("@#%&?")


def secure(s: str) -> bool:
    if len(s) < 10:
        return False
    inside = s[1:-1]        # the first and last characters do not count
    return (any(c.islower() for c in s)
            and any(c.isupper() for c in inside)
            and any(c.isdigit() for c in inside)
            and any(c in SPECIAL for c in inside))


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = ["YES" if secure(data[1 + i].decode()) else "NO" for i in range(t)]
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(|S|)$ per test case
- **Space:** $O(1)$

## Edge cases

- **The lowercase rule applies to the whole string; the other three apply strictly inside.** That asymmetry is in the statement, and the code mirrors it — `islower` is tested over `s` while the rest are tested over `s[1:-1]`.
- **The interior exclusion is what fails the first row.** `#cookOff#P1` has a digit, but it is the final character, so it does not count and the answer is `NO`.
- **The length bar is $10$**, and the third row (`gR3@tPWD`, eight characters) fails on that alone despite satisfying every other rule.
- **The length check must come first**, or `s[1:-1]` on a very short string would be tested — harmlessly here, but the ordering keeps the logic honest.
- **The special set is exactly `@#%&?`**, so a character like `!` or `$` does not qualify even though it looks special; it also cannot appear, since the constraints limit the alphabet.
- **Sum of lengths up to $10^6$**: each predicate short-circuits, and the slice is taken once rather than per rule.

## Dry run

| password | length | lower (whole) | upper (inside) | digit (inside) | special (inside) | output |
|---|---:|:---:|:---:|:---:|:---:|---|
| `#cookOff#P1` | 11 | yes | `O`, `P` | **none** (the `1` is last) | `#` | `NO` |
| `U@code4CHEFINA` | 14 | yes | `C`,`H`,… | `4` | `@` | `YES` |
| `gR3@tPWD` | 8 | — | — | — | — | `NO` (too short) |

The first row's interior is `cookOff#P`, which has no digit at all.

---

Same problem in rating order (#267 of 486): [../../by-rating/267-PASSWD.md](../../by-rating/267-PASSWD.md)
