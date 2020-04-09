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
            gridCopy.remove(city) if not not gridCopy else gridCopy.append(-1)
            moves.append((gridCopy, newDist, pathCopy))

        if not grid:
            getMove(path[0])
        else:
            for i in grid:
                getMove(i)

        return moves
