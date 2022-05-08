def solve():
    row, col = map(int, input().split()) 
    arr = []
    for _ in range(row):
        arr.append(list(map(int, input())))
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    queue = [[0, 0]]

    while queue:
        x, y = queue[0][0], queue[0][1]
        # print(x, ', ', y)
        del queue[0]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and nx < row and  ny >= 0 and ny < col and arr[nx][ny] == 1:
                queue.append([nx, ny])
                arr[nx][ny] = arr[x][y] + 1    
                # print('x :', nx, ' y :', ny , ' / ',arr[nx][ny])         
                
    print(arr[row-1][col-1])
        
solve()