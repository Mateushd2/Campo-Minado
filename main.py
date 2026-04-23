from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys

# Configurações globais do tabuleiro
TAMANHO_GRID = 10

def inicializa():
    """Configurações de renderização e luz"""
    glClearColor(0.1, 0.1, 0.1, 1.0) # Fundo cinza escuro
    glEnable(GL_DEPTH_TEST)          # Habilita o teste de profundidade (essencial para 3D)

def desenha_eixos():
    """Desenha os eixos X, Y, Z para orientação no desenvolvimento"""
    glBegin(GL_LINES)
    # Eixo X (Vermelho)
    glColor3f(1.0, 0.0, 0.0)
    glVertex3f(0, 0, 0); glVertex3f(5, 0, 0)
    # Eixo Y (Verde)
    glColor3f(0.0, 1.0, 0.0)
    glVertex3f(0, 0, 0); glVertex3f(0, 5, 0)
    # Eixo Z (Azul)
    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(0, 0, 0); glVertex3f(0, 0, 5)
    glEnd()

def display():
    """Função principal de desenho"""
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    # --- CONFIGURAÇÃO DA CÂMERA (SRU) ---
    # Posicionamos a câmera no alto (15), olhando para o centro do tabuleiro (5,0,5)
    gluLookAt(12, 15, 12,  # Posição da câmera (Olho)
              5, 0, 5,     # Para onde a câmera olha (Alvo)
              0, 1, 0)     # Vetor UP (Cima é o eixo Y)

    desenha_eixos()
    
    # Próxima Task: Aqui entrará o laço de repetição do tabuleiro (Task 3.1)

    glutSwapBuffers()

def reshape(w, h):
    """Ajusta a perspectiva quando a janela é redimensionada"""
    if h == 0: h = 1
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    # Define o campo de visão (FOV), aspecto, e planos de corte (Near/Far)
    gluPerspective(45, w/h, 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(800, 600)
    glutCreateWindow(b"Campo Minado 3D - Projeto Pedagogico")
    
    inicializa()
    
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    
    print("Projeto iniciado! Use o mouse para fechar a janela.")
    glutMainLoop()

if __name__ == "__main__":
    main()