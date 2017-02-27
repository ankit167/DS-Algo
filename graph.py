
class Graph:
    def __init__(self,v,e):
        self.v = v
        self.e = e
        self.d = {k: [] for k in range(1,v+1)}

    def insert(self,u,v):
        l = self.d.get(u)
        l.append(v)
        self.d[u] = l

    # If there is directed edge from vertex a to vertex b --> a knows b
    def knows(self,a,b):
        l = self.d[a]
        if len(l) > 0 and b in l:
            return True
        return False

    # Find the celebrity from a group of people.
    # A celebrity is a person who everyone knows, but he does not know anyone.
    # From a graph perspective, a celebrity vertex is a vertex with n-1
    # incoming edges and 0 outgoing edges.
    # T(n)- O(n). The other methods include- (i) Traversing the adjacency
    # list/matrix to  check indegree and outdegree values of all vertices
    # (ii) Divide and conquer (iii) Use stack. Refer gfg for these methods
    def celeb(self):
        l = list(self.d.keys())
        i,j = 0,len(l)-1
        while i < j:
            if self.knows(l[i],l[j]) is True:
                c = l[j]
                i += 1
            else:
                c = l[i]
                j -= 1
        for i in l:
            if i == c:
                continue
            if self.knows(c,i) is False and self.knows(i,c) is True:
                continue
            return -1
        return c


def main():
    v,e = list(map(int,raw_input().split()))
    g = Graph(v,e)
    for i in range(e):
        a,b = list(map(int,raw_input().split()))
        g.insert(a,b)
    print g.celeb()


if __name__ == "__main__":
    main()


#1 --> 3
#1 --> 2
#2 --> 3
#4 --> 3
#4 --> 5
#5 --> 1
#5 --> 3
#6 --> 3
