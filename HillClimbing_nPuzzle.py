import time

# The goal state
goal_state = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]  # '0' for the blank space

# Find the position of the blank space (0)
def find_blank_position(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return (i, j)
    return None

# Check if the current state is the goal state
def is_goal_state(state):
    return state == goal_state

# Generate possible neighbors by sliding tiles
def generate_neighbors(state):
    neighbors = []
    blank_row, blank_col = find_blank_position(state)

    # List of possible moves (row, col) changes
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up, down, left, right

    for move in moves:
        new_row = blank_row + move[0]
        new_col = blank_col + move[1]

        # Check if the move is within bounds
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            # Create a new state by swapping the blank space with the tile
            new_state = [row[:] for row in state]
            new_state[blank_row][blank_col], new_state[new_row][new_col] = \
                new_state[new_row][new_col], new_state[blank_row][blank_col]
            neighbors.append(new_state)

    return neighbors

# Heuristic function: Count the number of misplaced tiles
def heuristic(state):
    misplaced = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != goal_state[i][j] and state[i][j] != 0:
                misplaced += 1
    return misplaced

# Hill Climbing algorithm for 8-puzzle
def hill_climbing(initial_state):
    current_state = initial_state
    while not is_goal_state(current_state):
        neighbors = generate_neighbors(current_state)
        if not neighbors:
            return None  #means local max

        # Evaluate neighbors based on the min heuristic 
        next_state = min(neighbors, key=heuristic)

        # If no better state found, we are stuck
        if heuristic(next_state) >= heuristic(current_state):
            return None

        current_state = next_state
        print_state(current_state)
    return current_state

#print tiles state
def print_state(state):
    for row in state:
        print(row)
    print()

# Test the Hill Climbing algorithm with a random initial state
def test_hill_climbing():
    initial_state = [
        [0, 1, 3],
        [4, 2, 5],
        [8, 7, 6]
    ] 

    print("Initial State:")
    print_state(initial_state)

    start_time = time.time()
    result = hill_climbing(initial_state)
    end_time = time.time()

    if result:
        print("Goal State Reached:")
        print_state(result)
    else:
        print("No solution found, stuck in local maximum.")
    print(f"Time taken: {end_time - start_time:.6f} seconds")

test_hill_climbing()