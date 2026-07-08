Markdown
# Warehouse Routing Optimizer 🏭🗺️

## Overview
A logistical simulation designed to find the most efficient path for retrieving inventory in a large storage facility. By representing the warehouse floor plan as a graph network, this project applies foundational data structures and algorithms to solve a practical routing problem. 

## Features
*   **Graph Representation:** Models warehouse zones and connecting aisles using an Adjacency List (Python Dictionaries).
*   **Breadth-First Search (BFS):** Implements a shortest-path algorithm to navigate from receiving docks to specific heavy goods or electronics aisles.
*   **Scalable Architecture:** Easily expandable to include weighted edges for travel time or distance (Dijkstra's Algorithm).

## Technologies Used
*   Python 3.x
*   `collections.deque` for optimized queue operations

## How to Run
1. Clone this repository.
2. Execute the routing script:
   ```bash
   python warehouse_router.py
