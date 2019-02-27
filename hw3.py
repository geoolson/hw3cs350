import sys
from collections import defaultdict

#recursice implementation of 2^n = 2^(n-1) + 2^(n-1)
def twoN(n):
    if n == 0:
        return 1
    else:
        return twoN(n - 1) + twoN(n - 1)

#2^n equation done in linear time.
def twoNlinear(n):
    product = 1
    for i in range(n):
        product *= 2
    return product


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.buildVisited = dict()

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def addMazeEdge(self, maze, v, e):
        edge = (v[0] + e[0], v[1] + e[1])
        if edge[0] > len(maze) - 1 or edge[0] < 0 or edge[1] <0 or edge[1] > len(maze[0]) - 1:
            return (-1, -1)
        if edge in self.buildVisited:
            return (-1, -1)
        try:
            if maze[edge[0]][edge[1]] == 0:
                self.addEdge(v, edge)
                self.buildVisited[edge] = 1
                return edge
        except:
            return (-1,-1)
        return (-1,-1)

    def createMaze(self, maze, start):
        if start[0] != -1 or start[1] != -1:
            self.createMaze(maze, self.addMazeEdge(maze, start, (0, 1)))
            self.createMaze(maze, self.addMazeEdge(maze, start, (0, -1)))
            self.createMaze(maze, self.addMazeEdge(maze, start, (1, 0)))
            self.createMaze(maze, self.addMazeEdge(maze, start, (-1, 0)))

    def backtrace(self, parent, start, end):
        path = [end]
        while path[-1] != start:
            path.append(parent[path[-1]])
        path.reverse()
        print(path)
        return path

    def BFS(self, s, maze):
        parent = {}
        visited = dict()
        dim = (len(maze), len(maze[0]))
        queue = []
        queue.append(s)
        visited[s] = True
        while queue:
            s = queue.pop(0)
            if s[0] == dim[0]-1 and s[1] == dim[1]-1:
                return self.backtrace(parent, (0,0), (8,8))
            for i in self.graph[s]:
                if not i in visited:
                    parent[i] = s
                    queue.append(i)
                    visited[i] = True


if __name__ == "__main__":
    maze = [
        [0, 1, 0, 0, 1, 0, 0, 0, 0],
        [0, 1, 1, 0, 1, 0, 0, 0, 0],
        [0, 0, 1, 0, 1, 1, 0, 1, 0],
        [1, 0, 1, 0, 0, 0, 0, 1, 0],
        [0, 0, 1, 1, 1, 1, 0, 1, 0],
        [1, 0, 0, 0, 0, 1, 0, 1, 0],
        [1, 1, 1, 1, 0, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 1, 1, 1, 0]
    ]
    graph = Graph()
    graph.createMaze(maze, (0, 0))
    graph.BFS((0,0),maze)
    #if len(sys.argv) > 1:
     #   print(twoNlinear(int(sys.argv[1])))
