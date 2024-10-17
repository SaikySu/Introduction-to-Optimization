import networkx as nx
import matplotlib.pyplot as plt

def create_graph():
    edgelist = [(5,6),(5,9),(6,7),(6,10),(7,8),(7,11),
                (8,12),(1,2),(1,5),(2,3),(2,6),(3,4),
                (3,7),(4,8),(9,10),(9,13),(10,11),
                (10,14),(11,12),(11,15),(13,14),(14,15),
                (15,16),(12,16)]
    G = nx.Graph(edgelist)
    return G
def generate_grid_2d_graph_dataset(grid_size):
    cols = [(i * grid_size + j, i * grid_size + j + 1) for i in range(grid_size) for j in range(grid_size-1)]
    rows = [(j*grid_size+i,j*grid_size+i+grid_size) for i in range(grid_size) for j in range(grid_size-1)]
    edgeList = cols + rows
    return nx.Graph(edgeList)
G = generate_grid_2d_graph_dataset(10)
nx.draw(G, with_labels=True)
plt.show()
