# Problems in rating order

Every solved problem, ordered by CodeChef difficulty rating and numbered so a plain directory listing follows the same order: `001-<CODE>.md` is the easiest, `486-<CODE>.md` the hardest. One file per problem, each carrying the topic used, the problem and its constraints, the approach, the solution, its edge cases and a dry run.

**486 problems** &middot; ratings 420 upward &middot; **12 with edge cases and a dry run written so far**. Problems CodeChef has not rated carry no place on the ladder, so they sit at the end.

Same write-ups grouped by topic instead: [`../docs`](../docs).

## Bands

| Band | Problems | Written | Most common topic |
|---|---:|---:|---|
| [400&ndash;599](#400599) | 34 | 12 | Basic Math (18) |
| [600&ndash;799](#600799) | 60 | 0 | Basic Math (31) |
| [800&ndash;999](#800999) | 69 | 0 | Basic Math (26) |
| [1000&ndash;1199](#10001199) | 15 | 0 | Strings (5) |
| [1200&ndash;1399](#12001399) | 46 | 0 | Number Theory (7) |
| [1400&ndash;1599](#14001599) | 118 | 0 | Greedy (18) |
| [1600&ndash;1799](#16001799) | 120 | 0 | Greedy (22) |
| [1800&ndash;1999](#18001999) | 10 | 0 | Arrays (2) |
| [2000&ndash;2199](#20002199) | 1 | 0 | Graphs (1) |
| [2200&ndash;2399](#22002399) | 1 | 0 | Heaps (1) |
| [2600&ndash;2799](#26002799) | 1 | 0 | Bit Manipulation (1) |
| [Unrated](#unrated) | 11 | 0 | Sorting (7) |

## 400&ndash;599

| # | Problem | Rating | Topic | Technique | Edge cases + dry run |
|---:|---|---:|---|---|:---:|
| 001 | [Small factorials](001-FCTRL2.md) `FCTRL2` | 420 | Big Integers | Arbitrary-precision arithmetic | &ndash; |
| 002 | [Reverse The Number](002-FLOW007.md) `FLOW007` | 420 | Strings | Digit reversal and leading zeros | &ndash; |
| 003 | [Finding Square Roots](003-FSQRT.md) `FSQRT` | 420 | Basic Math | Exact integer square root | yes |
| 004 | [Greater Average](004-AVGPROBLEM.md) `AVGPROBLEM` | 500 | Basic Math | Integer arithmetic, avoiding floats | yes |
| 005 | [Subscriptions](005-SUBSCRIBE_.md) `SUBSCRIBE_` | 504 | Basic Math | Ceiling division | yes |
| 006 | [Janmansh and Assignments](006-JASSIGNMENTS.md) `JASSIGNMENTS` | 513 | Basic Math | Conditional arithmetic | yes |
| 007 | [Exams](007-EXAMCHEF.md) `EXAMCHEF` | 519 | Basic Math | Percentage comparison without division | yes |
| 008 | [Chef And Operators](008-CHOPRT.md) `CHOPRT` | 520 | Conditionals & Case Work | Three-way comparison | yes |
| 009 | [Decrement OR Increment](009-DECINC.md) `DECINC` | 520 | Conditionals & Case Work | Single divisibility branch | yes |
| 010 | [Second Largest](010-FLOW017.md) `FLOW017` | 520 | Sorting | Median of three | yes |
| 011 | [HOW MANY DIGITS DO I HAVE](011-HOWMANY.md) `HOWMANY` | 520 | Basic Math | Counting digits | &ndash; |
| 012 | [Is it a VOWEL or CONSONANT](012-VOWELTB.md) `VOWELTB` | 520 | Strings | Membership test against a small set | yes |
| 013 | [Chef in his Office](013-OFFICE.md) `OFFICE` | 532 | Basic Math | Direct formula | yes |
| 014 | [CRED Coins](014-CREDCOINS.md) `CREDCOINS` | 539 | Basic Math | Floor division | yes |
| 015 | [Sale Season](015-SALESEASON.md) `SALESEASON` | 541 | Conditionals & Case Work | Ordered threshold ladder | yes |
| 016 | [Water Filling](016-WATERFILLING.md) `WATERFILLING` | 541 | Conditionals & Case Work | Counting flags instead of enumerating cases | &ndash; |
| 017 | [Minimum Pizzas](017-MINPIZZA.md) `MINPIZZA` | 546 | Basic Math | Ceiling division | &ndash; |
| 018 | [Chefland Games](018-CHEFGAMES.md) `CHEFGAMES` | 550 | Conditionals & Case Work | Reducing an AND over flags to a sum | &ndash; |
| 019 | [Expert Setter](019-EXPERT.md) `EXPERT` | 561 | Basic Math | Percentage comparison without division | &ndash; |
| 020 | [Chef and NextGen](020-HELIUM3.md) `HELIUM3` | 562 | Basic Math | Comparing two products | &ndash; |
| 021 | [Count the Notebooks](021-NOTEBOOK.md) `NOTEBOOK` | 563 | Basic Math | Chaining unit conversions | &ndash; |
| 022 | [Sugarcane Juice Business](022-SUGARCANE.md) `SUGARCANE` | 563 | Basic Math | Percentages that cancel | &ndash; |
| 023 | [Chef and Candies](023-CHEFCAND.md) `CHEFCAND` | 570 | Basic Math | Clamping before a ceiling division | &ndash; |
| 024 | [Car or Bike](024-TRAVELFAST.md) `TRAVELFAST` | 571 | Conditionals & Case Work | Three-way comparison | &ndash; |
| 025 | [Is the Score Consistent](025-TRUESCORE.md) `TRUESCORE` | 572 | Conditionals & Case Work | Monotonic quantities | &ndash; |
| 026 | [The Three Topics](026-THREETOPICS.md) `THREETOPICS` | 573 | Conditionals & Case Work | Membership test | &ndash; |
| 027 | [Monopoly](027-MONOPOLY2.md) `MONOPOLY2` | 578 | Basic Math | Maximum against the sum of the rest | &ndash; |
| 028 | [Problems in your to-do list](028-TODOLIST.md) `TODOLIST` | 580 | Arrays | Counting with a predicate | &ndash; |
| 029 | [Air Conditioner Temperature](029-ACTEMP.md) `ACTEMP` | 584 | Conditionals & Case Work | Intersecting interval constraints | &ndash; |
| 030 | [Nearest Exit](030-NEARESTEXIT.md) `NEARESTEXIT` | 585 | Basic Math | Comparing distances to two endpoints | &ndash; |
| 031 | [Area OR Perimeter](031-AREAPERI.md) `AREAPERI` | 590 | Geometry | Comparing area against perimeter | &ndash; |
| 032 | [Sasta Shark Tank](032-SST.md) `SST` | 592 | Basic Math | Recovering a whole from a percentage | &ndash; |
| 033 | [Good Program](033-NIBBLE.md) `NIBBLE` | 593 | Number Theory | Divisibility test | &ndash; |
| 034 | [Qualify the round](034-QUALIFY.md) `QUALIFY` | 594 | Basic Math | Weighted sum against a threshold | &ndash; |

## 600&ndash;799

| # | Problem | Rating | Topic | Technique | Edge cases + dry run |
|---:|---|---:|---|---|:---:|
| 035 | [Elections in Chefland](035-ELECTN.md) `ELECTN` | 604 | Arrays | Counting with a predicate | &ndash; |
| 036 | [Minimum Cars required](036-MINCARS.md) `MINCARS` | 608 | Basic Math | Ceiling division | &ndash; |
| 037 | [Test Score](037-CHEFSCORE.md) `CHEFSCORE` | 610 | Number Theory | Divisibility with an upper bound | &ndash; |
| 038 | [Jenga Night](038-JENGA.md) `JENGA` | 613 | Number Theory | Divisibility as an exact-fit condition | &ndash; |
| 039 | [Bus  Seat Numbering](039-SEATNUMBER.md) `SEATNUMBER` | 613 | Conditionals & Case Work | Decomposing an index into deck and position | &ndash; |
| 040 | [Discus Throw](040-DISCUS.md) `DISCUS` | 622 | Basic Math | Maximum of a fixed set | &ndash; |
| 041 | [Maximise the Tastiness](041-MAXTASTE.md) `MAXTASTE` | 627 | Greedy | Independent choices optimised separately | &ndash; |
| 042 | [Watching Movies at 2x](042-MOVIE2X.md) `MOVIE2X` | 628 | Basic Math | Rate and time | &ndash; |
| 043 | [Police and Thief](043-POLTHIEF.md) `POLTHIEF` | 639 | Basic Math | Relative speed | &ndash; |
| 044 | [Flip the cards](044-FLIPCARDS.md) `FLIPCARDS` | 641 | Basic Math | Choosing the cheaper of two targets | &ndash; |
| 045 | [Bath in Winters](045-BATH.md) `BATH` | 643 | Basic Math | Floor division by a composite unit | &ndash; |
| 046 | [Finding Shoes](046-FINDSHOES.md) `FINDSHOES` | 646 | Basic Math | Clamping one side of a two-part requirement | &ndash; |
| 047 | [Mario and Transformation](047-TRANSFORM.md) `TRANSFORM` | 649 | Number Theory | Cyclic state via modulo | &ndash; |
| 048 | [Mario and Bullet](048-BULLET.md) `BULLET` | 650 | Basic Math | Working backwards from a deadline | &ndash; |
| 049 | [Chess Ratings](049-C_RATING.md) `C_RATING` | 651 | Basic Math | Ceiling division with a clamp | &ndash; |
| 050 | [Complementary Strand in a DNA](050-DNASTRAND.md) `DNASTRAND` | 660 | Strings | Character-wise mapping with a translation table | &ndash; |
| 051 | [Chef and Water Bottles](051-CHEFBOTTLE.md) `CHEFBOTTLE` | 662 | Basic Math | Two competing limits | &ndash; |
| 052 | [Candy Distribution](052-CANDYDIST.md) `CANDYDIST` | 668 | Number Theory | Divisibility by a composite modulus | &ndash; |
| 053 | [The Last Levels](053-LASTLEVELS.md) `LASTLEVELS` | 679 | Basic Math | Counting separators, not groups | &ndash; |
| 054 | [Blackjack](054-BLACKJACK.md) `BLACKJACK` | 681 | Basic Math | Solving for the unknown, then range checking | &ndash; |
| 055 | [Fill Candies](055-FILLCANDIES.md) `FILLCANDIES` | 681 | Basic Math | Ceiling division by a composite capacity | &ndash; |
| 056 | [X Jumps](056-XJUMP.md) `XJUMP` | 686 | Greedy | Prefer the large step, then settle the remainder | &ndash; |
| 057 | [Chessboard Distance](057-CHESSDIST.md) `CHESSDIST` | 690 | Geometry | Chebyshev distance | &ndash; |
| 058 | [It is My Serve](058-MYSERVE.md) `MYSERVE` | 691 | Number Theory | Block index parity via modulo | &ndash; |
| 059 | [Valentine is Coming](059-VALENTINE.md) `VALENTINE` | 691 | Basic Math | Floor division | &ndash; |
| 060 | [Water Mixing](060-WTRMIXING.md) `WTRMIXING` | 694 | Conditionals & Case Work | Signed difference against one-sided supplies | &ndash; |
| 061 | [Weights](061-WGHTS.md) `WGHTS` | 697 | Brute Force | Enumerating every non-empty subset | &ndash; |
| 062 | [Small Factorial](062-FLOW018.md) `FLOW018` | 700 | Basic Math | Factorials within fixed-width limits | &ndash; |
| 063 | [Chef and his Apps](063-CHEFAPPS.md) `CHEFAPPS` | 702 | Greedy | Remove the largest item first | &ndash; |
| 064 | [Chef Eren](064-CHEFEREN.md) `CHEFEREN` | 706 | Basic Math | Counting odd and even positions | &ndash; |
| 065 | [Minimum number of coins](065-MINCOINS.md) `MINCOINS` | 711 | Greedy | Largest denomination first | &ndash; |
| 066 | [Airlines](066-SPCP2.md) `SPCP2` | 712 | Basic Math | Ceiling division with a clamp | &ndash; |
| 067 | [Cup Finals](067-CRICUP.md) `CRICUP` | 716 | Basic Math | Absolute difference against a tolerance | &ndash; |
| 068 | [Self Defence Training](068-SELFDEF.md) `SELFDEF` | 716 | Arrays | Counting values inside a closed range | &ndash; |
| 069 | [Too many Floors](069-FLOORS.md) `FLOORS` | 717 | Basic Math | Mapping an index to its block | &ndash; |
| 070 | [Speed Limit Test](070-SPEEDTEST.md) `SPEEDTEST` | 718 | Basic Math | Comparing ratios by cross-multiplication | &ndash; |
| 071 | [Mahasena](071-AMR15A.md) `AMR15A` | 720 | Arrays | Parity counting in a single pass | &ndash; |
| 072 | [The Block Game](072-PALL01.md) `PALL01` | 720 | Strings | Palindrome check by reversal | &ndash; |
| 073 | [A or B](073-AORB.md) `AORB` | 728 | Greedy | Scheduling order and the exchange argument | &ndash; |
| 074 | [Pass or Fail](074-PASSORFAIL.md) `PASSORFAIL` | 730 | Basic Math | Scoring with a penalty | &ndash; |
| 075 | [Cyclic Quadrilateral](075-CYCLICQD.md) `CYCLICQD` | 735 | Geometry | Cyclic quadrilateral angle condition | &ndash; |
| 076 | [Too many items](076-POLYBAGS.md) `POLYBAGS` | 738 | Basic Math | Ceiling division | &ndash; |
| 077 | [Building Race](077-BUILDINGRACE.md) `BUILDINGRACE` | 739 | Basic Math | Comparing ratios by cross-multiplication | &ndash; |
| 078 | [Chef Fantasy 11](078-FIZZBUZZ2303.md) `FIZZBUZZ2303` | 739 | Combinatorics | Ordered pairs (permutations) | &ndash; |
| 079 | [Chef and Races](079-CHEFRACES.md) `CHEFRACES` | 745 | Sets | Set difference | &ndash; |
| 080 | [Smallest Numbers of Notes](080-FLOW005.md) `FLOW005` | 750 | Greedy | Greedy change-making in a canonical system | &ndash; |
| 081 | [Endless Appetizers](081-MOZZ.md) `MOZZ` | 752 | Basic Math | Inverting a reward, then a ceiling division | &ndash; |
| 082 | [Presents for Cheffina](082-PRESENTS.md) `PRESENTS` | 757 | Basic Math | Counting free items in a repeating group | &ndash; |
| 083 | [Dracula Eats](083-CHEAT.md) `CHEAT` | 763 | Number Theory | Counting residues in a range | &ndash; |
| 084 | [Possible Victory](084-T20MCH.md) `T20MCH` | 769 | Basic Math | Best-case bound | &ndash; |
| 085 | [Lucky Four](085-LUCKFOUR.md) `LUCKFOUR` | 775 | Strings | Counting a digit | &ndash; |
| 086 | [Reach fast](086-REACHFAST.md) `REACHFAST` | 777 | Basic Math | Ceiling division over a distance | &ndash; |
| 087 | [Single-use Attack](087-SINGLEUSE.md) `SINGLEUSE` | 777 | Greedy | Comparing both strategies explicitly | &ndash; |
| 088 | [Get Lowest Free](088-SALE.md) `SALE` | 778 | Basic Math | Total minus the extremum | &ndash; |
| 089 | [Minimum number of Flips](089-MINFLIPS.md) `MINFLIPS` | 781 | Arrays | Feasibility by parity, then distance to the target count | &ndash; |
| 090 | [Binary Battles](090-BIN_BAT.md) `BIN_BAT` | 786 | Basic Math | Tournament rounds, and separators between them | &ndash; |
| 091 | [Best of Two](091-DICEGAME2.md) `DICEGAME2` | 789 | Basic Math | Total minus the extremum, then compare | &ndash; |
| 092 | [Degree of Polynomial](092-DPOLY.md) `DPOLY` | 793 | Arrays | Last index satisfying a predicate | &ndash; |
| 093 | [Recent contest problems](093-RECENTCONT.md) `RECENTCONT` | 793 | Arrays | Counting two categories in one pass | &ndash; |
| 094 | [The Cooler Dilemma 2](094-WATERCOOLER2.md) `WATERCOOLER2` | 798 | Basic Math | Strict inequality turned into a floor | &ndash; |

## 800&ndash;999

| # | Problem | Rating | Topic | Technique | Edge cases + dry run |
|---:|---|---:|---|---|:---:|
| 095 | [Wordle](095-WORDLE.md) `WORDLE` | 804 | Strings | Position-wise comparison | &ndash; |
| 096 | [Cars and Bikes](096-TYRES.md) `TYRES` | 809 | Number Theory | Remainder modulo 4 | &ndash; |
| 097 | [Buy 2 Get 1 Free](097-SALE2.md) `SALE2` | 821 | Basic Math | Counting free items in a repeating group | &ndash; |
| 098 | [Equalizing Numbers](098-EQLZING.md) `EQLZING` | 823 | Number Theory | Finding the invariant | &ndash; |
| 099 | [The Preparations](099-SUPCHEF.md) `SUPCHEF` | 823 | Basic Math | Strict comparison against a deadline | &ndash; |
| 100 | [Genes](100-GENE01.md) `GENE01` | 826 | Conditionals & Case Work | Ranking by priority | &ndash; |
| 101 | [Best of N Sets](101-BESTOFTENNIS.md) `BESTOFTENNIS` | 830 | Basic Math | Inverting a stopping condition | &ndash; |
| 102 | [Mileage matters](102-MILEAGE.md) `MILEAGE` | 831 | Basic Math | Comparing ratios by cross-multiplication | &ndash; |
| 103 | [Melt Gold](103-MELTGOLD.md) `MELTGOLD` | 835 | Basic Math | Triangular numbers and their inverse | &ndash; |
| 104 | [Circular Track](104-LOOP.md) `LOOP` | 838 | Basic Math | Distance on a circle | &ndash; |
| 105 | [Primality Test](105-PRB01.md) `PRB01` | 850 | Number Theory | Trial division to the square root | &ndash; |
| 106 | [Summer Heat](106-COCONUT.md) `COCONUT` | 852 | Basic Math | Independent requirements summed | &ndash; |
| 107 | [Equal Integers](107-INCREAR.md) `INCREAR` | 852 | Basic Math | Asymmetric step sizes | &ndash; |
| 108 | [Devendra and Water Sports](108-DEVSPORTS.md) `DEVSPORTS` | 859 | Basic Math | Remaining budget against a total cost | &ndash; |
| 109 | [Construct N](109-CONN.md) `CONN` | 860 | Number Theory | Parity plus a threshold | &ndash; |
| 110 | [Highest Divisor](110-HDIVISR.md) `HDIVISR` | 860 | Brute Force | Searching a small range downward | &ndash; |
| 111 | [Problem Category](111-PROBCAT.md) `PROBCAT` | 860 | Conditionals & Case Work | Ordered threshold ladder | &ndash; |
| 112 | [Car Choice](112-CARCHOICE.md) `CARCHOICE` | 861 | Basic Math | Comparing ratios by cross-multiplication | &ndash; |
| 113 | [Which Division](113-WHICHDIV.md) `WHICHDIV` | 867 | Conditionals & Case Work | Ordered threshold ladder | &ndash; |
| 114 | [Badminton Serves](114-BADMINTON.md) `BADMINTON` | 869 | Basic Math | Counting even values in a range | &ndash; |
| 115 | [Chef and Contest](115-CHEFCONTEST.md) `CHEFCONTEST` | 872 | Basic Math | Weighted penalty, then a three-way comparison | &ndash; |
| 116 | [Group Assignment](116-GROUPASSGN.md) `GROUPASSGN` | 872 | Basic Math | Pairing by reflection | &ndash; |
| 117 | [Relativity](117-RELATIVE.md) `RELATIVE` | 872 | Basic Math | Rearranging a given formula | &ndash; |
| 118 | [Counting Pretty Numbers](118-NUM239.md) `NUM239` | 873 | Number Theory | Counting residues with a prefix function | &ndash; |
| 119 | [Drunk Alcoholic](119-DRUNKALK.md) `DRUNKALK` | 874 | Basic Math | Net progress per cycle, with an odd remainder | &ndash; |
| 120 | [Chef On Island](120-CCISLAND.md) `CCISLAND` | 878 | Basic Math | Two independent supply checks | &ndash; |
| 121 | [Richie Rich](121-CHFRICH.md) `CHFRICH` | 878 | Basic Math | Exact division from a guaranteed divisor | &ndash; |
| 122 | [Find the Direction](122-FACEDIR.md) `FACEDIR` | 880 | Number Theory | Cyclic state via modulo | &ndash; |
| 123 | [Farmers League](123-LEAGUE.md) `LEAGUE` | 883 | Combinatorics | Extremal construction in a round robin | &ndash; |
| 124 | [Utkarsh and Placement tests](124-UTKPLC.md) `UTKPLC` | 886 | Conditionals & Case Work | Ranking by a given priority order | &ndash; |
| 125 | [Secret Recipe](125-CHEFRUN.md) `CHEFRUN` | 888 | Basic Math | Comparing ratios by cross-multiplication | &ndash; |
| 126 | [Chef and Profits](126-CHFPROFIT.md) `CHFPROFIT` | 889 | Basic Math | Factoring a repeated difference | &ndash; |
| 127 | [Inside The Stadium](127-INSTDUM.md) `INSTDUM` | 895 | Prefix Sums | Running total compared against the index | &ndash; |
| 128 | [Peaceful Party](128-MAYOR_PARTY.md) `MAYOR_PARTY` | 898 | Greedy | Choosing between mutually exclusive groups | &ndash; |
| 129 | [Grade The Steel](129-FLOW014.md) `FLOW014` | 900 | Conditionals & Case Work | Grading from a set of independent flags | &ndash; |
| 130 | [Chef and Battery ](130-FIFTYPE.md) `FIFTYPE` | 901 | Brute Force | Searching one variable of a linear Diophantine equation | &ndash; |
| 131 | [Passing Marks](131-PSGRADE.md) `PSGRADE` | 904 | Conditionals & Case Work | Conjunction of per-subject and aggregate thresholds | &ndash; |
| 132 | [Avoid Contact](132-AVOIDCONTACT.md) `AVOIDCONTACT` | 907 | Greedy | Packing with separation constraints | &ndash; |
| 133 | [Count the Holidays](133-SUNDAY.md) `SUNDAY` | 907 | Sets | Union of a fixed set with input values | &ndash; |
| 134 | [Problem](134-PR0BLEM.md) `PR0BLEM` | 908 | Number Theory | Parity invariant | &ndash; |
| 135 | [Two Ranges](135-TWORANGES.md) `TWORANGES` | 918 | Sets | Inclusion-exclusion on intervals | &ndash; |
| 136 | [Chef and IPC Certificates](136-IPCCERT.md) `IPCCERT` | 922 | Arrays | Filtering rows on two independent criteria | &ndash; |
| 137 | [Penalty Shots](137-PENALTY.md) `PENALTY` | 925 | Arrays | Summing alternate positions | &ndash; |
| 138 | [Shoe Fit](138-SHOEFIT.md) `SHOEFIT` | 925 | Conditionals & Case Work | Presence of both values in a small collection | &ndash; |
| 139 | [Make all equal using Pairs](139-PAIREQ.md) `PAIREQ` | 928 | Arrays | Keep the most frequent value | &ndash; |
| 140 | [Chef and Pairing Slippers](140-CHEFSLP.md) `CHEFSLP` | 930 | Basic Math | Pairing limited by the scarcer side | &ndash; |
| 141 | [Hoop Jump](141-HOOPS.md) `HOOPS` | 930 | Basic Math | Where two converging sequences meet | &ndash; |
| 142 | [Akash and Missing Class](142-CHFCLASS.md) `CHFCLASS` | 931 | Number Theory | Counting residues in a range | &ndash; |
| 143 | [Chef and Price Control](143-PRICECON.md) `PRICECON` | 931 | Arrays | Summing a clamped excess | &ndash; |
| 144 | [First and Last](144-FIRSTANDLAST.md) `FIRSTANDLAST` | 932 | Arrays | Cyclically adjacent pairs | &ndash; |
| 145 | [No Time to Wait](145-NOTIME.md) `NOTIME` | 932 | Arrays | Existence check over a list | &ndash; |
| 146 | [World Chess Championship](146-WCC.md) `WCC` | 935 | Strings | Counting characters, then a three-way branch | &ndash; |
| 147 | [Two vs Ten](147-TWOVSTEN.md) `TWOVSTEN` | 936 | Number Theory | Which prime factors an operation can supply | &ndash; |
| 148 | [Car Range](148-CARRANGE.md) `CARRANGE` | 938 | Basic Math | Reading an off-by-one from the statement | &ndash; |
| 149 | [Vaccine Dates ](149-VDATES.md) `VDATES` | 938 | Conditionals & Case Work | Classifying a value against an interval | &ndash; |
| 150 | [ Am I Lucky!](150-SPCP4.md) `SPCP4` | 941 | Basic Math | Remainders paired off | &ndash; |
| 151 | [Janmansh at Fruit Market](151-JMARKET.md) `JMARKET` | 947 | Greedy | Cheapest choice under a diversity constraint | &ndash; |
| 152 | [Non-Negative Product](152-NONNEGPROD.md) `NONNEGPROD` | 948 | Arrays | Sign of a product from the count of negatives | &ndash; |
| 153 | [Rearranging digits to get a multiple of 5](153-DIGARR.md) `DIGARR` | 949 | Strings | Divisibility decided by one digit | &ndash; |
| 154 | [Kitchen Timetable](154-KTTABLE.md) `KTTABLE` | 950 | Arrays | Consecutive differences as a window | &ndash; |
| 155 | [Marathon](155-MARARUN.md) `MARARUN` | 955 | Conditionals & Case Work | Largest achievable tier | &ndash; |
| 156 | [La Liga](156-COOK82A.md) `COOK82A` | 956 | Conditionals & Case Work | Parsing labelled input, then a single logical condition | &ndash; |
| 157 | [Chef and Cook-Off](157-CCOOK.md) `CCOOK` | 961 | Arrays | Sum of flags mapped to a label | &ndash; |
| 158 | [Chef and Spells](158-CHFSPL.md) `CHFSPL` | 965 | Basic Math | Total minus the extremum | &ndash; |
| 159 | [Mutated Minions](159-CHN15A.md) `CHN15A` | 970 | Number Theory | Divisibility after a uniform shift | &ndash; |
| 160 | [Joining Date](160-JOINING.md) `JOINING` | 970 | Number Theory | Counting residues in a range | &ndash; |
| 161 | [Playing with Matches](161-MATCHES.md) `MATCHES` | 986 | Basic Math | Per-digit lookup table | &ndash; |
| 162 | [Keplers Law](162-KEPLERSLAW.md) `KEPLERSLAW` | 992 | Basic Math | Testing proportionality by cross-multiplication | &ndash; |
| 163 | [Bear and Ladder](163-BRLADDER.md) `BRLADDER` | 999 | Conditionals & Case Work | Deriving an adjacency rule from an edge list | &ndash; |

## 1000&ndash;1199

| # | Problem | Rating | Topic | Technique | Edge cases + dry run |
|---:|---|---:|---|---|:---:|
| 164 | [Programming Languages](164-PROGLANG.md) `PROGLANG` | 1001 | Sets | Subset containment | &ndash; |
| 165 | [Chef in Vaccination Queue](165-VACCINQ.md) `VACCINQ` | 1016 | Arrays | Prefix sum with a per-element lookup | &ndash; |
| 166 | [Weight Balance](166-WEIGHTBL.md) `WEIGHTBL` | 1045 | Basic Math | Reachable range over repeated choices | &ndash; |
| 167 | [Devu and friendship testing](167-CFRTEST.md) `CFRTEST` | 1061 | Sets | Distinct values as a capacity bound | &ndash; |
| 168 | [Chef and Stock Prices ](168-CSTOCK.md) `CSTOCK` | 1069 | Basic Math | Percentage change without floating point | &ndash; |
| 169 | [Motivation](169-IMDB.md) `IMDB` | 1098 | Arrays | Maximum over a filtered subset | &ndash; |
| 170 | [Studying Alphabet](170-ALPHABET.md) `ALPHABET` | 1123 | Sets | Subset containment | &ndash; |
| 171 | [Two Dishes](171-TWODISH.md) `TWODISH` | 1140 | Greedy | Bottleneck across shared and exclusive resources | &ndash; |
| 172 | [Attendance](172-ATTND.md) `ATTND` | 1148 | Strings | Frequency of a key field | &ndash; |
| 173 | [Lapindromes](173-LAPIN.md) `LAPIN` | 1159 | Strings | Comparing character frequencies | &ndash; |
| 174 | [Lazy Salesman](174-HOLIDAYS.md) `HOLIDAYS` | 1161 | Greedy | Take the largest items first | &ndash; |
| 175 | [Play Piano](175-PLAYPIAN.md) `PLAYPIAN` | 1180 | Strings | Validating fixed-size blocks | &ndash; |
| 176 | [Pawri Meme](176-PAWRI.md) `PAWRI` | 1182 | Strings | Substring replacement | &ndash; |
| 177 | [The Lead Game](177-TLG.md) `TLG` | 1190 | Arrays | Running totals with a tracked maximum | &ndash; |
| 178 | [Chef and Feedback](178-ERROR.md) `ERROR` | 1199 | Strings | Substring search | &ndash; |

## 1200&ndash;1399

| # | Problem | Rating | Topic | Technique | Edge cases + dry run |
|---:|---|---:|---|---|:---:|
| 179 | [Chef and Linear Chess](179-LINCHESS.md) `LINCHESS` | 1200 | Number Theory | Divisors as reachable positions | &ndash; |
| 180 | [ICPC Balloons](180-BALLOON.md) `BALLOON` | 1205 | Sets | Smallest prefix covering a required set | &ndash; |
| 181 | [Watson asks Does Permutation Exist](181-PERMEXIS.md) `PERMEXIS` | 1207 | Sorting | Adjacent gaps in sorted order | &ndash; |
| 182 | [A Subtask Problem](182-SUBTASK.md) `SUBTASK` | 1217 | Arrays | Ordered condition checks | &ndash; |
| 183 | [Version Control System](183-VCS.md) `VCS` | 1217 | Sets | Intersection and complement of a union | &ndash; |
| 184 | [Maximum Length Even Subarray](184-MXEVNSUB.md) `MXEVNSUB` | 1221 | Number Theory | Parity of a triangular number | &ndash; |
| 185 | [Simple Statistics](185-SIMPSTAT.md) `SIMPSTAT` | 1222 | Sorting | Trimmed mean | &ndash; |
| 186 | [Racing Horses](186-HORSES.md) `HORSES` | 1231 | Sorting | Minimum adjacent difference after sorting | &ndash; |
| 187 | [Cops and the Thief Devu](187-COPS.md) `COPS` | 1242 | Simulation | Marking covered ranges over a small domain | &ndash; |
| 188 | [The Two Dishes](188-MAX_DIFF.md) `MAX_DIFF` | 1254 | Greedy | Pushing one variable to its bound | &ndash; |
| 189 | [Chef and the Wildcard Matching](189-TWOSTR.md) `TWOSTR` | 1254 | Strings | Wildcard matching, position by position | &ndash; |
| 190 | [Hiring Test](190-HIRETEST.md) `HIRETEST` | 1260 | Strings | Counting characters, then a two-branch rule | &ndash; |
| 191 | [Sticks](191-STICKS.md) `STICKS` | 1261 | Greedy | Largest two pairs by frequency | &ndash; |
| 192 | [Gasoline Introduction](192-BEGGASOL.md) `BEGGASOL` | 1263 | Simulation | Collecting fuel while moving forward | &ndash; |
| 193 | [Carvans](193-CARVANS.md) `CARVANS` | 1264 | Arrays | Running minimum over a prefix | &ndash; |
| 194 | [Pushpa ](194-PUSH7PA.md) `PUSH7PA` | 1266 | Arrays | Frequency combined with value | &ndash; |
| 195 | [Make them equal](195-MAKEEQUAL.md) `MAKEEQUAL` | 1267 | Greedy | Bounded by the widest gap | &ndash; |
| 196 | [Equinox Strings](196-EQUINOX.md) `EQUINOX` | 1272 | Strings | First-character membership test | &ndash; |
| 197 | [Even Splits](197-EVENSPLIT.md) `EVENSPLIT` | 1282 | Strings | Which orderings are reachable | &ndash; |
| 198 | [Reversal Sorting](198-REVSORT.md) `REVSORT` | 1288 | Arrays | Constraining which inversions may be undone | &ndash; |
| 199 | [Snake Procession](199-SNAKPROC.md) `SNAKPROC` | 1290 | Strings | Single-pass state machine | &ndash; |
| 200 | [Points and Lines](200-POLIN.md) `POLIN` | 1296 | Sets | Counting distinct coordinates independently | &ndash; |
| 201 | [Digit Longest Increasing Subsequences 2](201-LISDIGIT.md) `LISDIGIT` | 1297 | Constructive | Using the LIS value itself as the digit | &ndash; |
| 202 | [Hard Cash](202-CASH.md) `CASH` | 1300 | Number Theory | A conserved total modulo K | &ndash; |
| 203 | [Sudhanva and Books](203-SUDBOOKS.md) `SUDBOOKS` | 1300 | Simulation | A stack, with an empty-pop guard | &ndash; |
| 204 | [Smallest Possible Whole Number](204-SMOL.md) `SMOL` | 1306 | Number Theory | Modulo, with a zero-divisor guard | &ndash; |
| 205 | [Maximum Weight Difference](205-MAXDIFF.md) `MAXDIFF` | 1308 | Sorting | Taking an extreme K-subset | &ndash; |
| 206 | [Maximise the Subsequence Sum](206-SIGNFLIP.md) `SIGNFLIP` | 1308 | Greedy | Flip the largest magnitudes first | &ndash; |
| 207 | [Chopsticks](207-TACHSTCK.md) `TACHSTCK` | 1320 | Greedy | Pairing adjacent elements after sorting | &ndash; |
| 208 | [Arranging Cup-cakes](208-RESQ.md) `RESQ` | 1322 | Number Theory | Divisor nearest the square root | &ndash; |
| 209 | [Chef and Keyboard](209-CHEFKEY.md) `CHEFKEY` | 1323 | Number Theory | Divisor pairs under a box constraint | &ndash; |
| 210 | [Cooking Machine](210-COOKMACH.md) `COOKMACH` | 1329 | Bit Manipulation | Halving and doubling toward a power of two | &ndash; |
| 211 | [Indivisible Permutation](211-INDIPERM.md) `INDIPERM` | 1329 | Constructive | A single cyclic shift | &ndash; |
| 212 | [Count Substrings](212-CSUB.md) `CSUB` | 1330 | Combinatorics | Counting pairs from a tally | &ndash; |
| 213 | [Maximum Trio](213-MXMTRIO.md) `MXMTRIO` | 1349 | Sorting | Choosing extremes for a product | &ndash; |
| 214 | [Turn It](214-NFS.md) `NFS` | 1350 | Basic Math | Rearranging a kinematic inequality | &ndash; |
| 215 | [The Smallest Pair](215-SMPAIR.md) `SMPAIR` | 1352 | Sorting | The two smallest elements | &ndash; |
| 216 | [Magical Doors](216-MAGDOORS.md) `MAGDOORS` | 1355 | Greedy | Tracking a global flip as parity | &ndash; |
| 217 | [Appy and Contest](217-HMAPPY2.md) `HMAPPY2` | 1358 | Number Theory | Counting multiples with inclusion-exclusion | &ndash; |
| 218 | [Maximize the Minimum](218-MAXTHEMIN.md) `MAXTHEMIN` | 1358 | Sorting | The (K+1)-th smallest survives | &ndash; |
| 219 | [Gift Shop and Coupon](219-GFTSHP.md) `GFTSHP` | 1364 | Prefix Sums | Prefix sums with a single discount | &ndash; |
| 220 | [Chocolate Monger](220-CM164364.md) `CM164364` | 1369 | Sets | Distinct count capped by a budget | &ndash; |
| 221 | [Nobel Prize](221-NOBEL.md) `NOBEL` | 1372 | Sets | Counting distinct values against a capacity | &ndash; |
| 222 | [Make it Divisible](222-MAKEDIV3.md) `MAKEDIV3` | 1379 | Constructive | Fixing the digit sum, then the last digit | &ndash; |
| 223 | [Tom And Jerry 1](223-TANDJ1.md) `TANDJ1` | 1379 | Basic Math | Grid reachability by distance and parity | &ndash; |
| 224 | [Daanish and Problems](224-DIV03.md) `DIV03` | 1388 | Greedy | Spending a budget from the top down | &ndash; |

## 1400&ndash;1599

| # | Problem | Rating | Topic | Technique | Edge cases + dry run |
|---:|---|---:|---|---|:---:|
| 225 | [Chef and Chefina](225-CHFNA.md) `CHFNA` | 1400 | Bit Manipulation | Independent bits give a closed form | &ndash; |
| 226 | [Average Permutation](226-AVGPERM.md) `AVGPERM` | 1401 | Greedy | Pair large values with small weights | &ndash; |
| 227 | [Hotel Bytelandia](227-HOTEL.md) `HOTEL` | 1405 | Sorting | Event sweep | &ndash; |
| 228 | [Mighty Friend](228-MTYFRI.md) `MTYFRI` | 1406 | Greedy | Exchange the largest for the smallest | &ndash; |
| 229 | [Array Halves](229-ARRHALVES.md) `ARRHALVES` | 1407 | Arrays | Minimum adjacent swaps to gather a set | &ndash; |
| 230 | [Bella ciao](230-CHFHEIST.md) `CHFHEIST` | 1410 | Basic Math | Summing an arithmetic progression | &ndash; |
| 231 | [Guessing Game](231-GUESS.md) `GUESS` | 1410 | Basic Math | Counting by parity, reduced to lowest terms | &ndash; |
| 232 | [Plusle and Minun on Array](232-PMA.md) `PMA` | 1412 | Greedy | Best single swap | &ndash; |
| 233 | [String Game ](233-STRAME.md) `STRAME` | 1413 | Game Theory | Counting the forced number of moves | &ndash; |
| 234 | [Maximize Colours](234-COLOUR.md) `COLOUR` | 1415 | Brute Force | Enumerating a tiny decision space | &ndash; |
| 235 | [Remove Element](235-REMELEM.md) `REMELEM` | 1415 | Greedy | The smallest element as universal partner | &ndash; |
| 236 | [Equality](236-EQUALITY.md) `EQUALITY` | 1419 | Basic Math | Solving a symmetric linear system by summing | &ndash; |
| 237 | [Mix the Colors](237-MIXCOLOR.md) `MIXCOLOR` | 1419 | Arrays | Counting duplicates | &ndash; |
| 238 | [Fit to Play](238-PLAYFIT.md) `PLAYFIT` | 1419 | Arrays | Best gain against a running minimum | &ndash; |
| 239 | [Decreasing Srrnmieeda](239-DECREM.md) `DECREM` | 1423 | Number Theory | A strictly decreasing chain of remainders | &ndash; |
| 240 | [Average Array](240-AVGARR.md) `AVGARR` | 1424 | Constructive | Pairing symmetrically around the mean | &ndash; |
| 241 | [Say No To Drugs](241-NODRUGS.md) `NODRUGS` | 1425 | Conditionals & Case Work | Monotone objective, so only an endpoint dose matters | &ndash; |
| 242 | [Parallel Processing](242-PLPROCESS.md) `PLPROCESS` | 1425 | Prefix Sums | Minimising the heavier side of a split | &ndash; |
| 243 | [Reversing directions](243-DIRECTI.md) `DIRECTI` | 1426 | Strings | Parsing and reversing a route | &ndash; |
| 244 | [Full Barrier Alchemist](244-PIPSQUIK.md) `PIPSQUIK` | 1426 | Simulation | Walking a sequence with a consumable resource | &ndash; |
| 245 | [Balanced and Unique Arrays](245-UNQEQ.md) `UNQEQ` | 1431 | Constructive | Balanced split with distinct prefixes | &ndash; |
| 246 | [Maximum Angriness](246-MAXAGRY.md) `MAXAGRY` | 1432 | Combinatorics | Maximising inversions with limited swaps | &ndash; |
| 247 | [Permutation Xority](247-PERMXORITY.md) `PERMXORITY` | 1437 | Constructive | Cancelling a XOR with a 1-2-3 triple | &ndash; |
| 248 | [Akash and Dinner](248-CHEFDINE.md) `CHEFDINE` | 1438 | Greedy | Cheapest representative per group | &ndash; |
| 249 | [HTML Tags](249-HTMLTAGS.md) `HTMLTAGS` | 1441 | Strings | Validating a format | &ndash; |
| 250 | [The Nights Watch](250-WTCH.md) `WTCH` | 1441 | Greedy | Leftmost-feasible placement | &ndash; |
| 251 | [Average Flex](251-AVGFLEX.md) `AVGFLEX` | 1442 | Arrays | Counting against a global threshold | &ndash; |
| 252 | [Chef and Coins Game](252-CHCOINSG.md) `CHCOINSG` | 1442 | Game Theory | Losing positions form a residue class | &ndash; |
| 253 | [High Frequency](253-HIGHFREQ.md) `HIGHFREQ` | 1443 | Greedy | Halving the top frequency against the runner-up | &ndash; |
| 254 | [Sleepy Chef](254-FILL01.md) `FILL01` | 1445 | Greedy | Independent runs, each packed by division | &ndash; |
| 255 | [Make Array Odd](255-MAKEARRAYODD.md) `MAKEARRAYODD` | 1445 | Bit Manipulation | Tracking a single bit through XOR and OR | &ndash; |
| 256 | [Cutting Pizza](256-CUTPIZ.md) `CUTPIZ` | 1446 | Number Theory | GCD of angular gaps | &ndash; |
| 257 | [Counting Flags](257-FLAGS.md) `FLAGS` | 1446 | Combinatorics | Chromatic polynomials of small graphs | &ndash; |
| 258 | [K-MEX](258-KMEX.md) `KMEX` | 1450 | Conditionals & Case Work | Feasibility as a counting interval | &ndash; |
| 259 | [Control the Pollution](259-SMOKE.md) `SMOKE` | 1450 | Brute Force | Searching one variable over a small range | &ndash; |
| 260 | [Yet another SOD problem](260-SOD3.md) `SOD3` | 1459 | Number Theory | Digit sum congruent to the value mod 3 | &ndash; |
| 261 | [Polygon Relationship](261-POLYREL.md) `POLYREL` | 1460 | Geometry | Halving the vertex count down to a triangle | &ndash; |
| 262 | [Chef and Adventures](262-CHEFADV.md) `CHEFADV` | 1462 | Number Theory | Divisibility with an optional one-off offset | &ndash; |
| 263 | [GCD operations](263-GCDOPS.md) `GCDOPS` | 1462 | Constructive | Each reduction has a self-fixing pivot | &ndash; |
| 264 | [Triangle Classification](264-TRIANGCL.md) `TRIANGCL` | 1462 | Geometry | Classifying with squared lengths | &ndash; |
| 265 | [Magical Planks](265-MKGPLNKS.md) `MKGPLNKS` | 1467 | Strings | Counting runs | &ndash; |
| 266 | [Good Pairs](266-GOODPAIRS.md) `GOODPAIRS` | 1469 | Sets | One-pass tally of mirrored keys | &ndash; |
| 267 | [Password](267-PASSWD.md) `PASSWD` | 1470 | Strings | Several predicates, one with a positional restriction | &ndash; |
| 268 | [Approximately II](268-APPROX2.md) `APPROX2` | 1471 | Sorting | Two pointers, then counting by value | &ndash; |
| 269 | [Dense Bracket Sequence](269-DENSE.md) `DENSE` | 1472 | Prefix Sums | Best split between an open prefix and a close suffix | &ndash; |
| 270 | [Magic Set](270-MGCSET.md) `MGCSET` | 1472 | Combinatorics | A condition that reduces to its singletons | &ndash; |
| 271 | [Chef and Three Dogs](271-CHDOGS.md) `CHDOGS` | 1473 | Geometry | Pursuit curve by relative closing speed | &ndash; |
| 272 | [Cakewalk](272-CKWLK.md) `CKWLK` | 1474 | Number Theory | Prime factorisation into a two-variable range test | &ndash; |
| 273 | [Order by XOR](273-XOR_ORDER.md) `XOR_ORDER` | 1476 | Bit Manipulation | The highest differing bit decides an XOR comparison | &ndash; |
| 274 | [Chef and Numbers](274-CHEFFED.md) `CHEFFED` | 1477 | Brute Force | Bounding the search window | &ndash; |
| 275 | [Majin Vegeta](275-VEGETA.md) `VEGETA` | 1477 | Number Theory | Sieve counting distinct prime factors | &ndash; |
| 276 | [Max Mex](276-MEX.md) `MEX` | 1478 | Greedy | Spending a budget on the smallest gaps first | &ndash; |
| 277 | [Count Subarrays](277-SUBINC.md) `SUBINC` | 1478 | Arrays | Counting subarrays by maximal runs | &ndash; |
| 278 | [Distinct Pair Sums](278-MANYSUMS.md) `MANYSUMS` | 1480 | Basic Math | Range of achievable sums | &ndash; |
| 279 | [Chef and GCD](279-CHFGCD.md) `CHFGCD` | 1481 | Number Theory | Case analysis on parity | &ndash; |
| 280 | [Digital clock](280-ONOZ.md) `ONOZ` | 1482 | Brute Force | Enumerating a small product space | &ndash; |
| 281 | [Alternating Divisibility](281-ALTERNATEDIV.md) `ALTERNATEDIV` | 1483 | Constructive | Pairing k with 2k | &ndash; |
| 282 | [Jogging](282-JOGGING.md) `JOGGING` | 1484 | Number Theory | A doubling recurrence, taken modulo | &ndash; |
| 283 | [Correct Sentence](283-CORTSENT.md) `CORTSENT` | 1485 | Strings | Per-word alphabet membership | &ndash; |
| 284 | [Alternating Work Days](284-ALTER.md) `ALTER` | 1486 | Number Theory | Divisibility plus an alternation constraint | &ndash; |
| 285 | [Chef Odd](285-CHEFODD.md) `CHEFODD` | 1486 | Number Theory | Parity and capacity constraints together | &ndash; |
| 286 | [Weird Palindrome Making](286-MAKEPAL.md) `MAKEPAL` | 1486 | Arrays | Odd counts and palindrome feasibility | &ndash; |
| 287 | [Interesting XOR!](287-IRSTXOR.md) `IRSTXOR` | 1487 | Bit Manipulation | Maximising a product under a fixed XOR | &ndash; |
| 288 | [Anti Palindrome](288-ANTIPALINDR.md) `ANTIPALINDR` | 1488 | Strings | Forcing a palindrome to be impossible | &ndash; |
| 289 | [CAO Stage-1](289-CAOS1.md) `CAOS1` | 1488 | Arrays | Contiguous runs in four directions | &ndash; |
| 290 | [Chef Goes to the Cinema](290-CO92SUBW.md) `CO92SUBW` | 1493 | Basic Math | Triangular numbers and a local search | &ndash; |
| 291 | [Harrenhal](291-HHAL.md) `HHAL` | 1495 | Strings | Covering a two-letter string with palindromes | &ndash; |
| 292 | [Exactly N plus 1 Values](292-N1VALUES.md) `N1VALUES` | 1495 | Constructive | Building a sum from a run plus a remainder | &ndash; |
| 293 | [Gcd of Subarrays](293-GCDSUBARRAYS.md) `GCDSUBARRAYS` | 1498 | Constructive | Starting from the minimum and adding the slack | &ndash; |
| 294 | [Total Correct Submissions](294-TOTCRT.md) `TOTCRT` | 1499 | Arrays | Aggregating by key, then sorting | &ndash; |
| 295 | [Equal Difference](295-EQDIFFER.md) `EQDIFFER` | 1500 | Arrays | Which multisets have all pairwise differences equal | &ndash; |
| 296 | [IPC Trainers](296-IPCTRAIN.md) `IPCTRAIN` | 1500 | Greedy | Exchange argument with a max-heap | &ndash; |
| 297 | [Subarray permutations](297-SUBPERM.md) `SUBPERM` | 1502 | Constructive | Forcing every good subsegment to be a prefix | &ndash; |
| 298 | [Subarray Removal](298-SUBARRAYREM.md) `SUBARRAYREM` | 1505 | Greedy | Budgeting two resources | &ndash; |
| 299 | [Palindrome Pain](299-PALINPAIN.md) `PALINPAIN` | 1506 | Constructive | Counting distinct palindrome halves | &ndash; |
| 300 | [Equal by XORing](300-EQBYXOR.md) `EQBYXOR` | 1507 | Bit Manipulation | The XOR span of an initial segment | &ndash; |
| 301 | [Reduce to One](301-REDONE.md) `REDONE` | 1507 | Number Theory | A telescoping product in disguise | &ndash; |
| 302 | [Magda and Silly Pairs](302-SILLYPRS.md) `SILLYPRS` | 1507 | Greedy | Matching by parity | &ndash; |
| 303 | [Chef Drinks Coke](303-COKE.md) `COKE` | 1511 | Basic Math | Closed form for a drift-to-target process | &ndash; |
| 304 | [One-XOR Deletions](304-DELXORONE.md) `DELXORONE` | 1516 | Bit Manipulation | Grouping by the value with its low bit dropped | &ndash; |
| 305 | [College Life 2](305-COLGLF2.md) `COLGLF2` | 1519 | Arrays | Group total with a per-group adjustment | &ndash; |
| 306 | [Concat Palindrome](306-CONCATPAL.md) `CONCATPAL` | 1520 | Strings | Multiset containment forced by mirroring | &ndash; |
| 307 | [When to take medicine](307-MEDIC.md) `MEDIC` | 1522 | Simulation | Where a parity rule breaks at month boundaries | &ndash; |
| 308 | [Median of adjacent maximum numbers](308-MXMEDIAN.md) `MXMEDIAN` | 1523 | Sorting | Pairing extremes to lift the median | &ndash; |
| 309 | [Split Sums](309-SPSUM.md) `SPSUM` | 1524 | Number Theory | Splitting a fixed total under a gcd condition | &ndash; |
| 310 | [Guddu on a Date](310-KS2.md) `KS2` | 1525 | Number Theory | A bijection between prefixes and solutions | &ndash; |
| 311 | [Positive or Negative Subarrays](311-POSITNEG.md) `POSITNEG` | 1526 | Bit Manipulation | One power of two dominates all the lower ones | &ndash; |
| 312 | [Monsters](312-SPCP5.md) `SPCP5` | 1527 | Number Theory | Sieve plus a short search | &ndash; |
| 313 | [Admins and Shopping](313-ADMINSHOP.md) `ADMINSHOP` | 1529 | Greedy | The larger of two independent lower bounds | &ndash; |
| 314 | [The White Knight](314-E1.md) `E1` | 1530 | Dynamic Programming | Layered DP over columns of a DAG | &ndash; |
| 315 | [Largest Family](315-LARGEFAM.md) `LARGEFAM` | 1532 | Greedy | Maximising a set size under a sum budget | &ndash; |
| 316 | [Minimum Number of Pizzas](316-MINPIZZAS.md) `MINPIZZAS` | 1532 | Number Theory | Smallest multiplier for divisibility | &ndash; |
| 317 | [Prefix Permutation](317-PREFPERM.md) `PREFPERM` | 1532 | Constructive | Blocks that only close at the right moment | &ndash; |
| 318 | [Sheokand and Number](318-SHKNUM.md) `SHKNUM` | 1534 | Binary Search | Precomputed candidate set with a bisect | &ndash; |
| 319 | [Flip the String](319-FLIP.md) `FLIP` | 1538 | Strings | Two independent parity classes | &ndash; |
| 320 | [Javelin Qualification](320-JAVELIN.md) `JAVELIN` | 1538 | Sorting | Two-stage selection | &ndash; |
| 321 | [Magic Rankings](321-MGCRNK.md) `MGCRNK` | 1540 | Dynamic Programming | Maximising an average with a fixed denominator | &ndash; |
| 322 | [Let us play with rank list](322-RANKLIST.md) `RANKLIST` | 1543 | Greedy | How much deficit a given number of edits can absorb | &ndash; |
| 323 | [Unstable Subarray](323-COUNTSUB.md) `COUNTSUB` | 1545 | Arrays | A telescoping sum, then counting equal pairs | &ndash; |
| 324 | [Count K-Primes](324-KPRIME.md) `KPRIME` | 1549 | Number Theory | Sieve of distinct prime factors plus prefix counts | &ndash; |
| 325 | [Catch the Thief](325-CATHIEF.md) `CATHIEF` | 1550 | Number Theory | An invariant from step size and parity | &ndash; |
| 326 | [XxOoRr](326-XXOORR.md) `XXOORR` | 1551 | Bit Manipulation | Bits are independent, so count per column | &ndash; |
| 327 | [Sticks and Rectangles](327-RECSTI.md) `RECSTI` | 1555 | Greedy | Pairing by length, then pairing the pairs | &ndash; |
| 328 | [Increasing Decreasing](328-INCRDEC.md) `INCRDEC` | 1557 | Constructive | Multiplicity bounds for a bitonic arrangement | &ndash; |
| 329 | [Chef and Sign Sequences](329-CHEFSIGN.md) `CHEFSIGN` | 1563 | Strings | Run lengths scanned from both directions | &ndash; |
| 330 | [Nice Pairs ](330-NPAIRS.md) `NPAIRS` | 1564 | Combinatorics | Counting pairs that share an invariant key | &ndash; |
| 331 | [Boring String](331-BORSTR.md) `BORSTR` | 1566 | Strings | Longest repeated run | &ndash; |
| 332 | [List of Lists](332-LISTLIST.md) `LISTLIST` | 1567 | Greedy | Counting how many singletons can survive | &ndash; |
| 333 | [Gravity Guy](333-GRGUY.md) `GRGUY` | 1568 | Dynamic Programming | Two-state DP with a zero-cost move | &ndash; |
| 334 | [Maximal crosses](334-MAXCROSS.md) `MAXCROSS` | 1570 | Arrays | Maximal runs along rows, columns and both diagonals | &ndash; |
| 335 | [Chef and squares](335-CHSQR.md) `CHSQR` | 1576 | Constructive | A shifted cyclic Latin square | &ndash; |
| 336 | [Yet Another Constructive Problem](336-ORANDCON.md) `ORANDCON` | 1580 | Bit Manipulation | The expression computes a bitwise majority | &ndash; |
| 337 | [Chef In Infinite Plane](337-CHFPLN.md) `CHFPLN` | 1582 | Combinatorics | Capacity per value | &ndash; |
| 338 | [Yet Another Palindrome Problem](338-ARRPAL.md) `ARRPAL` | 1594 | Arrays | Prefix increments force a non-increasing profile | &ndash; |
| 339 | [Missing Numbers](339-MISS_NUM.md) `MISS_NUM` | 1594 | Brute Force | Guessing which two values are the sum and difference | &ndash; |
| 340 | [Dish Distribution](340-DISHDIS.md) `DISHDIS` | 1596 | Dynamic Programming | Bounded compositions via a prefix-sum convolution | &ndash; |
| 341 | [The One On The Last Night](341-S06E06.md) `S06E06` | 1596 | Greedy | Raise the smallest digit first | &ndash; |
| 342 | [Andrew and the Meatballs again](342-AMMEAT2.md) `AMMEAT2` | 1597 | Number Theory | A shared prime factor guarantees non-coprimality | &ndash; |

## 1600&ndash;1799

| # | Problem | Rating | Topic | Technique | Edge cases + dry run |
|---:|---|---:|---|---|:---:|
| 343 | [Odd Sum](343-ODDSUM.md) `ODDSUM` | 1600 | Basic Math | Parity of consecutive prefix sums | &ndash; |
| 344 | [Chef And Adjacent Sums](344-CHFADJSUM.md) `CHFADJSUM` | 1604 | Greedy | Keeping the heaviest elements apart | &ndash; |
| 345 | [Bouncing Ball](345-BOUNCE_BALL.md) `BOUNCE_BALL` | 1607 | Prefix Sums | Alternating hits balance two totals | &ndash; |
| 346 | [Chef and Bulb Invention](346-CHFINVNT.md) `CHFINVNT` | 1607 | Basic Math | Counting residues below a threshold in closed form | &ndash; |
| 347 | [ChefWatson uses Social Network](347-BOOKCHEF.md) `BOOKCHEF` | 1610 | Sorting | Sorting on a composite key | &ndash; |
| 348 | [Bench Press](348-BENCHP.md) `BENCHP` | 1611 | Greedy | Frequency pairing for a symmetric load | &ndash; |
| 349 | [Chain of Doughnuts](349-DONUTS.md) `DONUTS` | 1611 | Greedy | Trading sacrificed chains against links needed | &ndash; |
| 350 | [Squirrel and chestnut](350-SQUIRREL.md) `SQUIRREL` | 1611 | Binary Search | Searching time, with a greedy capacity check | &ndash; |
| 351 | [Consecutive Xor](351-XOR2.md) `XOR2` | 1611 | Bit Manipulation | The total XOR is invariant | &ndash; |
| 352 | [Different String](352-DIFSTR.md) `DIFSTR` | 1612 | Constructive | Cantor diagonalisation | &ndash; |
| 353 | [Break Free](353-REMOSET.md) `REMOSET` | 1612 | Combinatorics | A condition pinned down by its singletons | &ndash; |
| 354 | [Chef And The Hiring Event](354-CHEARMY.md) `CHEARMY` | 1613 | Number Theory | Product expansion for parity, then base-5 indexing | &ndash; |
| 355 | [Maximum Subarray ](355-MAXSUBARR.md) `MAXSUBARR` | 1613 | Greedy | Kadane plus a freely orderable block | &ndash; |
| 356 | [K Odd Sum](356-ADVITIYA5.md) `ADVITIYA5` | 1614 | Constructive | Parity blocks and the number of switches | &ndash; |
| 357 | [Survive in ChocoLand](357-SURVIVE.md) `SURVIVE` | 1616 | Basic Math | Ceiling division with a running feasibility check | &ndash; |
| 358 | [GCD of Prefixes](358-GCDPRF.md) `GCDPRF` | 1617 | Constructive | Divisibility chain, realised by the array itself | &ndash; |
| 359 | [MaxEdges](359-MAXEDGES.md) `MAXEDGES` | 1618 | Combinatorics | Complete layered DAG minus the forbidden pairs | &ndash; |
| 360 | [Positive array](360-CIREQ.md) `CIREQ` | 1620 | Greedy | Hall's condition on value-capped positions | &ndash; |
| 361 | [Max Out](361-IOPC17C.md) `IOPC17C` | 1621 | Sorting | The second largest distinct value is the answer | &ndash; |
| 362 | [XOR-ORED](362-XORORED.md) `XORORED` | 1621 | Bit Manipulation | Choosing X bit by bit against an OR | &ndash; |
| 363 | [Non-Divisor Array](363-DIVCOL.md) `DIVCOL` | 1623 | Number Theory | Colouring the divisibility order by prime-factor count | &ndash; |
| 364 | [Construct Array](364-CONSTRRAY.md) `CONSTRRAY` | 1624 | Constructive | A symmetry that forces the parity of N | &ndash; |
| 365 | [Zebra Crossing](365-ZEBRA.md) `ZEBRA` | 1626 | Greedy | Earliest hops, then one long final leap | &ndash; |
| 366 | [Stamps 100](366-S100.md) `S100` | 1631 | Greedy | A right-to-left cascade zeroes everything after one position | &ndash; |
| 367 | [XOR Engine](367-ENGXOR.md) `ENGXOR` | 1632 | Bit Manipulation | Popcount parity is additive under XOR | &ndash; |
| 368 | [Encrypt Value](368-ENV.md) `ENV` | 1633 | Greedy | Choosing which elements to add rather than multiply | &ndash; |
| 369 | [UEFA Champions League](369-UCL.md) `UCL` | 1633 | Simulation | Building a league table and sorting by two keys | &ndash; |
| 370 | [Bitwise Tuples](370-BITTUP.md) `BITTUP` | 1634 | Combinatorics | Independent bits, each a complement count | &ndash; |
| 371 | [XOR with smallest element](371-SMALLXOR.md) `SMALLXOR` | 1635 | Heaps | Detecting the two-cycle that ends the process | &ndash; |
| 372 | [Maximum Damage](372-MAXDMGE.md) `MAXDMGE` | 1636 | Bit Manipulation | AND is monotone, so only adjacent pairs matter | &ndash; |
| 373 | [Concat Sort](373-CONCATSORT.md) `CONCATSORT` | 1637 | Sorting | Counting descents in the sorted order's position sequence | &ndash; |
| 374 | [Number Hunt](374-NUMHUNT.md) `NUMHUNT` | 1638 | Number Theory | Product of the two smallest admissible primes | &ndash; |
| 375 | [ALIEN-OR](375-ALIENOR.md) `ALIENOR` | 1639 | Bit Manipulation | Single-bit values are necessary and sufficient | &ndash; |
| 376 | [Exam Cheating](376-EXAMCHT.md) `EXAMCHT` | 1639 | Number Theory | Counting divisors of a difference | &ndash; |
| 377 | [Charges](377-CHARGES.md) `CHARGES` | 1645 | Arrays | Local update of an adjacency count | &ndash; |
| 378 | [Chef and Interesting Subsequences ](378-CHEFINSQ.md) `CHEFINSQ` | 1646 | Combinatorics | Choosing among the tied boundary value | &ndash; |
| 379 | [Maximum Median Matching](379-MEDMAXMATCH.md) `MEDMAXMATCH` | 1647 | Greedy | Opposite pairing of the top halves | &ndash; |
| 380 | [Range Assign, Number of Distinct Elements Minimize](380-RANGEASSIGN.md) `RANGEASSIGN` | 1648 | Conditionals & Case Work | Fixed endpoints bound what the operation can reach | &ndash; |
| 381 | [Minimise Maximum Subarray Sum](381-MINIMISEMAX.md) `MINIMISEMAX` | 1649 | Greedy | Two independent lower bounds that are jointly attainable | &ndash; |
| 382 | [MEX-OR](382-MEXOR.md) `MEXOR` | 1650 | Bit Manipulation | OR of a prefix of the integers | &ndash; |
| 383 | [Find eX](383-FIND_X.md) `FIND_X` | 1651 | Number Theory | Shared remainder forces a multiple of the LCM | &ndash; |
| 384 | [Permutation and Palindrome](384-PERMPAL.md) `PERMPAL` | 1651 | Strings | Pairing equal letters inward from both ends | &ndash; |
| 385 | [Frequency Array Retrieval](385-FREQARRRET.md) `FREQARRRET` | 1654 | Greedy | Lexicographic labelling of equal-frequency groups | &ndash; |
| 386 | [OR Matrix](386-ORMATRIX.md) `ORMATRIX` | 1656 | Arrays | Case analysis on the nearest reachable one | &ndash; |
| 387 | [Chef Product](387-CHEFPRODUCT.md) `CHEFPRODUCT` | 1658 | Number Theory | Size feasibility from a square bound and a parity | &ndash; |
| 388 | [K-Subarrays](388-KSUB.md) `KSUB` | 1663 | Greedy | Earliest cut maximises the number of GCD-$G$ pieces | &ndash; |
| 389 | [The Optimal Pairs](389-OPTPAIRS.md) `OPTPAIRS` | 1666 | Number Theory | The minimum is always N, attained by a divisor family | &ndash; |
| 390 | [Chef and Frogs](390-FROGV.md) `FROGV` | 1668 | Sorting | Connected components from gaps in sorted order | &ndash; |
| 391 | [Fire Escape Routes](391-FIRESC.md) `FIRESC` | 1671 | Graphs | Connected components by DSU, then a product of sizes | &ndash; |
| 392 | [Powered Parameters](392-POWPM.md) `POWPM` | 1673 | Sorting | Bounding the exponent, then counting by integer root | &ndash; |
| 393 | [Gcd Queries](393-GCDQ.md) `GCDQ` | 1674 | Prefix Sums | Prefix and suffix GCD arrays | &ndash; |
| 394 | [Three Numbers](394-THREENUMBERS.md) `THREENUMBERS` | 1675 | Basic Math | Parity invariant plus a counting identity | &ndash; |
| 395 | [Bitwise Equation](395-BITEQU.md) `BITEQU` | 1679 | Constructive | Neutralising the AND to reduce to one XOR | &ndash; |
| 396 | [Array sorting](396-ARRSORT.md) `ARRSORT` | 1681 | Number Theory | GCD of the displacements | &ndash; |
| 397 | [Chef and Water Car](397-CHEFCAR.md) `CHEFCAR` | 1683 | Greedy | Pricing each litre by its earliest legal purchase | &ndash; |
| 398 | [Anti-Palindrome Queries](398-ANTIPALQ.md) `ANTIPALQ` | 1688 | Prefix Sums | Reducing a rotation condition to one count | &ndash; |
| 399 | [Boxes](399-BOX95.md) `BOX95` | 1688 | Bit Manipulation | The top bit caps a box at two elements | &ndash; |
| 400 | [Gritty Grid](400-GRITGRID.md) `GRITGRID` | 1691 | Basic Math | Checkerboard parity across alternating moves | &ndash; |
| 401 | [Subarrays with length](401-SUBARRAYLEN.md) `SUBARRAYLEN` | 1691 | Arrays | Grouping by length, then a union of intervals | &ndash; |
| 402 | [Flu Shot Lineup](402-FLUSHOT.md) `FLUSHOT` | 1692 | Binary Search | Binary search on a real-valued answer | &ndash; |
| 403 | [Building Towers](403-TOWERTOP.md) `TOWERTOP` | 1693 | Greedy | Doubling to the first tower, then one per operation | &ndash; |
| 404 | [The Vowel Matrix](404-VOWMTRX.md) `VOWMTRX` | 1694 | Combinatorics | Independent cut choices between vowel blocks | &ndash; |
| 405 | [Fencing](405-FENCE.md) `FENCE` | 1696 | Sets | Perimeter as sides minus shared edges | &ndash; |
| 406 | [3-Blast Palindrome](406-BLAST3.md) `BLAST3` | 1699 | Strings | Residue classes of the surviving positions | &ndash; |
| 407 | [Remove One Element](407-REMONE.md) `REMONE` | 1700 | Sorting | Two candidate offsets, verified by a merge | &ndash; |
| 408 | [Chef and Football Match](408-WATCHFB.md) `WATCHFB` | 1700 | Simulation | Tracking the at-most-two consistent states | &ndash; |
| 409 | [Average Gift](409-AVGGIFT.md) `AVGGIFT` | 1701 | Basic Math | Mean reachability as a sign condition | &ndash; |
| 410 | [Mystical Numbers](410-XORGAND.md) `XORGAND` | 1702 | Prefix Sums | The comparison reduces to equal bit lengths | &ndash; |
| 411 | [OR Tuples](411-ORTUPLES.md) `ORTUPLES` | 1703 | Combinatorics | Independent bits with an eight-case table | &ndash; |
| 412 | [Game on a Strip](412-ARRGAME.md) `ARRGAME` | 1705 | Game Theory | Largest free run against the runner-up | &ndash; |
| 413 | [Buying Sweets](413-BUYSWEET.md) `BUYSWEET` | 1706 | Greedy | Batching purchases of the cheapest net-cost sweet | &ndash; |
| 414 | [Spreading Charges](414-CHRGES.md) `CHRGES` | 1708 | Strings | Runs of zeros classified by their bounding charges | &ndash; |
| 415 | [Devu and Perfume](415-DEVPERF.md) `DEVPERF` | 1708 | Geometry | Manhattan 1-centre via rotated coordinates | &ndash; |
| 416 | [Lumpy - The Bus Driver](416-LUMPYBUS.md) `LUMPYBUS` | 1708 | Greedy | Cheapest refunds first, paid with coins of the larger denomination | &ndash; |
| 417 | [Summary Power](417-SUMPOWER.md) `SUMPOWER` | 1709 | Prefix Sums | Counting each boundary's contribution | &ndash; |
| 418 | [Ceiling Sum](418-CEILSUM.md) `CEILSUM` | 1712 | Basic Math | Parity bonus on a fixed total | &ndash; |
| 419 | [Minimum Coloring](419-MINCOLOR.md) `MINCOLOR` | 1713 | Constructive | Checkerboard parity, with a third colour only when forced | &ndash; |
| 420 | [Sum Product Segments](420-SUMPRODSEG.md) `SUMPRODSEG` | 1713 | Number Theory | Every family shares a pivot, so the pair must be mixed | &ndash; |
| 421 | [Even Subset Xor](421-EVENXOR.md) `EVENXOR` | 1714 | Bit Manipulation | Even-popcount numbers form a linear subspace | &ndash; |
| 422 | [Max Mex](422-MAXMEX.md) `MAXMEX` | 1714 | Sets | Keep everything except the forbidden value | &ndash; |
| 423 | [Matchsticks](423-MSTICK.md) `MSTICK` | 1714 | Arrays | Sparse-table range min and max with end aggregates | &ndash; |
| 424 | [Find an integer](424-SUMDIV2.md) `SUMDIV2` | 1714 | Number Theory | Simultaneous congruences solved by inspection | &ndash; |
| 425 | [Maximise Sum](425-MAXIMISESUM.md) `MAXIMISESUM` | 1715 | Prefix Sums | Per-position ceiling from prefix and suffix maxima | &ndash; |
| 426 | [Team Formation](426-TEAMFOR.md) `TEAMFOR` | 1715 | Greedy | Pair the specialists first, then spend the all-rounders | &ndash; |
| 427 | [Chef and Prime Divisors](427-CHAPD.md) `CHAPD` | 1720 | Number Theory | Stripping shared factors with repeated GCDs | &ndash; |
| 428 | [Iron, Magnet and Wall](428-FEMA2.md) `FEMA2` | 1725 | Greedy | Interval bipartite matching with two queues | &ndash; |
| 429 | [Oracle Devu and Longest Common Subsequence](429-ORACLCS.md) `ORACLCS` | 1726 | Strings | Binary alphabet reduces the LCS to two letter counts | &ndash; |
| 430 | [Book Exercises](430-BEX.md) `BEX` | 1728 | Stacks | Prefix minimum carried alongside a stack | &ndash; |
| 431 | [Set Difference ](431-SETDIFF.md) `SETDIFF` | 1729 | Combinatorics | Counting how often each element is the extreme | &ndash; |
| 432 | [Box of Chocolates](432-CHCBOX.md) `CHCBOX` | 1730 | Arrays | Fitting a window into the gaps between maxima | &ndash; |
| 433 | [XOR Equal](433-PALINT.md) `PALINT` | 1731 | Bit Manipulation | XOR pairs values into two-element orbits | &ndash; |
| 434 | [Bon Appetit](434-FGFS.md) `FGFS` | 1734 | Greedy | Independent activity selection per compartment | &ndash; |
| 435 | [Penalty Shoot-Out II](435-PSHOT.md) `PSHOT` | 1735 | Simulation | Best and worst completions of a prefix | &ndash; |
| 436 | [Crushed Apples and a Balance Scale](436-APP_BAL_SCA.md) `APP_BAL_SCA` | 1736 | Number Theory | Halving only reaches the odd part | &ndash; |
| 437 | [Prefixing](437-FIX.md) `FIX` | 1736 | Greedy | Forced slots, and the maximum everywhere else | &ndash; |
| 438 | [Add to Subsequence](438-SUBSEQDIST.md) `SUBSEQDIST` | 1737 | Combinatorics | Operations as bits of a distinguishing code | &ndash; |
| 439 | [Maximum Value](439-MVALUE.md) `MVALUE` | 1738 | Basic Math | Factoring the expression, then checking the extremes | &ndash; |
| 440 | [Pokemon Battles](440-PBATTLE.md) `PBATTLE` | 1739 | Sorting | Counting Pareto maxima of two orderings | &ndash; |
| 441 | [Weird Subarrays](441-WEIRDSUBARR.md) `WEIRDSUBARR` | 1739 | Arrays | Counting valley subarrays from run lengths | &ndash; |
| 442 | [Xor and Multiply](442-XORMUL.md) `XORMUL` | 1739 | Bit Manipulation | Lift the shared bits, then balance the differing ones | &ndash; |
| 443 | [Fair Distribution](443-FAIR_DISTRIB.md) `FAIR_DISTRIB` | 1741 | Prefix Sums | Reparametrising by gaps turns it into suffix sums | &ndash; |
| 444 | [Modular GCD](444-GCDMOD.md) `GCDMOD` | 1741 | Number Theory | Reducing the big operand modulo the small one | &ndash; |
| 445 | [Army Training](445-ARMTRN.md) `ARMTRN` | 1742 | Sorting | Sorted split maximising a product of two sums | &ndash; |
| 446 | [One Dimensional Kingdoms](446-ONEKING.md) `ONEKING` | 1743 | Greedy | Stabbing intervals at earliest right endpoints | &ndash; |
| 447 | [Lucky Palin](447-LUCKPAL.md) `LUCKPAL` | 1744 | Strings | Placing a block and its mirror, costed in O(1) | &ndash; |
| 448 | [Copy and Paste](448-NCOPIES.md) `NCOPIES` | 1745 | Prefix Sums | Splitting a repeated string's running total | &ndash; |
| 449 | [Eugene and function](449-KFUNC.md) `KFUNC` | 1746 | Number Theory | Digital roots are periodic along an arithmetic progression | &ndash; |
| 450 | [Same Parity Swaps in Binary Strings](450-MAX01EVSWP.md) `MAX01EVSWP` | 1747 | Constructive | Matching on a path, with a parity-forced shortfall | &ndash; |
| 451 | [The One Who Knocks!](451-EOOPR.md) `EOOPR` | 1749 | Conditionals & Case Work | Reachability of a difference by odd and even steps | &ndash; |
| 452 | [Save People](452-FIZZBUZZ2306.md) `FIZZBUZZ2306` | 1750 | Basic Math | Manhattan bisector from an adjacent placement | &ndash; |
| 453 | [Chef and String](453-CHRL2.md) `CHRL2` | 1751 | Greedy | Pipelined counters along a fixed pattern | &ndash; |
| 454 | [Bear and AB](454-ABREPEAT.md) `ABREPEAT` | 1754 | Combinatorics | Splitting pairs into within-copy and across-copy | &ndash; |
| 455 | [Digit Removal](455-DIGITREM.md) `DIGITREM` | 1754 | Basic Math | Digit-position candidates for the next clean number | &ndash; |
| 456 | [Too Many Candies](456-ICL1903.md) `ICL1903` | 1754 | Number Theory | Linear congruence solved with the extended GCD | &ndash; |
| 457 | [Shortest Route](457-SHROUTE.md) `SHROUTE` | 1756 | Prefix Sums | Nearest qualifying index from each side | &ndash; |
| 458 | [Compare those strings](458-STRCOMPARE.md) `STRCOMPARE` | 1756 | Strings | Suffix comparison answered by one backward pass | &ndash; |
| 459 | [Modular Equation](459-MODEQ.md) `MODEQ` | 1761 | Number Theory | Reducing a nested modulo to a divisibility test | &ndash; |
| 460 | [Chef Restaurant ](460-CHEFRES.md) `CHEFRES` | 1776 | Sorting | Binary search over disjoint intervals | &ndash; |
| 461 | [Minion Chef and Bananas](461-MINEAT.md) `MINEAT` | 1781 | Binary Search | Searching the answer on a monotonic predicate | &ndash; |
| 462 | [Stacks](462-STACKS.md) `STACKS` | 1799 | Binary Search | Patience stacking with a sorted top list | &ndash; |

## 1800&ndash;1999

| # | Problem | Rating | Topic | Technique | Edge cases + dry run |
|---:|---|---:|---|---|:---:|
| 463 | [A temple of Snakes](463-SNTEMPLE.md) `SNTEMPLE` | 1800 | Arrays | Runs computed from both directions | &ndash; |
| 464 | [W String](464-WSTRING.md) `WSTRING` | 1809 | Prefix Sums | Per-letter counts over hash-delimited blocks | &ndash; |
| 465 | [Chef and Easy Problem](465-XXOR.md) `XXOR` | 1810 | Prefix Sums | Per-bit prefix counts, decided bit by bit | &ndash; |
| 466 | [Forest Gathering](466-FORESTGA.md) `FORESTGA` | 1829 | Binary Search | Searching time on a monotonic yield | &ndash; |
| 467 | [Chef and Wedding Arrangements](467-CHEFWED.md) `CHEFWED` | 1841 | Dynamic Programming | Partition DP with an incrementally maintained segment cost | &ndash; |
| 468 | [Yet Another Cute Girl](468-PRETNUM.md) `PRETNUM` | 1850 | Number Theory | Segmented sieve plus prime-power exponents | &ndash; |
| 469 | [XOR with Subset](469-XORSUB.md) `XORSUB` | 1879 | Bit Manipulation | XOR linear basis over GF(2) | &ndash; |
| 470 | [ChefTown Parade](470-CHEFTOWN.md) `CHEFTOWN` | 1882 | Arrays | Sliding-window maximum and minimum with deques | &ndash; |
| 471 | [Snake Eating](471-SNAKEEAT.md) `SNAKEEAT` | 1940 | Binary Search | Feasibility check with prefix sums | &ndash; |
| 472 | [Chef and Good Subsequences](472-GDSUB.md) `GDSUB` | 1999 | Combinatorics | Elementary symmetric polynomials by DP | &ndash; |

## 2000&ndash;2199

| # | Problem | Rating | Topic | Technique | Edge cases + dry run |
|---:|---|---:|---|---|:---:|
| 473 | [Maximum Size](473-RISK.md) `RISK` | 2113 | Graphs | Connected components, then alternating greedy picks | &ndash; |

## 2200&ndash;2399

| # | Problem | Rating | Topic | Technique | Edge cases + dry run |
|---:|---|---:|---|---|:---:|
| 474 | [Lowest Sum](474-LOWSUM.md) `LOWSUM` | 2302 | Heaps | $k$ smallest pairwise sums | &ndash; |

## 2600&ndash;2799

| # | Problem | Rating | Topic | Technique | Edge cases + dry run |
|---:|---|---:|---|---|:---:|
| 475 | [Hussain Set](475-COOK82C.md) `COOK82C` | 2608 | Bit Manipulation | Grouping a halving process by bit length | &ndash; |

## Unrated

CodeChef publishes no difficulty rating for these.

| # | Problem | Rating | Topic | Technique | Edge cases + dry run |
|---:|---|---:|---|---|:---:|
| 476 | [Prajit and bits](476-ADDI.md) `ADDI` | &ndash; | Bit Manipulation | Zero bits inside the binary width | &ndash; |
| 477 | [Sort by Adjacent Swaps](477-ADJSRT.md) `ADJSRT` | &ndash; | Sorting | Insertion sort performs exactly the inversions | &ndash; |
| 478 | [Count Distinct Values](478-CNTDIST.md) `CNTDIST` | &ndash; | Sets | Replacing a linear scan with a hash set | &ndash; |
| 479 | [Counting Sort](479-CNTSORT.md) `CNTSORT` | &ndash; | Sorting | Counting sort over a small value range | &ndash; |
| 480 | [Pair Sort Version 3](480-PSORT3.md) `PSORT3` | &ndash; | Sorting | Mixed-direction composite key | &ndash; |
| 481 | [Missing a Point](481-PTMSSNG.md) `PTMSSNG` | &ndash; | Bit Manipulation | XOR cancels everything that appears twice | &ndash; |
| 482 | [Stable Quick Sort](482-QCKSRT2.md) `QCKSRT2` | &ndash; | Sorting | Which pivot choices preserve stability | &ndash; |
| 483 | [Jon and Selina](483-SELINA.md) `SELINA` | &ndash; | Bit Manipulation | Parity bitmask over a 26-letter alphabet | &ndash; |
| 484 | [Sort Checker](484-SRTCHK.md) `SRTCHK` | &ndash; | Sorting | Verifying a claimed sort | &ndash; |
| 485 | [Fair distribution](485-SUBS.md) `SUBS` | &ndash; | Sorting | Sliding a fixed-size window | &ndash; |
| 486 | [Sort by swaps](486-SWPSRT1.md) `SWPSRT1` | &ndash; | Sorting | Selection sort meets the swap budget exactly | &ndash; |

---

Generated by `python3 tools/build_docs.py` - edit `data/authored/<CODE>.md` or `solutions/<CODE>.py` and rebuild.
