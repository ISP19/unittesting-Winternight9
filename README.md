## Unit Testing Assignment

by Supakorn Tangpremsri.


## Test Cases for unique

Write a table describing your test cases.

| Test case              |  Expected Result    |
|------------------------|---------------------|
| empty list             |  empty list         |
| one item               |  list with 1 item   |
| one item many times    |  list with 1 item   |
| 2 items, many times, many orders | 2 item list, items in same order  |
| input int              |  type error         |


## Test Cases for Fraction

| Test case              |  Expected Result    |
|------------------------|---------------------|
| 0/0                    |  NaN                |
| 1/0                    |  infinity           |
| -1/0                   |  negative infinity  |
| input list             |  type error         |
| input str              |  type error         |
| 1/2 == 1/0             |  false              |
| 1/3 + 2/3              |  1                  |
| 4/9 * 9/4              |  1                  |
| 3/7 - 6/7              |  -3/7               |
| 1/2 > 1/3              |  true               |
| 5/6 ** 2               |  25/36              |
| 2/3 >= 2/3             |  true               | 
| (2/3) / (3/2)          |  4/9                |
