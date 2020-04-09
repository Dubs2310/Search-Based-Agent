from AI_problem import SearchProblem
class TravellingSalesman2(SearchProblem):
    def __init__(self, grid):
        self.grid = list(grid)

    #initial distance is -1, since no paths
    def getStartState(self):
        return 0, [0]

    def getGoalState(self, state):
        return len(state[1]) == len(self.grid) + 1 and state[1][0] == state[1][-1]

    def getSuccessors(self, state):
        moves = []
        dist, path = state

        def getMove(dist_grid):
            pathCopy = list(path)
            distCopy = 0
            if not not path:
                distCopy += dist + dist_grid[pathCopy[-1]]
            pathCopy.append(dist_grid.index(0))
            moves.append((distCopy, pathCopy))

        if len(path) == len(self.grid):
            getMove(self.grid[path[0]])
        else:
            for i in range(len(self.grid)):
                if i not in path:
                    getMove(self.grid[i])
        return moves

    def hammingCost(self, state):
        return len(self.grid) + 1 - len(state[1])

    def manhattanCost(self, state):
        return state[0]
