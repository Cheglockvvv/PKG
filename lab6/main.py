import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

vertices = (
    (0, 0, 2),
    (0, 0, 0),
    (0.83, 0, 2),
    (0.83, 0, 0),
    (1.17, 0, 1.67),
    (1.17, 0, 0.33),
    (1.17, 0, 1.17),
    (1.17, 0, 0.83),
    (0.83, 0, 1),
    (0, 0.5, 2),
    (0, 0.5, 0),
    (0.83, 0.5, 2),
    (0.83, 0.5, 0),
    (1.17, 0.5, 1.67),
    (1.17, 0.5, 0.33),
    (1.17, 0.5, 1.17),
    (1.17, 0.5, 0.83),
    (0.83, 0.5, 1),
    (0.33, 0, 1.67),
    (0.83, 0, 1.67),
    (1, 0, 1.5),
    (1, 0, 1.33),
    (0.83, 0, 1.16),
    (0.33, 0, 1.16),
    (0.33, 0, 0.83),
    (0.83, 0, 0.83),
    (1, 0, 0.66),
    (1, 0, 0.5),
    (0.83, 0, 0.33),
    (0.33, 0, 0.33),
    (0.33, 0.5, 1.67),
    (0.83, 0.5, 1.67),
    (1, 0.5, 1.5),
    (1, 0.5, 1.33),
    (0.83, 0.5, 1.16),
    (0.33, 0.5, 1.16),
    (0.33, 0.5, 0.83),
    (0.83, 0.5, 0.83),
    (1, 0.5, 0.66),
    (1, 0.5, 0.5),
    (0.83, 0.5, 0.33),
    (0.33, 0.5, 0.33)
)

edges = (
    (0, 1),
    (0, 2),
    (1, 3),
    (2, 4),
    (3, 5),
    (4, 6),
    (5, 7),
    (7, 8),
    (6, 8),
    (9, 10),
    (9, 11),
    (10, 12),
    (11, 13),
    (12, 14),
    (13, 15),
    (14, 16),
    (16, 17),
    (15, 17),
    (0, 9),
    (2, 11),
    (1, 10),
    (3, 12),
    (5, 14),
    (4, 13),
    (6, 15),
    (7, 16),
    (8, 17),
    (18, 19),
    (19, 20),
    (20, 21),
    (21, 22),
    (22, 23),
    (23, 18),
    (24, 25),
    (25, 26),
    (26, 27),
    (27, 28),
    (28, 29),
    (24, 29),
    (30, 31),
    (31, 32),
    (32, 33),
    (33, 34),
    (34, 35),
    (30, 35),
    (36, 37),
    (37, 38),
    (38, 39),
    (39, 40),
    (40, 41),
    (36, 41),
    (18, 30),
    (19, 31),
    (20, 32),
    (21, 33),
    (22, 34),
    (23, 35),
    (24, 36),
    (25, 37),
    (26, 38),
    (27, 39),
    (28, 40),
    (29, 41)
)

def draw_axes():
    glBegin(GL_LINES)
    glColor3f(2, 0, 0)  # X-axis (Red)
    glVertex3f(-2, 0, 0)
    glVertex3f(2, 0, 0)
    glColor3f(0, 2, 0)  # Y-axis (Green)
    glVertex3f(0, -2, 0)
    glVertex3f(0, 2, 0)
    glColor3f(0, 0, 2)  # Z-axis (Blue)
    glVertex3f(0, 0, -2)
    glVertex3f(0, 0, 2)
    glEnd()

def B():
    glColor3f(1, 1, 1)
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0, 0, -7)

    clock = pygame.time.Clock()
    mouse_prev_pos = None
    scale_factor = 1.0
    translate_speed = 0.1

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button pressed
                    mouse_prev_pos = pygame.mouse.get_pos()
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:  # Left mouse button released
                    mouse_prev_pos = None
            elif event.type == pygame.MOUSEMOTION and mouse_prev_pos:
                x, y = event.pos
                dx, dy = x - mouse_prev_pos[0], y - mouse_prev_pos[1]
                mouse_prev_pos = (x, y)

                sensitivity = 0.2  # Adjust rotation sensitivity here
                glRotatef(dy * sensitivity, 1, 0, 0)
                glRotatef(dx * sensitivity, 0, 1, 0)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:  # "SPACE" key pressed
                    scale_factor += 0.1
                elif event.key == pygame.K_LSHIFT:  # "LSHIFT" key pressed
                    scale_factor -= 0.1
                    if scale_factor < 0.1:
                        scale_factor = 0.1
                elif event.key == pygame.K_a:  # Left arrow key pressed
                    glTranslatef(-translate_speed, 0, 0)
                elif event.key == pygame.K_d:  # Right arrow key pressed
                    glTranslatef(translate_speed, 0, 0)
                elif event.key == pygame.K_s:  # Page Up key pressed
                    glTranslatef(0, 0, translate_speed)
                elif event.key == pygame.K_w:  # Page Down key pressed
                    glTranslatef(0, 0, -translate_speed)
                elif event.key == pygame.K_x:  # "x" key pressed
                    glRotatef(30, 1, 0, 0)  # Rotate around X-axis
                elif event.key == pygame.K_y:  # "y" key pressed
                    glRotatef(30, 0, 1, 0)  # Rotate around Y-axis
                elif event.key == pygame.K_z:  # "z" key pressed
                    glRotatef(30, 0, 0, 1)  # Rotate around Z-axis

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        
        glPushMatrix()  # Сохраняем текущую матрицу
        glScalef(scale_factor, scale_factor, scale_factor)  # Масштабирование
        B()
        glPopMatrix()  # Восстанавливаем матрицу перед вращением и перемещением

        draw_axes()
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
