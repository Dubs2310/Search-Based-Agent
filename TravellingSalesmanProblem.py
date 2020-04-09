from AI_problem import SearchProblem

class TravellingSalesmanProblem(SearchProblem):
    #grid contains the name and coordinates of a city
    #format --> (name, x, y)
    def __init__(self, grid):
        self.grid = list(grid)

    #initial distance is 0
    def getStartState(self):
        return (self.grid, 0, [])

    def getGoalState(self, state):
        if len(state[2]) == len(self.grid) + 1:
            for i in self.grid:
                if i not in state[2]:
                    return False
            return True
        return False

    def getSuccessors(self, state):
        moves = []
        grid, dist, path = state

        def getMove(city):
            pathCopy = list(path)
            if len(pathCopy) == 0:
                newDist = dist
            else:
                newDist = dist + ((city[1] - pathCopy[-1][1])**2 + (city[2] - pathCopy[-1][2])**2)**0.5
            pathCopy.append(city)
            gridCopy = list(grid)
            if not gridCopy:
                gridCopy = []
            else:
                gridCopy.remove(city)
            moves.append((gridCopy, newDist, pathCopy))

        if not grid:
            getMove(path[0])
        else:
            for i in grid:
                getMove(i)

        return moves

    def hammingCost(self,state):
        return len(state[0])+1

    def manhattanCost(self,state):
        distance = 0
        for i in range(len(self.grid)):
            if self.grid[i] in state[0]:
                if len(state[-1])>0:
                    distance+=abs(state[-1][-1][-1]-self.grid[i][-1])+abs(state[-1][-1][-2]-self.grid[i][-2])
        return distance
