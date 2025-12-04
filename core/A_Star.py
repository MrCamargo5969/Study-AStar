import heapq
import networkx as nx

class A_Star():
    def __init__(self, graph):
        self.graph = graph

    def heuristic(self, node, goal):
        return abs(self.graph.nodes[node]['weight'] - self.graph.nodes[goal]['weight'])
    
    def search(self, start, goal):
        open_set = []
        heapq.heappush(open_set, (0, start))

        g_score = {n: float('inf') for n in self.graph.nodes}
        g_score[start] = 0

        f_score = {n: float('inf') for n in self.graph.nodes}
        f_score[start] = self.heuristic(start, goal)

        came_from = {}

        while open_set:
            _, current = heapq.heappop(open_set)
            if current == goal:
                return self.reconstruct_path(came_from, current)
            for neighbor in self.graph.neighbors(current):
                tentative_g = g_score[current] + 1

                if tentative_g < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g
                    f_score[neighbor] = g_score[neighbor] + self.heuristic(neighbor, goal)
                    heapq.heappush(open_set, (f_score[neighbor], neighbor))
        return None
    
    def reconstruct_path(self, came_from, current):
        path = [current]
        while current in came_from:
            current = came_from[current]
            path.append(current)
        return list(reversed(path))
