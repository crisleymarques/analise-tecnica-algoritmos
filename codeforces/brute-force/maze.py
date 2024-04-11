# codeforces Maze problem
# https://codeforces.com/problemset/problem/1808/A


# n = altura
# m =largura
# k = numero de paredes
# s = numero de celulas vazias no original


def transform_maze(n, m, k, maze):
    if k == 0: 
        for row in maze:
            for element in row:
                print(element, end="")
            print("")
        exit(0)

    x, y = -1, -1
    to_visit = -k 
    for i in range(n):
        for j in range(m):
            if maze[i][j] == '.':
                to_visit += 1
                x = i
                y = j

    s = [(x, y)]
    while to_visit > 0 and len(s) > 0:
        i, j = s.pop()
        maze[i][j] = '?'
        to_visit -= 1

        if i > 0 and maze[i - 1][j] == '.':
            s.append((i - 1, j))
            maze[i-1][j] = '@'

        if i < n - 1 and maze[i + 1][j] == '.':
            s.append((i + 1, j))
            maze[i+1][j] = '@'

        if j > 0 and maze[i][j - 1] == '.':
            s.append((i, j - 1))
            maze[i][j-1] = '@'

        if j < m - 1 and maze[i][j + 1] == '.':
            s.append((i, j + 1))
            maze[i][j+1] = '@'

    for row in maze:
        for element in row:
            if element == '?':
                print('.', end="")
            elif element == '.' or element == '@':
                print('X', end="")
            else:
                print(element, end="")
        print("")


n, m, k = map(int, input().split())
original_maze = []
for i in range(n):
  original_maze.append(list(input()))

transform_maze(n, m, k, original_maze)