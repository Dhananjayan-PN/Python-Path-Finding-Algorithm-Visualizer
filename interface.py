from tkinter import *
import pygame
import platform
import os


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


gridSize = 20
blockSize = 40
CYAN = (21, 244, 238)
nodes = []
for i in range(gridSize):
    nodeRow = [Node(i, j) for j in range(gridSize)]
    nodes.insert(0, nodeRow)
grid = Grid(gridSize, nodes)
interface = Interface(grid)
interface.start()

root = Tk()
embed = Frame(root, width=1280,
              height=800)  #creates embed frame for pygame window
embed.grid(columnspan=(600), rowspan=500)  # Adds grid
embed.pack(side=LEFT)  #packs window to the left
# buttonwin = Frame(root, width=75, height=500)
# buttonwin.pack(side=LEFT)
os.environ['SDL_WINDOWID'] = str(embed.winfo_id())
if platform.system == "Windows":
    os.environ['SDL_VIDEODRIVER'] = 'windib'
pygame.init()
screen = pygame.display.set_mode([800, 800])
pygame.display.set_caption("Path FInding Algorithm Visualizer")
icon = pygame.image.load('d_icon.ico')
pygame.display.set_icon(icon)
screen.fill((0, 0, 0))
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        for row in grid.nodes:
            for node in row:
                rect = pygame.Rect(node.x * blockSize, node.y * blockSize,
                                   blockSize, blockSize)
                pygame.draw.rect(screen, CYAN, rect, 1)
    pygame.display.update()
    root.update()

pygame.quit()
