# Problems in order of complexity

Every problem ordered by the time complexity of its solution, cheapest first, and numbered so a plain directory listing follows that order. Each file carries the topic used, the problem constraints, the approach, the solution, its edge cases and a dry run.

How a problem lands in a class is set out in `tools/complexity.py`: the class is the cost of **one test case** in the bounds the problem states, so a cost quoted per query or per item is multiplied up, and a one-off sieve is flagged rather than counted.

**12 of 486 written.**

| # | Class | Problems | Written |
|---|---|---:|---:|
| 1 | [Constant time $O(1)$](#1-constant-time) | 187 | 12 |
| 2 | [Logarithmic $O(\log n)$](#2-logarithmic) | 22 | 0 |
| 3 | [Polylogarithmic $O(\log^2 n)$](#3-polylogarithmic) | 4 | 0 |
| 4 | [Square root $O(\sqrt{n})$](#4-square-root) | 7 | 0 |
| 5 | [Linear $O(n)$](#5-linear) | 184 | 0 |
| 6 | [Near-linear $O(n \log \log n)$](#6-near-linear) | 2 | 0 |
| 7 | [Linearithmic $O(n \log n)$](#7-linearithmic) | 57 | 0 |
| 8 | [Linear times polylog $O(n \log^2 n)$](#8-linear-times-polylog) | 1 | 0 |
| 9 | [Product of two sizes $O(n m)$](#9-product-of-two-sizes) | 12 | 0 |
| 10 | [Quadratic $O(n^2)$](#10-quadratic) | 10 | 0 |

## 1. Constant time

$O(1)$ &mdash; 187 problems

| # | Problem | Difficulty | Topic | Technique |
|---:|---|---:|---|---|
| 001 | [Finding Square Roots](001-FSQRT.md) `FSQRT` | 420 | Basic Math | Exact integer square root |
| 002 | [Greater Average](002-AVGPROBLEM.md) `AVGPROBLEM` | 500 | Basic Math | Integer arithmetic, avoiding floats |
| 003 | [Subscriptions](003-SUBSCRIBE_.md) `SUBSCRIBE_` | 504 | Basic Math | Ceiling division |
| 004 | [Janmansh and Assignments](004-JASSIGNMENTS.md) `JASSIGNMENTS` | 513 | Basic Math | Conditional arithmetic |
| 005 | [Exams](005-EXAMCHEF.md) `EXAMCHEF` | 519 | Basic Math | Percentage comparison without division |
| 006 | [Chef And Operators](006-CHOPRT.md) `CHOPRT` | 520 | Conditionals & Case Work | Three-way comparison |
| 007 | [Decrement OR Increment](007-DECINC.md) `DECINC` | 520 | Conditionals & Case Work | Single divisibility branch |
| 008 | [Second Largest](008-FLOW017.md) `FLOW017` | 520 | Sorting | Median of three |
| 009 | [Is it a VOWEL or CONSONANT](009-VOWELTB.md) `VOWELTB` | 520 | Strings | Membership test against a small set |
| 010 | [Chef in his Office](010-OFFICE.md) `OFFICE` | 532 | Basic Math | Direct formula |
| 011 | [CRED Coins](011-CREDCOINS.md) `CREDCOINS` | 539 | Basic Math | Floor division |
| 012 | [Sale Season](012-SALESEASON.md) `SALESEASON` | 541 | Conditionals & Case Work | Ordered threshold ladder |
| 013 | `WATERFILLING` _(not written yet)_ | | | |
| 014 | `MINPIZZA` _(not written yet)_ | | | |
| 015 | `CHEFGAMES` _(not written yet)_ | | | |
| 016 | `EXPERT` _(not written yet)_ | | | |
| 017 | `HELIUM3` _(not written yet)_ | | | |
| 018 | `NOTEBOOK` _(not written yet)_ | | | |
| 019 | `SUGARCANE` _(not written yet)_ | | | |
| 020 | `CHEFCAND` _(not written yet)_ | | | |
| 021 | `TRAVELFAST` _(not written yet)_ | | | |
| 022 | `TRUESCORE` _(not written yet)_ | | | |
| 023 | `THREETOPICS` _(not written yet)_ | | | |
| 024 | `MONOPOLY2` _(not written yet)_ | | | |
| 025 | `ACTEMP` _(not written yet)_ | | | |
| 026 | `NEARESTEXIT` _(not written yet)_ | | | |
| 027 | `AREAPERI` _(not written yet)_ | | | |
| 028 | `SST` _(not written yet)_ | | | |
| 029 | `NIBBLE` _(not written yet)_ | | | |
| 030 | `QUALIFY` _(not written yet)_ | | | |
| 031 | `MINCARS` _(not written yet)_ | | | |
| 032 | `CHEFSCORE` _(not written yet)_ | | | |
| 033 | `JENGA` _(not written yet)_ | | | |
| 034 | `SEATNUMBER` _(not written yet)_ | | | |
| 035 | `DISCUS` _(not written yet)_ | | | |
| 036 | `MAXTASTE` _(not written yet)_ | | | |
| 037 | `MOVIE2X` _(not written yet)_ | | | |
| 038 | `POLTHIEF` _(not written yet)_ | | | |
| 039 | `FLIPCARDS` _(not written yet)_ | | | |
| 040 | `BATH` _(not written yet)_ | | | |
| 041 | `FINDSHOES` _(not written yet)_ | | | |
| 042 | `TRANSFORM` _(not written yet)_ | | | |
| 043 | `BULLET` _(not written yet)_ | | | |
| 044 | `C_RATING` _(not written yet)_ | | | |
| 045 | `CHEFBOTTLE` _(not written yet)_ | | | |
| 046 | `CANDYDIST` _(not written yet)_ | | | |
| 047 | `LASTLEVELS` _(not written yet)_ | | | |
| 048 | `BLACKJACK` _(not written yet)_ | | | |
| 049 | `FILLCANDIES` _(not written yet)_ | | | |
| 050 | `XJUMP` _(not written yet)_ | | | |
| 051 | `CHESSDIST` _(not written yet)_ | | | |
| 052 | `MYSERVE` _(not written yet)_ | | | |
| 053 | `VALENTINE` _(not written yet)_ | | | |
| 054 | `WTRMIXING` _(not written yet)_ | | | |
| 055 | `WGHTS` _(not written yet)_ | | | |
| 056 | `CHEFAPPS` _(not written yet)_ | | | |
| 057 | `CHEFEREN` _(not written yet)_ | | | |
| 058 | `MINCOINS` _(not written yet)_ | | | |
| 059 | `SPCP2` _(not written yet)_ | | | |
| 060 | `CRICUP` _(not written yet)_ | | | |
| 061 | `FLOORS` _(not written yet)_ | | | |
| 062 | `SPEEDTEST` _(not written yet)_ | | | |
| 063 | `AORB` _(not written yet)_ | | | |
| 064 | `PASSORFAIL` _(not written yet)_ | | | |
| 065 | `CYCLICQD` _(not written yet)_ | | | |
| 066 | `POLYBAGS` _(not written yet)_ | | | |
| 067 | `BUILDINGRACE` _(not written yet)_ | | | |
| 068 | `FIZZBUZZ2303` _(not written yet)_ | | | |
| 069 | `CHEFRACES` _(not written yet)_ | | | |
| 070 | `FLOW005` _(not written yet)_ | | | |
| 071 | `MOZZ` _(not written yet)_ | | | |
| 072 | `PRESENTS` _(not written yet)_ | | | |
| 073 | `CHEAT` _(not written yet)_ | | | |
| 074 | `T20MCH` _(not written yet)_ | | | |
| 075 | `REACHFAST` _(not written yet)_ | | | |
| 076 | `SINGLEUSE` _(not written yet)_ | | | |
| 077 | `SALE` _(not written yet)_ | | | |
| 078 | `BIN_BAT` _(not written yet)_ | | | |
| 079 | `DICEGAME2` _(not written yet)_ | | | |
| 080 | `WATERCOOLER2` _(not written yet)_ | | | |
| 081 | `WORDLE` _(not written yet)_ | | | |
| 082 | `TYRES` _(not written yet)_ | | | |
| 083 | `SALE2` _(not written yet)_ | | | |
| 084 | `EQLZING` _(not written yet)_ | | | |
| 085 | `SUPCHEF` _(not written yet)_ | | | |
| 086 | `GENE01` _(not written yet)_ | | | |
| 087 | `BESTOFTENNIS` _(not written yet)_ | | | |
| 088 | `MILEAGE` _(not written yet)_ | | | |
| 089 | `MELTGOLD` _(not written yet)_ | | | |
| 090 | `LOOP` _(not written yet)_ | | | |
| 091 | `COCONUT` _(not written yet)_ | | | |
| 092 | `INCREAR` _(not written yet)_ | | | |
| 093 | `DEVSPORTS` _(not written yet)_ | | | |
| 094 | `CONN` _(not written yet)_ | | | |
| 095 | `HDIVISR` _(not written yet)_ | | | |
| 096 | `PROBCAT` _(not written yet)_ | | | |
| 097 | `CARCHOICE` _(not written yet)_ | | | |
| 098 | `WHICHDIV` _(not written yet)_ | | | |
| 099 | `BADMINTON` _(not written yet)_ | | | |
| 100 | `CHEFCONTEST` _(not written yet)_ | | | |
| 101 | `GROUPASSGN` _(not written yet)_ | | | |
| 102 | `RELATIVE` _(not written yet)_ | | | |
| 103 | `NUM239` _(not written yet)_ | | | |
| 104 | `DRUNKALK` _(not written yet)_ | | | |
| 105 | `CCISLAND` _(not written yet)_ | | | |
| 106 | `CHFRICH` _(not written yet)_ | | | |
| 107 | `FACEDIR` _(not written yet)_ | | | |
| 108 | `LEAGUE` _(not written yet)_ | | | |
| 109 | `UTKPLC` _(not written yet)_ | | | |
| 110 | `CHEFRUN` _(not written yet)_ | | | |
| 111 | `CHFPROFIT` _(not written yet)_ | | | |
| 112 | `MAYOR_PARTY` _(not written yet)_ | | | |
| 113 | `FLOW014` _(not written yet)_ | | | |
| 114 | `FIFTYPE` _(not written yet)_ | | | |
| 115 | `PSGRADE` _(not written yet)_ | | | |
| 116 | `AVOIDCONTACT` _(not written yet)_ | | | |
| 117 | `PR0BLEM` _(not written yet)_ | | | |
| 118 | `TWORANGES` _(not written yet)_ | | | |
| 119 | `PENALTY` _(not written yet)_ | | | |
| 120 | `SHOEFIT` _(not written yet)_ | | | |
| 121 | `CHEFSLP` _(not written yet)_ | | | |
| 122 | `HOOPS` _(not written yet)_ | | | |
| 123 | `CHFCLASS` _(not written yet)_ | | | |
| 124 | `TWOVSTEN` _(not written yet)_ | | | |
| 125 | `CARRANGE` _(not written yet)_ | | | |
| 126 | `VDATES` _(not written yet)_ | | | |
| 127 | `SPCP4` _(not written yet)_ | | | |
| 128 | `JMARKET` _(not written yet)_ | | | |
| 129 | `MARARUN` _(not written yet)_ | | | |
| 130 | `COOK82A` _(not written yet)_ | | | |
| 131 | `CHFSPL` _(not written yet)_ | | | |
| 132 | `JOINING` _(not written yet)_ | | | |
| 133 | `KEPLERSLAW` _(not written yet)_ | | | |
| 134 | `PROGLANG` _(not written yet)_ | | | |
| 135 | `WEIGHTBL` _(not written yet)_ | | | |
| 136 | `CSTOCK` _(not written yet)_ | | | |
| 137 | `TWODISH` _(not written yet)_ | | | |
| 138 | `MXEVNSUB` _(not written yet)_ | | | |
| 139 | `MAX_DIFF` _(not written yet)_ | | | |
| 140 | `SMOL` _(not written yet)_ | | | |
| 141 | `NFS` _(not written yet)_ | | | |
| 142 | `TANDJ1` _(not written yet)_ | | | |
| 143 | `DIV03` _(not written yet)_ | | | |
| 144 | `CHFNA` _(not written yet)_ | | | |
| 145 | `CHFHEIST` _(not written yet)_ | | | |
| 146 | `COLOUR` _(not written yet)_ | | | |
| 147 | `DECREM` _(not written yet)_ | | | |
| 148 | `MAXAGRY` _(not written yet)_ | | | |
| 149 | `CHCOINSG` _(not written yet)_ | | | |
| 150 | `FLAGS` _(not written yet)_ | | | |
| 151 | `SMOKE` _(not written yet)_ | | | |
| 152 | `SOD3` _(not written yet)_ | | | |
| 153 | `CHEFADV` _(not written yet)_ | | | |
| 154 | `TRIANGCL` _(not written yet)_ | | | |
| 155 | `CHDOGS` _(not written yet)_ | | | |
| 156 | `XOR_ORDER` _(not written yet)_ | | | |
| 157 | `CHEFFED` _(not written yet)_ | | | |
| 158 | `MANYSUMS` _(not written yet)_ | | | |
| 159 | `ALTER` _(not written yet)_ | | | |
| 160 | `CHEFODD` _(not written yet)_ | | | |
| 161 | `IRSTXOR` _(not written yet)_ | | | |
| 162 | `CO92SUBW` _(not written yet)_ | | | |
| 163 | `EQBYXOR` _(not written yet)_ | | | |
| 164 | `REDONE` _(not written yet)_ | | | |
| 165 | `MEDIC` _(not written yet)_ | | | |
| 166 | `KPRIME` _(not written yet)_ | | | |
| 167 | `CATHIEF` _(not written yet)_ | | | |
| 168 | `ORANDCON` _(not written yet)_ | | | |
| 169 | `MISS_NUM` _(not written yet)_ | | | |
| 170 | `S06E06` _(not written yet)_ | | | |
| 171 | `ODDSUM` _(not written yet)_ | | | |
| 172 | `CHFINVNT` _(not written yet)_ | | | |
| 173 | `MAXEDGES` _(not written yet)_ | | | |
| 174 | `UCL` _(not written yet)_ | | | |
| 175 | `MINIMISEMAX` _(not written yet)_ | | | |
| 176 | `MEXOR` _(not written yet)_ | | | |
| 177 | `CHEFPRODUCT` _(not written yet)_ | | | |
| 178 | `THREENUMBERS` _(not written yet)_ | | | |
| 179 | `BITEQU` _(not written yet)_ | | | |
| 180 | `CHEFCAR` _(not written yet)_ | | | |
| 181 | `GRITGRID` _(not written yet)_ | | | |
| 182 | `TOWERTOP` _(not written yet)_ | | | |
| 183 | `ORTUPLES` _(not written yet)_ | | | |
| 184 | `CEILSUM` _(not written yet)_ | | | |
| 185 | `EOOPR` _(not written yet)_ | | | |
| 186 | `FIZZBUZZ2306` _(not written yet)_ | | | |
| 187 | `ADDI` _(not written yet)_ | | | |

## 2. Logarithmic

$O(\log n)$ &mdash; 22 problems

| # | Problem | Difficulty | Topic | Technique |
|---:|---|---:|---|---|
| 188 | `FLOW007` _(not written yet)_ | | | |
| 189 | `HOWMANY` _(not written yet)_ | | | |
| 190 | `PALL01` _(not written yet)_ | | | |
| 191 | `MATCHES` _(not written yet)_ | | | |
| 192 | `HMAPPY2` _(not written yet)_ | | | |
| 193 | `GUESS` _(not written yet)_ | | | |
| 194 | `CKWLK` _(not written yet)_ | | | |
| 195 | `CHFGCD` _(not written yet)_ | | | |
| 196 | `JOGGING` _(not written yet)_ | | | |
| 197 | `SPSUM` _(not written yet)_ | | | |
| 198 | `KS2` _(not written yet)_ | | | |
| 199 | `SPCP5` _(not written yet)_ | | | |
| 200 | `MINPIZZAS` _(not written yet)_ | | | |
| 201 | `SHKNUM` _(not written yet)_ | | | |
| 202 | `CHEARMY` _(not written yet)_ | | | |
| 203 | `BITTUP` _(not written yet)_ | | | |
| 204 | `FIND_X` _(not written yet)_ | | | |
| 205 | `SUMDIV2` _(not written yet)_ | | | |
| 206 | `APP_BAL_SCA` _(not written yet)_ | | | |
| 207 | `GCDMOD` _(not written yet)_ | | | |
| 208 | `KFUNC` _(not written yet)_ | | | |
| 209 | `ICL1903` _(not written yet)_ | | | |

## 3. Polylogarithmic

$O(\log^2 n)$ &mdash; 4 problems

| # | Problem | Difficulty | Topic | Technique |
|---:|---|---:|---|---|
| 210 | `COOKMACH` _(not written yet)_ | | | |
| 211 | `NUMHUNT` _(not written yet)_ | | | |
| 212 | `CHAPD` _(not written yet)_ | | | |
| 213 | `DIGITREM` _(not written yet)_ | | | |

## 4. Square root

$O(\sqrt{n})$ &mdash; 7 problems

| # | Problem | Difficulty | Topic | Technique |
|---:|---|---:|---|---|
| 214 | `PRB01` _(not written yet)_ | | | |
| 215 | `RESQ` _(not written yet)_ | | | |
| 216 | `CHEFKEY` _(not written yet)_ | | | |
| 217 | `RANKLIST` _(not written yet)_ | | | |
| 218 | `EXAMCHT` _(not written yet)_ | | | |
| 219 | `OPTPAIRS` _(not written yet)_ | | | |
| 220 | `SUMPRODSEG` _(not written yet)_ | | | |

## 5. Linear

$O(n)$ &mdash; 184 problems

| # | Problem | Difficulty | Topic | Technique |
|---:|---|---:|---|---|
| 221 | `FCTRL2` _(not written yet)_ | | | |
| 222 | `TODOLIST` _(not written yet)_ | | | |
| 223 | `ELECTN` _(not written yet)_ | | | |
| 224 | `DNASTRAND` _(not written yet)_ | | | |
| 225 | `FLOW018` _(not written yet)_ | | | |
| 226 | `SELFDEF` _(not written yet)_ | | | |
| 227 | `AMR15A` _(not written yet)_ | | | |
| 228 | `LUCKFOUR` _(not written yet)_ | | | |
| 229 | `MINFLIPS` _(not written yet)_ | | | |
| 230 | `DPOLY` _(not written yet)_ | | | |
| 231 | `RECENTCONT` _(not written yet)_ | | | |
| 232 | `INSTDUM` _(not written yet)_ | | | |
| 233 | `SUNDAY` _(not written yet)_ | | | |
| 234 | `PAIREQ` _(not written yet)_ | | | |
| 235 | `PRICECON` _(not written yet)_ | | | |
| 236 | `FIRSTANDLAST` _(not written yet)_ | | | |
| 237 | `NOTIME` _(not written yet)_ | | | |
| 238 | `WCC` _(not written yet)_ | | | |
| 239 | `NONNEGPROD` _(not written yet)_ | | | |
| 240 | `DIGARR` _(not written yet)_ | | | |
| 241 | `KTTABLE` _(not written yet)_ | | | |
| 242 | `CCOOK` _(not written yet)_ | | | |
| 243 | `CHN15A` _(not written yet)_ | | | |
| 244 | `BRLADDER` _(not written yet)_ | | | |
| 245 | `VACCINQ` _(not written yet)_ | | | |
| 246 | `CFRTEST` _(not written yet)_ | | | |
| 247 | `IMDB` _(not written yet)_ | | | |
| 248 | `ALPHABET` _(not written yet)_ | | | |
| 249 | `ATTND` _(not written yet)_ | | | |
| 250 | `LAPIN` _(not written yet)_ | | | |
| 251 | `PLAYPIAN` _(not written yet)_ | | | |
| 252 | `PAWRI` _(not written yet)_ | | | |
| 253 | `TLG` _(not written yet)_ | | | |
| 254 | `ERROR` _(not written yet)_ | | | |
| 255 | `LINCHESS` _(not written yet)_ | | | |
| 256 | `BALLOON` _(not written yet)_ | | | |
| 257 | `SUBTASK` _(not written yet)_ | | | |
| 258 | `VCS` _(not written yet)_ | | | |
| 259 | `COPS` _(not written yet)_ | | | |
| 260 | `TWOSTR` _(not written yet)_ | | | |
| 261 | `BEGGASOL` _(not written yet)_ | | | |
| 262 | `CARVANS` _(not written yet)_ | | | |
| 263 | `PUSH7PA` _(not written yet)_ | | | |
| 264 | `MAKEEQUAL` _(not written yet)_ | | | |
| 265 | `EQUINOX` _(not written yet)_ | | | |
| 266 | `REVSORT` _(not written yet)_ | | | |
| 267 | `SNAKPROC` _(not written yet)_ | | | |
| 268 | `POLIN` _(not written yet)_ | | | |
| 269 | `LISDIGIT` _(not written yet)_ | | | |
| 270 | `CASH` _(not written yet)_ | | | |
| 271 | `SUDBOOKS` _(not written yet)_ | | | |
| 272 | `INDIPERM` _(not written yet)_ | | | |
| 273 | `CSUB` _(not written yet)_ | | | |
| 274 | `SMPAIR` _(not written yet)_ | | | |
| 275 | `MAGDOORS` _(not written yet)_ | | | |
| 276 | `CM164364` _(not written yet)_ | | | |
| 277 | `NOBEL` _(not written yet)_ | | | |
| 278 | `MAKEDIV3` _(not written yet)_ | | | |
| 279 | `AVGPERM` _(not written yet)_ | | | |
| 280 | `ARRHALVES` _(not written yet)_ | | | |
| 281 | `PMA` _(not written yet)_ | | | |
| 282 | `STRAME` _(not written yet)_ | | | |
| 283 | `REMELEM` _(not written yet)_ | | | |
| 284 | `EQUALITY` _(not written yet)_ | | | |
| 285 | `MIXCOLOR` _(not written yet)_ | | | |
| 286 | `PLAYFIT` _(not written yet)_ | | | |
| 287 | `AVGARR` _(not written yet)_ | | | |
| 288 | `NODRUGS` _(not written yet)_ | | | |
| 289 | `PLPROCESS` _(not written yet)_ | | | |
| 290 | `DIRECTI` _(not written yet)_ | | | |
| 291 | `PIPSQUIK` _(not written yet)_ | | | |
| 292 | `UNQEQ` _(not written yet)_ | | | |
| 293 | `PERMXORITY` _(not written yet)_ | | | |
| 294 | `HTMLTAGS` _(not written yet)_ | | | |
| 295 | `WTCH` _(not written yet)_ | | | |
| 296 | `HIGHFREQ` _(not written yet)_ | | | |
| 297 | `FILL01` _(not written yet)_ | | | |
| 298 | `MAKEARRAYODD` _(not written yet)_ | | | |
| 299 | `CUTPIZ` _(not written yet)_ | | | |
| 300 | `KMEX` _(not written yet)_ | | | |
| 301 | `POLYREL` _(not written yet)_ | | | |
| 302 | `GCDOPS` _(not written yet)_ | | | |
| 303 | `MKGPLNKS` _(not written yet)_ | | | |
| 304 | `GOODPAIRS` _(not written yet)_ | | | |
| 305 | `PASSWD` _(not written yet)_ | | | |
| 306 | `DENSE` _(not written yet)_ | | | |
| 307 | `MGCSET` _(not written yet)_ | | | |
| 308 | `VEGETA` _(not written yet)_ | | | |
| 309 | `MEX` _(not written yet)_ | | | |
| 310 | `SUBINC` _(not written yet)_ | | | |
| 311 | `ALTERNATEDIV` _(not written yet)_ | | | |
| 312 | `CORTSENT` _(not written yet)_ | | | |
| 313 | `MAKEPAL` _(not written yet)_ | | | |
| 314 | `ANTIPALINDR` _(not written yet)_ | | | |
| 315 | `HHAL` _(not written yet)_ | | | |
| 316 | `N1VALUES` _(not written yet)_ | | | |
| 317 | `GCDSUBARRAYS` _(not written yet)_ | | | |
| 318 | `EQDIFFER` _(not written yet)_ | | | |
| 319 | `SUBPERM` _(not written yet)_ | | | |
| 320 | `SUBARRAYREM` _(not written yet)_ | | | |
| 321 | `PALINPAIN` _(not written yet)_ | | | |
| 322 | `SILLYPRS` _(not written yet)_ | | | |
| 323 | `COKE` _(not written yet)_ | | | |
| 324 | `DELXORONE` _(not written yet)_ | | | |
| 325 | `COLGLF2` _(not written yet)_ | | | |
| 326 | `CONCATPAL` _(not written yet)_ | | | |
| 327 | `POSITNEG` _(not written yet)_ | | | |
| 328 | `ADMINSHOP` _(not written yet)_ | | | |
| 329 | `PREFPERM` _(not written yet)_ | | | |
| 330 | `FLIP` _(not written yet)_ | | | |
| 331 | `COUNTSUB` _(not written yet)_ | | | |
| 332 | `RECSTI` _(not written yet)_ | | | |
| 333 | `CHEFSIGN` _(not written yet)_ | | | |
| 334 | `NPAIRS` _(not written yet)_ | | | |
| 335 | `BORSTR` _(not written yet)_ | | | |
| 336 | `LISTLIST` _(not written yet)_ | | | |
| 337 | `GRGUY` _(not written yet)_ | | | |
| 338 | `CHFPLN` _(not written yet)_ | | | |
| 339 | `ARRPAL` _(not written yet)_ | | | |
| 340 | `AMMEAT2` _(not written yet)_ | | | |
| 341 | `CHFADJSUM` _(not written yet)_ | | | |
| 342 | `BOUNCE_BALL` _(not written yet)_ | | | |
| 343 | `BENCHP` _(not written yet)_ | | | |
| 344 | `XOR2` _(not written yet)_ | | | |
| 345 | `DIFSTR` _(not written yet)_ | | | |
| 346 | `REMOSET` _(not written yet)_ | | | |
| 347 | `MAXSUBARR` _(not written yet)_ | | | |
| 348 | `ADVITIYA5` _(not written yet)_ | | | |
| 349 | `SURVIVE` _(not written yet)_ | | | |
| 350 | `CIREQ` _(not written yet)_ | | | |
| 351 | `IOPC17C` _(not written yet)_ | | | |
| 352 | `XORORED` _(not written yet)_ | | | |
| 353 | `CONSTRRAY` _(not written yet)_ | | | |
| 354 | `ZEBRA` _(not written yet)_ | | | |
| 355 | `S100` _(not written yet)_ | | | |
| 356 | `ENGXOR` _(not written yet)_ | | | |
| 357 | `ENV` _(not written yet)_ | | | |
| 358 | `MAXDMGE` _(not written yet)_ | | | |
| 359 | `CHARGES` _(not written yet)_ | | | |
| 360 | `RANGEASSIGN` _(not written yet)_ | | | |
| 361 | `PERMPAL` _(not written yet)_ | | | |
| 362 | `FREQARRRET` _(not written yet)_ | | | |
| 363 | `ANTIPALQ` _(not written yet)_ | | | |
| 364 | `BOX95` _(not written yet)_ | | | |
| 365 | `SUBARRAYLEN` _(not written yet)_ | | | |
| 366 | `VOWMTRX` _(not written yet)_ | | | |
| 367 | `FENCE` _(not written yet)_ | | | |
| 368 | `BLAST3` _(not written yet)_ | | | |
| 369 | `WATCHFB` _(not written yet)_ | | | |
| 370 | `AVGGIFT` _(not written yet)_ | | | |
| 371 | `XORGAND` _(not written yet)_ | | | |
| 372 | `ARRGAME` _(not written yet)_ | | | |
| 373 | `CHRGES` _(not written yet)_ | | | |
| 374 | `SUMPOWER` _(not written yet)_ | | | |
| 375 | `EVENXOR` _(not written yet)_ | | | |
| 376 | `MAXMEX` _(not written yet)_ | | | |
| 377 | `MAXIMISESUM` _(not written yet)_ | | | |
| 378 | `TEAMFOR` _(not written yet)_ | | | |
| 379 | `FEMA2` _(not written yet)_ | | | |
| 380 | `BEX` _(not written yet)_ | | | |
| 381 | `CHCBOX` _(not written yet)_ | | | |
| 382 | `PALINT` _(not written yet)_ | | | |
| 383 | `PSHOT` _(not written yet)_ | | | |
| 384 | `FIX` _(not written yet)_ | | | |
| 385 | `SUBSEQDIST` _(not written yet)_ | | | |
| 386 | `WEIRDSUBARR` _(not written yet)_ | | | |
| 387 | `XORMUL` _(not written yet)_ | | | |
| 388 | `FAIR_DISTRIB` _(not written yet)_ | | | |
| 389 | `NCOPIES` _(not written yet)_ | | | |
| 390 | `MAX01EVSWP` _(not written yet)_ | | | |
| 391 | `CHRL2` _(not written yet)_ | | | |
| 392 | `ABREPEAT` _(not written yet)_ | | | |
| 393 | `SHROUTE` _(not written yet)_ | | | |
| 394 | `STRCOMPARE` _(not written yet)_ | | | |
| 395 | `SNTEMPLE` _(not written yet)_ | | | |
| 396 | `WSTRING` _(not written yet)_ | | | |
| 397 | `XXOR` _(not written yet)_ | | | |
| 398 | `PRETNUM` _(not written yet)_ | | | |
| 399 | `CHEFTOWN` _(not written yet)_ | | | |
| 400 | `CNTDIST` _(not written yet)_ | | | |
| 401 | `CNTSORT` _(not written yet)_ | | | |
| 402 | `PTMSSNG` _(not written yet)_ | | | |
| 403 | `QCKSRT2` _(not written yet)_ | | | |
| 404 | `SELINA` _(not written yet)_ | | | |

## 6. Near-linear

$O(n \log \log n)$ &mdash; 2 problems

| # | Problem | Difficulty | Topic | Technique |
|---:|---|---:|---|---|
| 405 | `DIVCOL` _(not written yet)_ | | | |
| 406 | `FIRESC` _(not written yet)_ | | | |

## 7. Linearithmic

$O(n \log n)$ &mdash; 57 problems

| # | Problem | Difficulty | Topic | Technique |
|---:|---|---:|---|---|
| 407 | `HOLIDAYS` _(not written yet)_ | | | |
| 408 | `PERMEXIS` _(not written yet)_ | | | |
| 409 | `SIMPSTAT` _(not written yet)_ | | | |
| 410 | `HORSES` _(not written yet)_ | | | |
| 411 | `STICKS` _(not written yet)_ | | | |
| 412 | `EVENSPLIT` _(not written yet)_ | | | |
| 413 | `MAXDIFF` _(not written yet)_ | | | |
| 414 | `SIGNFLIP` _(not written yet)_ | | | |
| 415 | `TACHSTCK` _(not written yet)_ | | | |
| 416 | `MXMTRIO` _(not written yet)_ | | | |
| 417 | `MAXTHEMIN` _(not written yet)_ | | | |
| 418 | `GFTSHP` _(not written yet)_ | | | |
| 419 | `HOTEL` _(not written yet)_ | | | |
| 420 | `MTYFRI` _(not written yet)_ | | | |
| 421 | `CHEFDINE` _(not written yet)_ | | | |
| 422 | `APPROX2` _(not written yet)_ | | | |
| 423 | `TOTCRT` _(not written yet)_ | | | |
| 424 | `IPCTRAIN` _(not written yet)_ | | | |
| 425 | `MXMEDIAN` _(not written yet)_ | | | |
| 426 | `LARGEFAM` _(not written yet)_ | | | |
| 427 | `JAVELIN` _(not written yet)_ | | | |
| 428 | `XXOORR` _(not written yet)_ | | | |
| 429 | `INCRDEC` _(not written yet)_ | | | |
| 430 | `BOOKCHEF` _(not written yet)_ | | | |
| 431 | `DONUTS` _(not written yet)_ | | | |
| 432 | `GCDPRF` _(not written yet)_ | | | |
| 433 | `SMALLXOR` _(not written yet)_ | | | |
| 434 | `CONCATSORT` _(not written yet)_ | | | |
| 435 | `CHEFINSQ` _(not written yet)_ | | | |
| 436 | `MEDMAXMATCH` _(not written yet)_ | | | |
| 437 | `KSUB` _(not written yet)_ | | | |
| 438 | `FROGV` _(not written yet)_ | | | |
| 439 | `POWPM` _(not written yet)_ | | | |
| 440 | `GCDQ` _(not written yet)_ | | | |
| 441 | `ARRSORT` _(not written yet)_ | | | |
| 442 | `FLUSHOT` _(not written yet)_ | | | |
| 443 | `REMONE` _(not written yet)_ | | | |
| 444 | `BUYSWEET` _(not written yet)_ | | | |
| 445 | `LUMPYBUS` _(not written yet)_ | | | |
| 446 | `MSTICK` _(not written yet)_ | | | |
| 447 | `SETDIFF` _(not written yet)_ | | | |
| 448 | `FGFS` _(not written yet)_ | | | |
| 449 | `MVALUE` _(not written yet)_ | | | |
| 450 | `PBATTLE` _(not written yet)_ | | | |
| 451 | `ARMTRN` _(not written yet)_ | | | |
| 452 | `ONEKING` _(not written yet)_ | | | |
| 453 | `CHEFRES` _(not written yet)_ | | | |
| 454 | `MINEAT` _(not written yet)_ | | | |
| 455 | `STACKS` _(not written yet)_ | | | |
| 456 | `FORESTGA` _(not written yet)_ | | | |
| 457 | `XORSUB` _(not written yet)_ | | | |
| 458 | `SNAKEEAT` _(not written yet)_ | | | |
| 459 | `LOWSUM` _(not written yet)_ | | | |
| 460 | `COOK82C` _(not written yet)_ | | | |
| 461 | `PSORT3` _(not written yet)_ | | | |
| 462 | `SRTCHK` _(not written yet)_ | | | |
| 463 | `SUBS` _(not written yet)_ | | | |

## 8. Linear times polylog

$O(n \log^2 n)$ &mdash; 1 problems

| # | Problem | Difficulty | Topic | Technique |
|---:|---|---:|---|---|
| 464 | `SQUIRREL` _(not written yet)_ | | | |

## 9. Product of two sizes

$O(n m)$ &mdash; 12 problems

| # | Problem | Difficulty | Topic | Technique |
|---:|---|---:|---|---|
| 465 | `IPCCERT` _(not written yet)_ | | | |
| 466 | `HIRETEST` _(not written yet)_ | | | |
| 467 | `ONOZ` _(not written yet)_ | | | |
| 468 | `CAOS1` _(not written yet)_ | | | |
| 469 | `DISHDIS` _(not written yet)_ | | | |
| 470 | `ALIENOR` _(not written yet)_ | | | |
| 471 | `ORMATRIX` _(not written yet)_ | | | |
| 472 | `DEVPERF` _(not written yet)_ | | | |
| 473 | `MINCOLOR` _(not written yet)_ | | | |
| 474 | `ORACLCS` _(not written yet)_ | | | |
| 475 | `MODEQ` _(not written yet)_ | | | |
| 476 | `RISK` _(not written yet)_ | | | |

## 10. Quadratic

$O(n^2)$ &mdash; 10 problems

| # | Problem | Difficulty | Topic | Technique |
|---:|---|---:|---|---|
| 477 | `AVGFLEX` _(not written yet)_ | | | |
| 478 | `E1` _(not written yet)_ | | | |
| 479 | `MGCRNK` _(not written yet)_ | | | |
| 480 | `MAXCROSS` _(not written yet)_ | | | |
| 481 | `CHSQR` _(not written yet)_ | | | |
| 482 | `LUCKPAL` _(not written yet)_ | | | |
| 483 | `CHEFWED` _(not written yet)_ | | | |
| 484 | `GDSUB` _(not written yet)_ | | | |
| 485 | `ADJSRT` _(not written yet)_ | | | |
| 486 | `SWPSRT1` _(not written yet)_ | | | |

---

Generated by `python3 tools/build_docs.py`.
