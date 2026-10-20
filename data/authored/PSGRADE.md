---
topic: Conditionals & Case Work
subtopic: Conjunction of per-subject and aggregate thresholds
time: $O(1)$ per test case
space: $O(1)$
---
Chef passes only if **all four** conditions hold:

$$A \geq A_{\min}, \quad B \geq B_{\min}, \quad C \geq C_{\min}, \quad A + B + C \geq T_{\min}$$

The per-subject minimums and the aggregate minimum are independent requirements, so this is a conjunction — a strong total cannot rescue a failed subject, and clearing every subject does not guarantee the total.

The samples are built to show both failure modes. Case 1 clears all three subjects comfortably but totals $6$ against $T_{\min} = 300$, so the aggregate check is what fails. Cases 2 through 4 each fail exactly one subject — $A$, then $B$, then $C$ — while the other two pass, which is a deliberate sweep to catch a solution that forgets one of the three comparisons. Case 5 passes everything with no margin at all, landing exactly on each threshold.

That last case makes the inclusivity essential: "at least" means `>=`, and a strict `>` would fail all five samples.

The input order is $A_{\min}, B_{\min}, C_{\min}, T_{\min}, A, B, C$ — all four minimums first, then all three scores. Interleaving them while reading is the likeliest bug, and the constraint $A_{\min} + B_{\min} + C_{\min} \leq T_{\min}$ confirms the grouping, since it only makes sense among the minimums.
