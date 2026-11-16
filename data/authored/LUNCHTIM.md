---
topic: Stacks
subtopic: Monotone groups bounded by taller students
time: $O(N)$ per test case
space: $O(N)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
Maintain a decreasing stack of height groups. Shorter groups are closed when a taller student arrives, because that student blocks any future equal-height student. Finalise a group of size $f$ by assigning $f-1$ to every member. If the current student has the height of the top group, append their index; otherwise create a new group.

Each index is inserted and finalised once. Lower students can be removed without blocking taller equal-height groups.

## Edge cases

- Count other students only, excluding the student itself.
- Equal-height intervening students do not block visibility.
- A taller student splits equal heights into different groups.

## Dry run

For `[1,2,2,3,2]`, height 1 closes alone, the two adjacent height-2 students form a group of size two, and height 3 closes that group. The final 2 stands alone: `[0,1,1,0,0]`.
