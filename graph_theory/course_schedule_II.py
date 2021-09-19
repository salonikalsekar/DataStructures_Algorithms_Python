class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        result = [0] * numCourses

        if numCourses == 0:
            return result

        if not prerequisites or len(prerequisites) == 0:
            result = [i for i in range(numCourses)]
            return result

        nodependencies = []
        indegree = [0] * numCourses

        for pre in prerequisites:
            indegree[pre[0]] += 1

        for i in range(len(indegree)):
            if indegree[i] == 0:
                nodependencies.append(i)

        if not nodependencies:
            return []

        index = 0
        while nodependencies:
            course = nodependencies.pop(0)
            result[index] = course
            index += 1

            for pre in prerequisites:
                if course == pre[1]:
                    indegree[pre[0]] -= 1
                    if indegree[pre[0]] == 0:
                        nodependencies.append(pre[0])

        for i in indegree:
            if i != 0:
                return []

        return result