class DisjointUnionSets:
    def __init__(self, n):
        self.rank = [0] * n
        self.parent = list(range(n))

    def find(self, i):
        if self.parent[i] != i:   # if i is not the root
            self.parent[i] = self.find(self.parent[i])  # path compression
        return self.parent[i]

    
    def unionSets(self, x, y):
        xRoot = self.find(x)
        yRoot = self.find(y)

        if xRoot == yRoot:
            return
        
        #Union by Rank
        if self.rank[xRoot] < self.rank[yRoot]:
            self.parent[xRoot] = yRoot
        elif self.rank[yRoot] < self.rank[xRoot]:
            self.parent[yRoot] = xRoot
        else:
            self.parent[yRoot] = xRoot
            self.rank[xRoot] += 1


if __name__ == '__main__':

    n = 5 # Let there be 5 persons with ids 0, 1, 2, 3, and 4
    dus = DisjointUnionSets(n)

    dus.unionSets(0, 2) # 0 is a friend of 2
    dus.unionSets(4, 2) # 4 is a friend of 2
    dus.unionSets(3, 1) # 3 is a friend of 1

    # Check if 4 is a friend of 0
    if dus.find(4) == dus.find(0):
        print('Yes')
    else:
        print('No')

    # Check if 1 is a friend of 0
    if dus.find(1) == dus.find(0):
        print('Yes')
    else:
        print('No')
        