---
topic: Strings
subtopic: Validating a format
time: $O(|S|)$ per test case
space: $O(1)$
---
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

## Edge cases

- **The length check must come first.** A valid tag needs at least four characters (`</x>`), so `</>` with an empty body is an `Error` — and slicing before checking would hand `all` an empty sequence, which returns `True`.
- **`isalnum()` would be wrong.** It accepts uppercase letters, so `</aA>` would pass; the last sample row is exactly this and must be an `Error`. The test is `islower() or isdigit()` per character.
- **A digit-only body is valid** — the fourth row, `</5>`.
- **A `/` inside the body is invalid** (the last row, `<//aA>`), so checking the `</` prefix alone is not enough; every body character needs testing.
- **Both ends must match**: `Clearly_Invalid` fails the prefix and the suffix together, but either one alone is disqualifying.
- **Characters are confined to ASCII $33$–$126$ with no spaces**, which is what makes `islower()` and `isdigit()` safe here — both would also accept non-ASCII letters and digits that the input cannot contain — and lets each tag be read as a single whitespace-delimited token.

## Dry run

| tag | length $\geq 4$ | starts `</` | ends `>` | body | all lower/digit | output |
|---|:---:|:---:|:---:|---|:---:|---|
| `</h1>` | yes | yes | yes | `h1` | yes | `Success` |
| `Clearly_Invalid` | yes | **no** | no | — | — | `Error` |
| `</singlabharat>` | yes | yes | yes | `singlabharat` | yes | `Success` |
| `</5>` | yes | yes | yes | `5` | yes | `Success` |
| `<//aA>` | yes | yes | yes | `/aA` | **no** | `Error` |
