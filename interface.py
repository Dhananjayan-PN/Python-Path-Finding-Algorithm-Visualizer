import pygame


class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Grid:
    def __init__(self, side, nodes):
        self.side = side
        self.nodes = nodes


class Interface:
    def __init__(self, grid):
        self.gridSize = gridSize

    def start(self):
        print("Initializing user interface...")


gridSize = 16
nodes = []
for i in range(gridSize):
    nodeRow = [Node(i, j) for j in range(gridSize)]
    nodes.insert(0, nodeRow)
grid = Grid(gridSize, nodes)
interface = Interface(grid)
interface.start()

pygame.init()
screen = pygame.display.set_mode([1200, 800])
pygame.display.set_caption("Path FInding Algorithm Visualizer")
icon = pygame.image.load('d_icon.ico')
pygame.display.set_icon(icon)
screen.fill((0, 0, 0))
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)
    pygame.display.flip()

pygame.quit()
