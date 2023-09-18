# This is my thought process to make a Tree Visualizer in the terminal


# Height 1

"""
-> Height =  1
-> Number of Lines = 4 (This is minimum)
-> Number of Underscores = 3 (This is minimum)
-> The spaces needed to make it are:
    -> L1 = 4
    -> L2 = 1
    -> L3 = 0
    -> L4 = 0
"""

h1 = """
    7
 ___|___
|       |
9       12
"""

# Height 2

"""
-> Height =  2
-> Number of Lines = 7 = 4 * 2 - (2 - 1)
-> Number of Underscores = 6 = 3 * 2 = 3 * 2^1
-> The spaces needed to make it are:
    -> L1 = 11
    -> L2 = 5
    -> L3 = 4
    -> L4 = 4
    -> L5 = 1
    -> L6 = 0
    -> L7 = 0
"""

h2 = """
           4 
     ______|______
    |             |
    7             8
 ___|___       ___|___
|       |     |       |    
9       12    5       2 
"""

# Height 3

"""
-> Height =  3
-> Number of Lines = 10 = 4 * 3 - (3 - 1)
-> Number of Underscores = 12 = 6 * 2 = 3 * 2^2
-> The spaces needed to make it are:
    -> L1 = 24
    -> L2 = 12
    -> L3 = 11
    -> L4 = 11
    -> L5 = 5
    -> L6 = 4
    -> L7 = 4
    -> L8 = 1
    -> L9 = 0
    -> L10 = 0
"""

h3 = """
                        3
            ____________|____________
           |                         |
           4                         10
     ______|______             ______|______
    |             |           |             |
    7             8           1             5
 ___|___       ___|___     ___|___       ___|___
|       |     |       |   |       |     |       |
9       12    5       2   4       7     13      9
"""
