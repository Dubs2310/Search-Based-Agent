from AI_problem import SearchProblem

class PacmanProblem(SearchProblem):
    # grid is a 2D array
    # pacman & food are tuples (r,c)
    def __init__(self, grid, pacman, food):
        self.grid = list(grid)
        self.rows = len(grid)
        self.columns = len(grid[0])
        self.pacman = pacman
        self.food = food

    # Since this problem requires us to output the path taken
    # to reach the food pellet, we'll store the path in the state
    # state has this form:
    # tuple(tuple(r,c), [tuple(r1,c1), tuple(r2,c2), ...])
    # where the first tuple is the current position of pacman
    # and the list stores the path taken to reach here
    def getStartState(self):
        return self.pacman, 0, [self.pacman] 

    def getGoalState(self, state):
        return state[0] == self.food # checks whether the given state is the goal state or not

    def getSuccessors(self, state): # gets all the possible outcomes of the current state
        moves = []
        pathCost = state[1]
        path = state[2]

        def getMove(r, c):
            if self.grid[r][c] != '%':
                newPath = list(path)
                move = (r, c)
                newPath.append(move)
                moves.append((move, pathCost + 1, newPath))

        if state[0][0] > 0:  # Go UP
            getMove(state[0][0] - 1, state[0][1])
        if state[0][1] > 0:  # Go LEFT
            getMove(state[0][0], state[0][1] - 1)
        if state[0][1] < self.columns - 1:  # Go RIGHT
            getMove(state[0][0], state[0][1] + 1)
        if state[0][0] < self.rows - 1:  # Go DOWN
            getMove(state[0][0] + 1, state[0][1])
        return moves

    def manhattanCost(self, grid): # manhattan distance: sum of vertical distance from food + sun of horzontal distance from food
        return abs(grid[0][0]-self.food[0])+abs(grid[0][1]-self.food[1]) 

    def hammingCost(self, grid): # number of positions in the current coordinate which is different from the goal coordinate
        return 0 if grid[0][0]==self.food[0] and grid[0][1]==self.food[1] else 2 if grid[0][0]!=self.food[0] and grid[0][1]!=self.food[1] else 1
