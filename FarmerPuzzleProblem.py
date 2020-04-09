from AI_problem import SearchProblem

class FarmerPuzzleProblem(SearchProblem):
    def __init__(self, farmer, wolf, sheep, cabbage):
        self.grid = [farmer, wolf, sheep, cabbage]

    def getStartState(self):
        return (self.grid, 0, [self.grid]) # returns the initial state of the problem

    def getGoalState(self, state): # checks whether the given state is the goal state or not
        return state[0] == [0, 0, 0, 0]

    def getSuccessors(self, state): # returns all the possible outcomes of the current state
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

    def hammingCost(self, grid): # returns the number ofpositions not in order 
        distance = 0;
        for i in range(len(grid[0])):
            if grid[0][i]!=0:
                distance+=1
        return distance

    def manhattanCost(self, grid): # returns the total steps required for the goal state
        distance = 0;
        for i in range(len(grid[0])):
            if grid[0][i]!=0:
                distance+=1
        return distance
