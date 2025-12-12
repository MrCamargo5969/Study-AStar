A* Pathfinding Visualizer

Visualizador interativo do algoritmo A* desenvolvido em Python, com interface baseada em PyQt6 e renderização gráfica utilizando NetworkX e Matplotlib. O sistema permite a construção de grafos aleatórios, configuração de vértices e arestas, definição de origem e destino e visualização animada da execução do algoritmo.

1. Objetivo

Este projeto tem como finalidade demonstrar, de forma prática e visual, o funcionamento do algoritmo A*, abrangendo:

Estruturação e manipulação de grafos.

Aplicação da heurística no processo de busca.

Visualização dos passos percorridos pelo algoritmo.

Integração entre lógica algorítmica e interface gráfica.

2. Tecnologias Utilizadas

Python 3.10+

PyQt6 — Interface gráfica

NetworkX — Criação e manipulação de grafos

Matplotlib — Renderização e animação

NumPy — Operações numéricas

Tabulate — Exibição tabular de dados no terminal

3. Estrutura do Projeto
/core
 ├── A_Star.py        # Implementação do algoritmo A*
 ├── GrafoMaker.py    # Manipulação e geração de grafos
gui.py                # Interface gráfica principal

4. Componentes Principais
4.1. A_Star.py

Implementa o algoritmo A*, utilizando:

Fila de prioridade (heapq);

Funções de custo g_score e f_score;

Construção do caminho final via tabela came_from;

Heurística baseada na diferença absoluta entre pesos dos nós.

A implementação prioriza clareza e demonstrabilidade em ambiente acadêmico.

4.2. GrafoMaker.py

Responsável por:

Criação, modificação e remoção de nós e arestas;

Atribuição de pesos aos vértices;

Geração da matriz de adjacência e matriz de pesos;

Renderização do grafo utilizando Matplotlib;

Animação da trajetória calculada pelo algoritmo.

O grafo utiliza layout spring_layout, que produz uma distribuição espacial estável e visualmente compreensível.

4.3. gui.py

Interface principal construída em PyQt6, com:

Definição de quantidade de vértices e arestas;

Geração automática de grafos;

Seleção de nó inicial (origem) e nó objetivo (destino);

Execução do A* com animação incremental do caminho encontrado;

Exibição textual da rota final.

A interface apresenta estilo escuro (dark theme) e prioriza organização visual e acessibilidade.

5. Instalação
5.1. Dependências

Instale as bibliotecas obrigatórias:

pip install pyqt6 networkx matplotlib numpy tabulate

5.2. Estrutura recomendada do diretório
seu_projeto/
 ├── gui.py
 └── core/
      ├── A_Star.py
      └── GrafoMaker.py

6. Execução

Para iniciar o visualizador:

python gui.py

7. Funcionamento Geral

O usuário define o número de vértices e arestas.

O sistema gera um grafo não direcionado com pesos aleatórios.

A interface permite a escolha de origem e destino.

O algoritmo A* é executado sobre o grafo.

A animação mostra progressivamente os nós visitados.

O caminho final obtido é exibido em formato textual e visual.

8. Exemplo de Saída
Caminho: V2 → V5 → V8 → V7

9. Finalidade Educacional

Este projeto é adequado para:

Apresentações acadêmicas sobre algoritmos de busca;

Estudos de heurísticas e estruturas de dados;

Demonstrações de integração entre algoritmos e interface gráfica;

Ambientes de aprendizagem em disciplinas de Grafos e Inteligência Artificial.