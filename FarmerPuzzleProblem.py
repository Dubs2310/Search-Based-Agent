from AI_problem import SearchProblem

class FarmerPuzzleProblem(SearchProblem):
    def __init__(self, farmer, wolf, sheep, cabbage):
        self.grid = [farmer, wolf, sheep, cabbage]

    def getStartState(self):
        return (self.grid, 0, [self.grid])

    def getGoalState(self, state):
        return state[0] == [0, 0, 0, 0]

    def getSuccessors(self, state):
        moves = []
        grid, pathCost, path = state

        def getMove(*pos):
            if not ((1 - grid[0]) == grid[1] == grid[2] or (1 - grid[0]) == grid[2] == grid[3]):
                pathCopy = list(path)
                gridCopy = list(grid)
                pathCopy.append(gridCopy)
                for i in pos:
                    gridCopy[i] = 1 - gridCopy[i]
                moves.append((gridCopy, pathCost + 1, pathCopy))

        getMove(0)     #Farmer crosses ALONE
        getMove(0, 1) #Farmer crosses WITH WOLF
        getMove(0, 2) #Farmer crosses WITH SHEEP
        getMove(0, 3) #Farmer crosses WITH CABBAGE

        return moves
