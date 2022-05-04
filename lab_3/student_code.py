import common

# ---------------------------------------------------------------------------- #
#                                Custom Classes                                #
# ---------------------------------------------------------------------------- #
class Node:
    def __init__(self, pos, parent, cost_so_far, a_star):
        self.pos = pos
        self.parent = parent
        self.cost_so_far = cost_so_far
        self.a_star = a_star

# ---------------------------------------------------------------------------- #
#                                     Main                                     #
# ---------------------------------------------------------------------------- #
def astar_search(map):
    '''
        access the map using "map[y][x]"
        y between 0 and common.constants.MAP_HEIGHT-1
        x between 0 and common.constants.MAP_WIDTH-1
        search order: x-1, y-1, x+1, y+1
    '''

    # ----------------------------- Helper Functions ----------------------------- #
    def _find_start(map):
        for y in range(common.constants.MAP_HEIGHT):
            for x in range(common.constants.MAP_WIDTH):
                if map[y][x] == 2:
                    return [y,x]

    def _find_end(map):
        for y in range(common.constants.MAP_HEIGHT):
            for x in range(common.constants.MAP_WIDTH):
                if map[y][x] == 3:
                    return [y,x]

    # expands frontiers, sorts by A* algorithm, with minimizations for x and y
    def _find_neighbors(pos):
        
        neighbors = []

        # initialize coordinates
        y, x = pos[0], pos[1]
        left_x = pos[1] - 1
        top_y = pos[0] - 1
        right_x = pos[1] + 1
        bottom_y = pos[0] + 1

        # move left
        if left_x >= 0 and map[y][left_x] != 1 and map[y][left_x] != 4:
            neighbors.append([y, left_x])
        # move up
        if top_y >= 0 and map[top_y][x] != 1 and map[top_y][x] != 4:
            neighbors.append([top_y, x])
        # move right
        if right_x < common.constants.MAP_WIDTH and map[y][right_x] != 1 and map[y][right_x] != 4:
            neighbors.append([y, right_x])
        # move down
        if bottom_y < common.constants.MAP_HEIGHT and map[bottom_y][x] != 1 and map[bottom_y][x] != 4:
            neighbors.append([bottom_y, x])

        return neighbors

    # returns a_star distance
    def heuristic(pos, cost_so_far):
        estimated_cost = abs(end[0] - pos[0]) + abs(end[1] - pos[1])
        return cost_so_far + estimated_cost

    # --------------------------------- A* Search -------------------------------- #

    found = False

    # finds the starting point and initializes variable
    start = _find_start(map)
    end = _find_end(map)

    root_node = Node(start, None, 0, heuristic(start, 0))

    # establishes frontier
    frontier = [root_node]

    # graph search with A* algorithm
    while frontier:
        frontier.sort(key=lambda x: x.a_star, reverse=False)
        # choose a node from frontier according to the smallest f(n) 
        current = frontier.pop(0)
        
        y, x = current.pos[0], current.pos[1]
        # check for solution
         # check if visited - done in find_neighbors function

         # check if goal
        if map[y][x] == 3:
            # mark the path and return True
            while current is not None:
                map[current.pos[0]][current.pos[1]] = 5
                current = current.parent
            found = True
            return True
        # mark as visited
        map[y][x] = 4

        # expand curr (add children/successor to frontier)
        neighbors = _find_neighbors(current.pos)

        # process neighbors and add to frontier
        for neigh in neighbors:
            neigh_node = Node(neigh, 
                                current, 
                                current.cost_so_far + 1, 
                                heuristic(neigh, current.cost_so_far + 1))

            frontier.append(neigh_node)
    return found
