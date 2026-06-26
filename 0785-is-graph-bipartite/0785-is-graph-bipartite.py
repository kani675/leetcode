class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        n = len(graph)
        color = [0] * n  
        
        for i in range(n):
            if color[i] != 0:
                continue
                
            queue = deque([i])
            color[i] = 1  
            
            while queue:
                curr = queue.popleft()
                
                for neighbor in graph[curr]:
                    if color[neighbor] == 0:
                        color[neighbor] = -color[curr]
                        queue.append(neighbor)
                    elif color[neighbor] == color[curr]:
                        return False
                        
        return True
