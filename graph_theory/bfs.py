def bfs(graph):

    visited = set('A')
    queue = ['A']
    res = []
    while queue:
        curr = queue.pop(0)
        res.append(curr)

        for i in graph[curr]:
            if i not in visited:
                visited.add(i)
                queue.append(i)

    return res

graph = {
  'A' : ['B','C'],
  'B' : ['D', 'E'],
  'C' : ['F'],
  'D' : [],
  'E' : ['F'],
  'F' : []
}

print(bfs(graph))