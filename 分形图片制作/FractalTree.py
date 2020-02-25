import pygame
import math

def game_initialize(tuple_model):
    pygame.init()
    window = pygame.display.set_mode(tuple_model)
    pygame.display.set_caption("fractal tree")
    screen = pygame.display.get_surface()
    return window, screen


window, screen = game_initialize((600, 600))

# x1,y1为熟的根节点的启动， angle是节点到根节点距离与投影的角度，depth是深度
def drawTree(x1, y1, angle, depth):
    if depth:
        x2 = x1 + int(math.cos(math.radians(angle)) * depth * 10)
        y2 = y1 + int(math.sin(math.radians(angle)) * depth * 10)
        pygame.draw.line(screen, (255, 255, 255), (x1, y1), (x2, y2), 2)
        drawTree(x2, y2, angle-20, depth-1)
        drawTree(x2, y2, angle+20, depth-1)

def input(event):
    if event.type == pygame.QUIT:
        exit(0)


if __name__ == '__main__':
    drawTree(300, 550, -90, 9)
    # 页面不关闭
    pygame.display.flip()
    while True:
        input(pygame.event.wait())

