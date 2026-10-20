# CodeChef - Become 5 Star roadmap

Worked documentation for every problem I have solved on the CodeChef [Become 5 Star](https://www.codechef.com/roadmap/become-5-star) roadmap: the question, its constraints, an explained Python solution, the time and space complexity, and the topic or data structure it belongs to.

**248 of 486 solved problems documented.**

## Roadmap progress

| Level | Course | Solved | Total | Documented |
|---|---|---:|---:|---:|
| 1 | 500 to 1000 difficulty rating | 156 | 156 | 156 |
| 2 | Level up from 1* to 2* | 66 | 66 | 63 |
| 2 | 1400 to 1600 difficulty problems | 85 | 85 | 29 |
| 3 | Jump from 2* to 3* | 96 | 96 | 0 |
| 3 | 1600 to 1800 difficulty problems | 98 | 128 | 0 |
| 4 | Rise from 3* to 4* | 1 | 118 | 0 |
| 5 | 2000 to 2500 difficulty problems | 0 | 112 | 0 |
| | **Total** | **502** | **761** | **248** |

The roadmap counts 502 solved entries across its seven courses; 486 of those are distinct problems (a few appear in two courses) and that is what is documented here.

## Phases

| Phase | Problems | Documented |
|---|---:|---:|
| 1 | 100 | 100 |
| 2 | 100 | 100 |
| 3 | 100 | 48 |
| 4 | 100 | 0 |
| 5 | 86 | 0 |

## Problems by topic

<details open><summary><b>Arrays</b> (27)</summary>

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

</details>

<details open><summary><b>Basic Math</b> (82)</summary>

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

</details>

<details open><summary><b>Big Integers</b> (1)</summary>

| # | Problem | Difficulty | Technique | Time |
|---:|---|---:|---|---|
| 40 | [Small factorials](docs/big-integers/FCTRL2.md) | 420 | Arbitrary-precision arithmetic | $O(n)$ big-integer multiplications per test case |

</details>

<details open><summary><b>Bit Manipulation</b> (2)</summary>

| # | Problem | Difficulty | Technique | Time |
|---:|---|---:|---|---|
| 217 | [Cooking Machine](docs/bit-manipulation/COOKMACH.md) | 1329 | Halving and doubling toward a power of two | $O(\log A \cdot \log B)$ per test case |
| 242 | [Make Array Odd](docs/bit-manipulation/MAKEARRAYODD.md) | 1445 | Tracking a single bit through XOR and OR | $O(N)$ per test case |

</details>

<details open><summary><b>Brute Force</b> (5)</summary>

| # | Problem | Difficulty | Technique | Time |
|---:|---|---:|---|---|
| 56 | [Weights](docs/brute-force/WGHTS.md) | 697 | Enumerating every non-empty subset | $O(2^k)$ per test case with $k = 3$, so $O(1)$ |
| 110 | [Highest Divisor](docs/brute-force/HDIVISR.md) | 860 | Searching a small range downward | $O(1)$ — at most 10 divisibility tests |
| 128 | [Chef and Battery ](docs/brute-force/FIFTYPE.md) | 901 | Searching one variable of a linear Diophantine equation | $O(1)$ per test case — the search is bounded by a small constant |
| 228 | [Maximize Colours](docs/brute-force/COLOUR.md) | 1415 | Enumerating a tiny decision space | $O(1)$ per test case — eight combinations |
| 245 | [Control the Pollution](docs/brute-force/SMOKE.md) | 1450 | Searching one variable over a small range | $O(N/100)$ per test case — at most 11 iterations |

</details>

<details open><summary><b>Combinatorics</b> (5)</summary>

| # | Problem | Difficulty | Technique | Time |
|---:|---|---:|---|---|
| 71 | [Chef Fantasy 11](docs/combinatorics/FIZZBUZZ2303.md) | 739 | Ordered pairs (permutations) | $O(1)$ per test case |
| 122 | [Farmers League](docs/combinatorics/LEAGUE.md) | 883 | Extremal construction in a round robin | $O(1)$ per test case |
| 192 | [Count Substrings](docs/combinatorics/CSUB.md) | 1330 | Counting pairs from a tally | $O(N)$ per test case |
| 237 | [Maximum Angriness](docs/combinatorics/MAXAGRY.md) | 1432 | Maximising inversions with limited swaps | $O(1)$ per test case |
| 244 | [Counting Flags](docs/combinatorics/FLAGS.md) | 1446 | Chromatic polynomials of small graphs | $O(1)$ per test case |

</details>

<details open><summary><b>Conditionals & Case Work</b> (22)</summary>

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

</details>

<details open><summary><b>Constructive</b> (3)</summary>

| # | Problem | Difficulty | Technique | Time |
|---:|---|---:|---|---|
| 232 | [Average Array](docs/constructive/AVGARR.md) | 1424 | Pairing symmetrically around the mean | $O(N)$ per test case |
| 236 | [Balanced and Unique Arrays](docs/constructive/UNQEQ.md) | 1431 | Balanced split with distinct prefixes | $O(N)$ per test case |
| 238 | [Permutation Xority](docs/constructive/PERMXORITY.md) | 1437 | Cancelling a XOR with a 1-2-3 triple | $O(N)$ per test case |

</details>

<details open><summary><b>Game Theory</b> (2)</summary>

| # | Problem | Difficulty | Technique | Time |
|---:|---|---:|---|---|
| 226 | [String Game ](docs/game-theory/STRAME.md) | 1413 | Counting the forced number of moves | $O(N)$ per test case |
| 241 | [Chef and Coins Game](docs/game-theory/CHCOINSG.md) | 1442 | Losing positions form a residue class | $O(1)$ per test case |

</details>

<details open><summary><b>Geometry</b> (4)</summary>

| # | Problem | Difficulty | Technique | Time |
|---:|---|---:|---|---|
| 52 | [Chessboard Distance](docs/geometry/CHESSDIST.md) | 690 | Chebyshev distance | $O(1)$ per test case |
| 69 | [Cyclic Quadrilateral](docs/geometry/CYCLICQD.md) | 735 | Cyclic quadrilateral angle condition | $O(1)$ per test case |
| 108 | [Area OR Perimeter](docs/geometry/AREAPERI.md) | 590 | Comparing area against perimeter | $O(1)$ |
| 247 | [Triangle Classification](docs/geometry/TRIANGCL.md) | 1462 | Classifying with squared lengths | $O(1)$ per test case |

</details>

<details open><summary><b>Greedy</b> (24)</summary>

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

</details>

<details open><summary><b>Number Theory</b> (26)</summary>

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

</details>

<details open><summary><b>Prefix Sums</b> (3)</summary>

| # | Problem | Difficulty | Technique | Time |
|---:|---|---:|---|---|
| 126 | [Inside The Stadium](docs/prefix-sums/INSTDUM.md) | 895 | Running total compared against the index | $O(N)$ per test case |
| 211 | [Gift Shop and Coupon](docs/prefix-sums/GFTSHP.md) | 1364 | Prefix sums with a single discount | $O(N \log N)$ per test case |
| 233 | [Parallel Processing](docs/prefix-sums/PLPROCESS.md) | 1425 | Minimising the heavier side of a split | $O(N)$ per test case |

</details>

<details open><summary><b>Sets</b> (10)</summary>

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

</details>

<details open><summary><b>Simulation</b> (3)</summary>

| # | Problem | Difficulty | Technique | Time |
|---:|---|---:|---|---|
| 178 | [Gasoline Introduction](docs/simulation/BEGGASOL.md) | 1263 | Collecting fuel while moving forward | $O(N)$ per test case |
| 184 | [Cops and the Thief Devu](docs/simulation/COPS.md) | 1242 | Marking covered ranges over a small domain | $O(100 + M)$ per test case |
| 235 | [Full Barrier Alchemist](docs/simulation/PIPSQUIK.md) | 1426 | Walking a sequence with a consumable resource | $O(N)$ per test case |

</details>

<details open><summary><b>Sorting</b> (9)</summary>

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

</details>

<details open><summary><b>Strings</b> (20)</summary>

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
| 216 | [Even Splits](docs/strings/EVENSPLIT.md) | 1282 | Which orderings are reachable | $O(N \log N)$ per test case |
| 234 | [Reversing directions](docs/strings/DIRECTI.md) | 1426 | Parsing and reversing a route | $O(N)$ per test case |
| 240 | [HTML Tags](docs/strings/HTMLTAGS.md) | 1441 | Validating a format | $O(|S|)$ per test case |

</details>

## Repository layout

```
docs/<topic>/<CODE>.md    generated problem write-ups
solutions/<CODE>.py       runnable Python solutions
data/authored/<CODE>.md   hand written approach + metadata
data/raw/<CODE>.json      problem payloads fetched from CodeChef
data/problem_meta.json    code -> contest, course, level, order
tools/                    fetch, build and verify scripts
```

## Regenerating

```bash
python3 tools/fetch_raw.py     # pull problem payloads into data/raw/
python3 tools/build_docs.py    # rebuild docs/ and this README
python3 tools/verify.py        # run every solution against its samples
```

Docs are generated, so edit `data/authored/<CODE>.md` or `solutions/<CODE>.py` and rebuild rather than editing `docs/` directly.
