from collections import deque

def find_shortest_path(warehouse_graph, start_zone, target_zone):
    # Queue stores paths, not just nodes
    queue = deque([[start_zone]])
    visited = set()
    
    while queue:
        path = queue.popleft()
        current_zone = path[-1]
        
        if current_zone == target_zone:
            return path
            
        if current_zone not in visited:
            for neighbor in warehouse_graph.get(current_zone, []):
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)
            visited.add(current_zone)
            
    return None

if __name__ == "__main__":
    # Graph representing warehouse zones connected by aisles
    warehouse = {
        'Receiving': ['Aisle_1', 'Aisle_2'],
        'Aisle_1': ['Receiving', 'Electronics', 'Aisle_3'],
        'Aisle_2': ['Receiving', 'Clothing'],
        'Electronics': ['Aisle_1', 'Shipping'],
        'Clothing': ['Aisle_2', 'Shipping'],
        'Aisle_3': ['Aisle_1', 'Heavy_Goods'],
        'Heavy_Goods': ['Aisle_3', 'Shipping'],
        'Shipping': ['Electronics', 'Clothing', 'Heavy_Goods']
    }
    
    start = 'Receiving'
    target = 'Heavy_Goods'
    shortest_route = find_shortest_path(warehouse, start, target)
    
    print(f"Shortest path from {start} to {target}:")
    print(" -> ".join(shortest_route))
