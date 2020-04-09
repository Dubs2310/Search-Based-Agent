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
        for element in self.heap:
            print("++",element,"++")
        print("====",item,"====")
        input()
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
    expanded = 0
    while not strategy.empty():
        node = strategy.pop()
        if problem.getGoalState(node):
            print('Nodes Expanded:', expanded)
            print('Nodes Generated:', len(explored))

            '''if type(problem).__name__ not in ['TravellingSalesmanProblem', 'TravellingSalesman2']:
                print('Path Cost:', len(node[-1]) - 1)
            else:'''

            print('Path Cost:', node[-2])
            return node[-1]
        successors = problem.getSuccessors(node)
        expanded += len(successors)
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

def depthLimitedDFS(problem, state, depth, expanded = 0, explored = set()):
    if problem.getGoalState(state):
        print('Nodes Expanded:', expanded)
        print('Nodes Generated:',len(explored))
        print('Path Cost:', state[-2])
        return state[-1]
    if depth <= 0:
        return None
    successors = problem.getSuccessors(state)
    expanded += len(successors)
    for move in successors:
        gridCopy = str(move[0])
        if gridCopy not in explored:
            explored.add(gridCopy)

        solution = depthLimitedDFS(problem, move, depth-1, expanded, explored)
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
    return graphSearch(problem, PriorityQueue(lambda state: state[-2]))

def greedySearch(problem, heuristic):
    return graphSearch(problem, PriorityQueue(heuristic))

def astarSearch(problem, heuristic):
    # A* uses path cost from start state + heuristic estimate to a goal
    totalCost = lambda state: state[-2] + heuristic(state)
    return graphSearch(problem, PriorityQueue(totalCost))
