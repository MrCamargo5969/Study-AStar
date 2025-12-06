import sys
import random
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton,
    QLabel, QSpinBox, QComboBox, QMessageBox, QFrame
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
import networkx as nx
import matplotlib.pyplot as plt
from core.GrafoMaker import GrafoMaker
from core.A_Star import A_Star

class AStarGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("A* Visualizer - AAA UI")
        self.setGeometry(200, 100, 800, 500)
        self.setStyleSheet("background-color: #1e1e1e; color: white;")

        self.grafo = None
        self.astar = None

        main = QVBoxLayout()
        main.setContentsMargins(30, 30, 30, 30)
        main.setSpacing(25)

        title = QLabel("A* Pathfinding Visualizer")
        title.setFont(QFont("Segoe UI", 26, QFont.Weight.Bold))
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main.addWidget(title)

        row1 = QHBoxLayout()
        row1.setSpacing(20)

        self.spin_vertices = QSpinBox()
        self.spin_vertices.setRange(2, 26)
        self.spin_vertices.setValue(10)
        self.stylize_spin(self.spin_vertices)
        row1.addWidget(self.labeled_box("Vértices", self.spin_vertices))

        self.spin_arestas = QSpinBox()
        self.spin_arestas.setRange(1, 200)
        self.spin_arestas.setValue(15)
        self.stylize_spin(self.spin_arestas)
        row1.addWidget(self.labeled_box("Arestas", self.spin_arestas))

        btn_criar = self.button("Criar Grafo", self.criar_grafo)
        row1.addWidget(btn_criar)

        main.addLayout(row1)

        row2 = QHBoxLayout()
        row2.setSpacing(20)

        self.combo_origem = QComboBox()
        self.stylize_combo(self.combo_origem)
        row2.addWidget(self.labeled_box("Origem", self.combo_origem))

        self.combo_destino = QComboBox()
        self.stylize_combo(self.combo_destino)
        row2.addWidget(self.labeled_box("Destino", self.combo_destino))

        btn_astar = self.button("Executar A*", self.run_astar)
        row2.addWidget(btn_astar)

        main.addLayout(row2)

        self.setLayout(main)

    def labeled_box(self, label_text, widget):
        frame = QFrame()
        frame.setStyleSheet("background: transparent;")
        box = QVBoxLayout(frame)

        label = QLabel(label_text)
        label.setFont(QFont("Segoe UI", 13))

        box.addWidget(label)
        box.addWidget(widget)

        frame.setLayout(box)
        return frame

    def button(self, text, func):
        btn = QPushButton(text)
        btn.setFont(QFont("Segoe UI", 12))
        btn.setStyleSheet("background-color: #3a3a3a; padding: 10px; border-radius: 8px;")
        btn.clicked.connect(func)
        return btn

    def stylize_spin(self, spin):
        spin.setStyleSheet("background-color: #2b2b2b; padding: 5px; color: white; border-radius: 6px;")

    def stylize_combo(self, combo):
        combo.setStyleSheet("background-color: #2b2b2b; padding: 5px; color: white; border-radius: 6px;")

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

        G.draw()

        

    def run_astar(self):
        if not self.grafo:
            
            return

        origem = self.combo_origem.currentText()
        destino = self.combo_destino.currentText()

        path = self.astar.search(origem, destino)
        if not path:
            
            return

        self.grafo.animate_path(path)

        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    gui = AStarGUI()
    gui.show()
    sys.exit(app.exec())
