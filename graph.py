
class Graph:
    def __init__(self, v, e):
        self.v = v
        self.e = e
        # Note: The vertices are numbered starting from 1
        self.d = {k: [] for k in range(1, v+1)}

    def add_edge(self, u, v):
        self.d[u].append(v)  # Directed graph

    #
    # Utility function to do DFS
    #
    def dfs_util(self, s, visited):
        visited[s] = True
        print s,

        for adj in self.d[s]:
            if visited[adj] is False:
                self.dfs_util(adj, visited)

    #
    # DFS Traversal of a graph
    # T(n)- O(V+E)
    #
    def dfs(self, s):
        # The vertices are numbered starting from 1
        visited = [False]*(self.v+1)
        self.dfs_util(s, visited)

    #
    # Utility function to do BFS
    #
    def bfs_util(self, s, visited):
        q = [s]
        while len(q) > 0:
            node = q.pop(0)
            visited[node] = True
            print node,

            for adj in self.d[node]:
                if visited[adj] is False:
                    q.append(adj)

    #
    # BFS Traversal of a graph
    # T(n)- O(V+E)
    #
    def bfs(self, s):
        visited = [False]*(self.v+1)
        self.bfs_util(s, visited)

    # If there is directed edge from vertex a to vertex b --> a knows b
    def knows(self, a, b):
        l = self.d[a]
        if len(l) > 0 and b in l:
            return True
        return False

    #
    # Find the celebrity from a group of people.
    # A celebrity is a person who everyone knows, but he does not know anyone.
    # From a graph perspective, a celebrity vertex is a vertex with n-1
    # incoming edges and 0 outgoing edges.
    # T(n)- O(n)
    #
    # Other approaches- (i) Traversing the adjacency list/matrix to  check
    #                       indegree and outdegree values of all vertices
    #                   (ii) Divide and conquer
    #                   (iii) Use stack
    #                   Refer gfg for these methods
    #
    def celeb(self):
        l = self.d.keys()
        i, j = 0, len(l)-1

        while i < j:
            if self.knows(l[i], l[j]) is True:
                c = l[j]
                i += 1
            else:
                c = l[i]
                j -= 1

        for i in l:
            if i == c:
                continue
            if self.knows(c, i) is False and self.knows(i, c) is True:
                continue
            return -1
        return c

    #
    # Utility function to print all paths from a given source to a destination
    # in a directed graph.
    #
    def print_paths_util(self, s, d, path, visited):
        visited[s] = True

        path.append(s)  # Append current node to path
        if s == d:
            print path  # print path when destination node is reached
        else:
            for i in self.d[s]:  # DFS on all adjacent nodes
                if not visited[i]:
                    self.print_paths_util(i, d, path, visited)

        # Remove current element from the path on completion of recursion
        # and reset its visited state
        path.pop()
        visited[s] = False

    #
    # Print all paths from a given source to a destination in a directed graph.
    # Approach: Apply DFS and keep storing path nodes in a list.
    #           Display the list on reaching the destination.
    #
    # T(n)- O(V+E)
    #
    def print_paths(self, s, d):
        visited = [False]*(self.v+1)
        path = []
        self.print_paths_util(s, d, path, visited)

    #
    # Utility function to detect cycle in a directed graph
    #
    def cycle_detection_util(self, v, visited, recursion_stack):
        visited[v] = True
        recursion_stack[v] = True

        for node in self.d[v]:
            if not visited[node]:
                if self.cycle_detection_util(node, visited, recursion_stack):
                    return True
            # If the node is visited and present in the recursion stack,
            # it confirms a cycle in the graph.
            elif recursion_stack[node]:
                return True

        recursion_stack[v] = False
        return False

    #
    # Detect a cycle in a directed graph.
    # Approach: Use DFS and maintain a recursion stack, to detect cycle
    # T(n)- O(V+E)
    #
    # Application: To detect a deadlock between processes.
    #
    # Exercise: Detect cycle in undirected graph.
    #           (http://www.geeksforgeeks.org/detect-cycle-undirected-graph/)
    #
    def cycle_detection(self):
        visited = [False]*(self.v+1)
        recursion_stack = [False]*(self.v+1)

        for i in range(1, self.v+1):
            if not visited[i]:
                if self.cycle_detection_util(i, visited, recursion_stack):
                    return True
        return False

    #
    # Utility function for topological sort
    #
    def topological_sort_util(self, node, visited, st):
        visited[node] = True

        for adj in self.d[node]:
            if not visited[adj]:
                self.topological_sort_util(adj, visited, st)

        st.append(node)

    #
    # Topological sorting for Directed Acyclic Graph (DAG) is a linear
    # ordering of vertices such that for every directed edge uv, vertex
    # u comes before v in the ordering. Topological Sorting for a graph
    # is not possible if the graph is not a DAG.
    #
    # Problem solved using TS
    # https://www.geeksforgeeks.org/given-sorted-dictionary-find-precedence-characters/ 
    #
    # T(n)- O(V+E)
    #
    def topological_sort(self):
        visited = [False]*(self.v+1)
        st = []

        for i in range(1, self.v+1):
            if not visited[i]:
                self.topological_sort_util(i, visited, st)

        while len(st) > 0:
            print st[-1],
            st.pop()


def main():
    v, e = map(int, raw_input().split())
    g = Graph(v, e)
    for i in range(e):
        a, b = map(int, raw_input().split())
        g.add_edge(a, b)
    g.topological_sort()


if __name__ == "__main__":
    main()
