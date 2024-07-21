import networkx as nx

def create_graph():
    G = nx.Graph()
    # Add edges with weights representing distances
    G.add_edge('A', 'B', weight=1)
    G.add_edge('B', 'C', weight=2)
    G.add_edge('A', 'C', weight=2)
    G.add_edge('C', 'D', weight=1)
    return G

def find_shortest_path(graph, start, end):
    return nx.shortest_path(graph, source=start, target=end, weight='weight')

# Example usage
if __name__ == "__main__":
    G = create_graph()
    path = find_shortest_path(G, 'A', 'D')
    print("Shortest path:", path)
