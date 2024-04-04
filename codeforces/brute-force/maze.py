# codeforces Maze problem
# https://codeforces.com/problemset/problem/1808/A


# n = altura
# m =largura
# k = numero de paredes
# s = numero de celulas vazias no original


dirrow = [-1, 1, 0, 0]
dircol = [0, 0, -1, 1]

def bfs(i, j):
    global k, maze, newmaze, used, delcount
    used[i][j] = 1
    ccounter = 0
    if k <= 0:
        return 1
    for d in range(4):
        newdirrow = i + dirrow[d]
        newdircol = j + dircol[d]
        if 0 <= newdirrow < n and 0 <= newdircol < m:
            if maze[newdirrow][newdircol] != '#' and used[newdirrow][newdircol] != 1:
                result = bfs(newdirrow, newdircol)
                if result == 1:
                    ccounter += 1
    if ccounter > 1:
        return 1
    else:
        k -= 1
        if k < 0:
            return 1
        newmaze[i][j] = 'X'
        return 0

n, m, k = map(int, input().split())

maze = []
newmaze = []
used = []

for i in range(n):
    row = input().strip()
    maze.append(row)
    newmaze.append(list(row))
    used.append([0] * m)
    if '.' in row:
        si, sj = i, row.index('.')

bfs(si, sj)

    
    
def transform_maze(n, m, k, original_maze):
  print(n, m, k, original_maze)
  return 0


n, m, k = map(int, input().split())
original_maze = []
for i in range(n):
  original_maze.append(list(input()))

maze = transform_maze(n, m, k, original_maze)
for line in maze:
  print(line)


'''

#..#
..#.
#...

'''