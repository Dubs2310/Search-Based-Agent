from AI_problem import SearchProblem

class EightPuzzleProblem(SearchProblem):
    # grid is 9-array of the 3x3 8-puzzle grid in row-major order
    # 0 represents empty block
    def __init__(self, grid):
        self.grid = list(grid)
        for i in range(len(grid)):
            if self.grid[i] == 0:
                self.pos0 = i
                break
        self.goal = [i for i in range(len(self.grid) + 1)]

    # We'll define state to be tuple([grid], pos0, [path])
    def getStartState(self):
        return (self.grid, self.pos0, 0, [self.grid])

    # Goal state is [1,2,3,4,5,6,7,8,0]
    def getGoalState(self, state):
        grid, pos0, _, _2 = state
        for i in range(8):
            if grid[i] != i+1:
                return False
        return pos0 == 8

    def getSuccessors(self, state):
        moves = []
        grid, pos0, pathCost, path = state

        def generateMove(incr):
            pathCopy = list(path)
            gridCopy = list(grid)
            gridCopy[pos0], gridCopy[pos0 + incr] = gridCopy[pos0 + incr], gridCopy[pos0]
            pathCopy.append(gridCopy)
            moves.append((gridCopy, pos0 + incr, pathCost + 1, pathCopy))

        if pos0 >= 3: # Slide empty block UP
            generateMove(-3)
        if pos0 <= 5: # Slide empty block DOWN
            generateMove(3)
        if (pos0 % 3) > 0: # Slide empty block LEFT
            generateMove(-1)
        if (pos0 % 3) < 2: # Slide empty block RIGHT
            generateMove(1)
        return moves
