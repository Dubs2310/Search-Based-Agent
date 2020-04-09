from AI_problem import SearchProblem

class HanoiTowerProblem(SearchProblem):
    def __init__(self, num_disks, num_towers, t_from, t_to):
        self.grid = [[] for i in range(num_towers)]
        self.disks = num_disks
        self.to = t_to
        for i in range(num_disks):
            self.grid[t_from].append(i)

    def getStartState(self):
        return (self.grid, 0, [self.grid]) # returns the initial state of the problem

    def getGoalState(self, state):
        return state[0][self.to] == [i for i in range(self.disks)] # returns whether the given state is the goal state or not

    def getSuccessors(self, state): # returns all the possible outcomes of the current state
        moves = []
        grid, pathCost, path = state

        def getMove(t_from, t_to):
            gridCopy = [i[:] for i in grid]
            gridCopy[t_to].insert(0, gridCopy[t_from].pop(0))
            pathCopy = list(path)
            pathCopy.append(gridCopy)
            moves.append((gridCopy, pathCost + 1, pathCopy))

        for i in range(len(self.grid) - 1):
            for j in range(1, len(self.grid)):
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

    def hammingCost(self, state): # returns the number of positions not in order
        return self.disks - len(state[0][self.to])

    def manhattanCost(self, state): # returns the total number of moves required to reach the goal state
        #len(grid[0]) * abs(self.to - 0) + len(grid[1]) * abs(self.to - 0) + len()
        return sum(len(state[0][i]) * abs(self.to - i) for i in range(len(state[0]))) + 1
