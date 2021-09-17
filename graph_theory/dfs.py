# def dfs(graph):
#
#     visited = set('A')
#     stack = ['A']
#     res = []
#     while stack:
#         curr = stack.pop()
#         res.append(curr)
#
#         for i in graph[curr]:
#             if i not in visited:
#                 visited.add(i)
#                 stack.append(i)
#
#     return res
#


def dfs(graph, visited, node, res):
    if node:
        res.append(node)

        for i in graph[node]:
            if i not in visited:
                visited.add(i)
                dfs(graph, visited, i, res)

    return res

graph = {
  'A' : ['B','C'],
  'B' : ['D', 'E'],
  'C' : ['F'],
  'D' : [],
  'E' : ['F'],
  'F' : []
}
visited = set()
res = []
print(dfs(graph, visited, 'A', res))