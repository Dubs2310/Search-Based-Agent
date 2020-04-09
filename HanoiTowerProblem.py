from AI_problem import SearchProblem

class HanoiTowerProblem(SearchProblem):
    def __init__(self, num_disks, num_towers, t_from, t_to):
        self.grid = [[] for i in range(num_towers)]
        self.towers = num_towers
        self.disks = num_disks
        self.to = t_to
        for i in range(num_disks):
            self.grid[t_from].append(i)

    def getStartState(self):
        return (self.grid, 0, [self.grid])

    def getGoalState(self, state):
        return state[0][self.to] == [i for i in range(self.disks)]

    def getSuccessors(self, state):
        moves = []
        grid, pathCost, path = state

        def getMove(t_from, t_to):
            gridCopy = [i[:] for i in grid]
            gridCopy[t_to].insert(0, gridCopy[t_from].pop(0))
            pathCopy = list(path)
            pathCopy.append(gridCopy)
            moves.append((gridCopy, pathCost + 1, pathCopy))

        for i in range(self.towers - 1):
            for j in range(1, self.towers):
                if i != j:
                    if not (not grid[i] and not grid[j]):
                        if not grid[j]:
                            getMove(i, j)
                        elif not grid[i]:
                            getMove(j, i)
                        elif grid[i][0] < grid[j][0]:
                            getMove(i, j)
                        else:
                            getMove(j, i)
        return moves
