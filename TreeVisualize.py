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
"""
# {getBinaryLine(0, a - b, sfl//2 - b + 5, (a * 2 - (a - b) * 2), 2)}
# {getSpace(sfl - (a - b + 1))}{9}{getSpace((a - b) * 2 + 1)}{1}{getSpace((a * 2 - (a - b) * 2) - 1)}{3}{getSpace((a - b) * 2 + 1)}{2}


def getSpace(numSpace):
    space = " "
    return space * numSpace


def getUnderScore(quantity):
    return "_" * quantity

# hypothetical function which takes a list as space number between what is written
# for example 

h1 = """
    7
 ___|___
|       |
9       12
"""

# L1: [4], [7]
# L2: [1], ["___|___"] -> this will be generated
# L3: [0,7],["|","|"]
# L4: [0,7],[9,12]

def lineGenerator(spaces, values):
    final = ""
    for i in range(len(spaces)):
        final += f"{getSpace(spaces[i])}{values[i]}"

    return final


# print(lineGenerator([4], [7]))
# print(lineGenerator([1], ["___|___"]))
# print(lineGenerator([0,7],["|","|"]))
# print(lineGenerator([0,7],[9,12]))

print(lineGenerator([11], [4]))
print(lineGenerator([5], ["______|______"]))
print(lineGenerator([4,13],["|","|"]))
print(lineGenerator([4,13],[7,8]))
print(lineGenerator([1,7], ["___|___","___|___"]))
print(lineGenerator([0,7,5,7],["|","|","|","|"]))
print(lineGenerator([0,7,4,7],[9,12,5,2]))
