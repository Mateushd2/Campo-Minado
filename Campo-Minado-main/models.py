from OpenGL.GL import *

def desenha_cubo():
    """
    Task 1.2: Modelagem de um cubo unitário (1x1x1) via vértices.
    As cores diferentes em cada face ajudam na percepção de profundidade.
    """
    glBegin(GL_QUADS)
    
    # Face Superior (Verde)
    glColor3f(0.0, 0.7, 0.0)
    glVertex3f( 0.5,  0.5, -0.5); glVertex3f(-0.5,  0.5, -0.5)
    glVertex3f(-0.5,  0.5,  0.5); glVertex3f( 0.5,  0.5,  0.5)

    # Face Inferior (Cinza Escuro)
    glColor3f(0.2, 0.2, 0.2)
    glVertex3f( 0.5, -0.5,  0.5); glVertex3f(-0.5, -0.5,  0.5)
    glVertex3f(-0.5, -0.5, -0.5); glVertex3f( 0.5, -0.5, -0.5)

    # Face Frontal (Vermelho)
    glColor3f(0.7, 0.0, 0.0)
    glVertex3f( 0.5,  0.5,  0.5); glVertex3f(-0.5,  0.5,  0.5)
    glVertex3f(-0.5, -0.5,  0.5); glVertex3f( 0.5, -0.5,  0.5)

    # Face Traseira (Amarelo)
    glColor3f(0.7, 0.7, 0.0)
    glVertex3f( 0.5, -0.5, -0.5); glVertex3f(-0.5, -0.5, -0.5)
    glVertex3f(-0.5,  0.5, -0.5); glVertex3f( 0.5,  0.5, -0.5)

    # Face Esquerda (Azul)
    glColor3f(0.0, 0.0, 0.7)
    glVertex3f(-0.5,  0.5,  0.5); glVertex3f(-0.5,  0.5, -0.5)
    glVertex3f(-0.5, -0.5, -0.5); glVertex3f(-0.5, -0.5,  0.5)

    # Face Direita (Magenta)
    glColor3f(0.7, 0.0, 0.7)
    glVertex3f( 0.5,  0.5, -0.5); glVertex3f( 0.5,  0.5,  0.5)
    glVertex3f( 0.5, -0.5,  0.5); glVertex3f( 0.5, -0.5, -0.5)
    
    glEnd()

def desenha_mina():
    """Task 1.3: Mina (Octaedro) - Geometria de diamante."""
    glColor3f(0.0, 0.0, 0.0) 
    glBegin(GL_TRIANGLES)
    # Pirâmide Superior
    glVertex3f( 0.0,  0.4,  0.0); glVertex3f(-0.3,  0.0,  0.3); glVertex3f( 0.3,  0.0,  0.3)
    glVertex3f( 0.0,  0.4,  0.0); glVertex3f( 0.3,  0.0,  0.3); glVertex3f( 0.3,  0.0, -0.3)
    glVertex3f( 0.0,  0.4,  0.0); glVertex3f( 0.3,  0.0, -0.3); glVertex3f(-0.3,  0.0, -0.3)
    glVertex3f( 0.0,  0.4,  0.0); glVertex3f(-0.3,  0.0, -0.3); glVertex3f(-0.3,  0.0,  0.3)
    # Pirâmide Inferior
    glVertex3f( 0.0, -0.4,  0.0); glVertex3f( 0.3,  0.0,  0.3); glVertex3f(-0.3,  0.0,  0.3)
    glVertex3f( 0.0, -0.4,  0.0); glVertex3f( 0.3,  0.0, -0.3); glVertex3f( 0.3,  0.0,  0.3)
    glVertex3f( 0.0, -0.4,  0.0); glVertex3f(-0.3,  0.0, -0.3); glVertex3f( 0.3,  0.0, -0.3)
    glVertex3f( 0.0, -0.4,  0.0); glVertex3f(-0.3,  0.0,  0.3); glVertex3f(-0.3,  0.0, -0.3)
    glEnd()