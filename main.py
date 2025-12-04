from core.GrafoMaker import GrafoMaker
from core.A_Star import A_Star

import random

lista_A_F = [chr(c) for c in range(ord('A'), ord('F') + 1)]
lista_A_Z = [chr(c) for c in range(ord('A'), ord('Z') + 1)]

def main():
    G = GrafoMaker()
    for v in lista_A_Z:
        G.add_node(v, weight=random.randint(1, 20))
        # G.draw()
    
    # edges = [('A', 'B'), ('A', 'C'), ('B', 'D'), ('C', 'D'), ('D', 'E'), ('E', 'F')]
    edges = [
    ('A', 'M'), ('A', 'F'), ('B', 'Q'), ('C', 'T'), ('D', 'A'), ('E', 'Z'),
    
    ('F', 'K'), ('F', 'R'), ('G', 'B'), ('H', 'L'), ('H', 'X'), ('I', 'N'),
    ('J', 'G'), ('K', 'S'), ('L', 'P'), ('M', 'D'), ('N', 'E'), ('O', 'C'),
    ('P', 'Y'), ('Q', 'J'), ('R', 'V'), ('S', 'I'), ('T', 'H'), ('U', 'O'),
    ('V', 'F'), ('W', 'U'), ('X', 'B'), ('Y', 'A'), ('Z', 'L'), ('C', 'V'),
    ('D', 'W'), ('G', 'X'), ('H', 'Q'), ('J', 'R'), ('M', 'S'), ('N', 'T')]

    for u, v in edges:
        G.add_edge(u, v)
        # G.draw()
    
    astar = A_Star(G.grafo)
    path = astar.search('A', 'Z')

    G.animate_path(path, delay=0.5)
    G.hold()

    nodes, adj_matrix = G.adjacency_matrix()
    print("Matriz de Adjacência:")
    G.show(nodes, adj_matrix, item_type="Matriz")
    print()
    nodes, weights = G.matrix_with_weights()
    print("Pesos dos Vértices:")
    G.show(nodes, weights, item_type="Pesos")





if __name__ == "__main__":
    main()