from AI_problem import SearchProblem

class StonePuzzleProblem(SearchProblem):
    def __init__(self, grid):
        self.grid = list(grid)
        for i in range(len(grid)):
            if grid[i] == 0:
                self.pos0 = i
                break

    def getStartState(self):
        return (self.grid, self.pos0, [self.grid])

    def getGoalState(self, state):
        return state[0] == [2, 2, 0, 1, 1]

    def getSuccessors(self, state):
        moves = []
        grid, pos0, path = state

        '''def getMove(incr, action):
            pathCopy = list(path)
            pathCopy.append(action)
            gridCopy = list(grid)
            gridCopy[pos0], gridCopy[pos0 + incr] = gridCopy[pos0 + incr], gridCopy[pos0]
            moves.append((gridCopy, pos0 + incr, pathCopy))

        if pos0 - 1 >= 0 and grid[pos0 - 1] == 1:         # Move empty block LEFT
            getMove(-1, 'L')
        if pos0 - 2 >= 0 and grid[pos0 - 2] == 1:         # Jump empty block LEFT
            getMove(-2, 'JL')
        if pos0 + 1 < len(grid) and grid[pos0 + 1] == 2:  # Move empty block RIGHT
            getMove(1, 'R')
        if pos0 + 2 < len(grid) and grid[pos0 + 2] == 2:  # Jump empty block RIGHT
            getMove(2, 'JR')'''

        #Prints solution path instead of letters
        def getMove(incr):
            pathCopy = list(path)
            gridCopy = list(grid)
            gridCopy[pos0], gridCopy[pos0 + incr] = gridCopy[pos0 + incr], gridCopy[pos0]
            pathCopy.append(gridCopy)
            moves.append((gridCopy, pos0 + incr, pathCopy))

        if pos0 - 1 >= 0 and grid[pos0 - 1] == 1:         # Move empty block LEFT
            getMove(-1)
        if pos0 - 2 >= 0 and grid[pos0 - 2] == 1:         # Jump empty block LEFT
            getMove(-2)
        if pos0 + 1 < len(grid) and grid[pos0 + 1] == 2:  # Move empty block RIGHT
            getMove(1)
        if pos0 + 2 < len(grid) and grid[pos0 + 2] == 2:  # Jump empty block RIGHT
            getMove(2)

        return moves