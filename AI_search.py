class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()

    def top(self):
        return self.stack[-1]

    def empty(self):
        return len(self.stack) == 0


from collections import deque
class Queue:
    def __init__(self):
        self.queue = deque()

    def push(self, item):
        self.queue.append(item)

    def pop(self):
        return self.queue.popleft()

    def empty(self):
        return len(self.queue) == 0


import heapq
class PriorityQueue:
    def __init__(self, priorityFunction):
        self.priorityFunction = priorityFunction
        self.heap = []

    def push(self, item):
        heapq.heappush(self.heap, (self.priorityFunction(item), item))

    def pop(self):
        (_, item) = heapq.heappop(self.heap)
        return item

    def empty(self):
        return len(self.heap) == 0


# Search Algorithms
def treeSearch(problem, strategy):
    start = problem.getStartState()
    explored = set([str(start[0])])
    strategy.push(start)
    while not strategy.empty():
        node = strategy.pop()
        if problem.getGoalState(node):
            return (node[-1], len(explored))
        for move in problem.getSuccessors(node):
            strategy.push(move)
        return None

def graphSearch(problem, strategy):
    start = problem.getStartState()
    explored = set([str(start[0])])
    strategy.push(start)
    generated = 0
    while not strategy.empty():
        node = strategy.pop()
        if problem.getGoalState(node):
            # return the solution path, no. of explored nodes and no. of generated nodes
            #return (node[1], node[2], len(explored), generated) #for TSP, will try to make one return which works for all
            return (node[-1], len(explored), generated)
        successors = problem.getSuccessors(node)
        generated += len(successors)
        for move in successors:
            gridCopy = str(move[0])
            if gridCopy not in explored:
                explored.add(gridCopy)
                strategy.push(move)
    return None

def depthFirstSearch(problem):
    return graphSearch(problem, Stack())

def breadthFirstSearch(problem):
    return graphSearch(problem, Queue())

def depthLimitedDFS(problem, state, depth):
    if problem.getGoalState(state):
        #return state[1], state[2] #for TSP, will try to make one return which works for all
        return state[-1]
    if depth <= 0:
        return None
    for move in problem.getSuccessors(state):
        solution = depthLimitedDFS(problem, move, depth-1)
        if solution is not None:
            return solution
    return None

def iterativeDeepeningDFS(problem):
    depth = 1
    while True:
        solution = depthLimitedDFS(problem, problem.getStartState(), depth)
        if solution is not None:
            return solution
        depth += 1

def uniformCostSearch(problem):
    return graphSearch(problem, PriorityQueue(lambda state: len(state[-1])))

def greedySearch(problem, heuristic):
    return graphSearch(problem, PriorityQueue(heuristic))

def astarSearch(problem, heuristic):
    # A* uses path cost from start state + heuristic estimate to a goal
    totalCost = lambda state: len(state[-1])+heuristic(state)
    return graphSearch(problem, PriorityQueue(totalCost))
