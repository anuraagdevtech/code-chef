---
topic: Strings
subtopic: Frequency of a key field
time: $O(N)$ per test case
space: $O(N)$
---
Chef calls a student's full name exactly when their **first name is shared** with someone else in the class. So tally the first names, then make a second pass deciding each student's output.

Two passes are needed and cannot be merged: when the first student is printed, we do not yet know whether a later student shares their first name. Counting everything before emitting anything resolves that.

$$\text{output}_i = \begin{cases} \text{first}_i & \text{count}[\text{first}_i] = 1 \\ \text{first}_i \; \text{last}_i & \text{otherwise}\end{cases}$$

The sample is built around this. Two students share the first name `hasan`, so **both** are called in full — including the first one, which is the detail a single-pass solution gets wrong. The other two have unique first names and are called by first name alone.

Note the rule depends only on the first name; last names are never compared and may freely repeat.

A `Counter` over the first names does the tally in one pass, and the decision per student is then an $O(1)$ lookup.

Each test case produces $N$ output lines, one per student in the original input order — the output is not sorted or grouped.

## Edge cases

- **Both students sharing a first name get the full name, the earlier one included.** A single pass that decides as it reads prints just `hasan` for the first of them, because the clash has not been seen yet — which is why the counting pass must complete first. The sample is built on exactly this.
- **Last names may repeat freely**; only first names are ever compared, so two students called `x jones` and `y jones` are both called by first name alone.
- **All first names distinct**: every line is a bare first name.
- **All first names identical**: every line is a full name.
- **Output is $N$ lines per test case, in the original input order** — not sorted and not grouped.

## Dry run

| student | first name | times that first name appears | output |
|---|---|---:|---|
| hasan jaddouh | hasan | 2 | `hasan jaddouh` |
| farhod khakimiyon | farhod | 1 | `farhod` |
| kerim kochekov | kerim | 1 | `kerim` |
| hasan khateeb | hasan | 2 | `hasan khateeb` |

The first line needs the count from the fourth, which is why one pass is not enough.
