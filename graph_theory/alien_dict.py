class Solution:
    def alienOrder(self, words: List[str]) -> str:
        if len(words) == 0:
            return ""

        indegrees = {}
        graph = {}
        output = []
        for word in words:
            for ch in word:
                indegrees[ch] = 0
                graph[ch] = []

        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]
            for j in range(min(len(word1), len(word2))):
                if word1[j] != word2[j]:
                    graph[word1[j]].append(word2[j])
                    indegrees[word2[j]] += 1
                    break
            else:  # Check that second word isn't a prefix of first word.
                if len(word2) < len(word1):
                    return ""

        nodependencies = []
        for k, v in indegrees.items():
            if v == 0:
                nodependencies.append(k)

        while nodependencies:
            ch = nodependencies.pop(0)
            output.append(ch)

            for i in graph[ch]:
                indegrees[i] -= 1
                if indegrees[i] == 0:
                    nodependencies.append(i)

        if len(output) < len(indegrees):
            return ""

        return ''.join(output)