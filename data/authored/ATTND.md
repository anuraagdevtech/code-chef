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
