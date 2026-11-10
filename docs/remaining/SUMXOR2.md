# SUMXOR2

For a bit present c times, the coefficient f_k of (1-z)^c(1+z)^(N-c) equals even-choice count minus odd-choice count. Its derivative identity gives (k+1)f_(k+1)=(N-2c)f_k-(N-k+1)f_(k-1), so all coefficients take linear time without convolution. The odd count is (C(N,k)-f_k)/2. Sum weighted bit contributions, group equal c values, and prefix over k to answer queries.

Complexity: O(30N+Q) time and O(N) space.

Validation: repository sample checks and deterministic differential checks where applicable; no online acceptance is claimed.
