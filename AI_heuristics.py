def hammingDistance(problem):
    def hammingCost(state):
        return problem.hammingCost(state)
    return hammingCost

def manhattanDistance(problem):
    def manhattanCost(state):
        return problem.manhattanCost(state)
    return manhattanCost
