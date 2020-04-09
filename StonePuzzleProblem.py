from AI_problem import SearchProblem

class StonePuzzleProblem(SearchProblem):
    def __init__(self, grid):
        self.grid = list(grid)
        self.goal = ['X', 'X', '_', 'O', 'O']
        for i in range(len(grid)):
            if grid[i] == '_':
                self.pos0 = i
                break

    def getStartState(self):
        return (self.grid, self.pos0, 0, [''.join(self.grid)])

    def getGoalState(self, state):
        return state[0] == ['X', 'X', '_', 'O', 'O']

    def getSuccessors(self, state):
        moves = []
        grid, pos0, pathCost, path = state

        #Prints solution path instead of letters
        def getMove(incr):
            pathCopy = list(path)
            gridCopy = list(grid)
            gridCopy[pos0], gridCopy[pos0 + incr] = gridCopy[pos0 + incr], gridCopy[pos0]
            pathCopy.append(''.join(gridCopy))
            moves.append((gridCopy, pos0 + incr, pathCost + 1, pathCopy))

        if pos0 - 1 >= 0 and grid[pos0 - 1] == 'O':         # Move empty block LEFT
            getMove(-1)
        if pos0 - 2 >= 0 and grid[pos0 - 2] == 'O':         # Jump empty block LEFT
            getMove(-2)
        if pos0 + 1 < len(grid) and grid[pos0 + 1] == 'X':  # Move empty block RIGHT
            getMove(1)
        if pos0 + 2 < len(grid) and grid[pos0 + 2] == 'X':  # Jump empty block RIGHT
            getMove(2)

        return moves

    def manhattanCost(self, grid):
        distance = 0
        for i in range(len(grid[0])):
            for j in range(len(self.goal)):
                if grid[0][i] == self.goal[j]:
                    distance += abs(i-j)
                    break
        return distance

    def hammingCost(self, grid):
        distance = 0
        for i in range(len(grid[0])):
            if grid[0][i]!=self.goal[i]:
                distance+=1
        return distance
