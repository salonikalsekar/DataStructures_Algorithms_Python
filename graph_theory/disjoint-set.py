

def union(x, y):
    rootX = find(x)
    rootY = find(y)
    print(rootX)
    print(rootY)
    if rootX != rootY:
        if rank[rootX] > rank[rootY]:
            root[rootY] = rootX
        elif rank[rootX] < rank[rootY]:
            root[rootX] = rootY
        else:
            root[rootY] = rootX
            rank[rootX] += 1

def find(x):
    if x == root[x]:
        return x

    return find(root[x])

def connected(x, y):
    return find(x) == find(y)



nodes = 5
arr = [[0, 1], [1, 2], [3, 4]]
rank = [1] * nodes
root = []
for i in range(nodes):
    root.append(i)

for i in arr:
    union(i[0], i[1])

print(connected(1, 3))

print(connected(1, 2))



