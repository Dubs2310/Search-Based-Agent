def hammingDistance(grid):
    return len([i for i in range(len(grid)) if grid[i] != 0 and grid[i] != i+1])

def manhattanDistance(goal):
    def calculateDistance(state):
        if isinstance(state,list):
            distance = 0
            for i in range(len(state)):
                if not isinstance(state[i],list):
                    if not state[i] == goal[i]:
                        for j in range(i,len(goal)):
                            if state[i]==goal[j]:
                                break
                            else:
                                distance+=1
                else:
                    for j in range(len(state[i])):
                        if not state[i][j]==goal[i][j]:
                            for k in range(i, len(goal)):
                                for l in range(j, len(goal[k])):
                                    if state[i][j]==goal[i][j]:
                                        break
                                    else:
                                        distance+=1
        else:
            return abs(state[0]-goal[0])+abs(state[1]-goal[1])
        return distance;
    return calculateDistance
