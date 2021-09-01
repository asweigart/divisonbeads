# divisonbeads
A small Python CLI app of the "divison beads" math education tool.

By Al Sweigart al@inventwithpython.com

"Division beads" are a concept I came up with to visualize divison. A string of beads is laid out in a rectangular area. The quotient and remainder can be found through simple counting. For example:

    $ python3 -m divisionbeads
    Enter a division problem (example: 23 / 7) or QUIT.
    > 23 / 7

    23 / 7 = 3 r 2

     ├─────7─────┤

     O─O─O─O─O─O─O┐ ┬
    ┌O─O─O─O─O─O─O┘ 3
    └O─O─O─O─O─O─O┐ ┴
               O─O┘

               ├2┤

    Enter a division problem (example: 23 / 7) or QUIT.
    > 40 / 10

    40 / 10 = 4 r 0

     ├────────10───────┤

     O─O─O─O─O─O─O─O─O─O┐ ┬
    ┌O─O─O─O─O─O─O─O─O─O┘ 4
    └O─O─O─O─O─O─O─O─O─O┐ │
     O─O─O─O─O─O─O─O─O─O┘ ┴


     0

    Enter a division problem (example: 23 / 7) or QUIT.
    > 42 / 10

    42 / 10 = 4 r 2

     ├────────10───────┤

     O─O─O─O─O─O─O─O─O─O┐ ┬
    ┌O─O─O─O─O─O─O─O─O─O┘ 4
    └O─O─O─O─O─O─O─O─O─O┐ │
    ┌O─O─O─O─O─O─O─O─O─O┘ ┴
    └O─O

     ├2┤

    Enter a division problem (example: 23 / 7) or QUIT.
    > quit

Support
-------

If you find this project helpful and would like to support its development, [consider donating to its creator on Patreon](https://www.patreon.com/AlSweigart).
