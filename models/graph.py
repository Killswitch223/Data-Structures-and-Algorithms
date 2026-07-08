class WarehouseGraph:
    def __init__(self):
        self.adjacency_list = {}

    def load_from_file(self, filepath="data/warehouse_map.txt"):
        """Parses the text database into a graph structure."""
        try:
            with open(filepath, "r", encoding="utf-8") as file:
                for line in file:
                    if not line.strip():
                        continue
                    zone, neighbors = line.strip().split(":")
                    self.adjacency_list[zone] = neighbors.split(",")
            print(f"Successfully loaded layout configuration from {filepath}.")
        except FileNotFoundError:
            print(f"Error: Map database file '{filepath}' not found.")

    def get_neighbors(self, zone):
        return self.adjacency_list.get(zone, [])
