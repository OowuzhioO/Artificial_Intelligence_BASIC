from BasicGraph import *
from SearchAgent import *

startMarker = 'P'
targetMarker = '.'
bg = BasicGraph("mediumMaze.txt")
bg.initGraph()
start = bg.findP(bg.graph_n, startMarker)
targets = bg.findTarget(bg.graph_n, targetMarker)
# print(start.row)
# print(targets[0].col)


# applied the functions to calculate steps
# record time occupied and find the best one

# miss time count for each agent and comparation
dfs_path = []
bfs_path = []
gbfs_path = []
astar_path = []

dfs_step_counter = dfs(bg.graph, dfs_path, start, targets)

bfs_step_counter = bfs(bg.graph, bfs_path, start, targets)

gbfs_step_counter = gbfs(bg.graph, gbfs_path, start, targets)

astar_step_counter = a_star(bg.graph, astar_path, start, targets)