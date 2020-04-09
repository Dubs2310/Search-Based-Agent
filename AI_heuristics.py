def hammingDistance(goal):
    def calculateDistance(state):
        if isinstance(state,list):
            distance = 0
            for i in range(len(state)):
                if not isinstance(state[i],list):
                    if state[i]!=goal[i]:
                        distance+=1
                else:
                    for j in range(len(state[i])):
                        if state[i][j]!=goal[i][j]:
                            distance+=1
            return distance
        else:
            return abs(state[0]-goal[0])+abs(state[1]-goal[1])
    return calculateDistance

def manhattanDistance(goal):
    def calculateDistance(state):
        distance = 0
        if isinstance(state,list):
            for i in range(len(state)):
                if not isinstance(state[i],list):
                    if not state[i] == goal[i]:
                        for j in range(len(goal)):
                            if state[i]==goal[j]:
                                distance+=abs(i-j)
                else:
                    for j in range(len(state[i])):
                        if not state[i][j]==goal[i][j]:
                            for k in range(len(goal)):
                                for l in range(len(goal[k])):
                                    if state[i][j]==goal[k][l]:
                                        distance+=abs(i-k)+abs(j-l)
        else:
            if isinstance(goal, list):
                for i in range(len(goal)):
                    distance+=abs(state[-1]-goal[i][-1])+abs(state[-2]-goal[i][-2])
            else:
                distance = abs(state[-1]-goal[-1])+abs(state[-2]-goal[-2])
        return distance
    return calculateDistance
