# Campo Minado 3D - PyOpenGL

Este é um projeto de desenvolvimento de um **Campo Minado Tridimensional** com fins pedagógicos, desenvolvido para a disciplina de Computação Gráfica. O foco principal é a aplicação prática de conceitos de modelagem geométrica e transformações no espaço 3D.

## Objetivo Pedagógico
O jogo foi projetado para estimular o raciocínio lógico e a percepção espacial. Ao transpor o clássico Campo Minado para o ambiente 3D, o usuário interage diretamente com conceitos de coordenadas cartesianas e transformações geométricas.

## Requisitos Técnicos Atendidos
O projeto cumpre integralmente os requisitos obrigatórios:

* **Modelagem por Vértices:** 5 objetos exclusivos criados manualmente (sem modelos prontos):
    1.  **Célula (Cubo):** Bloco base do grid.
    2.  **Mina (Octaedro):** Elemento de perigo modelado com triângulos.
    3.  **Bandeira:** Composta por haste e face triangular.
    4.  **Seletor:** Cursor de navegação (ex: cubo em wireframe ou pirâmide).
    5.  **Painel de Status:** Base para exibição de informações.
* **Transformações Geométricas:**
    * **Translação:** Posicionamento dos cubos no Grid e movimentação do seletor (**SRU**).
    * **Rotação:** Animação das minas (giro contínuo) e feedback visual.
    * **Escala:** Alteração de tamanho para destacar a célula selecionada.
* **Interatividade:** Suporte a comandos via Teclado e Mouse.
* **Tecnologia:** Implementado em **Python** utilizando a biblioteca **PyOpenGL**.

## Controles
- **Setas (↑, ↓, ←, →):** Movimentam o seletor pelo grid (Translação).
- **Enter / Barra de Espaço:** Revela a célula selecionada.
- **Tecla F:** Coloca/Remove uma bandeira.
- **Mouse:** Interação direta com os elementos do cenário.

## Como Executar o Projeto

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/Mateushd2/Campo-Minado.git](https://github.com/Mateushd2/Campo-Minado.git)
    ```

2.  **Instale as dependências:**
    Certifique-se de ter o Python instalado. É necessário instalar a biblioteca PyOpenGL:
    ```bash
    pip install PyOpenGL PyOpenGL_accelerate
    ```

3.  **Execute o jogo:**
    ```bash
    python src/main.py
    ```

## Estrutura de Pastas Sugerida
* `/src`: Código fonte (.py).
* `/assets`: (Opcional) Texturas ou sons.
* `/docs`: Relatório técnico (Modelagem, SRO, SRU).

## Time
* **Mateus Assis**
* **Patrícia Caselani**
* **Rael Rosenau**

---
*Gerenciado via Azure DevOps utilizando metodologias ágeis.*
