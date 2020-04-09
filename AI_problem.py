from abc import ABC, abstractmethod
class SearchProblem(ABC):
    def __init__(self, grid):
        self.grid = grid
        pass

    @abstractmethod
    def getStartState(self):
        pass

    @abstractmethod
    def getGoalState(self, state):
        pass

    @abstractmethod
    def getSuccessors(self, state):
        pass