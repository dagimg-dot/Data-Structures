from math import pow


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

# print(lineGenerator([11], [4])) # 0
# print(lineGenerator([5], ["______|______"])) # 1
# print(lineGenerator([4,13],["|","|"]))  # 2
# print(lineGenerator([4,13],[7,8])) # 3
# print(lineGenerator([1,7], ["___|___","___|___"])) # 4
# print(lineGenerator([0,7,5,7],["|","|","|","|"])) # 5
# print(lineGenerator([0,7,5,7],[9,3,5,2])) # 6



l1_spaces = [4, 11, 24, 49, 98]
# l1_spaces = []

# spaces = []
# values = []

# spaces.append(l1_spaces[height_count - 1])
# values.append(node_values[0])

# x = lineGenerator(spaces, values)
# print(x)

# print(lineGenerator([4], [7])) # 0
# print(lineGenerator([1], ["___|___"])) # 1
# print(lineGenerator([0,7],["|","|"])) # 2
# print(lineGenerator([0,7],[9,12])) # 3

# so we need three conditions in the for loop
# and the conditions are determined by modulus of 3

def spaceGenerator(current_height, current_line):
    spaces = []



    return spaces

def valueGenerator(current_height, current_line):
    values = []



    return values


######################
# Test for height: 2 #
######################

MIN_NUMBEROFLINE = 4
MIN_UNDERSCORE = 3
 
height = 2
total_line = MIN_NUMBEROFLINE + 3 * (height - 1)  # This is constant

node_values = [1, 2, 3, 4, 5, 6, 7]
current_height = height

underscore = MIN_UNDERSCORE * int(pow(2, current_height - 1))  # This is variable

# print(lineGenerator([11], [4])) # 0
# print(lineGenerator([5], ["______|______"])) # 1
# print(lineGenerator([4,13],["|","|"]))  # 2
# print(lineGenerator([4,13],[7,8])) # 3
# print(lineGenerator([1,7], ["___|___","___|___"])) # 4
# print(lineGenerator([0,7,5,7],["|","|","|","|"])) # 5
# print(lineGenerator([0,7,5,7],[9,3,5,2])) # 6

for i in range(total_line):
    current_line = i + 1
    spaces = []
    values = []

    # Do something and generate the spaces and values for lineGenerator function
    # spaces = ?
    # values = ?

    if i % 3 == 0:
        # This is where spaces and node values are given
        spaces = spaceGenerator(current_height, current_line)
        values = valueGenerator(current_height, current_line)

        # Change the height based on the current line
        if current_line % 4 == 3:
            current_height -= 1
    elif i % 3 == 1:
        # This is where spaces and "___|___" these things are given
        spaces = spaceGenerator(current_height, current_line)
        values = valueGenerator(current_height, current_line)
    elif i % 3 == 2:
        # This is where spaces and "|" these things are given
        spaces = spaceGenerator(current_height, current_line)
        values = valueGenerator(current_height, current_line)

    lineGenerator(spaces, values)
