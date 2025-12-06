import sys
import random
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas

from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton,
    QLabel, QSpinBox, QComboBox, QFrame
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont

from core.GrafoMaker import GrafoMaker
from core.A_Star import A_Star

# =========================
# GUI TOTALMENTE REVISADA
# =========================
class AStarGUI(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("A* Visualizer - AAA UI")
        self.setGeometry(200, 100, 1200, 700)
        self.setStyleSheet("background-color: #121212; color: white;")

        self.grafo = None
        self.astar = None

        # LAYOUT PRINCIPAL
        main = QHBoxLayout()
        self.setLayout(main)

        # =========================
        # PAINEL ESQUERDO (CONTROLES)
        # =========================
        left = QVBoxLayout()
        left.setContentsMargins(30, 30, 30, 30)
        left.setSpacing(25)
        main.addLayout(left, 2)

        title = QLabel("A* Pathfinding Visualizer")
        title.setFont(QFont("Segoe UI", 26, QFont.Weight.Bold))
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        left.addWidget(title)

        # INPUTS
        row1 = QHBoxLayout()
        left.addLayout(row1)

        self.spin_vertices = QSpinBox()
        self.spin_vertices.setRange(2, 26)
        self.spin_vertices.setValue(10)
        self.style_input(self.spin_vertices)
        row1.addWidget(self.labeled_box("Vértices", self.spin_vertices))

        self.spin_arestas = QSpinBox()
        self.spin_arestas.setRange(1, 200)
        self.spin_arestas.setValue(15)
        self.style_input(self.spin_arestas)
        row1.addWidget(self.labeled_box("Arestas", self.spin_arestas))

        btn_criar = self.button("Criar Grafo", self.criar_grafo)
        left.addWidget(btn_criar)

        row2 = QHBoxLayout()
        left.addLayout(row2)

        self.combo_origem = QComboBox()
        self.style_input(self.combo_origem)
        row2.addWidget(self.labeled_box("Origem", self.combo_origem))

        self.combo_destino = QComboBox()
        self.style_input(self.combo_destino)
        row2.addWidget(self.labeled_box("Destino", self.combo_destino))

        btn_astar = self.button("Executar A*", self.run_astar)
        left.addWidget(btn_astar)

        # CAMINHO TEXTO
        self.label_caminho = QLabel("")
        self.label_caminho.setFont(QFont("Segoe UI", 14))
        left.addWidget(self.label_caminho)

        # =========================
        # PAINEL DIREITO (GRAFO)
        # =========================
        self.fig, self.ax = plt.subplots(figsize=(6, 5))
        self.fig.patch.set_facecolor('#121212')
        self.ax.set_facecolor('#121212')
        self.canvas = FigureCanvas(self.fig)
        main.addWidget(self.canvas, 4)

    # -----------------
    # UI HELPERS
    # -----------------
    def labeled_box(self, text, widget):
        frame = QFrame()
        layout = QVBoxLayout()
        label = QLabel(text)
        label.setFont(QFont("Segoe UI", 13))
        layout.addWidget(label)
        layout.addWidget(widget)
        frame.setLayout(layout)
        return frame

    def style_input(self, widget):
        widget.setStyleSheet("background-color: #1e1e1e; padding: 6px; border-radius: 6px;")

    def button(self, text, func):
        btn = QPushButton(text)
        btn.setFont(QFont("Segoe UI", 12))
        btn.setStyleSheet(
            "background-color: #333333; padding: 10px; border-radius: 8px;"
        )
        btn.clicked.connect(func)
        return btn

    # -----------------
    # GRAFO
    # -----------------
    def criar_grafo(self):
        qtd_vertices = self.spin_vertices.value()
        qtd_arestas = self.spin_arestas.value()

        letras = [chr(c) for c in range(ord('A'), ord('A') + qtd_vertices)]

        G = GrafoMaker()

        for v in letras:
            G.add_node(v, weight=random.randint(1, 20))

        for _ in range(qtd_arestas):
            u, v = random.sample(letras, 2)
            G.add_edge(u, v)

        self.grafo = G
        self.astar = A_Star(G.grafo)

        self.combo_origem.clear()
        self.combo_destino.clear()
        self.combo_origem.addItems(letras)
        self.combo_destino.addItems(letras)

        self.draw_graph()
        self.label_caminho.setText("")

    # -----------------
    # DESENHO EMBUTIDO DO GRAFO
    # -----------------
    def draw_graph(self):
        self.ax.clear()
        pos = nx.spring_layout(self.grafo.grafo, seed=42)
        labels = {n: f"{n}(w={self.grafo.grafo.nodes[n]['weight']})" for n in self.grafo.grafo.nodes}

        nx.draw(
            self.grafo.grafo, pos, ax=self.ax,
            with_labels=True, labels=labels,
            node_color="#888888", edge_color="#555555",
            node_size=700, font_size=8
        )

        self.ax.set_title("Grafo", color="white")
        self.canvas.draw()

    # -----------------
    # ANIMAÇÃO EMBUTIDA
    # -----------------
    def animate_graph(self, path):
        import numpy as np
        pos = nx.spring_layout(self.grafo.grafo, seed=42)

        # cores neon estilo shader
        def neon(color_base, intensity):
            return (color_base[0] * intensity, color_base[1] * intensity, color_base[2] * intensity)

        red = (1.0, 0.2, 0.2)
        green = (0.2, 1.0, 0.4)
        gray = (0.5, 0.5, 0.5)

        for i, current in enumerate(path):
            for fade in np.linspace(0.2, 1.0, 10):  # animação suave
                self.ax.clear()
                colors = []
                for n in self.grafo.grafo.nodes:
                    if n == current:
                        colors.append(neon(red, fade))
                    elif n in path[:i]:
                        colors.append(neon(green, fade))
                    else:
                        colors.append(neon(gray, 0.6))

                nx.draw(
                    self.grafo.grafo, pos, ax=self.ax,
                    node_color=colors, edge_color="#555555",
                    with_labels=True, node_size=700, font_size=8
                )

                self.ax.set_title(f"Visitando {current}", color="white")
                self.canvas.draw()
                QApplication.processEvents()

    # -----------------
    # EXECUTAR A*
    # -----------------
    def run_astar(self):
        if not self.grafo:
            return

        origem = self.combo_origem.currentText()
        destino = self.combo_destino.currentText()

        path = self.astar.search(origem, destino)
        if not path:
            self.label_caminho.setText("Nenhum caminho encontrado.")
            return

        caminho_formatado = " → ".join(path)
        self.label_caminho.setText(f"Caminho: {caminho_formatado}")

        self.animate_graph(path)


# =========================
# MAIN
# =========================
if __name__ == "__main__":
    app = QApplication(sys.argv)
    gui = AStarGUI()
    gui.show()
    sys.exit(app.exec())
