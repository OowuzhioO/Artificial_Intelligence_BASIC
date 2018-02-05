from BasicGraph import *
import numpy as np


b = BasicGraph("mediumMaze.txt")
b.initGraph()
# g = np.array(b.graph)


gn = b.graph_n

print(gn)

r = b.findP(gn, 'P')
# print(r)
r = b.findTarget(gn, '.')
# r = zip(*np.where(gn == '%'))
# r = zip(np.where(gn == "%"))
# print(r[0].row)


# r = np.where(gn == 'P')
# r = r[1]
# print(r)

# p = Point(2, 3, 4, 5, 6 , 7)
# f = p.find
# print(p.y)


# a = "%"
# b = "%"
# if a == "%":
#     print("true")


# a = [[2, 3, 4], [5, 6, 7], [8, 9]]
# print(a.index(2))


# a = [1, 2, 3, 4, 5, 6]
# b = a.pop()
# print(b)