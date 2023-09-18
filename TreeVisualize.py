space = " "

output = """
                            7
             _______________|_______________
            |                               |
            9                               12
      ______|______                   ______|______
     |             |                 |             |
     5             4                 2             3
 ____|____     ____|____
|         |   |         |
8         7
"""


def getSpace(numSpace):
    space = " "
    return space * numSpace


def getUnderScore(quantity):
    return "_" * quantity


def getBinaryLine(numSpace, numUnderScore, spaceFromLeft, spaceBetween=0, quantity=1):
    if quantity != 1:
        binary_line = f"""
{getSpace(spaceFromLeft)}{getSpace(numSpace + 1)}{getUnderScore(numUnderScore)}|{getUnderScore(numUnderScore)}{getSpace(spaceBetween + 1)}{getUnderScore(numUnderScore)}|{getUnderScore(numUnderScore)}
{getSpace(spaceFromLeft)}{getSpace(numSpace)}|{getSpace(numUnderScore * 2 + 1)}|{getSpace(spaceBetween  - 1)}|{getSpace(numUnderScore * 2 + 1)}|
"""
        return binary_line
    else:
        binary_line = f"""
{getSpace(spaceFromLeft)}{getSpace(numSpace + 1)}{getUnderScore(numUnderScore)}|{getUnderScore(numUnderScore)} 
{getSpace(spaceFromLeft)}{getSpace(numSpace)}|{getSpace(numUnderScore * 2 + 1)}|
"""
        return binary_line


a = 6
b = 3
sfl = 20
c = f"{getSpace(sfl + a + 1)}{7}"
x = f"""
{c}
{getBinaryLine(0, a, sfl)}
{getSpace(sfl)}{9}{getSpace(a * 2 + 1)}{12}
{getBinaryLine(0, a - b, sfl//2 - b + 5, (a * 2 - (a - b) * 2), 2)}
{getSpace(sfl - (a - b + 1))}{9}{getSpace((a - b) * 2 + 1)}{1}{getSpace((a * 2 - (a - b) * 2) - 1)}{3}{getSpace((a - b) * 2 + 1)}{2}
"""


# {getBinaryLine(3, 4, 2)}{getSpace(3)}{5}{getSpace(9)}{4}{getSpace(5)}{2}{getSpace(9)}{3}

print(x)