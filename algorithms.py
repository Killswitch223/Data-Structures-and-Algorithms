from collections import deque

class Router:
    @staticmethod
    def find_shortest_route(graph, start, target):
        """Executes a Breadth-First Search to return the shortest path layer."""
        if start not in graph.adjacency_list or target not in graph.adjacency_list:
            return None
            
        queue = deque([[start]])
        visited = set()
        
        while queue:
            path = queue.popleft()
            current_zone = path[-1]
            
            if current_zone == target:
                return path
                
            if current_zone not in visited:
                for neighbor in graph.get_neighbors(current_zone):
                    new_path = list(path)
                    new_path.append(neighbor)
                    queue.append(new_path)
                visited.add(current_zone)
        return None
