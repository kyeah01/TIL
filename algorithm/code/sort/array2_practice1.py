def mabs(x,y):
    if x-y < 0:
        return -(x-y)
    else:
        return x-y

def isWall(x,y):
    if x < 0 or x >= 5:
        return True
    elif y < 0 or y >= 5:
        return True
    return False

arr = [[1,1,1,1,1],
       [1,0,0,0,1],
       [1,0,0,0,1],
       [1,0,0,0,1],
       [1,1,1,1,1]]

dx = [0,0,-1,1]
dy = [-1,1,0,0]

for x in range(len(arr)):
    for y in range(len(arr[x])):
        for i in range(4):
            testX = x + dx[i]
            testY = y + dy[i]
            if isWall(testX, testY) == False:
                sum += mabs(arr[y][x], arr[testY][testX])
print(sum)



