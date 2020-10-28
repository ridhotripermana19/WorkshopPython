# # TODO: 1
# squares = []
# for x in range(10):
#     squares.append(x**2)
# print(squares)

# TODO: 2
# squares = [x**2 for x in range(10)]
# print(squares)

# TODO: 3
# combs = []
# for x in [1,2,3]:
#     for y in [3,1,4]:
#         if x != y:
#             combs.append((x, y))
# print(combs)

# TODO: 4
# vec = [-4, -2, 0, 2, 4]
# print(vec)

# print("create a new list with the value is doubled")
# print([x*2 for x in vec])

# print("filter the list to exclude negative numbers")
# print([x for x in vec if x >= 0])

# print("apply a function to all the elements")
# print([abs(x) for x in vec])

# print("call a method on each element")
# freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
# print([weapon.strip() for weapon in freshfruit])

# print("create a list of 2-tuples like (number, square)")
# print([(x, x**2) for x in range(6)])

# print("flatten a list using a listcomp with two 'for'")
# vec = [[1,2,3], [4,5,6], [7,8,9]]
# print([num for elem in vec for num in elem])

# TODO: 5
from math import pi
print([str(round(pi, i)) for i in range(1, 6)])
