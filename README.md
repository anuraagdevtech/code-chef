[Rating-ordered index](by-rating/README.md) &middot; [001. Small factorials &rarr;](by-rating/001-FCTRL2.md)

# CodeChef - Become 5 Star roadmap

Worked Python solutions for the CodeChef [Become 5 Star](https://www.codechef.com/roadmap/become-5-star) roadmap: the question, constraints, approach, runnable code, complexity, edge cases, and a dry run.

**735 of 735 distinct roadmap problems documented.** **0 remain.** See [remaining problems](REMAINING.md).

## Roadmap progress

| Level | Course | Documented distinct problems | Distinct problems | Course slots |
|---|---|---:|---:|---:|
| 1 | 500 to 1000 difficulty rating | 156 | 156 | 156 |
| 2 | Level up from 1* to 2* | 63 | 63 | 66 |
| 2 | 1400 to 1600 difficulty problems | 85 | 85 | 85 |
| 3 | Jump from 2* to 3* | 92 | 92 | 96 |
| 3 | 1600 to 1800 difficulty problems | 128 | 128 | 128 |
| 4 | Rise from 3* to 4* | 118 | 118 | 118 |
| 5 | 2000 to 2500 difficulty problems | 112 | 112 | 112 |
| | **Total, deduplicated across courses** | **735** | **735** | **761** |

Course slots can repeat a problem within one course or across courses. Each distinct problem is implemented and documented once.

The saved CodeChef profile snapshot for `anuraag_147` was harvested on 2026-10-21: **502 solved course entries** and **486 distinct accepted problems**. That snapshot is retained in `data/all_solved.txt` and `data/roadmap_index.json`. New local solutions are tracked separately in `data/completed.txt`; they have not been submitted to CodeChef and do not change the account snapshot. Run `python3 tools/reconcile_counts.py` to audit the original counts.

## Views

Every problem is written up once and rendered into two views, which carry the same six sections and cross-link to each other.

- **[By topic](#problems-by-topic)** - the index below, and `docs/<topic>/<CODE>.md`.
- **[By rating](by-rating/README.md)** - the same 735 problems numbered `001`-`735` in difficulty order, so a plain directory listing runs easiest to hardest.

## Problems by topic

<details open><summary><b>Arrays</b> (53)</summary>

| # | Problem | Difficulty | Technique | Time |
|---:|---|---:|---|---|
| 6 | [Mahasena](docs/arrays/AMR15A.md) | 720 | Parity counting in a single pass | $O(N)$ |
| 21 | [Problems in your to-do list](docs/arrays/TODOLIST.md) | 580 | Counting with a predicate | $O(N)$ per test case |
| 28 | [Elections in Chefland](docs/arrays/ELECTN.md) | 604 | Counting with a predicate | $O(N)$ per test case |
| 61 | [Self Defence Training](docs/arrays/SELFDEF.md) | 716 | Counting values inside a closed range | $O(N)$ per test case |
| 84 | [Minimum number of Flips](docs/arrays/MINFLIPS.md) | 781 | Feasibility by parity, then distance to the target count | $O(N)$ per test case |
| 87 | [The Lead Game](docs/arrays/TLG.md) | 1190 | Running totals with a tracked maximum | $O(N)$ |
| 88 | [Degree of Polynomial](docs/arrays/DPOLY.md) | 793 | Last index satisfying a predicate | $O(N)$ per test case |
| 89 | [Recent contest problems](docs/arrays/RECENTCONT.md) | 793 | Counting two categories in one pass | $O(N)$ per test case |
| 135 | [Penalty Shots](docs/arrays/PENALTY.md) | 925 | Summing alternate positions | $O(1)$ per test case — ten fixed entries |
| 138 | [Chef and Price Control](docs/arrays/PRICECON.md) | 931 | Summing a clamped excess | $O(N)$ per test case |
| 140 | [No Time to Wait](docs/arrays/NOTIME.md) | 932 | Existence check over a list | $O(N)$ |
| 141 | [First and Last](docs/arrays/FIRSTANDLAST.md) | 932 | Cyclically adjacent pairs | $O(N)$ per test case |
| 147 | [Non-Negative Product](docs/arrays/NONNEGPROD.md) | 948 | Sign of a product from the count of negatives | $O(N)$ per test case |
| 151 | [Chef and Cook-Off](docs/arrays/CCOOK.md) | 961 | Sum of flags mapped to a label | $O(1)$ per contestant |
| 155 | [Kitchen Timetable](docs/arrays/KTTABLE.md) | 950 | Consecutive differences as a window | $O(N)$ per test case |
| 161 | [Motivation](docs/arrays/IMDB.md) | 1098 | Maximum over a filtered subset | $O(N)$ per test case |
| 173 | [Chef in Vaccination Queue](docs/arrays/VACCINQ.md) | 1016 | Prefix sum with a per-element lookup | $O(P)$ per test case |
| 174 | [Chef and IPC Certificates](docs/arrays/IPCCERT.md) | 922 | Filtering rows on two independent criteria | $O(N \cdot K)$ |
| 176 | [A Subtask Problem](docs/arrays/SUBTASK.md) | 1217 | Ordered condition checks | $O(N)$ per test case |
| 179 | [Carvans](docs/arrays/CARVANS.md) | 1264 | Running minimum over a prefix | $O(N)$ per test case |
| 181 | [Average Flex](docs/arrays/AVGFLEX.md) | 1442 | Counting against a global threshold | $O(N^2)$ per test case at these bounds, or $O(N \log N)$ sorted |
| 183 | [College Life 2](docs/arrays/COLGLF2.md) | 1519 | Group total with a per-group adjustment | $O(\sum E_i)$ per test case |
| 207 | [Make all equal using Pairs](docs/arrays/PAIREQ.md) | 928 | Keep the most frequent value | $O(N)$ per test case |
| 218 | [Pushpa ](docs/arrays/PUSH7PA.md) | 1266 | Frequency combined with value | $O(N)$ per test case |
| 219 | [Reversal Sorting](docs/arrays/REVSORT.md) | 1288 | Constraining which inversions may be undone | $O(N)$ per test case |
| 223 | [Array Halves](docs/arrays/ARRHALVES.md) | 1407 | Minimum adjacent swaps to gather a set | $O(N)$ per test case |
| 229 | [Fit to Play](docs/arrays/PLAYFIT.md) | 1419 | Best gain against a running minimum | $O(N)$ per test case |
| 261 | [Weird Palindrome Making](docs/arrays/MAKEPAL.md) | 1486 | Odd counts and palindrome feasibility | $O(N)$ per test case |
| 263 | [CAO Stage-1](docs/arrays/CAOS1.md) | 1488 | Contiguous runs in four directions | $O(R \cdot C)$ per test case |
| 269 | [Total Correct Submissions](docs/arrays/TOTCRT.md) | 1499 | Aggregating by key, then sorting | $O(N \log N)$ per test case |
| 287 | [Unstable Subarray](docs/arrays/COUNTSUB.md) | 1545 | A telescoping sum, then counting equal pairs | $O(N)$ per test case |
| 295 | [Yet Another Palindrome Problem](docs/arrays/ARRPAL.md) | 1594 | Prefix increments force a non-increasing profile | $O(N)$ per test case |
| 311 | [Mix the Colors](docs/arrays/MIXCOLOR.md) | 1419 | Counting duplicates | $O(N)$ per test case |
| 316 | [Equal Difference](docs/arrays/EQDIFFER.md) | 1500 | Which multisets have all pairwise differences equal | $O(N)$ per test case |
| 330 | [A temple of Snakes](docs/arrays/SNTEMPLE.md) | 1800 | Runs computed from both directions | $O(n)$ per test case |
| 343 | [ChefTown Parade](docs/arrays/CHEFTOWN.md) | 1882 | Sliding-window maximum and minimum with deques | $O(N)$ |
| 352 | [Count Subarrays](docs/arrays/SUBINC.md) | 1478 | Counting subarrays by maximal runs | $O(N)$ per test case |
| 363 | [Maximal crosses](docs/arrays/MAXCROSS.md) | 1570 | Maximal runs along rows, columns and both diagonals | $O(n^2)$ |
| 406 | [Charges](docs/arrays/CHARGES.md) | 1645 | Local update of an adjacency count | $O(N + K)$ per test case |
| 412 | [OR Matrix](docs/arrays/ORMATRIX.md) | 1656 | Case analysis on the nearest reachable one | $O(NM)$ per test case |
| 433 | [Subarrays with length](docs/arrays/SUBARRAYLEN.md) | 1691 | Grouping by length, then a union of intervals | $O(N)$ per test case |
| 453 | [Matchsticks](docs/arrays/MSTICK.md) | 1714 | Sparse-table range min and max with end aggregates | $O(N \log N + Q)$ |
| 460 | [Box of Chocolates](docs/arrays/CHCBOX.md) | 1730 | Fitting a window into the gaps between maxima | $O(N)$ per test case |
| 470 | [Weird Subarrays](docs/arrays/WEIRDSUBARR.md) | 1739 | Counting valley subarrays from run lengths | $O(N)$ per test case |
| 591 | [Chef and Rectangle Array](docs/arrays/CHSQARR.md) | 2088 | 2D sliding-window maximum with monotone deques plus 2D prefix sums | $O(Q \cdot N \cdot M)$, with repeated query sizes answered from a cache |
| 596 | [The Lost Arithmetic Sequences](docs/arrays/TAASEQ.md) | 2012 | A constant number of removal candidates, each verified in linear time | $O(N)$ per test case |
| 610 | [Appy Loves One](docs/arrays/HMAPPY1.md) | 1932 | All rotations answered at once with a sliding-window maximum over runs | $O(N + Q)$ |
| 613 | [Chef and Sub Array ](docs/arrays/CHEFSUBA.md) | 1908 | Window sums on the doubled array, then a sliding maximum per rotation | $O(N + P)$ |
| 626 | [Subarray Removal](docs/arrays/REMSUBARR.md) | 2007 | Positions of the largest values must form one contiguous block | $O(N)$ per test case |
| 636 | [Consecutive Adding](docs/arrays/CONSADD.md) | 2038 | Greedy elimination with window operations, rows first and then the last columns | $O(R \cdot C)$ per test case |
| 650 | [Can You Reach The End](docs/arrays/RECHEND.md) | 2095 | A diagonal chain of blocks touching both boundary arcs separates the corners | $O(N)$ per test case |
| 712 | [Ultimate Fencing](docs/arrays/KEEPOUT.md) | 1830 | Undo the insertions on a linked list of sorted posts | $O(N \log N)$ per test case |
| 730 | [Minimum Popping](docs/arrays/DEQUEUE.md) | 2463 | Keep the longest middle part that does not swallow all copies of any value | $O(N + M)$ per test case |

</details>

<details open><summary><b>Basic Math</b> (104)</summary>

| # | Problem | Difficulty | Technique | Time |
|---:|---|---:|---|---|
| 1 | [Greater Average](docs/basic-math/AVGPROBLEM.md) | 500 | Integer arithmetic, avoiding floats | $O(1)$ per test case |
| 2 | [Subscriptions](docs/basic-math/SUBSCRIBE_.md) | 504 | Ceiling division | $O(1)$ per test case |
| 3 | [Janmansh and Assignments](docs/basic-math/JASSIGNMENTS.md) | 513 | Conditional arithmetic | $O(1)$ per test case |
| 4 | [Exams](docs/basic-math/EXAMCHEF.md) | 519 | Percentage comparison without division | $O(1)$ per test case |
| 5 | [Chef in his Office](docs/basic-math/OFFICE.md) | 532 | Direct formula | $O(1)$ per test case |
| 7 | [CRED Coins](docs/basic-math/CREDCOINS.md) | 539 | Floor division | $O(1)$ per test case |
| 10 | [Minimum Pizzas](docs/basic-math/MINPIZZA.md) | 546 | Ceiling division | $O(1)$ per test case |
| 12 | [Expert Setter](docs/basic-math/EXPERT.md) | 561 | Percentage comparison without division | $O(1)$ per test case |
| 13 | [Chef and NextGen](docs/basic-math/HELIUM3.md) | 562 | Comparing two products | $O(1)$ per test case |
| 14 | [Sugarcane Juice Business](docs/basic-math/SUGARCANE.md) | 563 | Percentages that cancel | $O(1)$ per test case |
| 15 | [Count the Notebooks](docs/basic-math/NOTEBOOK.md) | 563 | Chaining unit conversions | $O(1)$ per test case |
| 16 | [Chef and Candies](docs/basic-math/CHEFCAND.md) | 570 | Clamping before a ceiling division | $O(1)$ per test case |
| 20 | [Monopoly](docs/basic-math/MONOPOLY2.md) | 578 | Maximum against the sum of the rest | $O(1)$ per test case |
| 23 | [Nearest Exit](docs/basic-math/NEARESTEXIT.md) | 585 | Comparing distances to two endpoints | $O(1)$ per test case |
| 25 | [Sasta Shark Tank](docs/basic-math/SST.md) | 592 | Recovering a whole from a percentage | $O(1)$ per test case |
| 27 | [Qualify the round](docs/basic-math/QUALIFY.md) | 594 | Weighted sum against a threshold | $O(1)$ per test case |
| 29 | [Minimum Cars required](docs/basic-math/MINCARS.md) | 608 | Ceiling division | $O(1)$ per test case |
| 33 | [Discus Throw](docs/basic-math/DISCUS.md) | 622 | Maximum of a fixed set | $O(1)$ per test case |
| 35 | [Watching Movies at 2x](docs/basic-math/MOVIE2X.md) | 628 | Rate and time | $O(1)$ |
| 36 | [Police and Thief](docs/basic-math/POLTHIEF.md) | 639 | Relative speed | $O(1)$ per test case |
| 37 | [Flip the cards](docs/basic-math/FLIPCARDS.md) | 641 | Choosing the cheaper of two targets | $O(1)$ per test case |
| 38 | [Bath in Winters](docs/basic-math/BATH.md) | 643 | Floor division by a composite unit | $O(1)$ per test case |
| 39 | [Finding Shoes](docs/basic-math/FINDSHOES.md) | 646 | Clamping one side of a two-part requirement | $O(1)$ per test case |
| 42 | [Mario and Bullet](docs/basic-math/BULLET.md) | 650 | Working backwards from a deadline | $O(1)$ per test case |
| 43 | [Chess Ratings](docs/basic-math/C_RATING.md) | 651 | Ceiling division with a clamp | $O(1)$ per test case |
| 45 | [Chef and Water Bottles](docs/basic-math/CHEFBOTTLE.md) | 662 | Two competing limits | $O(1)$ per test case |
| 47 | [Finding Square Roots](docs/basic-math/FSQRT.md) | 420 | Exact integer square root | $O(1)$ per test case in practice |
| 48 | [The Last Levels](docs/basic-math/LASTLEVELS.md) | 679 | Counting separators, not groups | $O(1)$ per test case |
| 49 | [Blackjack](docs/basic-math/BLACKJACK.md) | 681 | Solving for the unknown, then range checking | $O(1)$ per test case |
| 50 | [Fill Candies](docs/basic-math/FILLCANDIES.md) | 681 | Ceiling division by a composite capacity | $O(1)$ per test case |
| 53 | [Valentine is Coming](docs/basic-math/VALENTINE.md) | 691 | Floor division | $O(1)$ per test case |
| 58 | [Chef Eren](docs/basic-math/CHEFEREN.md) | 706 | Counting odd and even positions | $O(1)$ per test case |
| 60 | [Airlines](docs/basic-math/SPCP2.md) | 712 | Ceiling division with a clamp | $O(1)$ per test case |
| 62 | [Cup Finals](docs/basic-math/CRICUP.md) | 716 | Absolute difference against a tolerance | $O(1)$ per test case |
| 63 | [Too many Floors](docs/basic-math/FLOORS.md) | 717 | Mapping an index to its block | $O(1)$ per test case |
| 64 | [Speed Limit Test](docs/basic-math/SPEEDTEST.md) | 718 | Comparing ratios by cross-multiplication | $O(1)$ per test case |
| 68 | [Pass or Fail](docs/basic-math/PASSORFAIL.md) | 730 | Scoring with a penalty | $O(1)$ per test case |
| 70 | [Too many items](docs/basic-math/POLYBAGS.md) | 738 | Ceiling division | $O(1)$ per test case |
| 72 | [Building Race](docs/basic-math/BUILDINGRACE.md) | 739 | Comparing ratios by cross-multiplication | $O(1)$ per test case |
| 74 | [Endless Appetizers](docs/basic-math/MOZZ.md) | 752 | Inverting a reward, then a ceiling division | $O(1)$ per test case |
| 75 | [Presents for Cheffina](docs/basic-math/PRESENTS.md) | 757 | Counting free items in a repeating group | $O(1)$ per test case |
| 76 | [Small Factorial](docs/basic-math/FLOW018.md) | 700 | Factorials within fixed-width limits | $O(N)$ per test case |
| 78 | [Possible Victory](docs/basic-math/T20MCH.md) | 769 | Best-case bound | $O(1)$ |
| 81 | [Reach fast](docs/basic-math/REACHFAST.md) | 777 | Ceiling division over a distance | $O(1)$ per test case |
| 83 | [Get Lowest Free](docs/basic-math/SALE.md) | 778 | Total minus the extremum | $O(1)$ per test case |
| 85 | [Binary Battles](docs/basic-math/BIN_BAT.md) | 786 | Tournament rounds, and separators between them | $O(1)$ per test case |
| 86 | [Best of Two](docs/basic-math/DICEGAME2.md) | 789 | Total minus the extremum, then compare | $O(1)$ per test case |
| 91 | [The Cooler Dilemma 2](docs/basic-math/WATERCOOLER2.md) | 798 | Strict inequality turned into a floor | $O(1)$ per test case |
| 94 | [Buy 2 Get 1 Free](docs/basic-math/SALE2.md) | 821 | Counting free items in a repeating group | $O(1)$ per test case |
| 96 | [The Preparations](docs/basic-math/SUPCHEF.md) | 823 | Strict comparison against a deadline | $O(1)$ per test case |
| 98 | [Best of N Sets](docs/basic-math/BESTOFTENNIS.md) | 830 | Inverting a stopping condition | $O(1)$ per test case |
| 100 | [Mileage matters](docs/basic-math/MILEAGE.md) | 831 | Comparing ratios by cross-multiplication | $O(1)$ per test case |
| 101 | [Melt Gold](docs/basic-math/MELTGOLD.md) | 835 | Triangular numbers and their inverse | $O(1)$ per test case |
| 102 | [Circular Track](docs/basic-math/LOOP.md) | 838 | Distance on a circle | $O(1)$ per test case |
| 106 | [Equal Integers](docs/basic-math/INCREAR.md) | 852 | Asymmetric step sizes | $O(1)$ per test case |
| 107 | [Summer Heat](docs/basic-math/COCONUT.md) | 852 | Independent requirements summed | $O(1)$ per test case |
| 109 | [Devendra and Water Sports](docs/basic-math/DEVSPORTS.md) | 859 | Remaining budget against a total cost | $O(1)$ per test case |
| 112 | [Car Choice](docs/basic-math/CARCHOICE.md) | 861 | Comparing ratios by cross-multiplication | $O(1)$ per test case |
| 114 | [Badminton Serves](docs/basic-math/BADMINTON.md) | 869 | Counting even values in a range | $O(1)$ per test case |
| 115 | [Chef and Contest](docs/basic-math/CHEFCONTEST.md) | 872 | Weighted penalty, then a three-way comparison | $O(1)$ per test case |
| 116 | [Group Assignment](docs/basic-math/GROUPASSGN.md) | 872 | Pairing by reflection | $O(1)$ per test case |
| 117 | [Relativity](docs/basic-math/RELATIVE.md) | 872 | Rearranging a given formula | $O(1)$ per test case |
| 119 | [Drunk Alcoholic](docs/basic-math/DRUNKALK.md) | 874 | Net progress per cycle, with an odd remainder | $O(1)$ per test case |
| 120 | [Chef On Island](docs/basic-math/CCISLAND.md) | 878 | Two independent supply checks | $O(1)$ per test case |
| 124 | [Secret Recipe](docs/basic-math/CHEFRUN.md) | 888 | Comparing ratios by cross-multiplication | $O(1)$ per test case |
| 125 | [Chef and Profits](docs/basic-math/CHFPROFIT.md) | 889 | Factoring a repeated difference | $O(1)$ per test case |
| 133 | [HOW MANY DIGITS DO I HAVE](docs/basic-math/HOWMANY.md) | 520 | Counting digits | $O(d)$ |
| 137 | [Chef and Pairing Slippers](docs/basic-math/CHEFSLP.md) | 930 | Pairing limited by the scarcer side | $O(1)$ per test case |
| 144 | [Car Range](docs/basic-math/CARRANGE.md) | 938 | Reading an off-by-one from the statement | $O(1)$ per test case |
| 145 | [ Am I Lucky!](docs/basic-math/SPCP4.md) | 941 | Remainders paired off | $O(1)$ per test case |
| 154 | [Keplers Law](docs/basic-math/KEPLERSLAW.md) | 992 | Testing proportionality by cross-multiplication | $O(1)$ per test case |
| 157 | [Richie Rich](docs/basic-math/CHFRICH.md) | 878 | Exact division from a guaranteed divisor | $O(1)$ per test case |
| 159 | [Hoop Jump](docs/basic-math/HOOPS.md) | 930 | Where two converging sequences meet | $O(1)$ per test case |
| 165 | [Chef and Spells](docs/basic-math/CHFSPL.md) | 965 | Total minus the extremum | $O(1)$ per test case |
| 167 | [Weight Balance](docs/basic-math/WEIGHTBL.md) | 1045 | Reachable range over repeated choices | $O(1)$ per test case |
| 168 | [Chef and Stock Prices ](docs/basic-math/CSTOCK.md) | 1069 | Percentage change without floating point | $O(1)$ per test case |
| 169 | [Turn It](docs/basic-math/NFS.md) | 1350 | Rearranging a kinematic inequality | $O(1)$ per test case |
| 171 | [Distinct Pair Sums](docs/basic-math/MANYSUMS.md) | 1480 | Range of achievable sums | $O(1)$ per test case |
| 172 | [Tom And Jerry 1](docs/basic-math/TANDJ1.md) | 1379 | Grid reachability by distance and parity | $O(1)$ per test case |
| 206 | [Playing with Matches](docs/basic-math/MATCHES.md) | 986 | Per-digit lookup table | $O(d)$ per test case |
| 224 | [Bella ciao](docs/basic-math/CHFHEIST.md) | 1410 | Summing an arithmetic progression | $O(1)$ per test case |
| 230 | [Equality](docs/basic-math/EQUALITY.md) | 1419 | Solving a symmetric linear system by summing | $O(N)$ per test case |
| 265 | [Chef Goes to the Cinema](docs/basic-math/CO92SUBW.md) | 1493 | Triangular numbers and a local search | $O(1)$ per test case |
| 275 | [Chef Drinks Coke](docs/basic-math/COKE.md) | 1511 | Closed form for a drift-to-target process | $O(N)$ per test case |
| 371 | [Guessing Game](docs/basic-math/GUESS.md) | 1410 | Counting by parity, reduced to lowest terms | $O(\log \min(N,M))$ per test case |
| 389 | [Odd Sum](docs/basic-math/ODDSUM.md) | 1600 | Parity of consecutive prefix sums | $O(1)$ per test case |
| 390 | [Chef and Bulb Invention](docs/basic-math/CHFINVNT.md) | 1607 | Counting residues below a threshold in closed form | $O(1)$ per test case |
| 396 | [Survive in ChocoLand](docs/basic-math/SURVIVE.md) | 1616 | Ceiling division with a running feasibility check | $O(S)$ per test case |
| 414 | [Three Numbers](docs/basic-math/THREENUMBERS.md) | 1675 | Parity invariant plus a counting identity | $O(1)$ per test case |
| 429 | [Gritty Grid](docs/basic-math/GRITGRID.md) | 1691 | Checkerboard parity across alternating moves | $O(1)$ per test case |
| 439 | [Average Gift](docs/basic-math/AVGGIFT.md) | 1701 | Mean reachability as a sign condition | $O(N)$ per test case |
| 448 | [Ceiling Sum](docs/basic-math/CEILSUM.md) | 1712 | Parity bonus on a fixed total | $O(1)$ per test case |
| 467 | [Maximum Value](docs/basic-math/MVALUE.md) | 1738 | Factoring the expression, then checking the extremes | $O(N \log N)$ per test case |
| 480 | [Save People](docs/basic-math/FIZZBUZZ2306.md) | 1750 | Manhattan bisector from an adjacent placement | $O(1)$ per test case |
| 483 | [Digit Removal](docs/basic-math/DIGITREM.md) | 1754 | Digit-position candidates for the next clean number | $O(\log^2 N)$ per test case |
| 490 | [Racing](docs/basic-math/RACINGEN.md) | 1759 | Energy balance gives the shortest completion time | $O(1)$ per test case |
| 491 | [Little Elephant and Bamboo](docs/basic-math/LEBAMBOO.md) | 1761 | Solve the linear equations for operation counts | $O(N)$ per test case |
| 499 | [Chef and Polygon Cakes](docs/basic-math/PCJ18C.md) | 1773 | Recover the common difference from the angle sum | $O(\log V)$ per test case |
| 512 | [Server Trouble](docs/basic-math/SVRT.md) | 1791 | Balance the circular gaps by quotient and remainder | $O(1)$ per test case |
| 547 | [One more weird game](docs/basic-math/OMWG.md) | 1536 | Count each grid adjacency exactly once | $O(1)$ per test case |
| 656 | [Maximal Expression](docs/basic-math/MAXIMALEXP.md) | 2127 | The two residues have one of two possible sums - split it evenly | $O(1)$ per test case |
| 659 | [Love Squares Hate Cubes](docs/basic-math/SQRTCBRT.md) | 2150 | The answer is a square - iterate to the least fixed point | $O(1)$ expected per test case - a handful of iterations |
| 665 | [Minimize swaps](docs/basic-math/DIVBY3.md) | 2164 | Ones on even positions modulo three; the answer is always 0, 1, 2, 3 or -1 | $O(N)$ per test case |
| 706 | [Make that Array!](docs/basic-math/SWAPGAME.md) | 2323 | A potential function makes the score independent of the moves | $O(N)$ per test case |

</details>

<details open><summary><b>Big Integers</b> (1)</summary>

| # | Problem | Difficulty | Technique | Time |
|---:|---|---:|---|---|
| 40 | [Small factorials](docs/big-integers/FCTRL2.md) | 420 | Arbitrary-precision arithmetic | $O(n)$ big-integer multiplications per test case |

</details>

<details open><summary><b>Binary Search</b> (11)</summary>

| # | Problem | Difficulty | Technique | Time |
|---:|---|---:|---|---|
| 325 | [Minion Chef and Bananas](docs/binary-search/MINEAT.md) | 1781 | Searching the answer on a monotonic predicate | $O(N \log \max A)$ per test case |
| 326 | [Stacks](docs/binary-search/STACKS.md) | 1799 | Patience stacking with a sorted top list | $O(N \log N)$ per test case |
| 327 | [Forest Gathering](docs/binary-search/FORESTGA.md) | 1829 | Searching time on a monotonic yield | $O(N \log(\text{months}))$ |
| 329 | [Snake Eating](docs/binary-search/SNAKEEAT.md) | 1940 | Feasibility check with prefix sums | $O((N + Q) \log N)$ per test case |
| 331 | [Squirrel and chestnut](docs/binary-search/SQUIRREL.md) | 1611 | Searching time, with a greedy capacity check | $O(m \log m \log(\text{time}))$ per test case |
| 333 | [Flu Shot Lineup](docs/binary-search/FLUSHOT.md) | 1692 | Binary search on a real-valued answer | $O(N \log \frac{1}{\varepsilon})$ per test case |
| 387 | [Sheokand and Number](docs/binary-search/SHKNUM.md) | 1534 | Precomputed candidate set with a bisect | $O(\log C)$ per test case after an $O(C \log C)$ precomputation |
| 506 | [Problem-2](docs/binary-search/SET302.md) | 1620 | Binary search a monotone sum of ceiling divisions | $O(N\log V)$ per test case |
| 651 | [TripTastic](docs/binary-search/TRPTSTIC.md) | 2095 | Binary search on the Chebyshev radius with 2D prefix sums | $O(N \cdot M \cdot \log \max(N, M))$ per test case |
| 678 | [Is This JEE](docs/binary-search/ICM2003.md) | 2206 | Bisection on the sign of the derivative | $O(55)$ iterations per test case |
| 714 | [Two Averages](docs/binary-search/TWOAVG.md) | 2353 | Only K into A and 1 into B help; binary search the number of appends | $O(N + M + \log \text{answer})$ per test case |

</details>

<details open><summary><b>Bit Manipulation</b> (38)</summary>

| # | Problem | Difficulty | Technique | Time |
|---:|---|---:|---|---|
| 217 | [Cooking Machine](docs/bit-manipulation/COOKMACH.md) | 1329 | Halving and doubling toward a power of two | $O(\log A \cdot \log B)$ per test case |
| 242 | [Make Array Odd](docs/bit-manipulation/MAKEARRAYODD.md) | 1445 | Tracking a single bit through XOR and OR | $O(N)$ per test case |
| 253 | [Order by XOR](docs/bit-manipulation/XOR_ORDER.md) | 1476 | The highest differing bit decides an XOR comparison | $O(1)$ per test case |
| 262 | [Interesting XOR!](docs/bit-manipulation/IRSTXOR.md) | 1487 | Maximising a product under a fixed XOR | $O(1)$ per test case |
| 273 | [Equal by XORing](docs/bit-manipulation/EQBYXOR.md) | 1507 | The XOR span of an initial segment | $O(1)$ per test case |
| 276 | [One-XOR Deletions](docs/bit-manipulation/DELXORONE.md) | 1516 | Grouping by the value with its low bit dropped | $O(N)$ per test case |
| 281 | [Positive or Negative Subarrays](docs/bit-manipulation/POSITNEG.md) | 1526 | One power of two dominates all the lower ones | $O(N)$ per test case |
| 289 | [XxOoRr](docs/bit-manipulation/XXOORR.md) | 1551 | Bits are independent, so count per column | $O(N \log \max A)$ per test case |
| 293 | [Yet Another Constructive Problem](docs/bit-manipulation/ORANDCON.md) | 1580 | The expression computes a bitwise majority | $O(1)$ per test case |
| 303 | [Consecutive Xor](docs/bit-manipulation/XOR2.md) | 1611 | The total XOR is invariant | $O(N)$ per test case |
| 313 | [Missing a Point](docs/bit-manipulation/PTMSSNG.md) | unrated | XOR cancels everything that appears twice | $O(N)$ per test case |
| 341 | [Hussain Set](docs/bit-manipulation/COOK82C.md) | 2608 | Grouping a halving process by bit length | $O(N \log N + L)$, where $L$ is the number of moves reached |
| 344 | [Prajit and bits](docs/bit-manipulation/ADDI.md) | unrated | Zero bits inside the binary width | $O(1)$ per test case |
| 345 | [Jon and Selina](docs/bit-manipulation/SELINA.md) | unrated | Parity bitmask over a 26-letter alphabet | $O(N)$ per test case |
| 346 | [Chef and Chefina](docs/bit-manipulation/CHFNA.md) | 1400 | Independent bits give a closed form | $O(1)$ per test case |
| 347 | [XOR-ORED](docs/bit-manipulation/XORORED.md) | 1621 | Choosing X bit by bit against an OR | $O(N)$ per test case |
| 348 | [Maximum Damage](docs/bit-manipulation/MAXDMGE.md) | 1636 | AND is monotone, so only adjacent pairs matter | $O(N)$ per test case |
| 349 | [XOR Engine](docs/bit-manipulation/ENGXOR.md) | 1632 | Popcount parity is additive under XOR | $O(N + Q)$ per test case |
| 351 | [XOR with Subset](docs/bit-manipulation/XORSUB.md) | 1879 | XOR linear basis over GF(2) | $O(N \log V + \log^2 V)$ per test case |
| 420 | [ALIEN-OR](docs/bit-manipulation/ALIENOR.md) | 1639 | Single-bit values are necessary and sufficient | $O(NK)$ per test case |
| 426 | [Boxes](docs/bit-manipulation/BOX95.md) | 1688 | The top bit caps a box at two elements | $O(N)$ per test case |
| 436 | [MEX-OR](docs/bit-manipulation/MEXOR.md) | 1650 | OR of a prefix of the integers | $O(1)$ per test case |
| 452 | [Even Subset Xor](docs/bit-manipulation/EVENXOR.md) | 1714 | Even-popcount numbers form a linear subspace | $O(N)$ per test case |
| 461 | [XOR Equal](docs/bit-manipulation/PALINT.md) | 1731 | XOR pairs values into two-element orbits | $O(N)$ per test case |
| 468 | [Xor and Multiply](docs/bit-manipulation/XORMUL.md) | 1739 | Lift the shared bits, then balance the differing ones | $O(N)$ per test case |
| 487 | [Subarray XOR](docs/bit-manipulation/SUB_XOR.md) | 1757 | Parity of contributions to each output bit | $O(N)$ per test case |
| 502 | [Binod](docs/bit-manipulation/BIN_OD.md) | 1776 | Offline queries grouped by bit with prefix counts | $O(NB+Q)$ per test case for $B$ queried bits |
| 507 | [Again XOR problem](docs/bit-manipulation/KLXOR.md) | 1786 | XOR prefix parity for each output position | $O(N)$ per test case |
| 598 | [Offer for Chef](docs/bit-manipulation/CHEFOFR.md) | 2100 | Greedy on answer bits with a partition DP over cluster counts | $O(Q \cdot B \cdot P^2)$ with $P \le 50$ topped slices and $B$ bits in the total sweetness |
| 604 | [Little Elephant and Median](docs/bit-manipulation/MEDIAN.md) | 2023 | Memoised search over bitmasks with maximal windows and dominance pruning | $O(2^N \cdot N^2)$ in the worst case; pruning keeps the visited states far below that for $N \le 30$ |
| 629 | [NASA](docs/bit-manipulation/PALIXOR.md) | 2014 | Counting pairs by xor value, directly or with a Walsh-Hadamard transform | $O(\min(D \cdot P,\; U \log U))$ per test case with $D$ distinct values, $P$ palindromes below $U = 2^{15}$ |
| 633 | [Maximum And Or](docs/bit-manipulation/MAXANDOR.md) | 2028 | Independent bits - free exactly where A and B differ | $O(1)$ per test case |
| 645 | [Double Burgers](docs/bit-manipulation/BURGER.md) | 2072 | Each streak is a power of two minus one - search the number of streaks | $O(\log^2 (Y / X))$ per test case |
| 671 | [Chef Is Just Throwing Random Words](docs/bit-manipulation/SSO.md) | 2181 | Count the supply of each bit and propagate carries | $O(N \log A)$ per test case |
| 684 | [Existence Of X](docs/bit-manipulation/EXISTENCEOFX.md) | 2235 | Column addition from the lowest bit - each bit of X is forced | $O(\log \max(A, B, C))$ per test case |
| 695 | [Longest Subarray](docs/bit-manipulation/LONGESTARRAY.md) | 2267 | Two pointers with per-bit counts - every bit must appear both inside and outside | $O(30 \cdot N)$ per test case |
| 702 | [Chefs Favourite Function](docs/bit-manipulation/CHEFFFUNC.md) | 2316 | Closed forms for f and g, and only O(log R) candidates | $O(\log R)$ per test case |
| 709 | [Chef and Queries](docs/bit-manipulation/CHEFQUE.md) | 2327 | A packed bitmap as the set, with an incrementally maintained sum | $O(Q)$ |

</details>

<details open><summary><b>Brute Force</b> (9)</summary>

| # | Problem | Difficulty | Technique | Time |
|---:|---|---:|---|---|
| 56 | [Weights](docs/brute-force/WGHTS.md) | 697 | Enumerating every non-empty subset | $O(2^k)$ per test case with $k = 3$, so $O(1)$ |
| 110 | [Highest Divisor](docs/brute-force/HDIVISR.md) | 860 | Searching a small range downward | $O(1)$ — at most 10 divisibility tests |
| 128 | [Chef and Battery ](docs/brute-force/FIFTYPE.md) | 901 | Searching one variable of a linear Diophantine equation | $O(1)$ per test case — the search is bounded by a small constant |
| 228 | [Maximize Colours](docs/brute-force/COLOUR.md) | 1415 | Enumerating a tiny decision space | $O(1)$ per test case — eight combinations |
| 245 | [Control the Pollution](docs/brute-force/SMOKE.md) | 1450 | Searching one variable over a small range | $O(N/100)$ per test case — at most 11 iterations |
| 254 | [Chef and Numbers](docs/brute-force/CHEFFED.md) | 1477 | Bounding the search window | $O(1)$ — a fixed-width scan |
| 256 | [Digital clock](docs/brute-force/ONOZ.md) | 1482 | Enumerating a small product space | $O(H \cdot M)$ per test case |
| 294 | [Missing Numbers](docs/brute-force/MISS_NUM.md) | 1594 | Guessing which two values are the sum and difference | $O(1)$ per test case — twelve candidate assignments |
| 648 | [Segment Three](docs/brute-force/SEGTHREE.md) | 2089 | Residues repeat with period three - try all nine patterns | $O(N)$ per test case |

</details>

<details open><summary><b>Combinatorics</b> (38)</summary>

| # | Problem | Difficulty | Technique | Time |
|---:|---|---:|---|---|
| 71 | [Chef Fantasy 11](docs/combinatorics/FIZZBUZZ2303.md) | 739 | Ordered pairs (permutations) | $O(1)$ per test case |
| 122 | [Farmers League](docs/combinatorics/LEAGUE.md) | 883 | Extremal construction in a round robin | $O(1)$ per test case |
| 192 | [Count Substrings](docs/combinatorics/CSUB.md) | 1330 | Counting pairs from a tally | $O(N)$ per test case |
| 237 | [Maximum Angriness](docs/combinatorics/MAXAGRY.md) | 1432 | Maximising inversions with limited swaps | $O(1)$ per test case |
| 244 | [Counting Flags](docs/combinatorics/FLAGS.md) | 1446 | Chromatic polynomials of small graphs | $O(1)$ per test case |
| 251 | [Magic Set](docs/combinatorics/MGCSET.md) | 1472 | A condition that reduces to its singletons | $O(n)$ per test case |
| 301 | [Break Free](docs/combinatorics/REMOSET.md) | 1612 | A condition pinned down by its singletons | $O(N)$ per test case |
| 336 | [Chef In Infinite Plane](docs/combinatorics/CHFPLN.md) | 1582 | Capacity per value | $O(N)$ per test case |
| 356 | [Chef and Good Subsequences](docs/combinatorics/GDSUB.md) | 1999 | Elementary symmetric polynomials by DP | $O(m \min(K, m))$ after an $O(N)$ tally, where $m$ is the number of distinct values |
| 375 | [Nice Pairs ](docs/combinatorics/NPAIRS.md) | 1564 | Counting pairs that share an invariant key | $O(N)$ per test case |
| 398 | [MaxEdges](docs/combinatorics/MAXEDGES.md) | 1618 | Complete layered DAG minus the forbidden pairs | $O(1)$ per test case |
| 403 | [Bitwise Tuples](docs/combinatorics/BITTUP.md) | 1634 | Independent bits, each a complement count | $O(\log N + \log M)$ per test case |
| 407 | [Chef and Interesting Subsequences ](docs/combinatorics/CHEFINSQ.md) | 1646 | Choosing among the tied boundary value | $O(N \log N)$ per test case |
| 416 | [The Vowel Matrix](docs/combinatorics/VOWMTRX.md) | 1694 | Independent cut choices between vowel blocks | $O(N)$ per test case |
| 441 | [OR Tuples](docs/combinatorics/ORTUPLES.md) | 1703 | Independent bits with an eight-case table | $O(20)$ per test case |
| 459 | [Set Difference ](docs/combinatorics/SETDIFF.md) | 1729 | Counting how often each element is the extreme | $O(N \log N)$ per test case |
| 466 | [Add to Subsequence](docs/combinatorics/SUBSEQDIST.md) | 1737 | Operations as bits of a distinguishing code | $O(N)$ per test case |
| 484 | [Bear and AB](docs/combinatorics/ABREPEAT.md) | 1754 | Splitting pairs into within-copy and across-copy | $O(N)$ per test case |
| 492 | [Distinct Elements](docs/combinatorics/DISTELE.md) | 1762 | Independent choice from each frequency class | $O(N)$ per test case |
| 582 | [Barcelona Gameplay Tactics](docs/combinatorics/FCBARCA.md) | 1658 | Closed form for walks returning to the starting player | $O(\log N+\log MOD)$ per test case |
| 595 | [Sereja and Arrays](docs/combinatorics/SEARRAYS.md) | 1999 | Counting tilings with a single zero and a block of K ones | $O(N)$ per test case |
| 602 | [Lucky Sum](docs/combinatorics/LUCKY3.md) | 1875 | Inclusion-exclusion over per-digit thresholds with a 4-level sum-over-subsets table | $O(D \cdot (N \cdot D + D \cdot 4^D))$ per test case, $D \le 9$ digits |
| 605 | [Strategy for the World Cup](docs/combinatorics/WORLDCUP.md) | 2055 | Multinomial over sixes, fours and the rest, with a prefix of binomials for wickets | $O(B_{\max} + T \cdot B)$ |
| 615 | [New Restaurant](docs/combinatorics/NEWREST.md) | 1800 | Stirling numbers of the second kind times a falling factorial | $O(N_{\max}^2 + \sum \min(N, M, K))$ |
| 616 | [Chef World](docs/combinatorics/CHEFWD.md) | 2049 | Fibonacci convolution in closed form with fast doubling | $O(\log N)$ per test case |
| 617 | [Gifts at Olympics](docs/combinatorics/OLYMPIC.md) | 2696 | Burnside for reversal, with multinomials updated along a sweep over box sizes | $O(S + Q \log Q + E \log N)$, $S$ the total number of chocolates and $E = \sum O(\sqrt{count})$ breakpoints |
| 618 | [The Uncountable Ways](docs/combinatorics/CNTWAYS.md) | 1992 | Lattice paths split at the unique step that passes below the cut-out corner | $O(\max(N + M) + \sum N)$ |
| 619 | [Adi and the Matrix](docs/combinatorics/ADIMAT.md) | 2900 | Burnside over row cycle types with a cycle-index DP for the columns | $O(p(n) \cdot m^2)$, $n = \min(N, M)$, $m = \max(N, M)$ and $p$ the partition function |
| 622 | [Trees and Degrees](docs/combinatorics/TREDEG.md) | 2783 | Pruefer codes and the coefficient of a power of an exponential generating function | $O(N)$ for $K = 1$; otherwise $O(N \log K)$ plus $O(\log N)$ levels of big-integer convolutions |
| 623 | [Counting Mobiles](docs/combinatorics/MOBCNT.md) | 2690 | Leaves forced by depth, choosing which slots of each level are leaves | $O(N + \log \sum a_i)$ per test case |
| 643 | [Parity Permutation](docs/combinatorics/PARPER.md) | 2066 | Index parity classes must be uniform in value parity | $O(N)$ per test case |
| 661 | [SUM OR](docs/combinatorics/AWESUM_OR.md) | 2152 | No carries - distribute the set bits of N among three non-empty owners | $O(\log N)$ per test case |
| 666 | [Sum of Goodness](docs/combinatorics/SEQGOODNESS.md) | 2167 | Each value contributes a difference of two binomial tails, maintained incrementally | $O(N)$ per test case after $O(\max N)$ precomputation |
| 675 | [Pyramid Traversal](docs/combinatorics/PYRAMIDMOVES.md) | 2194 | Convert labels to (row, column) and choose which steps go right | $O(\sqrt{V})$ precomputation and $O(1)$ per query, $V$ the largest label |
| 700 | [XOR Sums](docs/combinatorics/SUMXOR2.md) | 2306 | Per-bit signed coefficients from a three-term recurrence, grouped by bit count | $O(30 \cdot N + Q)$ |
| 704 | [Red Green Grids](docs/combinatorics/REDGREEN.md) | 2319 | Count (grid, path) pairs path by path | $O(N + M)$ precomputation, $O(\log (N M))$ per test case |
| 708 | [Potato to Gold](docs/combinatorics/SIMPLEARRAY.md) | 2326 | Independent choices per pair of complementary remainders | $O(N + K)$ per test case |
| 719 | [Weird Values](docs/combinatorics/WRDVLS.md) | 2393 | For each value, count subarrays containing exactly that many occurrences | $O(N)$ per test case |

</details>

<details open><summary><b>Conditionals & Case Work</b> (26)</summary>

| # | Problem | Difficulty | Technique | Time |
|---:|---|---:|---|---|
| 8 | [Water Filling](docs/conditionals-case-work/WATERFILLING.md) | 541 | Counting flags instead of enumerating cases | $O(1)$ per test case |
| 9 | [Sale Season](docs/conditionals-case-work/SALESEASON.md) | 541 | Ordered threshold ladder | $O(1)$ per test case |
| 11 | [Chefland Games](docs/conditionals-case-work/CHEFGAMES.md) | 550 | Reducing an AND over flags to a sum | $O(1)$ per test case |
| 17 | [Car or Bike](docs/conditionals-case-work/TRAVELFAST.md) | 571 | Three-way comparison | $O(1)$ per test case |
| 18 | [Is the Score Consistent](docs/conditionals-case-work/TRUESCORE.md) | 572 | Monotonic quantities | $O(1)$ per test case |
| 19 | [The Three Topics](docs/conditionals-case-work/THREETOPICS.md) | 573 | Membership test | $O(1)$ |
| 22 | [Air Conditioner Temperature](docs/conditionals-case-work/ACTEMP.md) | 584 | Intersecting interval constraints | $O(1)$ per test case |
| 32 | [Bus  Seat Numbering](docs/conditionals-case-work/SEATNUMBER.md) | 613 | Decomposing an index into deck and position | $O(1)$ per test case |
| 55 | [Water Mixing](docs/conditionals-case-work/WTRMIXING.md) | 694 | Signed difference against one-sided supplies | $O(1)$ per test case |
| 65 | [Decrement OR Increment](docs/conditionals-case-work/DECINC.md) | 520 | Single divisibility branch | $O(1)$ |
| 79 | [Chef And Operators](docs/conditionals-case-work/CHOPRT.md) | 520 | Three-way comparison | $O(1)$ per test case |
| 97 | [Genes](docs/conditionals-case-work/GENE01.md) | 826 | Ranking by priority | $O(1)$ |
| 103 | [Grade The Steel](docs/conditionals-case-work/FLOW014.md) | 900 | Grading from a set of independent flags | $O(1)$ per test case |
| 113 | [Which Division](docs/conditionals-case-work/WHICHDIV.md) | 867 | Ordered threshold ladder | $O(1)$ per test case |
| 123 | [Utkarsh and Placement tests](docs/conditionals-case-work/UTKPLC.md) | 886 | Ranking by a given priority order | $O(1)$ per test case |
| 129 | [Passing Marks](docs/conditionals-case-work/PSGRADE.md) | 904 | Conjunction of per-subject and aggregate thresholds | $O(1)$ per test case |
| 136 | [Shoe Fit](docs/conditionals-case-work/SHOEFIT.md) | 925 | Presence of both values in a small collection | $O(1)$ per test case |
| 149 | [Marathon](docs/conditionals-case-work/MARARUN.md) | 955 | Largest achievable tier | $O(1)$ per test case |
| 150 | [La Liga](docs/conditionals-case-work/COOK82A.md) | 956 | Parsing labelled input, then a single logical condition | $O(1)$ per test case |
| 156 | [Bear and Ladder](docs/conditionals-case-work/BRLADDER.md) | 999 | Deriving an adjacency rule from an edge list | $O(1)$ per query |
| 158 | [Vaccine Dates ](docs/conditionals-case-work/VDATES.md) | 938 | Classifying a value against an interval | $O(1)$ per test case |
| 163 | [Problem Category](docs/conditionals-case-work/PROBCAT.md) | 860 | Ordered threshold ladder | $O(1)$ per test case |
| 373 | [Say No To Drugs](docs/conditionals-case-work/NODRUGS.md) | 1425 | Monotone objective, so only an endpoint dose matters | $O(N)$ per test case |
| 378 | [K-MEX](docs/conditionals-case-work/KMEX.md) | 1450 | Feasibility as a counting interval | $O(N)$ per test case |
| 408 | [Range Assign, Number of Distinct Elements Minimize](docs/conditionals-case-work/RANGEASSIGN.md) | 1648 | Fixed endpoints bound what the operation can reach | $O(N)$ per test case |
| 479 | [The One Who Knocks!](docs/conditionals-case-work/EOOPR.md) | 1749 | Reachability of a difference by odd and even steps | $O(1)$ per test case |

</details>

<details open><summary><b>Constructive</b> (44)</summary>

| # | Problem | Difficulty | Technique | Time |
|---:|---|---:|---|---|
| 232 | [Average Array](docs/constructive/AVGARR.md) | 1424 | Pairing symmetrically around the mean | $O(N)$ per test case |
| 236 | [Balanced and Unique Arrays](docs/constructive/UNQEQ.md) | 1431 | Balanced split with distinct prefixes | $O(N)$ per test case |
| 238 | [Permutation Xority](docs/constructive/PERMXORITY.md) | 1437 | Cancelling a XOR with a 1-2-3 triple | $O(N)$ per test case |
| 257 | [Alternating Divisibility](docs/constructive/ALTERNATEDIV.md) | 1483 | Pairing k with 2k | $O(N)$ per test case |
| 267 | [Exactly N plus 1 Values](docs/constructive/N1VALUES.md) | 1495 | Building a sum from a run plus a remainder | $O(N)$ per test case |
| 268 | [Gcd of Subarrays](docs/constructive/GCDSUBARRAYS.md) | 1498 | Starting from the minimum and adding the slack | $O(N)$ per test case |
| 271 | [Palindrome Pain](docs/constructive/PALINPAIN.md) | 1506 | Counting distinct palindrome halves | $O(X + Y)$ per test case |
| 284 | [Prefix Permutation](docs/constructive/PREFPERM.md) | 1532 | Blocks that only close at the right moment | $O(N)$ per test case |
| 292 | [Chef and squares](docs/constructive/CHSQR.md) | 1576 | A shifted cyclic Latin square | $O(K^2)$ per test case |
| 300 | [K Odd Sum](docs/constructive/ADVITIYA5.md) | 1614 | Parity blocks and the number of switches | $O(N)$ per test case |
| 305 | [Make it Divisible](docs/constructive/MAKEDIV3.md) | 1379 | Fixing the digit sum, then the last digit | $O(N)$ per test case |
| 306 | [Indivisible Permutation](docs/constructive/INDIPERM.md) | 1329 | A single cyclic shift | $O(N)$ per test case |
| 355 | [Digit Longest Increasing Subsequences 2](docs/constructive/LISDIGIT.md) | 1297 | Using the LIS value itself as the digit | $O(n)$ per test case |
| 368 | [GCD operations](docs/constructive/GCDOPS.md) | 1462 | Each reduction has a self-fixing pivot | $O(N)$ per test case |
| 379 | [Subarray permutations](docs/constructive/SUBPERM.md) | 1502 | Forcing every good subsegment to be a prefix | $O(N)$ per test case |
| 382 | [Increasing Decreasing](docs/constructive/INCRDEC.md) | 1557 | Multiplicity bounds for a bitonic arrangement | $O(N \log N)$ per test case |
| 393 | [Different String](docs/constructive/DIFSTR.md) | 1612 | Cantor diagonalisation | $O(N)$ per test case |
| 397 | [GCD of Prefixes](docs/constructive/GCDPRF.md) | 1617 | Divisibility chain, realised by the array itself | $O(N \log A)$ per test case |
| 400 | [Construct Array](docs/constructive/CONSTRRAY.md) | 1624 | A symmetry that forces the parity of N | $O(N)$ per test case |
| 428 | [Bitwise Equation](docs/constructive/BITEQU.md) | 1679 | Neutralising the AND to reduce to one XOR | $O(1)$ per test case |
| 449 | [Minimum Coloring](docs/constructive/MINCOLOR.md) | 1713 | Checkerboard parity, with a third colour only when forced | $O(NM)$ per test case |
| 478 | [Same Parity Swaps in Binary Strings](docs/constructive/MAX01EVSWP.md) | 1747 | Matching on a path, with a parity-forced shortfall | $O(N)$ per test case |
| 495 | [Cybalphabit](docs/constructive/CAB.md) | 1771 | Split powers of two until the required length | $O(N+\log K)$ per test case |
| 511 | [Chef and Hamming Distance of arrays](docs/constructive/CHEFHAM.md) | 1790 | Rotate sorted values by the maximum frequency | $O(N\log N)$ per test case |
| 529 | [Even Edges](docs/constructive/EVEDG.md) | 1945 | Parity of the edge count and vertex degrees | $O(N+M)$ per test case |
| 539 | [Graph on an Array](docs/constructive/ARRGRAPH.md) | unrated | Check coprime connectivity, then add a universal prime | $O(N^2\log V)$ per test case with $V=50$ |
| 545 | [Path-etic Sums](docs/constructive/PATHSUMS.md) | 1838 | Assign one and two to the two tree colour classes | $O(N)$ per test case |
| 571 | [Yet Another Problem About Sequences](docs/constructive/EARTSEQ.md) | 2011 | Distinct large primes interleaved with a small cyclic colouring | $O(V\log\log V+\sum N)$ overall for fixed sieve bound $V=400000$ |
| 630 | [K Distinct Array](docs/constructive/DISTK.md) | 2015 | A distinct prefix, one calibrated repeat and a constant tail | $O(N)$ per test case |
| 634 | [No sequence](docs/constructive/NOSEQ.md) | 2031 | Balanced base-K digits read off from the residue | $O(N)$ per test case |
| 637 | [K Increment Palindrome](docs/constructive/KPAL.md) | 2038 | Only two obstructions - K = N, and a parity clash | $O(N)$ per test case |
| 639 | [Mountain](docs/constructive/MOUNTAIN.md) | 2047 | Shortest block of top rows, then greedy top-up from the heaviest row | $O(N)$ per query |
| 640 | [No Palindrome](docs/constructive/NOPALINDROME.md) | 2054 | The greedy smallest number is periodic - count the digits in one period | $O(1)$ per test case |
| 646 | [Array Sum](docs/constructive/SUMARRAY.md) | 2077 | Start from the minimum array and raise elements in steps of two | $O(N)$ per test case |
| 652 | [LCM Mania](docs/constructive/LCMMANIA.md) | 2098 | Three explicit families, impossible only for powers of two | $O(1)$ per test case |
| 653 | [Non Zero Subarray Xor](docs/constructive/SUBARRAYXOR.md) | 2101 | Choose the prefix xors first - make them 0, 1, ..., N | $O(N)$ per test case |
| 657 | [Interesting Array](docs/constructive/INTARR.md) | 2145 | Zigzag from the sorted halves, tried in both orientations | $O(N \log N)$ per test case |
| 663 | [Binary Substitution](docs/constructive/SUBSBIN.md) | 2161 | Fix the imbalance one unit per operation, then collapse the whole string | $O(N^2)$ per test case with $N \le 1000$ |
| 682 | [Yet Another Crossover Episode](docs/constructive/DIANE.md) | 2221 | Blocks with a computable contribution, separated by ones | $O(D / 99998 + 1)$ per test case |
| 698 | [Alternating Diameter](docs/constructive/ALTDIA.md) | 2300 | A star with the minority-friendly colour in the centre | $O(B + W)$ per test case |
| 718 | [Tree Distances](docs/constructive/TDISTS.md) | 2383 | Only the bipartition sizes matter; realise them with a double star | $O(\sqrt{x + y})$ per test case |
| 721 | [Construct An Array](docs/constructive/CONSTANARRAY.md) | 2419 | Blocks of M distinct values keep all frequencies within one of each other | $O(N + M)$ expected per test case |
| 723 | [Smallest Difference](docs/constructive/SMALLESTDIFF.md) | 2421 | A tight window of sorted values for the path, with decoys beside it | $O(N M \log (N M))$ per test case |
| 726 | [Adjacent Flips](docs/constructive/ADJFLIP.md) | 2426 | Ones on even positions minus ones on odd positions never changes | $O(N)$ per test case |

</details>

<details open><summary><b>Disjoint Set Union</b> (5)</summary>

| # | Problem | Difficulty | Technique | Time |
|---:|---|---:|---|---|
| 523 | [Queries with Bags](docs/disjoint-set-union/DSUBAGS.md) | unrated | Path compression and union by size | $O((N+Q)\alpha(N))$ overall |
| 543 | [Home Delivery](docs/disjoint-set-union/HDELIVER.md) | 1621 | Fast-road connected components | $O((N+M+Q)\alpha(N))$ per test case |
| 699 | [Spooky Sequences](docs/disjoint-set-union/SPOOKYSEQ.md) | 2304 | Interleave the components, then permute equal strengths inside each | $O((N + M)\,\alpha(N))$ per test case after factorial precomputation |
| 707 | [Ancient Berland Roads](docs/disjoint-set-union/ABROADS.md) | 2324 | Process the queries backwards - deletions become unions | $O((N + M + Q) \log (N + M + Q))$ |
| 720 | [Connect All Cities](docs/disjoint-set-union/CNCTCT.md) | 2417 | Kruskal over bits - each bit is a clique of equal-weight edges | $O(30 \cdot N \cdot \alpha(N))$ per test case |

</details>

<details open><summary><b>Dynamic Programming</b> (41)</summary>

| # | Problem | Difficulty | Technique | Time |
|---:|---|---:|---|---|
| 357 | [The White Knight](docs/dynamic-programming/E1.md) | 1530 | Layered DP over columns of a DAG | $O(N^2)$ per test case |
| 358 | [Magic Rankings](docs/dynamic-programming/MGCRNK.md) | 1540 | Maximising an average with a fixed denominator | $O(N^2)$ per test case |
| 359 | [Gravity Guy](docs/dynamic-programming/GRGUY.md) | 1568 | Two-state DP with a zero-cost move | $O(n)$ per test case |
| 360 | [Chef and Wedding Arrangements](docs/dynamic-programming/CHEFWED.md) | 1841 | Partition DP with an incrementally maintained segment cost | $O(N^2)$ per test case |
| 362 | [Dish Distribution](docs/dynamic-programming/DISHDIS.md) | 1596 | Bounded compositions via a prefix-sum convolution | $O(nm)$ per test case |
| 503 | [K-Concatenation](docs/dynamic-programming/KCON.md) | 1780 | Kadane over two copies plus profitable middle copies | $O(N)$ per test case |
| 515 | [The Great Wall of Byteland](docs/dynamic-programming/BWALL.md) | 1796 | Profile tiling with exponentiated transfer matrices | $O(\log N)$ per test case after $O(\log N_{max})$ fixed-size matrix preprocessing |
| 526 | [Subtree Removal](docs/dynamic-programming/SUBREM.md) | 2010 | Keep a subtree optimally or remove it for one penalty | $O(N)$ per test case |
| 534 | [Doubly Increasing Path](docs/dynamic-programming/DINCPATH.md) | 2493 | Process oriented edges in batches of equal differences | $O(N+M\log M)$ per test case |
| 558 | [Birthday Gift](docs/dynamic-programming/CHEFGIFT.md) | 1868 | Shortest transfer costs followed by stage DP | $O(M^3+NM^2)$ per test case |
| 559 | [Treasure Hunting](docs/dynamic-programming/N1.md) | 1634 | BFS distances between treasures and subset tour DP | $O((K+2)N^2+2^K K^2)$ per test case for $K$ treasures |
| 573 | [Polo the Penguin and the Test](docs/dynamic-programming/PPTEST.md) | 1603 | 0-1 knapsack with total test value | $O(NW)$ per test case |
| 574 | [Paying up](docs/dynamic-programming/MARCHA1.md) | 1510 | Subset-sum reachability as an integer bitset | $O(NM/w)$ word operations per test case |
| 575 | [MasterChef](docs/dynamic-programming/MCHEF.md) | 2016 | Interval-minimum sweep and pruned removal knapsack | $O((N+M)\log M+N\log K+KB)$ per test case with $B\le\min(N,\sum_{c=1}^{200}\lfloor K/c\rfloor)$ |
| 576 | [Permutation Split](docs/dynamic-programming/PERMSPL.md) | 2996 | Subset sum of inversion-graph degrees | $O(N^2+NI/w)$ word operations per test case for $I$ total inversions |
| 577 | [Coin Partition](docs/dynamic-programming/COINPART.md) | 2804 | Balanced partition by subset-sum bitset, then a simulated hand-out order | $O(N \cdot S / w)$ per test case, $S$ the sum of the values |
| 578 | [Chef and Pepperoni Pizza Again](docs/dynamic-programming/PEPPERA.md) | 2516 | Partition row imbalances and reconstruct the reversals | $O(N^2+ND/w)$ word operations per test case for $D\le N^2/2$ total absolute imbalance |
| 579 | [Blackjack](docs/dynamic-programming/BLKJK.md) | 2903 | Earliest-prefix dominance and cardinality subset-sum bitsets | $O((NC+NQ+CY)Y/w)$ word operations per test case for $C=\min(N,Y)$ and $Q$ an initial valid swap bound |
| 580 | [Mean Mean Medians](docs/dynamic-programming/MEANMEDI.md) | 2719 | Fixed median with cardinality-indexed subset-sum bitsets on both sides | $O(N \cdot K \cdot S / w + N \cdot S)$ per test case, $S$ the largest reachable sum |
| 581 | [Count palindromes](docs/dynamic-programming/COUNTPAL.md) | 1631 | Count prefix partitions using rolling palindrome states | $O(|S|^2)$ overall |
| 583 | [Pizza Delivery](docs/dynamic-programming/DBOY.md) | 1666 | Unbounded minimum-coin DP for each exact round trip | $O(KU+N)$ per test case for $U=2\max H$ and $K$ distinct fuel amounts |
| 585 | [Trip](docs/dynamic-programming/TRIP.md) | 2005 | Sliding reachability window and shortest-level prefix counts | $O(N)$ overall |
| 586 | [String Merging](docs/dynamic-programming/STRMRG.md) | 1965 | Run compression and a bit-parallel longest common subsequence | $O(N+M+AB/w)$ word operations per test case for compressed lengths $A,B$ |
| 587 | [Girl Friend and String Gift](docs/dynamic-programming/CHGLSTGT.md) | 1986 | Minimum prefix partition using rolling palindrome detection | $O(|S|^2)$ per test case |
| 588 | [Matrix](docs/dynamic-programming/MATRIX2.md) | 2209 | Largest upper-triangular square from the row run and the diagonal neighbour | $O(N \cdot M)$ |
| 589 | [Dessert Wizard](docs/dynamic-programming/DELISH.md) | 1804 | Kadane extremes on prefixes and suffixes, joined at every split point | $O(N)$ per test case |
| 590 | [Little Elephant and Mouses](docs/dynamic-programming/LEMOUSE.md) | 1941 | Grid path DP that remembers the last move to avoid double counting | $O(N \cdot M)$ per test case |
| 592 | [Chef and Two String](docs/dynamic-programming/CHEFTWOS.md) | 2233 | Three-state automaton for good strings, run on both strings at once | $O(N)$ per test case |
| 600 | [A-E Hash Function](docs/dynamic-programming/AEHASH.md) | 1832 | Memoised hash distributions per (length, number of A) with a max-convolution | $O(N \cdot A^2 \cdot H)$ in the worst case over all states, $H$ the largest hash value |
| 601 | [Bytelandian Robots](docs/dynamic-programming/F2.md) | 1844 | Distinct subsequences by end position, with last-occurrence correction | $O(N \cdot \min(N, L))$ per test case |
| 628 | [Rock Paper Scissors](docs/dynamic-programming/ROPASCI.md) | 2013 | Suffix as a function on the three moves, composed right to left | $O(N)$ per test case |
| 642 | [Tetris](docs/dynamic-programming/SPCP6.md) | 2062 | Ways by lines cleared and whose turn it is | $O(\max L + T)$ |
| 679 | [Circular Merging](docs/dynamic-programming/CIRMERGE.md) | 2208 | Interval merging on the doubled circle with Knuth optimisation | $O(N^2)$ per test case |
| 686 | [Little Elephant and T-Shirts](docs/dynamic-programming/TSHIRTS.md) | 2242 | Bitmask over people, processing the 100 shirts one at a time | $O(100 \cdot 2^N \cdot N)$ per test case |
| 697 | [Search for 404](docs/dynamic-programming/CS2023_404.md) | 2296 | Subsequence-counting DP summed over all replacements | $O(N)$ per test case |
| 701 | [K-Subarrays](docs/dynamic-programming/CHESUB.md) | 2306 | Two arrays per count - subarray still open, or best so far | $O(N \cdot K)$ per test case |
| 703 | [Merging Binary Strings](docs/dynamic-programming/MERGEBS.md) | 2318 | Merge DP where appending a zero costs the ones already placed | $O(N^2)$ per test case |
| 716 | [Chandelier](docs/dynamic-programming/CHANDWEIGHT.md) | 2368 | Requirements propagated outwards from the first support that breaks | $O(N)$ per test case |
| 725 | [Two Counters](docs/dynamic-programming/TWOCOUNTERS.md) | 2425 | Only the difference of the counters matters, and only within [-2, 2] | $O(N + M)$ per test case |
| 729 | [Good Sequence](docs/dynamic-programming/GSEQ.md) | 2451 | Longest chain of boundaries whose prefix value rises by exactly one | $O(N)$ expected per test case |
| 732 | [Mex Subsequence](docs/dynamic-programming/MEXSUB.md) | 2494 | Every part needs all values below the global MEX - count partitions with a prefix-sum DP | $O(N \log N)$ per test case |

</details>

<details open><summary><b>Fenwick Tree</b> (1)</summary>

| # | Problem | Difficulty | Technique | Time |
|---:|---|---:|---|---|
| 555 | [Gravel](docs/fenwick-tree/SPREAD.md) | 1822 | Range additions become two difference-array point updates | $O((N+M)\log N)$ overall |

</details>

<details open><summary><b>Game Theory</b> (6)</summary>

| # | Problem | Difficulty | Technique | Time |
|---:|---|---:|---|---|
| 226 | [String Game ](docs/game-theory/STRAME.md) | 1413 | Counting the forced number of moves | $O(N)$ per test case |
| 241 | [Chef and Coins Game](docs/game-theory/CHCOINSG.md) | 1442 | Losing positions form a residue class | $O(1)$ per test case |
| 442 | [Game on a Strip](docs/game-theory/ARRGAME.md) | 1705 | Largest free run against the runner-up | $O(N)$ per test case |
| 570 | [Prime Game](docs/game-theory/PRIGAME.md) | 1792 | Prime-count threshold via the smallest forbidden prime product | $O(V\log\log V+T)$ overall for $V=\max X$ |
| 635 | [Gold Mining](docs/game-theory/GOLMINE.md) | 2033 | Every mine is split in proportion to the mining speeds | $O(N)$ per test case |
| 722 | [One or All](docs/game-theory/ONEORALL.md) | 2420 | Parity of the total, plus the parity of the minimum when N is even | $O(N)$ per test case |

</details>

<details open><summary><b>Geometry</b> (9)</summary>

| # | Problem | Difficulty | Technique | Time |
|---:|---|---:|---|---|
| 52 | [Chessboard Distance](docs/geometry/CHESSDIST.md) | 690 | Chebyshev distance | $O(1)$ per test case |
| 69 | [Cyclic Quadrilateral](docs/geometry/CYCLICQD.md) | 735 | Cyclic quadrilateral angle condition | $O(1)$ per test case |
| 108 | [Area OR Perimeter](docs/geometry/AREAPERI.md) | 590 | Comparing area against perimeter | $O(1)$ |
| 247 | [Triangle Classification](docs/geometry/TRIANGCL.md) | 1462 | Classifying with squared lengths | $O(1)$ per test case |
| 252 | [Chef and Three Dogs](docs/geometry/CHDOGS.md) | 1473 | Pursuit curve by relative closing speed | $O(1)$ per test case |
| 383 | [Polygon Relationship](docs/geometry/POLYREL.md) | 1460 | Halving the vertex count down to a triangle | $O(N)$ per test case, all of it input reading |
| 446 | [Devu and Perfume](docs/geometry/DEVPERF.md) | 1708 | Manhattan 1-centre via rotated coordinates | $O(nm + n \log m)$ per test case |
| 517 | [Ada King](docs/geometry/ADAKNG.md) | 1581 | Clip a Chebyshev-distance square to the chessboard | $O(1)$ per test case |
| 593 | [Physical Exercise](docs/geometry/PHCUL.md) | 1865 | Precomputed nearest finish, then all pairs in both visiting orders | $O(N \cdot M + (N + M) \cdot K)$ per test case |

</details>

<details open><summary><b>Graphs</b> (28)</summary>

| # | Problem | Difficulty | Technique | Time |
|---:|---|---:|---|---|
| 413 | [Fire Escape Routes](docs/graphs/FIRESC.md) | 1671 | Connected components by DSU, then a product of sizes | $O((N + M)\,\alpha(N))$ per test case |
| 486 | [Maximum Size](docs/graphs/RISK.md) | 2113 | Connected components, then alternating greedy picks | $O(NM)$ per test case |
| 504 | [Capital Movement](docs/graphs/CAPIMOVE.md) | 1780 | Scan population order while marking each closed neighbourhood | $O(N\log N)$ per test case |
| 518 | [Snakes and transition from Capitalism to Socialism](docs/graphs/SNSOCIAL.md) | unrated | Multi-source BFS from all maximum-wealth cells | $O(NM)$ per test case |
| 520 | [Find Tree Diameter](docs/graphs/DIAMTREE.md) | 1620 | Two breadth-first searches find a tree diameter | $O(N)$ per test case |
| 521 | [Root the Tree](docs/graphs/ROOTTREE.md) | 1934 | Count excess incoming edges in a directed tree | $O(N)$ per test case |
| 525 | [Cricket Match](docs/graphs/CRIMCH.md) | 1350 | Bipartite colouring of every connected component | $O(N+M)$ per test case |
| 528 | [Fence - INOI 2017](docs/graphs/TINOI17A.md) | unrated | Sparse flood fill with exposed-side counting | $O(N)$ expected overall |
| 530 | [Moving Segments](docs/graphs/SEGDIR.md) | 1940 | Two-colour equal-speed interval overlaps by maximum depth | $O(N\log N)$ per test case |
| 533 | [Tourists in Mancunia](docs/graphs/TOURISTS.md) | 2133 | Orient an undirected Euler tour | $O(N+E)$ overall |
| 535 | [Chef and Reversing](docs/graphs/REVERSE.md) | 1879 | 0-1 BFS on original and reversed edge choices | $O(N+M)$ overall |
| 536 | [Chef and Digit Jumps](docs/graphs/DIGJUMP.md) | 1886 | BFS with each equal-digit group expanded once | $O(N)$ overall |
| 537 | [Galactik Football](docs/graphs/GALACTIK.md) | 1860 | Connect component minima in a star | $O(N+M)$ overall |
| 538 | [India Fights Corona](docs/graphs/CORONA.md) | 2560 | Multi-source Dijkstra seeded with hospital prices | $O((N+M)\log N)$ per test case |
| 540 | [Per Capita Income](docs/graphs/PERCAPTA.md) | 2132 | Largest component among maximum-ratio provinces | $O(N+M)$ per test case |
| 541 | [FCAR](docs/graphs/INSQ15_F.md) | unrated | Dijkstra on city and current travel mode | $O((N+R)\log N)$ overall |
| 542 | [Road Decoration](docs/graphs/AMR14B.md) | unrated | Compare the cheapest shortest-path tree with an MST | $O(M\log N)$ per test case |
| 548 | [Ciel and Tomya](docs/graphs/CIELTOMY.md) | 1877 | Dijkstra with counts of equal shortest routes | $O((N+M)\log N)$ per test case |
| 549 | [Petersen Graph](docs/graphs/PETERSEN.md) | 1894 | Try the two starting vertices and follow unique letter transitions | $O(|S|)$ per test case |
| 552 | [Kingdom Unity](docs/graphs/KINGCON.md) | 1851 | Iterative low-link articulation-point search | $O(N+M)$ per test case |
| 554 | [End Of The World](docs/graphs/CHEFHACK.md) | 1730 | Flood-fill nonprime parity components in row-major order | $O(V\log\log V+\pi(V)+K\log\pi(V)+\sum N^2)$ overall for $K$ prime cells and maximum password $V$ |
| 556 | [Curry Stained Napkin](docs/graphs/F3.md) | 1815 | Count mirrored copies of each original stained component | $O(64+\log N)$ per test case |
| 557 | [Maximal Score Path](docs/graphs/RG_01.md) | 1836 | Maximum spanning tree preserves all bottleneck paths | $O(E\log E+V^2)$ overall |
| 560 | [Maze of Digits](docs/graphs/K3.md) | 1859 | BFS over position and collected digit sum | $O((X+1)(M+1)(N+1))$ per test case |
| 561 | [Soccer League](docs/graphs/M3.md) | 1906 | League elimination as a maximum-flow feasibility test | $O(N^5)$ worst case per test case - $N$ Dinic runs on $O(N)$ vertices and $O(N^2)$ edges |
| 625 | [Winter](docs/graphs/ELWINTER.md) | 2007 | Lazy multi-source BFS driven by a time-ordered heap | $O((N + M) \log N + Q)$ |
| 655 | [Travelling in the Graph](docs/graphs/TRAVELLING.md) | 2108 | 0-1 BFS where only unit-length added edges are ever needed | $O(N + M)$ per test case |
| 717 | [Minimal Travel Time](docs/graphs/CLASSES.md) | 2379 | BFS distances from the hostel, then the K nearest subjects | $O(N + M + S \log S)$ per test case |

</details>

<details open><summary><b>Greedy</b> (76)</summary>

| # | Problem | Difficulty | Technique | Time |
|---:|---|---:|---|---|
| 34 | [Maximise the Tastiness](docs/greedy/MAXTASTE.md) | 627 | Independent choices optimised separately | $O(1)$ per test case |
| 51 | [X Jumps](docs/greedy/XJUMP.md) | 686 | Prefer the large step, then settle the remainder | $O(1)$ per test case |
| 57 | [Chef and his Apps](docs/greedy/CHEFAPPS.md) | 702 | Remove the largest item first | $O(1)$ per test case |
| 59 | [Minimum number of coins](docs/greedy/MINCOINS.md) | 711 | Largest denomination first | $O(1)$ per test case |
| 66 | [A or B](docs/greedy/AORB.md) | 728 | Scheduling order and the exchange argument | $O(1)$ per test case |
| 82 | [Single-use Attack](docs/greedy/SINGLEUSE.md) | 777 | Comparing both strategies explicitly | $O(1)$ per test case |
| 104 | [Smallest Numbers of Notes](docs/greedy/FLOW005.md) | 750 | Greedy change-making in a canonical system | $O(k)$ per test case, $k = 6$ denominations |
| 127 | [Peaceful Party](docs/greedy/MAYOR_PARTY.md) | 898 | Choosing between mutually exclusive groups | $O(1)$ per test case |
| 131 | [Avoid Contact](docs/greedy/AVOIDCONTACT.md) | 907 | Packing with separation constraints | $O(1)$ per test case |
| 146 | [Janmansh at Fruit Market](docs/greedy/JMARKET.md) | 947 | Cheapest choice under a diversity constraint | $O(1)$ per test case |
| 160 | [The Two Dishes](docs/greedy/MAX_DIFF.md) | 1254 | Pushing one variable to its bound | $O(1)$ per test case |
| 162 | [Two Dishes](docs/greedy/TWODISH.md) | 1140 | Bottleneck across shared and exclusive resources | $O(1)$ per test case |
| 175 | [Make them equal](docs/greedy/MAKEEQUAL.md) | 1267 | Bounded by the widest gap | $O(N)$ per test case |
| 187 | [Magical Doors](docs/greedy/MAGDOORS.md) | 1355 | Tracking a global flip as parity | $O(|S|)$ per test case |
| 199 | [Maximise the Subsequence Sum](docs/greedy/SIGNFLIP.md) | 1308 | Flip the largest magnitudes first | $O(N \log N)$ per test case |
| 200 | [Daanish and Problems](docs/greedy/DIV03.md) | 1388 | Spending a budget from the top down | $O(1)$ per test case — ten fixed difficulties |
| 202 | [Chopsticks](docs/greedy/TACHSTCK.md) | 1320 | Pairing adjacent elements after sorting | $O(N \log N)$ |
| 203 | [Sticks](docs/greedy/STICKS.md) | 1261 | Largest two pairs by frequency | $O(N \log N)$ per test case |
| 209 | [Lazy Salesman](docs/greedy/HOLIDAYS.md) | 1161 | Take the largest items first | $O(N \log N)$ per test case |
| 220 | [Average Permutation](docs/greedy/AVGPERM.md) | 1401 | Pair large values with small weights | $O(N)$ per test case |
| 222 | [Mighty Friend](docs/greedy/MTYFRI.md) | 1406 | Exchange the largest for the smallest | $O(N \log N)$ per test case |
| 225 | [Plusle and Minun on Array](docs/greedy/PMA.md) | 1412 | Best single swap | $O(N)$ per test case |
| 227 | [Remove Element](docs/greedy/REMELEM.md) | 1415 | The smallest element as universal partner | $O(N)$ per test case |
| 239 | [Akash and Dinner](docs/greedy/CHEFDINE.md) | 1438 | Cheapest representative per group | $O(N \log N)$ per test case |
| 270 | [Subarray Removal](docs/greedy/SUBARRAYREM.md) | 1505 | Budgeting two resources | $O(N)$ per test case |
| 272 | [Magda and Silly Pairs](docs/greedy/SILLYPRS.md) | 1507 | Matching by parity | $O(N)$ per test case |
| 283 | [Admins and Shopping](docs/greedy/ADMINSHOP.md) | 1529 | The larger of two independent lower bounds | $O(N)$ per test case |
| 286 | [Let us play with rank list](docs/greedy/RANKLIST.md) | 1543 | How much deficit a given number of edits can absorb | $O(\sqrt{S})$ per test case |
| 296 | [The One On The Last Night](docs/greedy/S06E06.md) | 1596 | Raise the smallest digit first | $O(d \log d)$ per test case with $d \leq 7$ digits |
| 302 | [Chef And Adjacent Sums](docs/greedy/CHFADJSUM.md) | 1604 | Keeping the heaviest elements apart | $O(N)$ per test case |
| 304 | [Positive array](docs/greedy/CIREQ.md) | 1620 | Hall's condition on value-capped positions | $O(N)$ per test case |
| 315 | [Max Mex](docs/greedy/MEX.md) | 1478 | Spending a budget on the smallest gaps first | $O(N + V)$ per test case |
| 340 | [IPC Trainers](docs/greedy/IPCTRAIN.md) | 1500 | Exchange argument with a max-heap | $O((N + D) \log N)$ per test case |
| 342 | [Iron, Magnet and Wall](docs/greedy/FEMA2.md) | 1725 | Interval bipartite matching with two queues | $O(N)$ per test case |
| 372 | [Sleepy Chef](docs/greedy/FILL01.md) | 1445 | Independent runs, each packed by division | $O(N)$ per test case |
| 374 | [The Nights Watch](docs/greedy/WTCH.md) | 1441 | Leftmost-feasible placement | $O(N)$ per test case |
| 377 | [High Frequency](docs/greedy/HIGHFREQ.md) | 1443 | Halving the top frequency against the runner-up | $O(N)$ per test case |
| 380 | [Largest Family](docs/greedy/LARGEFAM.md) | 1532 | Maximising a set size under a sum budget | $O(N \log N)$ per test case |
| 381 | [Sticks and Rectangles](docs/greedy/RECSTI.md) | 1555 | Pairing by length, then pairing the pairs | $O(N + \max L)$ per test case |
| 388 | [List of Lists](docs/greedy/LISTLIST.md) | 1567 | Counting how many singletons can survive | $O(N)$ per test case |
| 391 | [Chain of Doughnuts](docs/greedy/DONUTS.md) | 1611 | Trading sacrificed chains against links needed | $O(M \log M)$ per test case |
| 392 | [Bench Press](docs/greedy/BENCHP.md) | 1611 | Frequency pairing for a symmetric load | $O(N)$ per test case |
| 394 | [Maximum Subarray ](docs/greedy/MAXSUBARR.md) | 1613 | Kadane plus a freely orderable block | $O(N + M)$ per test case |
| 401 | [Zebra Crossing](docs/greedy/ZEBRA.md) | 1626 | Earliest hops, then one long final leap | $O(N)$ per test case |
| 411 | [Frequency Array Retrieval](docs/greedy/FREQARRRET.md) | 1654 | Lexicographic labelling of equal-frequency groups | $O(N)$ per test case |
| 415 | [Chef and Water Car](docs/greedy/CHEFCAR.md) | 1683 | Pricing each litre by its earliest legal purchase | $O(1)$ per test case |
| 422 | [Encrypt Value](docs/greedy/ENV.md) | 1633 | Choosing which elements to add rather than multiply | $O(N)$ per test case |
| 423 | [Minimise Maximum Subarray Sum](docs/greedy/MINIMISEMAX.md) | 1649 | Two independent lower bounds that are jointly attainable | $O(1)$ per test case |
| 427 | [Stamps 100](docs/greedy/S100.md) | 1631 | A right-to-left cascade zeroes everything after one position | $O(N)$ per test case |
| 430 | [K-Subarrays](docs/greedy/KSUB.md) | 1663 | Earliest cut maximises the number of GCD-$G$ pieces | $O(N \log A)$ per test case |
| 431 | [Maximum Median Matching](docs/greedy/MEDMAXMATCH.md) | 1647 | Opposite pairing of the top halves | $O(N \log N)$ per test case |
| 432 | [Building Towers](docs/greedy/TOWERTOP.md) | 1693 | Doubling to the first tower, then one per operation | $O(1)$ per test case |
| 443 | [Buying Sweets](docs/greedy/BUYSWEET.md) | 1706 | Batching purchases of the cheapest net-cost sweet | $O(N \log N)$ per test case |
| 444 | [Lumpy - The Bus Driver](docs/greedy/LUMPYBUS.md) | 1708 | Cheapest refunds first, paid with coins of the larger denomination | $O(N \log N)$ per test case |
| 455 | [Team Formation](docs/greedy/TEAMFOR.md) | 1715 | Pair the specialists first, then spend the all-rounders | $O(N)$ per test case |
| 462 | [Bon Appetit](docs/greedy/FGFS.md) | 1734 | Independent activity selection per compartment | $O(N \log N)$ per test case |
| 465 | [Prefixing](docs/greedy/FIX.md) | 1736 | Forced slots, and the maximum everywhere else | $O(N)$ per test case |
| 474 | [One Dimensional Kingdoms](docs/greedy/ONEKING.md) | 1743 | Stabbing intervals at earliest right endpoints | $O(N \log N)$ per test case |
| 481 | [Chef and String](docs/greedy/CHRL2.md) | 1751 | Pipelined counters along a fixed pattern | $O(|S|)$ |
| 493 | [Chefland and Electricity](docs/greedy/CHEFELEC.md) | 1767 | Remove the largest gap between consecutive powered villages | $O(N)$ per test case |
| 496 | [Broken Life](docs/greedy/BRKNLIFE.md) | 1772 | Avoid advancing the subsequence matcher at question marks | $O(N)$ per test case |
| 500 | [Monks](docs/greedy/MONKS.md) | 1776 | Keep the largest feasible prefix after sorting | $O(N\log N)$ per test case |
| 505 | [01 Subsequence](docs/greedy/ZEROONE.md) | 1781 | Sort zero blocks downwards and one blocks upwards | $O(N\log N)$ per test case |
| 510 | [Prefix Zeros](docs/greedy/PREZ.md) | 1790 | Maintain the exact cost of zeroing each prefix | $O(N)$ per test case |
| 532 | [Abdullah and Toll Discounts](docs/greedy/ABDTOLL.md) | unrated | Discount the shallowest active toll when a path exceeds budget | $O(N\log N)$ per test case |
| 562 | [Byteknights and Byteknaves](docs/greedy/BYTEISLE.md) | 1919 | Valid total counts followed by lexicographic candidate elimination | $O(N\log N)$ per test case |
| 654 | [Wishcraft](docs/greedy/MAJIK.md) | 2105 | Keep the two extremes and absorb the largest absolute values into them | $O(N \log N)$ per test case |
| 658 | [Maximising Vacations](docs/greedy/MAXVAC.md) | 2147 | Vacations per run of holidays, plus the best gain from bridging one workday | $O(N)$ per test case |
| 664 | [Chef Goes Shopping](docs/greedy/CHEFSHOPPING.md) | 2164 | Every original boundary is paid once, in its cheaper direction | $O(N)$ per test case |
| 673 | [Mexy Array](docs/greedy/MEXYARR.md) | 2190 | Reserve constrained values until their last use and always insert the smallest allowed value | $O(N \log N)$ per test case |
| 680 | [Mahesh and his lost array](docs/greedy/ANUMLA.md) | 2212 | Smallest unexplained subset sum is the next element | $O(N \cdot 2^N)$ per test case |
| 690 | [Maximize 1s](docs/greedy/MAX1S.md) | 2255 | Positional weights and a maximum-sum segment of flip gains | $O(N)$ per test case |
| 694 | [Saving a gift of love](docs/greedy/ASHIGIFT.md) | 2265 | Walk the path backwards, keeping the group size needed for the rest | $O((B + C) \log (B + C))$ per test case |
| 696 | [Chroma Swap](docs/greedy/ASH57.md) | 2271 | Colours present in B form free pools; pick the smallest usable value greedily | $O(N \log N)$ per test case |
| 705 | [Palindrome In Making](docs/greedy/MAKEPAL3.md) | 2322 | Mirror differences, removed in signed layers | $O(N)$ per test case |
| 728 | [Balanced Suffix](docs/greedy/BALSUFF.md) | 2447 | Build left to right, keeping the remaining multiset balanced | $O(26 \cdot N)$ per test case |

</details>

<details open><summary><b>Hashing</b> (4)</summary>

| # | Problem | Difficulty | Technique | Time |
|---:|---|---:|---|---|
| 494 | [Rectangles Counting](docs/hashing/RECTCNT.md) | 1770 | Group vertical sides by their two heights | $O(N)$ expected per test case |
| 519 | [IS IT DSU HARD!!](docs/hashing/CFMAR04.md) | unrated | Use letter-frequency tuples as anagram signatures | $O(\sum |S_i|+26N)$ overall |
| 693 | [ABC-Strings](docs/hashing/ABCSTR.md) | 2264 | Equal prefix states (A-B, A-C) mark balanced substrings | $O(N)$ expected |
| 727 | [Max Shift After XOR](docs/hashing/MAXCYCSHIFT.md) | 2444 | Sliding window over the prefix xors of the doubled array | $O(N)$ expected per test case |

</details>

<details open><summary><b>Heaps</b> (3)</summary>

| # | Problem | Difficulty | Technique | Time |
|---:|---|---:|---|---|
| 339 | [Lowest Sum](docs/heaps/LOWSUM.md) | 2302 | $k$ smallest pairwise sums | $O(K \log K + n \log n)$ per test case, where $n = \max q_i$ |
| 404 | [XOR with smallest element](docs/heaps/SMALLXOR.md) | 1635 | Detecting the two-cycle that ends the process | $O(N \log N)$ per test case |
| 692 | [Maximum K Sums](docs/heaps/KSUM.md) | 2260 | K-way merge of the decreasing lists of sums per left endpoint | $O(N + K \log N)$ |

</details>

<details open><summary><b>Number Theory</b> (86)</summary>

| # | Problem | Difficulty | Technique | Time |
|---:|---|---:|---|---|
| 26 | [Good Program](docs/number-theory/NIBBLE.md) | 593 | Divisibility test | $O(1)$ per test case |
| 30 | [Test Score](docs/number-theory/CHEFSCORE.md) | 610 | Divisibility with an upper bound | $O(1)$ per test case |
| 31 | [Jenga Night](docs/number-theory/JENGA.md) | 613 | Divisibility as an exact-fit condition | $O(1)$ per test case |
| 41 | [Mario and Transformation](docs/number-theory/TRANSFORM.md) | 649 | Cyclic state via modulo | $O(1)$ per test case |
| 46 | [Candy Distribution](docs/number-theory/CANDYDIST.md) | 668 | Divisibility by a composite modulus | $O(1)$ per test case |
| 54 | [It is My Serve](docs/number-theory/MYSERVE.md) | 691 | Block index parity via modulo | $O(1)$ per test case |
| 77 | [Dracula Eats](docs/number-theory/CHEAT.md) | 763 | Counting residues in a range | $O(1)$ per test case |
| 80 | [Mutated Minions](docs/number-theory/CHN15A.md) | 970 | Divisibility after a uniform shift | $O(N)$ per test case |
| 90 | [Primality Test](docs/number-theory/PRB01.md) | 850 | Trial division to the square root | $O(\sqrt{N})$ per test case |
| 93 | [Cars and Bikes](docs/number-theory/TYRES.md) | 809 | Remainder modulo 4 | $O(1)$ per test case |
| 95 | [Equalizing Numbers](docs/number-theory/EQLZING.md) | 823 | Finding the invariant | $O(1)$ per test case |
| 111 | [Construct N](docs/number-theory/CONN.md) | 860 | Parity plus a threshold | $O(1)$ per test case |
| 118 | [Counting Pretty Numbers](docs/number-theory/NUM239.md) | 873 | Counting residues with a prefix function | $O(1)$ per test case |
| 121 | [Find the Direction](docs/number-theory/FACEDIR.md) | 880 | Cyclic state via modulo | $O(1)$ per test case |
| 132 | [Problem](docs/number-theory/PR0BLEM.md) | 908 | Parity invariant | $O(1)$ per test case |
| 139 | [Akash and Missing Class](docs/number-theory/CHFCLASS.md) | 931 | Counting residues in a range | $O(1)$ per test case |
| 143 | [Two vs Ten](docs/number-theory/TWOVSTEN.md) | 936 | Which prime factors an operation can supply | $O(1)$ per test case |
| 152 | [Joining Date](docs/number-theory/JOINING.md) | 970 | Counting residues in a range | $O(1)$ per test case |
| 166 | [Smallest Possible Whole Number](docs/number-theory/SMOL.md) | 1306 | Modulo, with a zero-divisor guard | $O(1)$ per test case |
| 170 | [Maximum Length Even Subarray](docs/number-theory/MXEVNSUB.md) | 1221 | Parity of a triangular number | $O(1)$ per test case |
| 180 | [Hard Cash](docs/number-theory/CASH.md) | 1300 | A conserved total modulo K | $O(N)$ per test case |
| 204 | [Chef and Linear Chess](docs/number-theory/LINCHESS.md) | 1200 | Divisors as reachable positions | $O(N)$ per test case |
| 231 | [Decreasing Srrnmieeda](docs/number-theory/DECREM.md) | 1423 | A strictly decreasing chain of remainders | $O(1)$ per test case |
| 243 | [Cutting Pizza](docs/number-theory/CUTPIZ.md) | 1446 | GCD of angular gaps | $O(n + \log 360)$ per test case |
| 246 | [Yet another SOD problem](docs/number-theory/SOD3.md) | 1459 | Digit sum congruent to the value mod 3 | $O(1)$ per test case |
| 248 | [Chef and Adventures](docs/number-theory/CHEFADV.md) | 1462 | Divisibility with an optional one-off offset | $O(1)$ per test case |
| 255 | [Majin Vegeta](docs/number-theory/VEGETA.md) | 1477 | Sieve counting distinct prime factors | $O(V \log\log V)$ once, then $O(m - n)$ per query |
| 258 | [Jogging](docs/number-theory/JOGGING.md) | 1484 | A doubling recurrence, taken modulo | $O(\log N)$ per test case |
| 260 | [Chef Odd](docs/number-theory/CHEFODD.md) | 1486 | Parity and capacity constraints together | $O(1)$ per test case |
| 274 | [Reduce to One](docs/number-theory/REDONE.md) | 1507 | A telescoping product in disguise | $O(1)$ per test case after an $O(N)$ precomputation |
| 279 | [Split Sums](docs/number-theory/SPSUM.md) | 1524 | Splitting a fixed total under a gcd condition | $O(\log S)$ per test case |
| 280 | [Guddu on a Date](docs/number-theory/KS2.md) | 1525 | A bijection between prefixes and solutions | $O(\log N)$ per test case |
| 282 | [Monsters](docs/number-theory/SPCP5.md) | 1527 | Sieve plus a short search | $O(\log H)$ per test case after an $O(V \log\log V)$ sieve |
| 288 | [Catch the Thief](docs/number-theory/CATHIEF.md) | 1550 | An invariant from step size and parity | $O(1)$ per test case |
| 297 | [Andrew and the Meatballs again](docs/number-theory/AMMEAT2.md) | 1597 | A shared prime factor guarantees non-coprimality | $O(K)$ per test case |
| 299 | [Non-Divisor Array](docs/number-theory/DIVCOL.md) | 1623 | Colouring the divisibility order by prime-factor count | $O(N \log \log N)$ per test case |
| 307 | [Minimum Number of Pizzas](docs/number-theory/MINPIZZAS.md) | 1532 | Smallest multiplier for divisibility | $O(\log \min(N,K))$ per test case |
| 308 | [Alternating Work Days](docs/number-theory/ALTER.md) | 1486 | Divisibility plus an alternation constraint | $O(1)$ per test case |
| 332 | [Modular Equation](docs/number-theory/MODEQ.md) | 1761 | Reducing a nested modulo to a divisibility test | $O(N \cdot d)$ per test case after an $O(M)$ sieve |
| 353 | [Count K-Primes](docs/number-theory/KPRIME.md) | 1549 | Sieve of distinct prime factors plus prefix counts | $O(V \log \log V + 5V)$ precomputation, $O(1)$ per query |
| 364 | [Chef and GCD](docs/number-theory/CHFGCD.md) | 1481 | Case analysis on parity | $O(\log \min(X,Y))$ per test case |
| 365 | [Arranging Cup-cakes](docs/number-theory/RESQ.md) | 1322 | Divisor nearest the square root | $O(\sqrt{N})$ per test case |
| 366 | [Appy and Contest](docs/number-theory/HMAPPY2.md) | 1358 | Counting multiples with inclusion-exclusion | $O(\log \min(A,B))$ per test case |
| 367 | [Chef and Keyboard](docs/number-theory/CHEFKEY.md) | 1323 | Divisor pairs under a box constraint | $O(\sqrt{c})$ per test case |
| 370 | [Yet Another Cute Girl](docs/number-theory/PRETNUM.md) | 1850 | Segmented sieve plus prime-power exponents | $O(\sqrt{R} \log\log \sqrt{R} + (R-L))$ per test case |
| 376 | [Cakewalk](docs/number-theory/CKWLK.md) | 1474 | Prime factorisation into a two-variable range test | $O(\log N)$ per test case |
| 395 | [Chef And The Hiring Event](docs/number-theory/CHEARMY.md) | 1613 | Product expansion for parity, then base-5 indexing | $O(\log K)$ per test case |
| 410 | [Find eX](docs/number-theory/FIND_X.md) | 1651 | Shared remainder forces a multiple of the LCM | $O(\log \min(B,D))$ per test case |
| 419 | [Number Hunt](docs/number-theory/NUMHUNT.md) | 1638 | Product of the two smallest admissible primes | $O(g \log^3 X)$ per test case, where $g$ is the local prime gap |
| 424 | [Chef Product](docs/number-theory/CHEFPRODUCT.md) | 1658 | Size feasibility from a square bound and a parity | $O(1)$ per test case |
| 434 | [The Optimal Pairs](docs/number-theory/OPTPAIRS.md) | 1666 | The minimum is always N, attained by a divisor family | $O(\sqrt{N})$ per test case |
| 435 | [Array sorting](docs/number-theory/ARRSORT.md) | 1681 | GCD of the displacements | $O(N \log N)$ per test case |
| 437 | [Exam Cheating](docs/number-theory/EXAMCHT.md) | 1639 | Counting divisors of a difference | $O(\sqrt{|A-B|})$ per test case |
| 450 | [Sum Product Segments](docs/number-theory/SUMPRODSEG.md) | 1713 | Every family shares a pivot, so the pair must be mixed | $O(\sqrt{Y})$ per test case |
| 454 | [Find an integer](docs/number-theory/SUMDIV2.md) | 1714 | Simultaneous congruences solved by inspection | $O(\log \min(X,Y))$ per test case |
| 457 | [Chef and Prime Divisors](docs/number-theory/CHAPD.md) | 1720 | Stripping shared factors with repeated GCDs | $O(\log^2 \max(A,B))$ per test case |
| 464 | [Crushed Apples and a Balance Scale](docs/number-theory/APP_BAL_SCA.md) | 1736 | Halving only reaches the odd part | $O(\log M)$ per test case |
| 472 | [Modular GCD](docs/number-theory/GCDMOD.md) | 1741 | Reducing the big operand modulo the small one | $O(\log N)$ per test case |
| 477 | [Eugene and function](docs/number-theory/KFUNC.md) | 1746 | Digital roots are periodic along an arithmetic progression | $O(\log R)$ per test case |
| 482 | [Too Many Candies](docs/number-theory/ICL1903.md) | 1754 | Linear congruence solved with the extended GCD | $O(\log M)$ per test case |
| 489 | [Optimal Denomination](docs/number-theory/MINNOTES.md) | 1759 | Prefix and suffix GCD after one removal | $O(N \log V)$ per test case |
| 509 | [Strange Function](docs/number-theory/ABX01.md) | 1789 | Digital root from modular exponentiation | $O(\log N)$ per test case |
| 563 | [Prime Tuples](docs/number-theory/PTUPLES.md) | 1809 | Every prime-sum triple starts with two | $O(V\log\log V+T)$ overall for $V=\max N$ |
| 564 | [Odd Divisors](docs/number-theory/ODDDIV.md) | 1657 | Add every odd divisor to its multiples | $O(V\log V+T)$ overall for $V=\max R$ |
| 565 | [Number of Factors](docs/number-theory/NUMFACT.md) | 1710 | Add prime exponents across all factors | $O(N\pi(\sqrt V))$ trial divisions per test case after a sieve to $\sqrt V$ |
| 566 | [Special Triplets](docs/number-theory/SPCTRIPS.md) | 1673 | Reduce scaled triples to divisor summatory counts | $O(V\log V+T\sqrt V)$ overall for $V=\max N$ |
| 567 | [Levy Conjecture](docs/number-theory/LEVY.md) | 1510 | Precompute counts of prime plus twice-prime sums | $O(V\log\log V+\pi(V)^2+T)$ overall for $V=\max N$ |
| 568 | [Cool Guys](docs/number-theory/COOLGUYS.md) | 1758 | Dirichlet hyperbola count of divisible ordered pairs | $O(\sqrt N+\log N)$ per test case |
| 569 | [Churu and Balls](docs/number-theory/CBALLS.md) | 1697 | Try prime common divisors with bucketed rounding costs | $O(V\log\log V+N+V\sum_{p\le V+1}1/p+\pi(V+1))$ per test case |
| 572 | [Destroy Cells](docs/number-theory/DESTCELL.md) | 2297 | Enumerate periodic row-major positions and test column-major divisibility | $O(S\log S)$ per test case for $S=NM$ |
| 597 | [Kirito in labyrinth](docs/number-theory/KIRLAB.md) | 2047 | Longest chain DP keyed by prime factor, with a smallest-prime-factor sieve | $O(A \log \log A + N \log A)$ over the whole input, $A$ the largest value |
| 607 | [Odd Binomial Coefficients](docs/number-theory/ODDBIN.md) | 2107 | Polynomials over GF(2) split at the highest exponent bit | $O(60 \cdot 2^{M} \cdot M)$ worst case per test case with memoisation, $M \le 15$ |
| 624 | [Maximum Factors Problem](docs/number-theory/MXFACS.md) | 2006 | Remove one copy of the prime with the largest exponent | $O(\sqrt{N})$ per test case |
| 631 | [Prime Factor Division](docs/number-theory/PRIMEFACDIV.md) | 2016 | Strip common factors with repeated gcd | $O(\log^2 B)$ per test case |
| 632 | [Queries About Numbers](docs/number-theory/QNUMBER.md) | 2026 | Factorise N once and answer from prime exponents | $O(\sqrt{N} + Q \cdot \omega(N) \log K)$ |
| 647 | [Equivalent Numbers](docs/number-theory/EQUIVALENT.md) | 2087 | Reduce each number to its primitive root base | $O(\sqrt{A} + \sqrt{B})$ per uncached pair |
| 660 | [Lexicographically Largest ](docs/number-theory/LEXILARGEST.md) | 2151 | Largest multiplier coprime to the ratio of consecutive prefix gcds | $O(N \log M)$ per test case plus the short downward searches |
| 667 | [Minimum Operation](docs/number-theory/MINIMUMOP.md) | 2170 | At most two operations - common gcd, an unused prime, or 2 then 3 | $O(M_{\max} \log \log M_{\max})$ sieve, then $O(N \log A)$ per test case |
| 676 | [Chef and insomnia](docs/number-theory/CHINSM.md) | 2197 | Sliding window whose left end jumps past the latest bad partner | $O(V \log V + N \cdot \tau(V))$, $V$ the largest value |
| 677 | [Partition It](docs/number-theory/PARPERM.md) | 2202 | Only 1 and the primes above N/2 can be separated from the rest | $O(N \log \log N)$ sieve, then $O(N)$ per test case |
| 683 | [Cute Chef Gift](docs/number-theory/COPAR.md) | 2235 | Each prime spans an interval - find the first position no interval crosses | $O(V \log \log V + N \log V)$, $V$ the largest value |
| 689 | [Interesting Representation](docs/number-theory/INTREP.md) | 2251 | Multiply N by two neighbouring numbers that each add exactly one new prime | $O(1)$ per test case |
| 710 | [Candies](docs/number-theory/CANDIES3.md) | 2329 | Sum of floors as a harmonic sum over multiples | $O(N + M \log M)$ per test case |
| 715 | [Chef and Riffles](docs/number-theory/RIFFLES.md) | 2360 | A riffle is multiplication by two modulo N - 1 | $O(N + \log K)$ per test case |
| 724 | [GCD Queries](docs/number-theory/GCD_QUERIES.md) | 2422 | One min-heap of sorted indices per prime, with lazy deletion | $O(V \log \log V + (N + Q) \log V \log N)$ |
| 731 | [Squarified](docs/number-theory/SQUAR.md) | 2470 | Group by square-free kernel and take the largest non-trivial group | $O(V \log \log V + N \log V)$, $V$ the largest value in the input |

</details>

<details open><summary><b>Prefix Sums</b> (26)</summary>

| # | Problem | Difficulty | Technique | Time |
|---:|---|---:|---|---|
| 126 | [Inside The Stadium](docs/prefix-sums/INSTDUM.md) | 895 | Running total compared against the index | $O(N)$ per test case |
| 211 | [Gift Shop and Coupon](docs/prefix-sums/GFTSHP.md) | 1364 | Prefix sums with a single discount | $O(N \log N)$ per test case |
| 233 | [Parallel Processing](docs/prefix-sums/PLPROCESS.md) | 1425 | Minimising the heavier side of a split | $O(N)$ per test case |
| 298 | [Bouncing Ball](docs/prefix-sums/BOUNCE_BALL.md) | 1607 | Alternating hits balance two totals | $O(N)$ per test case |
| 328 | [Shortest Route](docs/prefix-sums/SHROUTE.md) | 1756 | Nearest qualifying index from each side | $O(N + M)$ per test case |
| 350 | [Chef and Easy Problem](docs/prefix-sums/XXOR.md) | 1810 | Per-bit prefix counts, decided bit by bit | $O(31(N + Q))$ |
| 361 | [W String](docs/prefix-sums/WSTRING.md) | 1809 | Per-letter counts over hash-delimited blocks | $O(|S| + 26 h)$ per test case, where $h$ is the number of '#' |
| 369 | [Gcd Queries](docs/prefix-sums/GCDQ.md) | 1674 | Prefix and suffix GCD arrays | $O(N \log A + Q \log A)$ per test case |
| 384 | [Dense Bracket Sequence](docs/prefix-sums/DENSE.md) | 1472 | Best split between an open prefix and a close suffix | $O(N)$ per test case |
| 418 | [Anti-Palindrome Queries](docs/prefix-sums/ANTIPALQ.md) | 1688 | Reducing a rotation condition to one count | $O(N + Q)$ per test case |
| 440 | [Mystical Numbers](docs/prefix-sums/XORGAND.md) | 1702 | The comparison reduces to equal bit lengths | $O(N + Q)$ per test case |
| 447 | [Summary Power](docs/prefix-sums/SUMPOWER.md) | 1709 | Counting each boundary's contribution | $O(N)$ per test case |
| 456 | [Maximise Sum](docs/prefix-sums/MAXIMISESUM.md) | 1715 | Per-position ceiling from prefix and suffix maxima | $O(N)$ per test case |
| 471 | [Fair Distribution](docs/prefix-sums/FAIR_DISTRIB.md) | 1741 | Reparametrising by gaps turns it into suffix sums | $O(N)$ per test case |
| 476 | [Copy and Paste](docs/prefix-sums/NCOPIES.md) | 1745 | Splitting a repeated string's running total | $O(N + M)$ per test case |
| 497 | [Triplets](docs/prefix-sums/SUMQ.md) | 1772 | Factor a triplet sum into two prefix sums | $O(P\log P+Q\log Q+R\log R)$ per test case |
| 584 | [Total Diamonds](docs/prefix-sums/VK18.md) | 1786 | Grow the square using a prefix sum of digit imbalances | $O(V+T)$ overall for $V=\max N$ |
| 594 | [Gerrymander](docs/prefix-sums/GERMANDE.md) | 1904 | Circular sliding window grouped by starting offset | $O(N)$ per test case |
| 608 | [Way Out](docs/prefix-sums/WOUT.md) | 1845 | Difference array per row, then the best window of H rows | $O(N)$ per test case |
| 611 | [Chef and Strings](docs/prefix-sums/STRQ.md) | 1930 | Prefix counts of ordered character pairs, corrected for starts before L | $O(16 \cdot N + Q)$ |
| 612 | [Sereja and Commands](docs/prefix-sums/SEACO.md) | 1990 | Reverse sweep over commands with two difference arrays | $O(N + M)$ per test case |
| 641 | [Max Range Queries](docs/prefix-sums/MAXREMOV.md) | 2057 | Net gain of removing an interval as a range sum of +1 and -1 scores | $O(N + C)$ per test case, $C = 10^5$ |
| 644 | [Angry Cyborg](docs/prefix-sums/AGCY.md) | 2072 | Range updates of a linear function with two difference arrays | $O(N + Q)$ per test case |
| 668 | [Increase 2 consecutive characters](docs/prefix-sums/CCD.md) | 2171 | The alternating sum of differences is the only invariant | $O(N + Q)$ per test case |
| 670 | [Cherry and Bits](docs/prefix-sums/CENS20A.md) | 2179 | Two-dimensional xor difference array | $O(N \cdot M + Q)$ |
| 691 | [Sum of Cube ](docs/prefix-sums/SUMOFCUBE.md) | 2259 | Expand the cube of a prefix difference and keep three running power sums | $O(N)$ per test case |

</details>

<details open><summary><b>Probability</b> (6)</summary>

| # | Problem | Difficulty | Technique | Time |
|---:|---|---:|---|---|
| 514 | [A Plus B Again!](docs/probability/TAAPLUSB.md) | 1796 | Sum the carry probabilities as a geometric series | $O(1)$ per test case |
| 603 | [Random decreasing function](docs/probability/RDF.md) | 1975 | Expectation by layers with a running prefix average, cut off after 70 steps | $O(70 \cdot \max N + T)$ |
| 606 | [Player](docs/probability/RRPLAYER.md) | 2067 | Coupon collector - a sum of geometric waiting times | $O(\max N + T)$ |
| 620 | [E - Make it Zero](docs/probability/INFDIV.md) | 2690 | Expectation recurrence over remainders, summed by quotient blocks | $O(N \sqrt{N})$ |
| 669 | [Expected Value](docs/probability/EXPVALUE.md) | 2177 | Carry the mean and the second moment through independent increments | $O(N)$ |
| 734 | [Expected Sum](docs/probability/EXPECTEDSUM.md) | 2495 | Linearity of expectation over the positions Chef draws | $O(\log p)$ per test case |

</details>

<details open><summary><b>Sets</b> (15)</summary>

| # | Problem | Difficulty | Technique | Time |
|---:|---|---:|---|---|
| 73 | [Chef and Races](docs/sets/CHEFRACES.md) | 745 | Set difference | $O(1)$ per test case |
| 130 | [Count the Holidays](docs/sets/SUNDAY.md) | 907 | Union of a fixed set with input values | $O(N)$ per test case |
| 134 | [Two Ranges](docs/sets/TWORANGES.md) | 918 | Inclusion-exclusion on intervals | $O(1)$ per test case |
| 164 | [Programming Languages](docs/sets/PROGLANG.md) | 1001 | Subset containment | $O(1)$ per test case |
| 177 | [ICPC Balloons](docs/sets/BALLOON.md) | 1205 | Smallest prefix covering a required set | $O(N)$ per test case |
| 182 | [Nobel Prize](docs/sets/NOBEL.md) | 1372 | Counting distinct values against a capacity | $O(N)$ per test case |
| 189 | [Studying Alphabet](docs/sets/ALPHABET.md) | 1123 | Subset containment | $O(|W|)$ per word |
| 201 | [Chocolate Monger](docs/sets/CM164364.md) | 1369 | Distinct count capped by a budget | $O(n)$ per test case |
| 208 | [Devu and friendship testing](docs/sets/CFRTEST.md) | 1061 | Distinct values as a capacity bound | $O(n)$ per test case |
| 215 | [Points and Lines](docs/sets/POLIN.md) | 1296 | Counting distinct coordinates independently | $O(N)$ per test case |
| 314 | [Count Distinct Values](docs/sets/CNTDIST.md) | unrated | Replacing a linear scan with a hash set | $O(n)$ overall |
| 337 | [Version Control System](docs/sets/VCS.md) | 1217 | Intersection and complement of a union | $O(M + K)$ per test case |
| 386 | [Good Pairs](docs/sets/GOODPAIRS.md) | 1469 | One-pass tally of mirrored keys | $O(N)$ per test case |
| 417 | [Fencing](docs/sets/FENCE.md) | 1696 | Perimeter as sides minus shared edges | $O(K)$ per test case |
| 451 | [Max Mex](docs/sets/MAXMEX.md) | 1714 | Keep everything except the forbidden value | $O(N)$ per test case |

</details>

<details open><summary><b>Simulation</b> (11)</summary>

| # | Problem | Difficulty | Technique | Time |
|---:|---|---:|---|---|
| 178 | [Gasoline Introduction](docs/simulation/BEGGASOL.md) | 1263 | Collecting fuel while moving forward | $O(N)$ per test case |
| 184 | [Cops and the Thief Devu](docs/simulation/COPS.md) | 1242 | Marking covered ranges over a small domain | $O(100 + M)$ per test case |
| 235 | [Full Barrier Alchemist](docs/simulation/PIPSQUIK.md) | 1426 | Walking a sequence with a consumable resource | $O(N)$ per test case |
| 278 | [When to take medicine](docs/simulation/MEDIC.md) | 1522 | Where a parity rule breaks at month boundaries | $O(1)$ per test case |
| 334 | [Sudhanva and Books](docs/simulation/SUDBOOKS.md) | 1300 | A stack, with an empty-pop guard | $O(1)$ per query |
| 402 | [UEFA Champions League](docs/simulation/UCL.md) | 1633 | Building a league table and sorting by two keys | $O(1)$ per test case (12 fixed matches) |
| 438 | [Chef and Football Match](docs/simulation/WATCHFB.md) | 1700 | Tracking the at-most-two consistent states | $O(N)$ per test case |
| 463 | [Penalty Shoot-Out II](docs/simulation/PSHOT.md) | 1735 | Best and worst completions of a prefix | $O(N)$ per test case |
| 627 | [Alternative Sufferings](docs/simulation/ALTSUFF.md) | 2011 | One simulated step, then distance to the nearest seed and parity | $O(N)$ per test case |
| 688 | [Make Them Alike](docs/simulation/ALIKE_THEM.md) | 2245 | Track which original position every final value comes from | $O(N)$ per test case |
| 735 | [College Admissions](docs/simulation/ADMIT.md) | 2496 | Simulate the admissions in exam-rank order until Chef chooses | $O(M \log M + \sum \text{list lengths})$ per test case |

</details>

<details open><summary><b>Sorting</b> (33)</summary>

| # | Problem | Difficulty | Technique | Time |
|---:|---|---:|---|---|
| 67 | [Second Largest](docs/sorting/FLOW017.md) | 520 | Median of three | $O(1)$ per test case |
| 196 | [The Smallest Pair](docs/sorting/SMPAIR.md) | 1352 | The two smallest elements | $O(N)$ per test case |
| 197 | [Racing Horses](docs/sorting/HORSES.md) | 1231 | Minimum adjacent difference after sorting | $O(N \log N)$ per test case |
| 198 | [Maximum Weight Difference](docs/sorting/MAXDIFF.md) | 1308 | Taking an extreme K-subset | $O(N \log N)$ per test case |
| 210 | [Simple Statistics](docs/sorting/SIMPSTAT.md) | 1222 | Trimmed mean | $O(N \log N)$ per test case |
| 212 | [Watson asks Does Permutation Exist](docs/sorting/PERMEXIS.md) | 1207 | Adjacent gaps in sorted order | $O(N \log N)$ per test case |
| 213 | [Maximize the Minimum](docs/sorting/MAXTHEMIN.md) | 1358 | The (K+1)-th smallest survives | $O(N \log N)$ per test case |
| 214 | [Maximum Trio](docs/sorting/MXMTRIO.md) | 1349 | Choosing extremes for a product | $O(N \log N)$ per test case |
| 221 | [Hotel Bytelandia](docs/sorting/HOTEL.md) | 1405 | Event sweep | $O(N \log N)$ per test case |
| 250 | [Approximately II](docs/sorting/APPROX2.md) | 1471 | Two pointers, then counting by value | $O(N \log N)$ per test case |
| 309 | [Sort Checker](docs/sorting/SRTCHK.md) | unrated | Verifying a claimed sort | $O(N \log N)$ per test case |
| 310 | [Counting Sort](docs/sorting/CNTSORT.md) | unrated | Counting sort over a small value range | $O(N + V)$ per test case with $V = 100$ |
| 312 | [Fair distribution](docs/sorting/SUBS.md) | unrated | Sliding a fixed-size window | $O(N \log N)$ per test case |
| 317 | [Javelin Qualification](docs/sorting/JAVELIN.md) | 1538 | Two-stage selection | $O(N \log N)$ per test case |
| 318 | [ChefWatson uses Social Network](docs/sorting/BOOKCHEF.md) | 1610 | Sorting on a composite key | $O(M \log M)$ |
| 319 | [Remove One Element](docs/sorting/REMONE.md) | 1700 | Two candidate offsets, verified by a merge | $O(N \log N)$ per test case |
| 320 | [Pair Sort Version 3](docs/sorting/PSORT3.md) | unrated | Mixed-direction composite key | $O(N \log N)$ |
| 321 | [Sort by swaps](docs/sorting/SWPSRT1.md) | unrated | Selection sort meets the swap budget exactly | $O(n^2)$ |
| 322 | [Chef Restaurant ](docs/sorting/CHEFRES.md) | 1776 | Binary search over disjoint intervals | $O((N + M) \log N)$ per test case |
| 323 | [Sort by Adjacent Swaps](docs/sorting/ADJSRT.md) | unrated | Insertion sort performs exactly the inversions | $O(n + \text{inversions})$ |
| 324 | [Stable Quick Sort](docs/sorting/QCKSRT2.md) | unrated | Which pivot choices preserve stability | $O(n)$ |
| 354 | [Chef and Frogs](docs/sorting/FROGV.md) | 1668 | Connected components from gaps in sorted order | $O(N \log N + P)$ |
| 385 | [Median of adjacent maximum numbers](docs/sorting/MXMEDIAN.md) | 1523 | Pairing extremes to lift the median | $O(N \log N)$ per test case |
| 399 | [Max Out](docs/sorting/IOPC17C.md) | 1621 | The second largest distinct value is the answer | $O(N)$ per test case |
| 405 | [Concat Sort](docs/sorting/CONCATSORT.md) | 1637 | Counting descents in the sorted order's position sequence | $O(N \log N)$ per test case |
| 421 | [Powered Parameters](docs/sorting/POWPM.md) | 1673 | Bounding the exponent, then counting by integer root | $O(N \log N + 30 \log N)$ per test case |
| 469 | [Pokemon Battles](docs/sorting/PBATTLE.md) | 1739 | Counting Pareto maxima of two orderings | $O(N \log N)$ per test case |
| 473 | [Army Training](docs/sorting/ARMTRN.md) | 1742 | Sorted split maximising a product of two sums | $O(N \log N)$ per test case |
| 638 | [Symmetric Swaps](docs/sorting/SYMARRSWAP.md) | 2041 | Smallest value window that contains an option for every index | $O(N \log N)$ per test case |
| 662 | [Musical Rods](docs/sorting/MUSROD.md) | 2160 | Exchange argument - order rods by beauty per unit length | $O(N \log N)$ per test case |
| 687 | [Chef and Ants](docs/sorting/ANTSCHEF.md) | 2244 | Swap identities at collisions, then count meetings ray by ray | $O(S \log S)$ per test case, $S$ the total number of ants |
| 711 | [Two Piles](docs/sorting/SPLITMIN.md) | 2347 | The larger maximum is at least the largest of the pair minima; pair it with its nearest lower value | $O(N \log N)$ per test case |
| 733 | [Chef Up](docs/sorting/CHEF7UP.md) | 2494 | Parity of the distance to Chef decides which officers can be cornered | $O(N \log N)$ per test case |

</details>

<details open><summary><b>Stacks</b> (4)</summary>

| # | Problem | Difficulty | Technique | Time |
|---:|---|---:|---|---|
| 338 | [Book Exercises](docs/stacks/BEX.md) | 1728 | Prefix minimum carried alongside a stack | $O(1)$ amortised per action, $O(N)$ overall |
| 498 | [Lunchtime](docs/stacks/LUNCHTIM.md) | 1773 | Monotone groups bounded by taller students | $O(N)$ per test case |
| 609 | [Chefs in Queue](docs/stacks/CHFQUEUE.md) | 2146 | Nearest strictly smaller element to the right with a monotonic stack | $O(N)$ |
| 685 | [Distinct Values](docs/stacks/DIST_VALS.md) | 2236 | Largest and second largest of a subarray are neighbours on a monotonic stack | $O(N)$ expected per test case |

</details>

<details open><summary><b>Strings</b> (44)</summary>

| # | Problem | Difficulty | Technique | Time |
|---:|---|---:|---|---|
| 24 | [Reverse The Number](docs/strings/FLOW007.md) | 420 | Digit reversal and leading zeros | $O(d)$ per test case, $d$ = number of digits |
| 44 | [Complementary Strand in a DNA](docs/strings/DNASTRAND.md) | 660 | Character-wise mapping with a translation table | $O(N)$ per test case |
| 92 | [Wordle](docs/strings/WORDLE.md) | 804 | Position-wise comparison | $O(L)$ per test case with $L = 5$ |
| 99 | [The Block Game](docs/strings/PALL01.md) | 720 | Palindrome check by reversal | $O(d)$ per test case, $d$ = number of digits |
| 105 | [Is it a VOWEL or CONSONANT](docs/strings/VOWELTB.md) | 520 | Membership test against a small set | $O(1)$ |
| 142 | [World Chess Championship](docs/strings/WCC.md) | 935 | Counting characters, then a three-way branch | $O(|S|)$ per test case |
| 148 | [Rearranging digits to get a multiple of 5](docs/strings/DIGARR.md) | 949 | Divisibility decided by one digit | $O(D)$ per test case |
| 153 | [Play Piano](docs/strings/PLAYPIAN.md) | 1180 | Validating fixed-size blocks | $O(|s|)$ per test case |
| 185 | [Pawri Meme](docs/strings/PAWRI.md) | 1182 | Substring replacement | $O(|S|)$ per test case |
| 186 | [Chef and the Wildcard Matching](docs/strings/TWOSTR.md) | 1254 | Wildcard matching, position by position | $O(|X|)$ per test case |
| 188 | [Chef and Feedback](docs/strings/ERROR.md) | 1199 | Substring search | $O(|S|)$ per test case |
| 190 | [Hiring Test](docs/strings/HIRETEST.md) | 1260 | Counting characters, then a two-branch rule | $O(N \cdot M)$ per test case |
| 191 | [Lapindromes](docs/strings/LAPIN.md) | 1159 | Comparing character frequencies | $O(|S|)$ per test case |
| 193 | [Equinox Strings](docs/strings/EQUINOX.md) | 1272 | First-character membership test | $O(N)$ per test case |
| 194 | [Snake Procession](docs/strings/SNAKPROC.md) | 1290 | Single-pass state machine | $O(L)$ per report |
| 195 | [Password](docs/strings/PASSWD.md) | 1470 | Several predicates, one with a positional restriction | $O(|S|)$ per test case |
| 205 | [Lucky Four](docs/strings/LUCKFOUR.md) | 775 | Counting a digit | $O(d)$ per number |
| 216 | [Even Splits](docs/strings/EVENSPLIT.md) | 1282 | Which orderings are reachable | $O(N)$ per test case |
| 234 | [Reversing directions](docs/strings/DIRECTI.md) | 1426 | Parsing and reversing a route | $O(N)$ per test case |
| 240 | [HTML Tags](docs/strings/HTMLTAGS.md) | 1441 | Validating a format | $O(|S|)$ per test case |
| 249 | [Magical Planks](docs/strings/MKGPLNKS.md) | 1467 | Counting runs | $O(N)$ per test case |
| 259 | [Correct Sentence](docs/strings/CORTSENT.md) | 1485 | Per-word alphabet membership | $O(\sum |S_i|)$ per test case |
| 264 | [Anti Palindrome](docs/strings/ANTIPALINDR.md) | 1488 | Forcing a palindrome to be impossible | $O(N)$ per test case |
| 266 | [Harrenhal](docs/strings/HHAL.md) | 1495 | Covering a two-letter string with palindromes | $O(|H|)$ per test case |
| 277 | [Concat Palindrome](docs/strings/CONCATPAL.md) | 1520 | Multiset containment forced by mirroring | $O(N + M)$ per test case |
| 285 | [Flip the String](docs/strings/FLIP.md) | 1538 | Two independent parity classes | $O(|A|)$ per test case |
| 290 | [Chef and Sign Sequences](docs/strings/CHEFSIGN.md) | 1563 | Run lengths scanned from both directions | $O(|s|)$ per test case |
| 291 | [Boring String](docs/strings/BORSTR.md) | 1566 | Longest repeated run | $O(N)$ per test case |
| 335 | [Attendance](docs/strings/ATTND.md) | 1148 | Frequency of a key field | $O(N)$ per test case |
| 409 | [Permutation and Palindrome](docs/strings/PERMPAL.md) | 1651 | Pairing equal letters inward from both ends | $O(n)$ per test case |
| 425 | [3-Blast Palindrome](docs/strings/BLAST3.md) | 1699 | Residue classes of the surviving positions | $O(N)$ per test case |
| 445 | [Spreading Charges](docs/strings/CHRGES.md) | 1708 | Runs of zeros classified by their bounding charges | $O(N)$ per test case |
| 458 | [Oracle Devu and Longest Common Subsequence](docs/strings/ORACLCS.md) | 1726 | Binary alphabet reduces the LCS to two letter counts | $O(nm)$ per test case |
| 475 | [Lucky Palin](docs/strings/LUCKPAL.md) | 1744 | Placing a block and its mirror, costed in O(1) | $O(|S|)$ per test case for the cost scan, plus $O(|S|)$ per tied placement |
| 485 | [Compare those strings](docs/strings/STRCOMPARE.md) | 1756 | Suffix comparison answered by one backward pass | $O(N)$ per test case |
| 488 | [Flip the Prefix](docs/strings/PREFIXFLIP.md) | 1758 | Sliding window over mandatory boundary flips | $O(N)$ per test case |
| 501 | [Palpal Strings](docs/strings/PALPALS.md) | 1776 | Pair supply must cover all odd-frequency centres | $O(|S|)$ per test case |
| 508 | [Art of Balance](docs/strings/ARTBALAN.md) | 1788 | Enumerate feasible alphabet sizes and retain most occurrences | $O(|S|+26^2)$ per test case |
| 513 | [String Reverse](docs/strings/STR_REVERSE.md) | 1792 | Keep the longest target prefix that is already a subsequence | $O(|S|)$ per test case |
| 516 | [Digit Operation](docs/strings/DIGITOP.md) | 1798 | Length invariance and global digit deficits | $O(\sum |A_i|+\sum |B_i|)$ per test case |
| 546 | [Lavanya Loves DFA](docs/strings/ICM2006.md) | 1586 | Read the accepting suffix from the five-state diagram | $O(|S|)$ per test case to read the input; $O(1)$ to check its suffix |
| 599 | [K-important Strings](docs/strings/N3.md) | 1729 | Pairwise overlaps by KMP, then a shortest walk with exactly K vertices | $O(N^2 L + K N^2)$ per test case |
| 674 | [Valid String](docs/strings/VSTRING.md) | 2194 | Circular gaps between ones - at most one may be too long | $O(N)$ per test case |
| 681 | [String Operations](docs/strings/STROPERS.md) | 2220 | A complete invariant - length, ones, and zeros seen after an odd number of ones | $O(N^2)$ per test case |

</details>

<details open><summary><b>Trees</b> (13)</summary>

| # | Problem | Difficulty | Technique | Time |
|---:|---|---:|---|---|
| 522 | [Wealth Disparity](docs/trees/INOI1601.md) | unrated | Carry the maximum ancestor wealth during iterative DFS | $O(N)$ overall |
| 524 | [Family Tree](docs/trees/FAMTREE.md) | 1720 | Carry the minimum and maximum ancestor wealth during DFS | $O(N)$ overall |
| 527 | [Cosmic Temple](docs/trees/COSTEMP.md) | unrated | Reroot distance sums using subtree sizes | $O(N)$ overall |
| 531 | [Treeversion](docs/trees/TREEVERS.md) | 2453 | Sort child blocks by an exact cross-product comparator | $O(N\log N)$ per test case |
| 544 | [Shortest Path in Binary Trees](docs/trees/BINTREE.md) | 1413 | Repeatedly move the larger heap label to its parent | $O(\log\max(i,j))$ per query |
| 550 | [Rendezvous](docs/trees/TR1.md) | 1638 | Count ordered pairs by their lowest common ancestor | $O(N)$ per test case |
| 551 | [Brush Fire](docs/trees/FIRE.md) | 1761 | Follow one burning branch while shielding its sibling | $O(N)$ per test case |
| 553 | [Robot Game](docs/trees/TR2.md) | 1754 | Merge root-path tries and count supporting maps | $O(\sum N_i+M)$ per test case |
| 614 | [Chef and Subarray Queries](docs/trees/CSUBQ.md) | 2345 | Segment tree counting all-good subarrays, used at two thresholds | $O((N + Q) \log N)$ |
| 621 | [Perfect Tree Problem](docs/trees/PTREE.md) | 2900 | Level widths of perfect subtrees as constant-width segments with arithmetic-geometric sums | $O(N \log N + D \cdot B \log N + Q (\sqrt{N} + D))$ with $D = O(\sqrt{N})$ branching depths and $B$ distinct anchors queried |
| 649 | [Full Path Eraser](docs/trees/FPE.md) | 2094 | Subtree gcds and a DP over where the removed root path continues | $O(N \log A)$ per test case |
| 672 | [Sardar and GCD](docs/trees/DLTNODE.md) | 2190 | Rerooting - subtree gcds below, complement gcds above | $O(N \log A)$ per test case |
| 713 | [A Special Tree](docs/trees/SPTREE.md) | 2350 | Rerooting a "best source minus distance" value in two passes | $O(N + K)$ per test case |

</details>

## Repository layout

```
docs/<topic>/<CODE>.md       write-ups grouped by topic
by-rating/<NNN>-<CODE>.md   the same problems in rating order
solutions/<CODE>.py          runnable Python solutions
data/authored/<CODE>.md      hand written approach + metadata
data/raw/<CODE>.json         problem payloads fetched from CodeChef
data/problem_meta.json       code -> contest, course, level, order
data/roadmap_slots.json      per-course problem slots, for the count audit
data/completed.txt           additional locally completed Python problems
REMAINING.md                 generated list of problems still to implement
tools/                       fetch, build, verify and audit scripts
```

## Regenerating

```bash
python3 tools/fetch_raw.py     # pull problem payloads into data/raw/
python3 tools/build_docs.py    # rebuild docs/ and this README
python3 tools/verify.py        # run every documented solution against its samples
python3 tools/verify_additions.py   # exhaustive and random small-instance oracles
python3 tools/reconcile_counts.py   # audit the roadmap solved count
```

Sample checks establish sample compatibility, not an online-judge acceptance. The additional oracle suite checks selected algorithms against exhaustive small instances.

Both views are generated, so edit `data/authored/<CODE>.md` or `solutions/<CODE>.py` and rebuild rather than editing `docs/` or `by-rating/` directly.
