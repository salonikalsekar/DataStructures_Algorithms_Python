
def path(mat):
     q = []
     q.append((0, set().add(0)))
     count = 0
     while q:
         curr, vis = q.pop()
         print(len(mat[curr]))
         for i in range(len(mat[curr])):
             print(i)
             if mat[curr][i] == 1 and i not in vis:
                 vis.append(i)
                 q.append(i, vis)
             if mat[curr][i] == 9:
                 count += 1
                 q.append(i, vis)

     print(count)

mat = [[1,1,0], [0,1,1], [0,9,1]]
path(mat)