from AI_problem import SearchProblem

class PacmanProblem(SearchProblem):
    # grid is a 2D array
    # pacman & food are tuples (r,c)
    def __init__(self, grid, pacman, food):
        self.grid = list(grid)
        self.rows = len(grid)
        self.columns = len(grid[0])
        self.pacman = pacman
        #self.grid[pacman[0]] = self.grid[pacman[0]][:pacman[1]] + 'P' + self.grid[pacman[0]][pacman[1] + 1:]
        self.food = food
        self.goal = self.food
        #self.grid[food[0]] = self.grid[food[0]][:food[1]] + 'F' + self.grid[food[0]][food[1] + 1:]

    # Since this problem requires us to output the path taken
    # to reach the food pellet, we'll store the path in the state
    # state has this form:
    # tuple(tuple(r,c), [tuple(r1,c1), tuple(r2,c2), ...])
    # where the first tuple is the current position of pacman
    # and the list stores the path taken to reach here
    def getStartState(self):
        return self.pacman, [self.pacman]

    def getGoalState(self, state):
        return state[0] == self.food

    def getSuccessors(self, state):
        moves = []
        path = state[1]

        def getMove(r, c):
            if self.grid[r][c] != '%':
                newPath = list(path)
                move = (r, c)
                #self.grid[r] = self.grid[r][:c] + '-' + self.grid[r][c + 1:]
                newPath.append(move)
                moves.append((move, newPath))

        if state[0][0] > 0:  # Go UP
            getMove(state[0][0] - 1, state[0][1])
        if state[0][1] > 0:  # Go LEFT
            getMove(state[0][0], state[0][1] - 1)
        if state[0][1] < self.columns - 1:  # Go RIGHT
            getMove(state[0][0], state[0][1] + 1)
        if state[0][0] < self.rows - 1:  # Go DOWN
            getMove(state[0][0] + 1, state[0][1])
        return moves
