# Remaining roadmap: 249 Python solutions

All 249 distinct problems missing from the original 486-solution snapshot now have standalone Python 3 implementations and approach notes. Together the two sets cover all 735 distinct problem codes in the saved roadmap catalog.

The historical CodeChef account progress in the main README and `data/all_solved.txt` remains unchanged. These additions are locally verified implementations; they have not been submitted to CodeChef.

## Run and verify

From the repository root:

```sh
python3 tools/fetch_raw.py --remaining
python3 tools/run_remaining_tests.py
```

Each solution also runs independently, for example:

```sh
python3 solutions/SUB_XOR.py < input.txt
```

Use PyPy 3 for the largest inputs, especially `TREDEG`, `INFDIV`, and `PTREE`. Solutions use only the Python standard library. Cached problem payloads live in ignored `data/raw/`; the fetcher uses the corresponding course contest when the generic PRACTICE endpoint does not serve a statement.

## Validation

- All 249 problem sample sets pass: 217 exact, 30 semantic/numerical, and 2 case-insensitive comparisons; zero failures or skips.
- The five deterministic regression suites pass 89,486 checks, including exhaustive state searches and comparisons with independent small-input models.
- Embedded statement examples cover all 17 problems without structured API samples.
- Maximum-subtask smoke tests cover selected heavier solutions. See [validation details](../../data/validation_remaining.json). Timings depend on the host and interpreter.
- `CHEFQUE` uses a 256 MiB bitmap plus interpreter overhead; run it with adequate memory.

## Problems

### 1600 to 1800 difficulty problems — 30 problems

| Code | Problem | Difficulty | Files |
|---|---|---:|---|
| `SUB_XOR` | [Subarray XOR](https://www.codechef.com/problems/SUB_XOR) | 1757 | [Python](../../solutions/SUB_XOR.py) · [Approach](SUB_XOR.md) |
| `PREFIXFLIP` | [Flip the Prefix](https://www.codechef.com/problems/PREFIXFLIP) | 1758 | [Python](../../solutions/PREFIXFLIP.py) · [Approach](PREFIXFLIP.md) |
| `MINNOTES` | [Optimal Denomination](https://www.codechef.com/problems/MINNOTES) | 1759 | [Python](../../solutions/MINNOTES.py) · [Approach](MINNOTES.md) |
| `RACINGEN` | [Racing](https://www.codechef.com/problems/RACINGEN) | 1759 | [Python](../../solutions/RACINGEN.py) · [Approach](RACINGEN.md) |
| `LEBAMBOO` | [Little Elephant and Bamboo](https://www.codechef.com/problems/LEBAMBOO) | 1761 | [Python](../../solutions/LEBAMBOO.py) · [Approach](LEBAMBOO.md) |
| `DISTELE` | [Distinct Elements](https://www.codechef.com/problems/DISTELE) | 1762 | [Python](../../solutions/DISTELE.py) · [Approach](DISTELE.md) |
| `CHEFELEC` | [Chefland and Electricity](https://www.codechef.com/problems/CHEFELEC) | 1767 | [Python](../../solutions/CHEFELEC.py) · [Approach](CHEFELEC.md) |
| `RECTCNT` | [Rectangles Counting](https://www.codechef.com/problems/RECTCNT) | 1770 | [Python](../../solutions/RECTCNT.py) · [Approach](RECTCNT.md) |
| `CAB` | [Cybalphabit](https://www.codechef.com/problems/CAB) | 1771 | [Python](../../solutions/CAB.py) · [Approach](CAB.md) |
| `BRKNLIFE` | [Broken Life](https://www.codechef.com/problems/BRKNLIFE) | 1772 | [Python](../../solutions/BRKNLIFE.py) · [Approach](BRKNLIFE.md) |
| `SUMQ` | [Triplets](https://www.codechef.com/problems/SUMQ) | 1772 | [Python](../../solutions/SUMQ.py) · [Approach](SUMQ.md) |
| `LUNCHTIM` | [Lunchtime](https://www.codechef.com/problems/LUNCHTIM) | 1773 | [Python](../../solutions/LUNCHTIM.py) · [Approach](LUNCHTIM.md) |
| `PCJ18C` | [Chef and Polygon Cakes](https://www.codechef.com/problems/PCJ18C) | 1773 | [Python](../../solutions/PCJ18C.py) · [Approach](PCJ18C.md) |
| `MONKS` | [Monks](https://www.codechef.com/problems/MONKS) | 1776 | [Python](../../solutions/MONKS.py) · [Approach](MONKS.md) |
| `PALPALS` | [Palpal Strings](https://www.codechef.com/problems/PALPALS) | 1776 | [Python](../../solutions/PALPALS.py) · [Approach](PALPALS.md) |
| `BIN_OD` | [Binod](https://www.codechef.com/problems/BIN_OD) | 1776 | [Python](../../solutions/BIN_OD.py) · [Approach](BIN_OD.md) |
| `KCON` | [K-Concatenation](https://www.codechef.com/problems/KCON) | 1780 | [Python](../../solutions/KCON.py) · [Approach](KCON.md) |
| `CAPIMOVE` | [Capital Movement](https://www.codechef.com/problems/CAPIMOVE) | 1780 | [Python](../../solutions/CAPIMOVE.py) · [Approach](CAPIMOVE.md) |
| `ZEROONE` | [01 Subsequence](https://www.codechef.com/problems/ZEROONE) | 1781 | [Python](../../solutions/ZEROONE.py) · [Approach](ZEROONE.md) |
| `SET302` | [Problem-2](https://www.codechef.com/problems/SET302) | 1620 | [Python](../../solutions/SET302.py) · [Approach](SET302.md) |
| `KLXOR` | [Again XOR problem](https://www.codechef.com/problems/KLXOR) | 1786 | [Python](../../solutions/KLXOR.py) · [Approach](KLXOR.md) |
| `ARTBALAN` | [Art of Balance](https://www.codechef.com/problems/ARTBALAN) | 1788 | [Python](../../solutions/ARTBALAN.py) · [Approach](ARTBALAN.md) |
| `ABX01` | [Strange Function](https://www.codechef.com/problems/ABX01) | 1789 | [Python](../../solutions/ABX01.py) · [Approach](ABX01.md) |
| `PREZ` | [Prefix Zeros](https://www.codechef.com/problems/PREZ) | 1790 | [Python](../../solutions/PREZ.py) · [Approach](PREZ.md) |
| `CHEFHAM` | [Chef and Hamming Distance of arrays](https://www.codechef.com/problems/CHEFHAM) | 1790 | [Python](../../solutions/CHEFHAM.py) · [Approach](CHEFHAM.md) |
| `SVRT` | [Server Trouble](https://www.codechef.com/problems/SVRT) | 1791 | [Python](../../solutions/SVRT.py) · [Approach](SVRT.md) |
| `STR_REVERSE` | [String Reverse](https://www.codechef.com/problems/STR_REVERSE) | 1792 | [Python](../../solutions/STR_REVERSE.py) · [Approach](STR_REVERSE.md) |
| `TAAPLUSB` | [A Plus B Again!](https://www.codechef.com/problems/TAAPLUSB) | 1796 | [Python](../../solutions/TAAPLUSB.py) · [Approach](TAAPLUSB.md) |
| `BWALL` | [The Great Wall of Byteland](https://www.codechef.com/problems/BWALL) | 1796 | [Python](../../solutions/BWALL.py) · [Approach](BWALL.md) |
| `DIGITOP` | [Digit Operation](https://www.codechef.com/problems/DIGITOP) | 1798 | [Python](../../solutions/DIGITOP.py) · [Approach](DIGITOP.md) |

### Rise from 3* to 4* — 107 problems

| Code | Problem | Difficulty | Files |
|---|---|---:|---|
| `ADAKNG` | [Ada King](https://www.codechef.com/problems/ADAKNG) | 1581 | [Python](../../solutions/ADAKNG.py) · [Approach](ADAKNG.md) |
| `SNSOCIAL` | [Snakes and transition from Capitalism to Socialism](https://www.codechef.com/problems/SNSOCIAL) | -1 | [Python](../../solutions/SNSOCIAL.py) · [Approach](SNSOCIAL.md) |
| `CFMAR04` | [IS IT DSU HARD!!](https://www.codechef.com/problems/CFMAR04) | -1 | [Python](../../solutions/CFMAR04.py) · [Approach](CFMAR04.md) |
| `DIAMTREE` | [Find Tree Diameter](https://www.codechef.com/problems/DIAMTREE) | 1620 | [Python](../../solutions/DIAMTREE.py) · [Approach](DIAMTREE.md) |
| `ROOTTREE` | [Root the Tree](https://www.codechef.com/problems/ROOTTREE) | 1934 | [Python](../../solutions/ROOTTREE.py) · [Approach](ROOTTREE.md) |
| `INOI1601` | [Wealth Disparity](https://www.codechef.com/problems/INOI1601) | -1 | [Python](../../solutions/INOI1601.py) · [Approach](INOI1601.md) |
| `DSUBAGS` | [Queries with Bags](https://www.codechef.com/problems/DSUBAGS) | -1 | [Python](../../solutions/DSUBAGS.py) · [Approach](DSUBAGS.md) |
| `FAMTREE` | [Family Tree](https://www.codechef.com/problems/FAMTREE) | 1720 | [Python](../../solutions/FAMTREE.py) · [Approach](FAMTREE.md) |
| `CRIMCH` | [Cricket Match](https://www.codechef.com/problems/CRIMCH) | 1350 | [Python](../../solutions/CRIMCH.py) · [Approach](CRIMCH.md) |
| `SUBREM` | [Subtree Removal](https://www.codechef.com/problems/SUBREM) | 2010 | [Python](../../solutions/SUBREM.py) · [Approach](SUBREM.md) |
| `COSTEMP` | [Cosmic Temple](https://www.codechef.com/problems/COSTEMP) | -1 | [Python](../../solutions/COSTEMP.py) · [Approach](COSTEMP.md) |
| `TINOI17A` | [Fence - INOI 2017](https://www.codechef.com/problems/TINOI17A) | -1 | [Python](../../solutions/TINOI17A.py) · [Approach](TINOI17A.md) |
| `EVEDG` | [Even Edges](https://www.codechef.com/problems/EVEDG) | 1945 | [Python](../../solutions/EVEDG.py) · [Approach](EVEDG.md) |
| `SEGDIR` | [Moving Segments](https://www.codechef.com/problems/SEGDIR) | 1940 | [Python](../../solutions/SEGDIR.py) · [Approach](SEGDIR.md) |
| `TREEVERS` | [Treeversion](https://www.codechef.com/problems/TREEVERS) | 2453 | [Python](../../solutions/TREEVERS.py) · [Approach](TREEVERS.md) |
| `ABDTOLL` | [Abdullah and Toll Discounts](https://www.codechef.com/problems/ABDTOLL) | -1 | [Python](../../solutions/ABDTOLL.py) · [Approach](ABDTOLL.md) |
| `TOURISTS` | [Tourists in Mancunia](https://www.codechef.com/problems/TOURISTS) | 2133 | [Python](../../solutions/TOURISTS.py) · [Approach](TOURISTS.md) |
| `DINCPATH` | [Doubly Increasing Path](https://www.codechef.com/problems/DINCPATH) | 2493 | [Python](../../solutions/DINCPATH.py) · [Approach](DINCPATH.md) |
| `REVERSE` | [Chef and Reversing](https://www.codechef.com/problems/REVERSE) | 1879 | [Python](../../solutions/REVERSE.py) · [Approach](REVERSE.md) |
| `DIGJUMP` | [Chef and Digit Jumps](https://www.codechef.com/problems/DIGJUMP) | 1886 | [Python](../../solutions/DIGJUMP.py) · [Approach](DIGJUMP.md) |
| `GALACTIK` | [Galactik Football](https://www.codechef.com/problems/GALACTIK) | 1860 | [Python](../../solutions/GALACTIK.py) · [Approach](GALACTIK.md) |
| `CORONA` | [India Fights Corona](https://www.codechef.com/problems/CORONA) | 2560 | [Python](../../solutions/CORONA.py) · [Approach](CORONA.md) |
| `ARRGRAPH` | [Graph on an Array](https://www.codechef.com/problems/ARRGRAPH) | -1 | [Python](../../solutions/ARRGRAPH.py) · [Approach](ARRGRAPH.md) |
| `PERCAPTA` | [Per Capita Income](https://www.codechef.com/problems/PERCAPTA) | 2132 | [Python](../../solutions/PERCAPTA.py) · [Approach](PERCAPTA.md) |
| `INSQ15_F` | [FCAR](https://www.codechef.com/problems/INSQ15_F) | -1 | [Python](../../solutions/INSQ15_F.py) · [Approach](INSQ15_F.md) |
| `AMR14B` | [Road Decoration](https://www.codechef.com/problems/AMR14B) | -1 | [Python](../../solutions/AMR14B.py) · [Approach](AMR14B.md) |
| `HDELIVER` | [Home Delivery](https://www.codechef.com/problems/HDELIVER) | 1621 | [Python](../../solutions/HDELIVER.py) · [Approach](HDELIVER.md) |
| `BINTREE` | [Shortest Path in Binary Trees](https://www.codechef.com/problems/BINTREE) | 1413 | [Python](../../solutions/BINTREE.py) · [Approach](BINTREE.md) |
| `PATHSUMS` | [Path-etic Sums](https://www.codechef.com/problems/PATHSUMS) | 1838 | [Python](../../solutions/PATHSUMS.py) · [Approach](PATHSUMS.md) |
| `ICM2006` | [Lavanya Loves DFA](https://www.codechef.com/problems/ICM2006) | 1586 | [Python](../../solutions/ICM2006.py) · [Approach](ICM2006.md) |
| `OMWG` | [One more weird game](https://www.codechef.com/problems/OMWG) | 1536 | [Python](../../solutions/OMWG.py) · [Approach](OMWG.md) |
| `CIELTOMY` | [Ciel and Tomya](https://www.codechef.com/problems/CIELTOMY) | 1877 | [Python](../../solutions/CIELTOMY.py) · [Approach](CIELTOMY.md) |
| `PETERSEN` | [Petersen Graph](https://www.codechef.com/problems/PETERSEN) | 1894 | [Python](../../solutions/PETERSEN.py) · [Approach](PETERSEN.md) |
| `TR1` | [Rendezvous](https://www.codechef.com/problems/TR1) | 1638 | [Python](../../solutions/TR1.py) · [Approach](TR1.md) |
| `FIRE` | [Brush Fire](https://www.codechef.com/problems/FIRE) | 1761 | [Python](../../solutions/FIRE.py) · [Approach](FIRE.md) |
| `KINGCON` | [Kingdom Unity](https://www.codechef.com/problems/KINGCON) | 1851 | [Python](../../solutions/KINGCON.py) · [Approach](KINGCON.md) |
| `TR2` | [Robot Game](https://www.codechef.com/problems/TR2) | 1754 | [Python](../../solutions/TR2.py) · [Approach](TR2.md) |
| `CHEFHACK` | [End Of The World](https://www.codechef.com/problems/CHEFHACK) | 1730 | [Python](../../solutions/CHEFHACK.py) · [Approach](CHEFHACK.md) |
| `SPREAD` | [Gravel](https://www.codechef.com/problems/SPREAD) | 1822 | [Python](../../solutions/SPREAD.py) · [Approach](SPREAD.md) |
| `F3` | [Curry Stained Napkin](https://www.codechef.com/problems/F3) | 1815 | [Python](../../solutions/F3.py) · [Approach](F3.md) |
| `RG_01` | [Maximal Score Path](https://www.codechef.com/problems/RG_01) | 1836 | [Python](../../solutions/RG_01.py) · [Approach](RG_01.md) |
| `CHEFGIFT` | [Birthday Gift](https://www.codechef.com/problems/CHEFGIFT) | 1868 | [Python](../../solutions/CHEFGIFT.py) · [Approach](CHEFGIFT.md) |
| `N1` | [Treasure Hunting](https://www.codechef.com/problems/N1) | 1634 | [Python](../../solutions/N1.py) · [Approach](N1.md) |
| `K3` | [Maze of Digits](https://www.codechef.com/problems/K3) | 1859 | [Python](../../solutions/K3.py) · [Approach](K3.md) |
| `M3` | [Soccer League](https://www.codechef.com/problems/M3) | 1906 | [Python](../../solutions/M3.py) · [Approach](M3.md) |
| `BYTEISLE` | [Byteknights and Byteknaves](https://www.codechef.com/problems/BYTEISLE) | 1919 | [Python](../../solutions/BYTEISLE.py) · [Approach](BYTEISLE.md) |
| `PTUPLES` | [Prime Tuples](https://www.codechef.com/problems/PTUPLES) | 1809 | [Python](../../solutions/PTUPLES.py) · [Approach](PTUPLES.md) |
| `ODDDIV` | [Odd Divisors](https://www.codechef.com/problems/ODDDIV) | 1657 | [Python](../../solutions/ODDDIV.py) · [Approach](ODDDIV.md) |
| `NUMFACT` | [Number of Factors](https://www.codechef.com/problems/NUMFACT) | 1710 | [Python](../../solutions/NUMFACT.py) · [Approach](NUMFACT.md) |
| `SPCTRIPS` | [Special Triplets](https://www.codechef.com/problems/SPCTRIPS) | 1673 | [Python](../../solutions/SPCTRIPS.py) · [Approach](SPCTRIPS.md) |
| `LEVY` | [Levy Conjecture](https://www.codechef.com/problems/LEVY) | 1510 | [Python](../../solutions/LEVY.py) · [Approach](LEVY.md) |
| `COOLGUYS` | [Cool Guys](https://www.codechef.com/problems/COOLGUYS) | 1758 | [Python](../../solutions/COOLGUYS.py) · [Approach](COOLGUYS.md) |
| `CBALLS` | [Churu and Balls](https://www.codechef.com/problems/CBALLS) | 1697 | [Python](../../solutions/CBALLS.py) · [Approach](CBALLS.md) |
| `PRIGAME` | [Prime Game](https://www.codechef.com/problems/PRIGAME) | 1792 | [Python](../../solutions/PRIGAME.py) · [Approach](PRIGAME.md) |
| `EARTSEQ` | [Yet Another Problem About Sequences](https://www.codechef.com/problems/EARTSEQ) | 2011 | [Python](../../solutions/EARTSEQ.py) · [Approach](EARTSEQ.md) |
| `DESTCELL` | [Destroy Cells](https://www.codechef.com/problems/DESTCELL) | 2297 | [Python](../../solutions/DESTCELL.py) · [Approach](DESTCELL.md) |
| `PPTEST` | [Polo the Penguin and the Test](https://www.codechef.com/problems/PPTEST) | 1603 | [Python](../../solutions/PPTEST.py) · [Approach](PPTEST.md) |
| `MARCHA1` | [Paying up](https://www.codechef.com/problems/MARCHA1) | 1510 | [Python](../../solutions/MARCHA1.py) · [Approach](MARCHA1.md) |
| `MCHEF` | [MasterChef](https://www.codechef.com/problems/MCHEF) | 2016 | [Python](../../solutions/MCHEF.py) · [Approach](MCHEF.md) |
| `PERMSPL` | [Permutation Split](https://www.codechef.com/problems/PERMSPL) | 2996 | [Python](../../solutions/PERMSPL.py) · [Approach](PERMSPL.md) |
| `COINPART` | [Coin Partition](https://www.codechef.com/problems/COINPART) | 2804 | [Python](../../solutions/COINPART.py) · [Approach](COINPART.md) |
| `PEPPERA` | [Chef and Pepperoni Pizza Again](https://www.codechef.com/problems/PEPPERA) | 2516 | [Python](../../solutions/PEPPERA.py) · [Approach](PEPPERA.md) |
| `BLKJK` | [Blackjack](https://www.codechef.com/problems/BLKJK) | 2903 | [Python](../../solutions/BLKJK.py) · [Approach](BLKJK.md) |
| `MEANMEDI` | [Mean Mean Medians](https://www.codechef.com/problems/MEANMEDI) | 2719 | [Python](../../solutions/MEANMEDI.py) · [Approach](MEANMEDI.md) |
| `COUNTPAL` | [Count palindromes](https://www.codechef.com/problems/COUNTPAL) | 1631 | [Python](../../solutions/COUNTPAL.py) · [Approach](COUNTPAL.md) |
| `FCBARCA` | [Barcelona Gameplay Tactics](https://www.codechef.com/problems/FCBARCA) | 1658 | [Python](../../solutions/FCBARCA.py) · [Approach](FCBARCA.md) |
| `DBOY` | [Pizza Delivery](https://www.codechef.com/problems/DBOY) | 1666 | [Python](../../solutions/DBOY.py) · [Approach](DBOY.md) |
| `VK18` | [Total Diamonds](https://www.codechef.com/problems/VK18) | 1786 | [Python](../../solutions/VK18.py) · [Approach](VK18.md) |
| `TRIP` | [Trip](https://www.codechef.com/problems/TRIP) | 2005 | [Python](../../solutions/TRIP.py) · [Approach](TRIP.md) |
| `STRMRG` | [String Merging](https://www.codechef.com/problems/STRMRG) | 1965 | [Python](../../solutions/STRMRG.py) · [Approach](STRMRG.md) |
| `CHGLSTGT` | [Girl Friend and String Gift](https://www.codechef.com/problems/CHGLSTGT) | 1986 | [Python](../../solutions/CHGLSTGT.py) · [Approach](CHGLSTGT.md) |
| `MATRIX2` | [Matrix](https://www.codechef.com/problems/MATRIX2) | 2209 | [Python](../../solutions/MATRIX2.py) · [Approach](MATRIX2.md) |
| `DELISH` | [Dessert Wizard](https://www.codechef.com/problems/DELISH) | 1804 | [Python](../../solutions/DELISH.py) · [Approach](DELISH.md) |
| `LEMOUSE` | [Little Elephant and Mouses](https://www.codechef.com/problems/LEMOUSE) | 1941 | [Python](../../solutions/LEMOUSE.py) · [Approach](LEMOUSE.md) |
| `CHSQARR` | [Chef and Rectangle Array](https://www.codechef.com/problems/CHSQARR) | 2088 | [Python](../../solutions/CHSQARR.py) · [Approach](CHSQARR.md) |
| `CHEFTWOS` | [Chef and Two String](https://www.codechef.com/problems/CHEFTWOS) | 2233 | [Python](../../solutions/CHEFTWOS.py) · [Approach](CHEFTWOS.md) |
| `PHCUL` | [Physical Exercise](https://www.codechef.com/problems/PHCUL) | 1865 | [Python](../../solutions/PHCUL.py) · [Approach](PHCUL.md) |
| `GERMANDE` | [Gerrymander](https://www.codechef.com/problems/GERMANDE) | 1904 | [Python](../../solutions/GERMANDE.py) · [Approach](GERMANDE.md) |
| `SEARRAYS` | [Sereja and Arrays](https://www.codechef.com/problems/SEARRAYS) | 1999 | [Python](../../solutions/SEARRAYS.py) · [Approach](SEARRAYS.md) |
| `TAASEQ` | [The Lost Arithmetic Sequences](https://www.codechef.com/problems/TAASEQ) | 2012 | [Python](../../solutions/TAASEQ.py) · [Approach](TAASEQ.md) |
| `KIRLAB` | [Kirito in labyrinth](https://www.codechef.com/problems/KIRLAB) | 2047 | [Python](../../solutions/KIRLAB.py) · [Approach](KIRLAB.md) |
| `CHEFOFR` | [Offer for Chef](https://www.codechef.com/problems/CHEFOFR) | 2100 | [Python](../../solutions/CHEFOFR.py) · [Approach](CHEFOFR.md) |
| `N3` | [K-important Strings](https://www.codechef.com/problems/N3) | 1729 | [Python](../../solutions/N3.py) · [Approach](N3.md) |
| `AEHASH` | [A-E Hash Function](https://www.codechef.com/problems/AEHASH) | 1832 | [Python](../../solutions/AEHASH.py) · [Approach](AEHASH.md) |
| `F2` | [Bytelandian Robots](https://www.codechef.com/problems/F2) | 1844 | [Python](../../solutions/F2.py) · [Approach](F2.md) |
| `LUCKY3` | [Lucky Sum](https://www.codechef.com/problems/LUCKY3) | 1875 | [Python](../../solutions/LUCKY3.py) · [Approach](LUCKY3.md) |
| `RDF` | [Random decreasing function](https://www.codechef.com/problems/RDF) | 1975 | [Python](../../solutions/RDF.py) · [Approach](RDF.md) |
| `MEDIAN` | [Little Elephant and Median](https://www.codechef.com/problems/MEDIAN) | 2023 | [Python](../../solutions/MEDIAN.py) · [Approach](MEDIAN.md) |
| `WORLDCUP` | [Strategy for the World Cup](https://www.codechef.com/problems/WORLDCUP) | 2055 | [Python](../../solutions/WORLDCUP.py) · [Approach](WORLDCUP.md) |
| `RRPLAYER` | [Player](https://www.codechef.com/problems/RRPLAYER) | 2067 | [Python](../../solutions/RRPLAYER.py) · [Approach](RRPLAYER.md) |
| `ODDBIN` | [Odd Binomial Coefficients](https://www.codechef.com/problems/ODDBIN) | 2107 | [Python](../../solutions/ODDBIN.py) · [Approach](ODDBIN.md) |
| `WOUT` | [Way Out](https://www.codechef.com/problems/WOUT) | 1845 | [Python](../../solutions/WOUT.py) · [Approach](WOUT.md) |
| `CHFQUEUE` | [Chefs in Queue](https://www.codechef.com/problems/CHFQUEUE) | 2146 | [Python](../../solutions/CHFQUEUE.py) · [Approach](CHFQUEUE.md) |
| `HMAPPY1` | [Appy Loves One](https://www.codechef.com/problems/HMAPPY1) | 1932 | [Python](../../solutions/HMAPPY1.py) · [Approach](HMAPPY1.md) |
| `STRQ` | [Chef and Strings](https://www.codechef.com/problems/STRQ) | 1930 | [Python](../../solutions/STRQ.py) · [Approach](STRQ.md) |
| `SEACO` | [Sereja and Commands](https://www.codechef.com/problems/SEACO) | 1990 | [Python](../../solutions/SEACO.py) · [Approach](SEACO.md) |
| `CHEFSUBA` | [Chef and Sub Array ](https://www.codechef.com/problems/CHEFSUBA) | 1908 | [Python](../../solutions/CHEFSUBA.py) · [Approach](CHEFSUBA.md) |
| `CSUBQ` | [Chef and Subarray Queries](https://www.codechef.com/problems/CSUBQ) | 2345 | [Python](../../solutions/CSUBQ.py) · [Approach](CSUBQ.md) |
| `NEWREST` | [New Restaurant](https://www.codechef.com/problems/NEWREST) | 1800 | [Python](../../solutions/NEWREST.py) · [Approach](NEWREST.md) |
| `CHEFWD` | [Chef World](https://www.codechef.com/problems/CHEFWD) | 2049 | [Python](../../solutions/CHEFWD.py) · [Approach](CHEFWD.md) |
| `OLYMPIC` | [Gifts at Olympics](https://www.codechef.com/problems/OLYMPIC) | 2696 | [Python](../../solutions/OLYMPIC.py) · [Approach](OLYMPIC.md) |
| `CNTWAYS` | [The Uncountable Ways](https://www.codechef.com/problems/CNTWAYS) | 1992 | [Python](../../solutions/CNTWAYS.py) · [Approach](CNTWAYS.md) |
| `ADIMAT` | [Adi and the Matrix](https://www.codechef.com/problems/ADIMAT) | 2900 | [Python](../../solutions/ADIMAT.py) · [Approach](ADIMAT.md) |
| `INFDIV` | [E - Make it Zero](https://www.codechef.com/problems/INFDIV) | 2690 | [Python](../../solutions/INFDIV.py) · [Approach](INFDIV.md) |
| `PTREE` | [Perfect Tree Problem](https://www.codechef.com/problems/PTREE) | 2900 | [Python](../../solutions/PTREE.py) · [Approach](PTREE.md) |
| `TREDEG` | [Trees and Degrees](https://www.codechef.com/problems/TREDEG) | 2783 | [Python](../../solutions/TREDEG.py) · [Approach](TREDEG.md) |
| `MOBCNT` | [Counting Mobiles](https://www.codechef.com/problems/MOBCNT) | 2690 | [Python](../../solutions/MOBCNT.py) · [Approach](MOBCNT.md) |

### 2000 to 2500 difficulty problems — 112 problems

| Code | Problem | Difficulty | Files |
|---|---|---:|---|
| `MXFACS` | [Maximum Factors Problem](https://www.codechef.com/problems/MXFACS) | 2006 | [Python](../../solutions/MXFACS.py) · [Approach](MXFACS.md) |
| `ELWINTER` | [Winter](https://www.codechef.com/problems/ELWINTER) | 2007 | [Python](../../solutions/ELWINTER.py) · [Approach](ELWINTER.md) |
| `REMSUBARR` | [Subarray Removal](https://www.codechef.com/problems/REMSUBARR) | 2007 | [Python](../../solutions/REMSUBARR.py) · [Approach](REMSUBARR.md) |
| `ALTSUFF` | [Alternative Sufferings](https://www.codechef.com/problems/ALTSUFF) | 2011 | [Python](../../solutions/ALTSUFF.py) · [Approach](ALTSUFF.md) |
| `ROPASCI` | [Rock Paper Scissors](https://www.codechef.com/problems/ROPASCI) | 2013 | [Python](../../solutions/ROPASCI.py) · [Approach](ROPASCI.md) |
| `PALIXOR` | [NASA](https://www.codechef.com/problems/PALIXOR) | 2014 | [Python](../../solutions/PALIXOR.py) · [Approach](PALIXOR.md) |
| `DISTK` | [K Distinct Array](https://www.codechef.com/problems/DISTK) | 2015 | [Python](../../solutions/DISTK.py) · [Approach](DISTK.md) |
| `PRIMEFACDIV` | [Prime Factor Division](https://www.codechef.com/problems/PRIMEFACDIV) | 2016 | [Python](../../solutions/PRIMEFACDIV.py) · [Approach](PRIMEFACDIV.md) |
| `QNUMBER` | [Queries About Numbers](https://www.codechef.com/problems/QNUMBER) | 2026 | [Python](../../solutions/QNUMBER.py) · [Approach](QNUMBER.md) |
| `MAXANDOR` | [Maximum And Or](https://www.codechef.com/problems/MAXANDOR) | 2028 | [Python](../../solutions/MAXANDOR.py) · [Approach](MAXANDOR.md) |
| `NOSEQ` | [No sequence](https://www.codechef.com/problems/NOSEQ) | 2031 | [Python](../../solutions/NOSEQ.py) · [Approach](NOSEQ.md) |
| `GOLMINE` | [Gold Mining](https://www.codechef.com/problems/GOLMINE) | 2033 | [Python](../../solutions/GOLMINE.py) · [Approach](GOLMINE.md) |
| `CONSADD` | [Consecutive Adding](https://www.codechef.com/problems/CONSADD) | 2038 | [Python](../../solutions/CONSADD.py) · [Approach](CONSADD.md) |
| `KPAL` | [K Increment Palindrome](https://www.codechef.com/problems/KPAL) | 2038 | [Python](../../solutions/KPAL.py) · [Approach](KPAL.md) |
| `SYMARRSWAP` | [Symmetric Swaps](https://www.codechef.com/problems/SYMARRSWAP) | 2041 | [Python](../../solutions/SYMARRSWAP.py) · [Approach](SYMARRSWAP.md) |
| `MOUNTAIN` | [Mountain](https://www.codechef.com/problems/MOUNTAIN) | 2047 | [Python](../../solutions/MOUNTAIN.py) · [Approach](MOUNTAIN.md) |
| `NOPALINDROME` | [No Palindrome](https://www.codechef.com/problems/NOPALINDROME) | 2054 | [Python](../../solutions/NOPALINDROME.py) · [Approach](NOPALINDROME.md) |
| `MAXREMOV` | [Max Range Queries](https://www.codechef.com/problems/MAXREMOV) | 2057 | [Python](../../solutions/MAXREMOV.py) · [Approach](MAXREMOV.md) |
| `SPCP6` | [Tetris](https://www.codechef.com/problems/SPCP6) | 2062 | [Python](../../solutions/SPCP6.py) · [Approach](SPCP6.md) |
| `PARPER` | [Parity Permutation](https://www.codechef.com/problems/PARPER) | 2066 | [Python](../../solutions/PARPER.py) · [Approach](PARPER.md) |
| `AGCY` | [Angry Cyborg](https://www.codechef.com/problems/AGCY) | 2072 | [Python](../../solutions/AGCY.py) · [Approach](AGCY.md) |
| `BURGER` | [Double Burgers](https://www.codechef.com/problems/BURGER) | 2072 | [Python](../../solutions/BURGER.py) · [Approach](BURGER.md) |
| `SUMARRAY` | [Array Sum](https://www.codechef.com/problems/SUMARRAY) | 2077 | [Python](../../solutions/SUMARRAY.py) · [Approach](SUMARRAY.md) |
| `EQUIVALENT` | [Equivalent Numbers](https://www.codechef.com/problems/EQUIVALENT) | 2087 | [Python](../../solutions/EQUIVALENT.py) · [Approach](EQUIVALENT.md) |
| `SEGTHREE` | [Segment Three](https://www.codechef.com/problems/SEGTHREE) | 2089 | [Python](../../solutions/SEGTHREE.py) · [Approach](SEGTHREE.md) |
| `FPE` | [Full Path Eraser](https://www.codechef.com/problems/FPE) | 2094 | [Python](../../solutions/FPE.py) · [Approach](FPE.md) |
| `RECHEND` | [Can You Reach The End](https://www.codechef.com/problems/RECHEND) | 2095 | [Python](../../solutions/RECHEND.py) · [Approach](RECHEND.md) |
| `TRPTSTIC` | [TripTastic](https://www.codechef.com/problems/TRPTSTIC) | 2095 | [Python](../../solutions/TRPTSTIC.py) · [Approach](TRPTSTIC.md) |
| `LCMMANIA` | [LCM Mania](https://www.codechef.com/problems/LCMMANIA) | 2098 | [Python](../../solutions/LCMMANIA.py) · [Approach](LCMMANIA.md) |
| `SUBARRAYXOR` | [Non Zero Subarray Xor](https://www.codechef.com/problems/SUBARRAYXOR) | 2101 | [Python](../../solutions/SUBARRAYXOR.py) · [Approach](SUBARRAYXOR.md) |
| `MAJIK` | [Wishcraft](https://www.codechef.com/problems/MAJIK) | 2105 | [Python](../../solutions/MAJIK.py) · [Approach](MAJIK.md) |
| `TRAVELLING` | [Travelling in the Graph](https://www.codechef.com/problems/TRAVELLING) | 2108 | [Python](../../solutions/TRAVELLING.py) · [Approach](TRAVELLING.md) |
| `MAXIMALEXP` | [Maximal Expression](https://www.codechef.com/problems/MAXIMALEXP) | 2127 | [Python](../../solutions/MAXIMALEXP.py) · [Approach](MAXIMALEXP.md) |
| `INTARR` | [Interesting Array](https://www.codechef.com/problems/INTARR) | 2145 | [Python](../../solutions/INTARR.py) · [Approach](INTARR.md) |
| `MAXVAC` | [Maximising Vacations](https://www.codechef.com/problems/MAXVAC) | 2147 | [Python](../../solutions/MAXVAC.py) · [Approach](MAXVAC.md) |
| `SQRTCBRT` | [Love Squares Hate Cubes](https://www.codechef.com/problems/SQRTCBRT) | 2150 | [Python](../../solutions/SQRTCBRT.py) · [Approach](SQRTCBRT.md) |
| `LEXILARGEST` | [Lexicographically Largest ](https://www.codechef.com/problems/LEXILARGEST) | 2151 | [Python](../../solutions/LEXILARGEST.py) · [Approach](LEXILARGEST.md) |
| `AWESUM_OR` | [SUM OR](https://www.codechef.com/problems/AWESUM_OR) | 2152 | [Python](../../solutions/AWESUM_OR.py) · [Approach](AWESUM_OR.md) |
| `MUSROD` | [Musical Rods](https://www.codechef.com/problems/MUSROD) | 2160 | [Python](../../solutions/MUSROD.py) · [Approach](MUSROD.md) |
| `SUBSBIN` | [Binary Substitution](https://www.codechef.com/problems/SUBSBIN) | 2161 | [Python](../../solutions/SUBSBIN.py) · [Approach](SUBSBIN.md) |
| `CHEFSHOPPING` | [Chef Goes Shopping](https://www.codechef.com/problems/CHEFSHOPPING) | 2164 | [Python](../../solutions/CHEFSHOPPING.py) · [Approach](CHEFSHOPPING.md) |
| `DIVBY3` | [Minimize swaps](https://www.codechef.com/problems/DIVBY3) | 2164 | [Python](../../solutions/DIVBY3.py) · [Approach](DIVBY3.md) |
| `SEQGOODNESS` | [Sum of Goodness](https://www.codechef.com/problems/SEQGOODNESS) | 2167 | [Python](../../solutions/SEQGOODNESS.py) · [Approach](SEQGOODNESS.md) |
| `MINIMUMOP` | [Minimum Operation](https://www.codechef.com/problems/MINIMUMOP) | 2170 | [Python](../../solutions/MINIMUMOP.py) · [Approach](MINIMUMOP.md) |
| `CCD` | [Increase 2 consecutive characters](https://www.codechef.com/problems/CCD) | 2171 | [Python](../../solutions/CCD.py) · [Approach](CCD.md) |
| `EXPVALUE` | [Expected Value](https://www.codechef.com/problems/EXPVALUE) | 2177 | [Python](../../solutions/EXPVALUE.py) · [Approach](EXPVALUE.md) |
| `CENS20A` | [Cherry and Bits](https://www.codechef.com/problems/CENS20A) | 2179 | [Python](../../solutions/CENS20A.py) · [Approach](CENS20A.md) |
| `SSO` | [Chef Is Just Throwing Random Words](https://www.codechef.com/problems/SSO) | 2181 | [Python](../../solutions/SSO.py) · [Approach](SSO.md) |
| `DLTNODE` | [Sardar and GCD](https://www.codechef.com/problems/DLTNODE) | 2190 | [Python](../../solutions/DLTNODE.py) · [Approach](DLTNODE.md) |
| `MEXYARR` | [Mexy Array](https://www.codechef.com/problems/MEXYARR) | 2190 | [Python](../../solutions/MEXYARR.py) · [Approach](MEXYARR.md) |
| `VSTRING` | [Valid String](https://www.codechef.com/problems/VSTRING) | 2194 | [Python](../../solutions/VSTRING.py) · [Approach](VSTRING.md) |
| `PYRAMIDMOVES` | [Pyramid Traversal](https://www.codechef.com/problems/PYRAMIDMOVES) | 2194 | [Python](../../solutions/PYRAMIDMOVES.py) · [Approach](PYRAMIDMOVES.md) |
| `CHINSM` | [Chef and insomnia](https://www.codechef.com/problems/CHINSM) | 2197 | [Python](../../solutions/CHINSM.py) · [Approach](CHINSM.md) |
| `PARPERM` | [Partition It](https://www.codechef.com/problems/PARPERM) | 2202 | [Python](../../solutions/PARPERM.py) · [Approach](PARPERM.md) |
| `ICM2003` | [Is This JEE](https://www.codechef.com/problems/ICM2003) | 2206 | [Python](../../solutions/ICM2003.py) · [Approach](ICM2003.md) |
| `CIRMERGE` | [Circular Merging](https://www.codechef.com/problems/CIRMERGE) | 2208 | [Python](../../solutions/CIRMERGE.py) · [Approach](CIRMERGE.md) |
| `ANUMLA` | [Mahesh and his lost array](https://www.codechef.com/problems/ANUMLA) | 2212 | [Python](../../solutions/ANUMLA.py) · [Approach](ANUMLA.md) |
| `STROPERS` | [String Operations](https://www.codechef.com/problems/STROPERS) | 2220 | [Python](../../solutions/STROPERS.py) · [Approach](STROPERS.md) |
| `DIANE` | [Yet Another Crossover Episode](https://www.codechef.com/problems/DIANE) | 2221 | [Python](../../solutions/DIANE.py) · [Approach](DIANE.md) |
| `COPAR` | [Cute Chef Gift](https://www.codechef.com/problems/COPAR) | 2235 | [Python](../../solutions/COPAR.py) · [Approach](COPAR.md) |
| `EXISTENCEOFX` | [Existence Of X](https://www.codechef.com/problems/EXISTENCEOFX) | 2235 | [Python](../../solutions/EXISTENCEOFX.py) · [Approach](EXISTENCEOFX.md) |
| `DIST_VALS` | [Distinct Values](https://www.codechef.com/problems/DIST_VALS) | 2236 | [Python](../../solutions/DIST_VALS.py) · [Approach](DIST_VALS.md) |
| `TSHIRTS` | [Little Elephant and T-Shirts](https://www.codechef.com/problems/TSHIRTS) | 2242 | [Python](../../solutions/TSHIRTS.py) · [Approach](TSHIRTS.md) |
| `ANTSCHEF` | [Chef and Ants](https://www.codechef.com/problems/ANTSCHEF) | 2244 | [Python](../../solutions/ANTSCHEF.py) · [Approach](ANTSCHEF.md) |
| `ALIKE_THEM` | [Make Them Alike](https://www.codechef.com/problems/ALIKE_THEM) | 2245 | [Python](../../solutions/ALIKE_THEM.py) · [Approach](ALIKE_THEM.md) |
| `INTREP` | [Interesting Representation](https://www.codechef.com/problems/INTREP) | 2251 | [Python](../../solutions/INTREP.py) · [Approach](INTREP.md) |
| `MAX1S` | [Maximize 1s](https://www.codechef.com/problems/MAX1S) | 2255 | [Python](../../solutions/MAX1S.py) · [Approach](MAX1S.md) |
| `SUMOFCUBE` | [Sum of Cube ](https://www.codechef.com/problems/SUMOFCUBE) | 2259 | [Python](../../solutions/SUMOFCUBE.py) · [Approach](SUMOFCUBE.md) |
| `KSUM` | [Maximum K Sums](https://www.codechef.com/problems/KSUM) | 2260 | [Python](../../solutions/KSUM.py) · [Approach](KSUM.md) |
| `ABCSTR` | [ABC-Strings](https://www.codechef.com/problems/ABCSTR) | 2264 | [Python](../../solutions/ABCSTR.py) · [Approach](ABCSTR.md) |
| `ASHIGIFT` | [Saving a gift of love](https://www.codechef.com/problems/ASHIGIFT) | 2265 | [Python](../../solutions/ASHIGIFT.py) · [Approach](ASHIGIFT.md) |
| `LONGESTARRAY` | [Longest Subarray](https://www.codechef.com/problems/LONGESTARRAY) | 2267 | [Python](../../solutions/LONGESTARRAY.py) · [Approach](LONGESTARRAY.md) |
| `ASH57` | [Chroma Swap](https://www.codechef.com/problems/ASH57) | 2271 | [Python](../../solutions/ASH57.py) · [Approach](ASH57.md) |
| `CS2023_404` | [Search for 404](https://www.codechef.com/problems/CS2023_404) | 2296 | [Python](../../solutions/CS2023_404.py) · [Approach](CS2023_404.md) |
| `ALTDIA` | [Alternating Diameter](https://www.codechef.com/problems/ALTDIA) | 2300 | [Python](../../solutions/ALTDIA.py) · [Approach](ALTDIA.md) |
| `SPOOKYSEQ` | [Spooky Sequences](https://www.codechef.com/problems/SPOOKYSEQ) | 2304 | [Python](../../solutions/SPOOKYSEQ.py) · [Approach](SPOOKYSEQ.md) |
| `SUMXOR2` | [XOR Sums](https://www.codechef.com/problems/SUMXOR2) | 2306 | [Python](../../solutions/SUMXOR2.py) · [Approach](SUMXOR2.md) |
| `CHESUB` | [K-Subarrays](https://www.codechef.com/problems/CHESUB) | 2306 | [Python](../../solutions/CHESUB.py) · [Approach](CHESUB.md) |
| `CHEFFFUNC` | [Chefs Favourite Function](https://www.codechef.com/problems/CHEFFFUNC) | 2316 | [Python](../../solutions/CHEFFFUNC.py) · [Approach](CHEFFFUNC.md) |
| `MERGEBS` | [Merging Binary Strings](https://www.codechef.com/problems/MERGEBS) | 2318 | [Python](../../solutions/MERGEBS.py) · [Approach](MERGEBS.md) |
| `REDGREEN` | [Red Green Grids](https://www.codechef.com/problems/REDGREEN) | 2319 | [Python](../../solutions/REDGREEN.py) · [Approach](REDGREEN.md) |
| `MAKEPAL3` | [Palindrome In Making](https://www.codechef.com/problems/MAKEPAL3) | 2322 | [Python](../../solutions/MAKEPAL3.py) · [Approach](MAKEPAL3.md) |
| `SWAPGAME` | [Make that Array!](https://www.codechef.com/problems/SWAPGAME) | 2323 | [Python](../../solutions/SWAPGAME.py) · [Approach](SWAPGAME.md) |
| `ABROADS` | [Ancient Berland Roads](https://www.codechef.com/problems/ABROADS) | 2324 | [Python](../../solutions/ABROADS.py) · [Approach](ABROADS.md) |
| `SIMPLEARRAY` | [Potato to Gold](https://www.codechef.com/problems/SIMPLEARRAY) | 2326 | [Python](../../solutions/SIMPLEARRAY.py) · [Approach](SIMPLEARRAY.md) |
| `CHEFQUE` | [Chef and Queries](https://www.codechef.com/problems/CHEFQUE) | 2327 | [Python](../../solutions/CHEFQUE.py) · [Approach](CHEFQUE.md) |
| `CANDIES3` | [Candies](https://www.codechef.com/problems/CANDIES3) | 2329 | [Python](../../solutions/CANDIES3.py) · [Approach](CANDIES3.md) |
| `SPLITMIN` | [Two Piles](https://www.codechef.com/problems/SPLITMIN) | 2347 | [Python](../../solutions/SPLITMIN.py) · [Approach](SPLITMIN.md) |
| `KEEPOUT` | [Ultimate Fencing](https://www.codechef.com/problems/KEEPOUT) | 1830 | [Python](../../solutions/KEEPOUT.py) · [Approach](KEEPOUT.md) |
| `SPTREE` | [A Special Tree](https://www.codechef.com/problems/SPTREE) | 2350 | [Python](../../solutions/SPTREE.py) · [Approach](SPTREE.md) |
| `TWOAVG` | [Two Averages](https://www.codechef.com/problems/TWOAVG) | 2353 | [Python](../../solutions/TWOAVG.py) · [Approach](TWOAVG.md) |
| `RIFFLES` | [Chef and Riffles](https://www.codechef.com/problems/RIFFLES) | 2360 | [Python](../../solutions/RIFFLES.py) · [Approach](RIFFLES.md) |
| `CHANDWEIGHT` | [Chandelier](https://www.codechef.com/problems/CHANDWEIGHT) | 2368 | [Python](../../solutions/CHANDWEIGHT.py) · [Approach](CHANDWEIGHT.md) |
| `CLASSES` | [Minimal Travel Time](https://www.codechef.com/problems/CLASSES) | 2379 | [Python](../../solutions/CLASSES.py) · [Approach](CLASSES.md) |
| `TDISTS` | [Tree Distances](https://www.codechef.com/problems/TDISTS) | 2383 | [Python](../../solutions/TDISTS.py) · [Approach](TDISTS.md) |
| `WRDVLS` | [Weird Values](https://www.codechef.com/problems/WRDVLS) | 2393 | [Python](../../solutions/WRDVLS.py) · [Approach](WRDVLS.md) |
| `CNCTCT` | [Connect All Cities](https://www.codechef.com/problems/CNCTCT) | 2417 | [Python](../../solutions/CNCTCT.py) · [Approach](CNCTCT.md) |
| `CONSTANARRAY` | [Construct An Array](https://www.codechef.com/problems/CONSTANARRAY) | 2419 | [Python](../../solutions/CONSTANARRAY.py) · [Approach](CONSTANARRAY.md) |
| `ONEORALL` | [One or All](https://www.codechef.com/problems/ONEORALL) | 2420 | [Python](../../solutions/ONEORALL.py) · [Approach](ONEORALL.md) |
| `SMALLESTDIFF` | [Smallest Difference](https://www.codechef.com/problems/SMALLESTDIFF) | 2421 | [Python](../../solutions/SMALLESTDIFF.py) · [Approach](SMALLESTDIFF.md) |
| `GCD_QUERIES` | [GCD Queries](https://www.codechef.com/problems/GCD_QUERIES) | 2422 | [Python](../../solutions/GCD_QUERIES.py) · [Approach](GCD_QUERIES.md) |
| `TWOCOUNTERS` | [Two Counters](https://www.codechef.com/problems/TWOCOUNTERS) | 2425 | [Python](../../solutions/TWOCOUNTERS.py) · [Approach](TWOCOUNTERS.md) |
| `ADJFLIP` | [Adjacent Flips](https://www.codechef.com/problems/ADJFLIP) | 2426 | [Python](../../solutions/ADJFLIP.py) · [Approach](ADJFLIP.md) |
| `MAXCYCSHIFT` | [Max Shift After XOR](https://www.codechef.com/problems/MAXCYCSHIFT) | 2444 | [Python](../../solutions/MAXCYCSHIFT.py) · [Approach](MAXCYCSHIFT.md) |
| `BALSUFF` | [Balanced Suffix](https://www.codechef.com/problems/BALSUFF) | 2447 | [Python](../../solutions/BALSUFF.py) · [Approach](BALSUFF.md) |
| `GSEQ` | [Good Sequence](https://www.codechef.com/problems/GSEQ) | 2451 | [Python](../../solutions/GSEQ.py) · [Approach](GSEQ.md) |
| `DEQUEUE` | [Minimum Popping](https://www.codechef.com/problems/DEQUEUE) | 2463 | [Python](../../solutions/DEQUEUE.py) · [Approach](DEQUEUE.md) |
| `SQUAR` | [Squarified](https://www.codechef.com/problems/SQUAR) | 2470 | [Python](../../solutions/SQUAR.py) · [Approach](SQUAR.md) |
| `MEXSUB` | [Mex Subsequence](https://www.codechef.com/problems/MEXSUB) | 2494 | [Python](../../solutions/MEXSUB.py) · [Approach](MEXSUB.md) |
| `CHEF7UP` | [Chef Up](https://www.codechef.com/problems/CHEF7UP) | 2494 | [Python](../../solutions/CHEF7UP.py) · [Approach](CHEF7UP.md) |
| `EXPECTEDSUM` | [Expected Sum](https://www.codechef.com/problems/EXPECTEDSUM) | 2495 | [Python](../../solutions/EXPECTEDSUM.py) · [Approach](EXPECTEDSUM.md) |
| `ADMIT` | [College Admissions](https://www.codechef.com/problems/ADMIT) | 2496 | [Python](../../solutions/ADMIT.py) · [Approach](ADMIT.md) |

