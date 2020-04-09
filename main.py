import AI_search
import AI_heuristics
from AI_problem import SearchProblem
from EightPuzzleProblem import EightPuzzleProblem
from PacmanProblem import PacmanProblem
from StonePuzzleProblem import StonePuzzleProblem
from FarmerPuzzleProblem import FarmerPuzzleProblem
from TravellingSalesmanProblem import TravellingSalesmanProblem
from TravellingSalesman2 import TravellingSalesman2
from HanoiTowerProblem import HanoiTowerProblem

def solve(problem: SearchProblem, *list_of_func):
    for f in list_of_func:
        if f.__name__ == "greedySearch" or f.__name__ == "astarSearch":
            print(f(problem, lambda state: AI_heuristics.hammingDistance(state[0])))
            print(f(problem, lambda state: AI_heuristics.manhattanDistance(problem.goal)(state[0])))
        else:
            print(f(problem))

p1 = EightPuzzleProblem([1, 2, 3, 0, 5, 6, 4, 7, 8])
solve(p1, AI_search.depthFirstSearch, AI_search.breadthFirstSearch,
      AI_search.uniformCostSearch, AI_search.greedySearch, AI_search.astarSearch,
      AI_search.iterativeDeepeningDFS
      )

p2 = PacmanProblem(["%%%%%%",
                    "%    %",
                    "% %% %",
                    "%    %",
                    "%%%% %",
                    "%    %",
                    "%%%%%%"], (1,1), (5,1))
solve(p2, AI_search.depthFirstSearch, AI_search.breadthFirstSearch,
      AI_search.uniformCostSearch, AI_search.greedySearch, AI_search.astarSearch,
      AI_search.iterativeDeepeningDFS)

'''p3 = StonePuzzleProblem([1, 1, 0, 2, 2])
solve(p3, AI_search.depthFirstSearch, AI_search.breadthFirstSearch,
      AI_search.uniformCostSearch, AI_search.iterativeDeepeningDFS,
      AI_search.greedySearch, AI_search.astarSearch)'''

'''p4 = FarmerPuzzleProblem(1, 1, 1, 1)
solve(p4, AI_search.depthFirstSearch, AI_search.breadthFirstSearch,
      AI_search.uniformCostSearch, AI_search.iterativeDeepeningDFS,
      AI_search.greedySearch, AI_search.astarSearch)'''

'''p5 = TravellingSalesmanProblem([('A', 5, 4), ('C', 4, 5), ('B', 3, 1), ('D', -1, -1)])
solve(p5, AI_search.depthFirstSearch, AI_search.breadthFirstSearch,
      AI_search.uniformCostSearch, AI_search.iterativeDeepeningDFS)'''

#UCS should be changed to state[0]
'''p6 = TravellingSalesman2([[0, 10, 15, 20], [10, 0, 35, 25], [15, 35, 0, 30], [20, 25, 30, 0]])
solve(p6, AI_search.depthFirstSearch, AI_search.breadthFirstSearch,
      AI_search.uniformCostSearch, AI_search.iterativeDeepeningDFS)'''


'''p7 = HanoiTowerProblem(3, 3, 0, 2)
solve(p7, AI_search.depthFirstSearch, AI_search.breadthFirstSearch,
      AI_search.uniformCostSearch, AI_search.iterativeDeepeningDFS)'''
