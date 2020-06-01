from tkinter import *
import pygame
import platform
import os
import sys


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


def resetGrid():
    algToUse.set('')
    selectingStart = False
    startSelected = False
    selectingEnd = False
    endSelected = False
    showStart = False
    screen.fill((0, 0, 0))
    for row in rects:
        for rect in row:
            pygame.draw.rect(screen, CYAN, rect, 1)


gridSize = 20
blockSize = 35
CYAN = (21, 244, 238)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
algorithms = ['Depth-First Search']
nodes = []
rects = []
for i in range(gridSize):
    nodeRow = [Node(i, j) for j in range(gridSize)]
    nodes.append(nodeRow)
    rectRow = [
        pygame.Rect(i * blockSize, j * blockSize, blockSize, blockSize)
        for j in range(gridSize)
    ]
    rects.append(rectRow)
root = Tk()
root.iconbitmap(r'd_icon.ico')
root.geometry('1100x750+200+100')
root.title('Path Finding Algorithm Visualizer')
root.configure(background='black')
root.resizable(0, 0)
embed = Frame(root, width=720, height=750, bg='black')
embed.grid(row=0, column=0, columnspan=20, rowspan=20, padx=20, pady=25)
os.environ['SDL_WINDOWID'] = str(embed.winfo_id())
if platform.system == "Windows":
    os.environ['SDL_VIDEODRIVER'] = 'windib'
pygame.init()
screen = pygame.display.set_mode([800, 800])
screen.fill((0, 0, 0))

algo = Label(root,
             text='Select an Algorithm: ',
             font=('Agency FB', 18),
             bg='black',
             fg='cyan')
algo.grid(row=2, column=20, columnspan=2)
algToUse = StringVar(root)
algToUse.set('')
dropMenu = OptionMenu(root, algToUse, *algorithms)
dropMenu.config(bg="black")
dropMenu.config(fg="cyan")
dropMenu["menu"].config(bg="black")
dropMenu["menu"].config(fg="cyan")
dropMenu.grid(row=2, column=22, columnspan=2)
reset = Button(root, text='Reset', bg='black', fg='cyan', command=resetGrid)
reset.grid(row=10, column=21, columnspan=4)
for row in rects:
    for rect in row:
        pygame.draw.rect(screen, CYAN, rect, 1)
running = True
selectingStart = False
startSelected = False
selectingEnd = False
endSelected = False
showStart = False
global startLabel
while running:
    if algToUse.get() and not startSelected:
        startLabel = Label(root,
                           text='Select a start point!',
                           font=('Agency FB', 18),
                           bg='black',
                           fg='cyan')
        startLabel.grid(row=3, column=20, columnspan=4)
        selectingStart = True

    if selectingEnd:
        endLabel = Label(root,
                         text='Select an end point!',
                         font=('Agency FB', 18),
                         bg='black',
                         fg='cyan')
        endLabel.grid(row=4, column=20, columnspan=4)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break
        elif event.type == pygame.MOUSEBUTTONDOWN and selectingStart:
            startX, startY = event.pos[0] // 35, event.pos[1] // 35
            try:
                pygame.draw.rect(screen, GREEN, rects[startX][startY], 0)
                selectingStart = False
                startSelected = True
                selectingEnd = True
            except:
                pass
        elif event.type == pygame.MOUSEBUTTONDOWN and selectingEnd:
            endX, endY = event.pos[0] // 35, event.pos[1] // 35
            try:
                pygame.draw.rect(screen, RED, rects[endX][endY], 0)
                selectingEnd = False
                endSelected = True
                showStart = True
            except:
                pass

    root.update()
    pygame.display.update()

root.destroy()
pygame.quit()
