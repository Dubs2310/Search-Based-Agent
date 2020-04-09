def hammingDistance(grid):
    return len([i for i in range(len(grid)) if grid[i] != 0 and grid[i] != i+1])

def manhattanDistance(grid):    #need to fix for stone puzzle
    def distance(i):
        return 0 if grid[i] == 0 else abs(((grid[i]-1) / 3) - (i / 3)) + abs(((grid[i]-1) % 3) - (i % 3))
    return sum(distance(i) for i in range(len(grid)))