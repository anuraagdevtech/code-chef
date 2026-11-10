# CHANDWEIGHT

After the first support breaks, its left and right sections evolve independently: weight falling toward an already destroyed support dissipates. Let pref[i] be the added weight needed to destroy a prefix from its right endpoint. Then pref[i+1]=max(A_i,pref[i])-W_i; compute suffix requirements symmetrically. Breaking i needs its threshold and enough weight to supply both sections, giving max(A_i,pref[i]+suf[i+1])-W_i.

Complexity: O(N) time and space.

Validation: repository sample checks and deterministic differential checks where applicable; no online acceptance is claimed.

Reference: [official editorial](https://discuss.codechef.com/t/113144).
