# OLYMPIC

Burnside's lemma for reversal gives (all arrangements + palindromic arrangements)/2. Both terms are multinomial coefficients over the required box counts. Sweep the queried box sizes in sorted order, updating those multinomials only at breakpoints of ceil(village_count / size), which has O(sqrt(village_count)) distinct values. Aggregate equal village counts.

Complexity: O(S + Q log Q + E log N) time and O(S+Q+E) space, where S is the total chocolate count and E=sum over distinct village counts of O(sqrt(count)).
