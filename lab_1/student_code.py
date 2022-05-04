from re import X
import common

# global variables
height = common.constants.MAP_HEIGHT
width = common.constants.MAP_WIDTH

# defines a node with a parent
class Node:
    def __init__(self, dims, parent = None): 
        self.dims = dims
        self.parent = parent

# iterative breadth first search
def df_search(map):
    # set up
    found = False
    start = _find_start(map)
    stack = [Node(start)]
    path = []

    while stack:
        curr = stack.pop()
        y = curr.dims[0]
        x = curr.dims[1]
        map[y][x] = 4
        for next in reversed(_expand(curr, map)):
            next_y = next.dims[0]
            next_x = next.dims[1]
            if map[next_y][next_x] == 3:
                stack = []
                found = True
                path.append(Node([next_y, next_x], curr))
            else:
                stack.append(Node([next_y, next_x], curr))
        
    # trace path
    if path:
        path_node = path[0]
        while path_node:
            y = path_node.dims[0]
            x = path_node.dims[1]
            map[y][x] = 5
            path_node = path_node.parent
    return found

########################################################################
                                #BFS
########################################################################

# iterative breadth first search
def bf_search(map):
    # set up
    found = False
    start = _find_start(map)
    queue = [Node(start)]
    path = []

    while queue:
        curr = queue.pop(0)
        for next in _expand(curr, map):
            next_y = next.dims[0]
            next_x = next.dims[1]
            if map[next_y][next_x] == 3:
                queue = []
                found = True
                path.append(Node([next_y, next_x], curr))
            else:
                map[next_y][next_x] = 4
                queue.append(Node([next_y, next_x], curr))
    
    # trace path
    if path:
        path_node = path[0]
        while path_node:
            y = path_node.dims[0]
            x = path_node.dims[1]
            map[y][x] = 5
            path_node = path_node.parent
    return found

################################
# Helper functions
################################

def _find_start(map):
      # find the starting position
    for y in range(height):
        for x in range(width):
            if map[y][x] == 2:
                return [y, x]
    return False

def _expand(node, map):
    '''
    input: node
    output: array of nodes
    '''
    output = []

    # extract x and y node
    y = node.dims[0]
    x = node.dims[1]

    # package possible neighbors
    # move right (x + 1)
    if x < width - 1 and map[y][x + 1] != 4 and map[y][x + 1] != 1:
        output.append(Node([y, x + 1], node))
    # move down (y + 1)
    if y < height - 1 and map[y + 1][x] != 4 and map[y + 1][x] != 1:
        output.append(Node([y + 1, x], node))
    # move left (x - 1)
    if x > 0 and map[y][x - 1] != 4 and map[y][x - 1] != 1:
        output.append(Node([y, x - 1], node))
    # move up (y - 1)
    if y > 0 and map[y - 1][x] != 4 and map[y - 1][x] != 1:
        output.append(Node([y - 1, x], node))

    # return array of neighbors
    return output

#################################
# Recursive DFS (doesn't work)
#################################
# def df_search(map):
    
#     #####################################
#     # define recursive dfs helper function
#     def dfs(node):
#         # return whether or not the result is true and the end node
#         # extract value
#         y, x = node.dims[0], node.dims[1]
#         value = map[y][x]
#         map[y][x] = 4

#         # check for goal
#         if value == 3:
#             path.append(node)
#             return True
        
#         # expand frontier
#         for n in _expand(node, map):
#             if dfs(n) != False:
#                 path.append(n)
#                 return dfs(n)
#         return False
#     #####################################

#     found = False
#     # find the starting position
#     start = _find_start(map)

#     # find the goal and mark the path
#     start_node = Node(start)
#     path = []
#     found = dfs(start_node)
#     # if dfs(start_node):
#     #     print('answer')
#     #     found = True
#     # mark path

#     if path:
#         path_node = path[0]
#         while path_node:
#             y = path_node.dims[0]
#             x = path_node.dims[1]
#             map[y][x] = 5
#             path_node = path_node.parent
#     print(found)
#     return found