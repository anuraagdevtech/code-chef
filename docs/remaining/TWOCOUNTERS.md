# TWOCOUNTERS

Track the counter difference d=a-b. It suffices to keep -2<=d<=2: any excursion from 2 to 3 can be folded into an excursion from 2 to 1 while preserving its positive sign, and symmetrically below -2. A five-state DP updates d by plus or minus one each minute, then applies the event’s score increment or reset exactly.

Complexity: O(N+M) time and O(M) space.

Validation: repository sample checks and deterministic differential checks where applicable; no online acceptance is claimed.
