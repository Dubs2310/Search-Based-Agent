from AI_problem import SearchProblem

class FarmerPuzzleProblem(SearchProblem):
    def __init__(self, farmer, wolf, sheep, cabbage):
        self.grid = [farmer, wolf, sheep, cabbage]

    def getStartState(self):
        return (self.grid, [])

    def getGoalState(self, state):
        return state[0] == [0, 0, 0, 0]

    def getSuccessors(self, state):
        moves = []
        grid, path = state

        def getMove(action, *pos):
            if not ((1 - grid[0]) == grid[1] == grid[2] or (1 - grid[0]) == grid[2] == grid[3]):
                pathCopy = list(path)
                pathCopy.append(action)
                gridCopy = list(grid)
                for i in pos:
                    gridCopy[i] = 1 - gridCopy[i]
                moves.append((gridCopy, pathCopy))

        getMove('A', 0)     #Farmer crosses ALONE
        getMove('WW', 0, 1) #Farmer crosses WITH WOLF
        getMove('WS', 0, 2) #Farmer crosses WITH SHEEP
        getMove('WC', 0, 3) #Farmer crosses WITH CABBAGE

        return moves