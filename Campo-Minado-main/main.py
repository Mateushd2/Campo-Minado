from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys
# Importamos as modelagens que criamos no outro arquivo
from models import desenha_cubo, desenha_mina

def inicializa():
    glClearColor(0.1, 0.1, 0.1, 1.0)
    glEnable(GL_DEPTH_TEST) # Fundamental para o cubo não parecer "transparente"

def desenha_eixos():
    glBegin(GL_LINES)
    glColor3f(1,0,0); glVertex3f(0,0,0); glVertex3f(5,0,0) # X
    glColor3f(0,1,0); glVertex3f(0,0,0); glVertex3f(0,5,0) # Y
    glColor3f(0,0,1); glVertex3f(0,0,0); glVertex3f(0,0,5) # Z
    glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    # Câmera configurada para visão diagonal do grid
    gluLookAt(12, 15, 12, 5, 0, 5, 0, 1, 0)

    desenha_eixos()

    # TESTE DA TASK 1.2: Desenhando um cubo posicionado
    glPushMatrix()
    glTranslatef(5, 0.5, 5) # Eleva 0.5 para ficar "em cima" do plano zero
    desenha_cubo()
    glPopMatrix()

    # TESTE DA TASK 1.3: Desenhando uma mina ao lado
    glPushMatrix()
    glTranslatef(7, 0.5, 5)
    desenha_mina()
    glPopMatrix()

    glutSwapBuffers()

def reshape(w, h):
    if h == 0: h = 1
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, w/h, 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(800, 600)
    glutCreateWindow(b"Campo Minado 3D - Task 1.1 e 1.2")
    inicializa()
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutMainLoop()

if __name__ == "__main__":
    main()