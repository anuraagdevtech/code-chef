---
topic: Strings
subtopic: Single-pass state machine
time: $O(L)$ per report
space: $O(1)$
---
Snakes pass one at a time, so at any moment the report is either *between* snakes or *inside* one. That is a two-state machine, and a single boolean tracks it.

Scanning left to right:

- `.` — always fine, in either state.
- `H` — a head. Valid only when **outside** a snake; seeing one while already inside means two overlapping snakes. Switches to inside.
- `T` — a tail. Valid only when **inside** a snake; seeing one while outside means a tail with no head. Switches to outside.

After the scan the state must be **outside**, or a snake was left unterminated.

All three failure modes appear in the samples, which is why the final check is as necessary as the in-loop ones:

- `H..H..T..T` — a head while already inside (case 3).
- `.T...H..H.T` — a tail before any head (case 5).
- `H..T..H` — ends inside, with a trailing head never closed (case 6).

A solution checking only that the counts of `H` and `T` match would accept the first and third of those, since `H..H..T..T` has two of each. Order and nesting are what the state machine captures.

The empty-ish case `...` is valid: zero snakes is allowed, and the state never leaves *outside*. Likewise `HT` is a snake of zero length between head and tail.

The given $L$ is redundant for Python, since the string carries its own length, but the token must still be consumed.

## Edge cases

- **Two heads in a row** (`H..H..T..T`): invalid, caught by the `inside` flag on the second `H`.
- **A tail before any head** (`.T...H..H.T`): invalid; without the `not inside` guard on `T` this string is silently accepted.
- **A head left unclosed at the end** (`H..T..H`): invalid, and only the post-loop `not inside` test catches it — every in-loop check passes.
- **No snakes at all** (`...`): `Valid`, since the flag never rises.
- **The minimal snake** (`HT`): `Valid`.
- **Dots are ignored entirely**, both between snakes and inside one, so `H..T` and `HT` are equally fine.
- **$L$ is given but unused in Python**, so its token must still be consumed or the next report's string is misread.

## Dry run

| report | where it fails | output |
|---|---|---|
| `..H..T...HTH....T.` | nowhere; ends outside | `Valid` |
| `...` | nowhere; never enters | `Valid` |
| `H..H..T..T` | second `H` while inside | `Invalid` |
| `HT` | nowhere | `Valid` |
| `.T...H..H.T` | first `T` while outside | `Invalid` |
| `H..T..H` | passes the loop, but ends **inside** | `Invalid` |

The last two rows fail by different mechanisms, which is why both the in-loop checks and the final flag test are needed.
