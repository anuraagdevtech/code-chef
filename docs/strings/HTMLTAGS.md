# 240. HTML Tags

> CodeChef problem code [`HTMLTAGS`](https://www.codechef.com/problems/HTMLTAGS) &middot; difficulty **1441** &middot; time limit **0.5s**

| | |
|---|---|
| **Topic** | Strings |
| **Technique** | Validating a format |
| **Time** | $O(|S|)$ per test case |
| **Space** | $O(1)$ |
| **Roadmap course** | 1400 to 1600 difficulty problems (Level 2) |

## Question

In addition to Competitive Programming, Chef recently developed an interest in Web Dev and started [learning HTML](https://www.codechef.com/learn/html). Now he wants to create his own HTML Code Editor. As a subproblem, he wants to check if a typed HTML closing tag has correct syntax or not.

A closing HTML tag **must**:
- Start with `"</"`
- End with `">"`
- Have only lower-case alpha-numeric characters as its body (between `"</"` and `">"`). That is, each character of the body should either be a digit or a lower-case English letter.
- Have a non-empty body.

Help Chef by printing `"Success"` if the tag is fine. If not, print `"Error"`.

**Input**

- The first line contains an integer $T$, the number of test cases. Then $T$ test cases follow.
- Each test case is a single line of input, a string describing the tag.

**Output**

For each test case, output in a single line, `"Success"` if it is a valid closing tag and `"Error"` otherwise (without quotes).

You may print each character of the string in uppercase or lowercase (for example, the strings `"SuccEss"`, `"success"`, `"Success"`, `"SUCCESS"` etc. will all be treated as identical).

## Constraints

- $1 \leq T \leq 1000$
- $1 \leq$ $\mathrm{length}(\mathrm{Tag})$ $\leq 1000$
- The characters of the string belong to the ASCII range $[33, 126]$ (note that this excludes space.)

## Sample

**Sample input**

```
5 
</h1>  
Clearly_Invalid  
</singlabharat>  
</5>  
<//aA>
```

**Sample output**

```
Success  
Error  
Success
Success
Error
```

<details><summary>Explanation</summary>

**Test Cases $1, 3, 4$:** The tags follow all mentioned constraints.

**Test Case $2$:** The tag doesn't contain opening and closing symbols and also includes characters other than lower-case alpha-numeric characters in its body.

**Test Case $5$:** The tag also includes an upper-case alpha-numeric character `"A"` and a non alpha-numeric character `"/"` in its body.

</details>

## Approach

Four conditions, all of which must hold:

1. starts with `</`
2. ends with `>`
3. the body — everything between — is non-empty
4. every body character is a lowercase letter or a digit

Checking the length first keeps the slicing safe: a string shorter than $4$ characters cannot satisfy all four, since `</` plus at least one body character plus `>` needs four. The body is then `s[2:-1]`.

For condition 4, Python's `str.isalnum` is tempting but **wrong** — it accepts uppercase letters and, worse, Unicode letters. The requirement is specifically lowercase ASCII letters and digits, so the test is `c.islower() or c.isdigit()`, or an explicit character-set membership.

The samples cover each failure mode. `Clearly_Invalid` fails the prefix outright. `<//aA>` is the instructive one: it *does* start with `</`, and it *does* end with `>`, but its body is `/aA`, which contains both a slash and uppercase letters. A solution checking only the delimiters would wrongly accept it.

`</5>` confirms that a purely numeric body is fine — the rule is alphanumeric, not alphabetic. `</h1>` mixes both.

Note the input characters span ASCII $33$–$126$, which **excludes space**, so each tag is a single whitespace-delimited token and can be read with a plain split. The leading `<` of an opening tag like `<h1>` fails the `</` prefix test, as it should.

## Solution (Python)

```python
import sys


def valid(s: str) -> bool:
    # "</" + at least one body character + ">" needs four characters.
    if len(s) < 4 or not s.startswith("</") or not s.endswith(">"):
        return False
    body = s[2:-1]
    # isalnum() would also accept uppercase and non-ASCII letters.
    return all(c.islower() or c.isdigit() for c in body)


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = ["Success" if valid(data[1 + i].decode()) else "Error" for i in range(t)]
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(|S|)$ per test case
- **Space:** $O(1)$

> CodeChef tags: `Special`, `Basic Programming Concepts`, `Algorithms`
