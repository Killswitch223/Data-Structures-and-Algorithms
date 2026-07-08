from models.graph import WarehouseGraph
from algorithms.pathfinder import Router

def main():
    # 1. Instantiate and load graph data
    warehouse_network = WarehouseGraph()
    warehouse_network.load_from_file()
    
    print("\n=== Warehouse Route Optimization System ===")
    start_zone = input("Enter worker starting zone (e.g., Receiving): ").strip()
    target_zone = input("Enter item target zone (e.g., Heavy_Goods): ").strip()
    
    # 2. Compute path
    route = Router.find_shortest_route(warehouse_network, start_zone, target_zone)
    
    # 3. Output results
    if route:
        print("\nOptimal Retrieval Route:")
        print(" ➔ ".join(route))
    else:
        print("\nRoute could not be calculated. Verify zone naming conventions.")

if __name__ == "__main__":
    main()
