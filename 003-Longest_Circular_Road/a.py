from collections import deque

class Tree():
    """
    無向で，サイクルがないグラフ構造を想定
    """
    def __init__(self):
        self.edges = dict()
        self.sign = dict()
    def add_edge(self,n1, n2):
        if self.edges.get(n1) == None:
            self.edges[n1] = list()
        if self.edges.get(n2) == None:
            self.edges[n2] = list()
        self.edges[n1].append(n2)
        self.edges[n2].append(n1)

    def get_nodes(self):
        return self.edges.keys()

    def set_sign(self):
        for n in self.edges.keys():
            self.sign[n] = -1

    def get_longest_node_bfs(self, node):
        self.set_sign()

        self.sign[node] = 0

        queue = deque()
        queue.append(node)

        while queue:
            node = queue.popleft()
            for neighbor in self.edges[node]:
                if self.sign[neighbor] == -1:
                    self.sign[neighbor] = self.sign[node] + 1
                    queue.append(neighbor)
        longest_node = max(self.sign, key=self.sign.get)
        return longest_node, self.sign[longest_node]

    def get_longest_node_dfs(self, node):
        self.set_sign()
        self.sign[node] = 0
        queue = deque()
        queue.append(node)
        while queue:
            node = queue.pop()
            for neighbor in self.edges[node]:
                if self.sign[neighbor] == -1:
                    self.sign[neighbor] = self.sign[node] + 1
                    queue.append(neighbor)
        longest_node = max(self.sign, key=self.sign.get)

        return longest_node, self.sign[longest_node]

N = int(input())

graph = Tree()

for i in range(N-1):
    A, B = input().split()
    graph.add_edge(A,B)

node, _ = graph.get_longest_node_bfs('1')
_, res = graph.get_longest_node_bfs(node)

_node, _ = graph.get_longest_node_dfs('1')
_, _res = graph.get_longest_node_dfs(node)

assert res == _res

print(res+1)
