import networkx as nx
import numpy as np
from tabulate import tabulate
import matplotlib.pyplot as plt

class GrafoMaker:
    def __init__(self):
        self.grafo = nx.Graph()
# --------------------------------------------------------------
    def add_node(self, v, weight=0):
        self.grafo.add_node(v, weight=weight)
    
    def delete_node(self, v):
        self.grafo.remove_node(v)
    
    def change_node_weight(self, v, new_weight):
        if self.grafo.has_node(v):
            self.grafo[v]['weight'] = new_weight
        print(f"Aresta {v} não existe no grafo.")
    
# --------------------------------------------------------------
    def add_edge(self, u, v):
        self.grafo.add_edge(u, v)
    
    def delete_edge(self, u, v):
        self.grafo.remove_edge(u, v)
# --------------------------------------------------------------
    def adjacency_matrix(self):
        nodes = list(self.grafo.nodes)
        matrix = nx.to_numpy_array(self.grafo, nodelist=nodes, weight=None)
        return nodes, matrix

    def matrix_with_weights(self):
        nodes = list(self.grafo.nodes)
        pesos = np.array([self.grafo.nodes[n]['weight'] for n in nodes])
        return nodes, pesos
# --------------------------------------------------------------
    def show(self, nodes, matrix, item_type="Matriz"):
        if item_type == "Matriz":
            tabela = tabulate(matrix,
                            headers=nodes, 
                            showindex=nodes,
                            tablefmt="grid")
            print(tabela)
        elif item_type == "Pesos":
            matrix_list = [[row] for row in matrix]
            tabela = tabulate(matrix_list,
                            headers=[item_type],
                            showindex=nodes,
                            tablefmt="grid")
            print(tabela)
        else:
            print("Tipo de item desconhecido.")
# --------------------------------------------------------------
    def draw(self):
        plt.clf()
        pos = nx.spring_layout(self.grafo, seed=42)
        labels = {n: f"{n}\n(w={self.grafo.nodes[n]['weight']})"
                for n in self.grafo.nodes}
        nx.draw_networkx_nodes(self.grafo, pos, node_size=800)
        nx.draw_networkx_edges(self.grafo, pos)
        nx.draw_networkx_labels(self.grafo, pos, labels=labels, font_size=10)

        plt.title("Grafo Atual")
        plt.axis("off")
        plt.pause(0.5)
        plt.show(block=False)
    
    def hold(self):
        plt.show()
    
# --------------------------------------------------------------
    def animate_path(self, path, delay=0.7):
            pos = nx.spring_layout(self.grafo, seed=42)
            for i, current in enumerate(path):
                plt.clf()
                colors = []
                for n in self.grafo.nodes:
                    if n == current:
                        colors.append((1, 0.5, 0.5))
                    elif n in path[:i]:
                        colors.append("lightgreen")
                    else:
                        colors.append("lightgray")
                labels = {n: f"{n}\n(w={self.grafo.nodes[n]['weight']})"
                    for n in self.grafo.nodes}
                nx.draw_networkx_nodes(self.grafo, pos,
                    node_color=colors,
                    edgecolors="black",
                    node_size=900)
                nx.draw_networkx_edges(self.grafo, pos)
                nx.draw_networkx_labels(self.grafo, pos, labels=labels)
                plt.title(f"Passo {i+1}: Visitando {current}")
                plt.axis("off")
                plt.pause(delay)
