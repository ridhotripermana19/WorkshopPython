matrix = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
]

# TODO: 1
# print([[row[i] for row in matrix] for i in range(4)])

# TODO: 2
# transposed = []
# for i in range(4):
#     transposed.append([row[i] for row in matrix])
# print(transposed)

# TODO: 3
print(list(zip(*matrix)))