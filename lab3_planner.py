# -------------------------------------------
# Libraries

from pyamaze import maze, COLOR
import pyhop

r, c = 3, 3

# -------------------------------------------
# Initialize maze
m=maze(r, c)
m.CreateMaze(theme=COLOR.light)
print(m.maze_map)
m.run()
# map of position -> E, W, N, S
position_walls = m.maze_map


# -------------------------------------------
# Set start state
start = pyhop.State('start')
start.position = (r, c)
start.walls = position_walls[start.position]
start.E_wall = position_walls[start.position]['E']
start.W_wall = position_walls[start.position]['W']
start.N_wall = position_walls[start.position]['N']
start.S_wall = position_walls[start.position]['S']
start.goal = (1, 1)
start.exit = False

# -------------------------------------------
# Set goal state
goal = pyhop.State('goal')
goal.position = (1, 1)
goal.walls = position_walls[goal.position]
goal.E_wall = position_walls[goal.position]['E']
goal.W_wall = position_walls[goal.position]['W']
goal.N_wall = position_walls[goal.position]['N']
goal.S_wall = position_walls[goal.position]['S']

# -------------------------------------------
# Operators

def move_north(state, a):
    if state.N_wall[a] == 1:
        prev_position = state.position[a]
        new_row = prev_position[a][0] - 1
        col = prev_position[1]
        state.postion[a] = (new_row, col)
        return state
    else: return False

def move_south(state, a):
    if state.S_wall[a] == 1:
        prev_position = state.position[a]
        new_row = prev_position[a][0] + 1
        col = prev_position[1]
        state.postion[a] = (new_row, col)
        return state
    else: return False

def move_east(state, a):
    if state.E_wall[a] == 1:
        prev_position = state.position[a]
        new_col = prev_position[a][1] + 1
        row = prev_position[0]
        state.postion[a] = (row, new_col)
        return state
    else: return False

def move_west(state, a):
    if state.W_wall[a] == 1:
        prev_position = state.position[a]
        new_col = prev_position[a][1] - 1
        row = prev_position[0]
        state.postion[a] = (row, new_col)
        return state
    else: return False

pyhop.declare_operators(move_north, move_south, move_east, move_west)
print('')
pyhop.print_operators()

# -------------------------------------------
# Methods

def go_north(state, a):
    if state.N_wall == 1:
        return [('move_north', a)]
    else: return False

def go_south(state, a):
    if state.S_wall == 1:
        return [('move_south', a)]
    else: return False

def go_east(state, a):
    if state.E_wall == 1:
        return [('move_east', a)]
    else: return False

def go_west(state, a):
    if state.W_wall == 1:
        return [('move_west', a)]
    else: return False

pyhop.declare_methods('go', go_north, go_south, go_east, go_west)

def solve_maze(state, a):
    if (state.position[0] == state.goal[0]) and (state.position[1] == state.goal[1]):
        return []
    else:
        return [('go', a), ('solve', a)]

pyhop.declare_methods('solve', solve_maze)

# -------------------------------------------
# Test

pyhop.pyhop(start, [('solve','start')],verbose=3)