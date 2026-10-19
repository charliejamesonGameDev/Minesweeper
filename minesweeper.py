import pygame
import sys
import random

pygame.init()

HEIGHT = 10
WIDTH = 10

res = (WIDTH*32,HEIGHT*32)

screen = pygame.display.set_mode(res)

colour = (255,255,255)

width = screen.get_width()

height = screen.get_height()

revealed = []
flagged = []
exploded = []
dead = False
generated = False

board = []

def prepare(p):
    for i in range(WIDTH):
        p.append([])
        for j in range(HEIGHT):
            p[i].append(0)

prepare(board)

def addMines(Pboard,row,column):
    counter = 0
    while counter <= (WIDTH * HEIGHT)//6:
        randomR = random.randint(0,WIDTH-1)
        randomC = random.randint(0,HEIGHT-1)
        if randomR > row+1 or randomR < row-1 and randomC > column+1 or randomC < column-1:
            Pboard[randomR][randomC] = 9
            counter += 1

def checkSurroundings(pinput,Pboard):
    row = pinput[0]
    column = pinput[1]
    value = 0
    for i in range(3):
        for j in range(3):
            targetR = row + i - 1
            targetC = column + j - 1 
            if (0 <= targetR < WIDTH) and (0 <= targetC < HEIGHT) and not (i == 1 and j == 1):
                if Pboard[targetR][targetC] == 9:
                    value += 1
    return value

def calcAll(Pboard):
    for row in range(WIDTH):
        for column in range(HEIGHT):
            if Pboard[row][column] != 9:
                Pboard[row][column] = checkSurroundings([row,column],Pboard)

def checkWin():
    print(len(revealed))
    if len(revealed) == (WIDTH * HEIGHT) - ((WIDTH * HEIGHT)//6) and len(revealed) >= 1:
        return True
    else:
        return False

def showBoard(Pboard):
    for i in range(len(Pboard)):
        for j in range(len(Pboard[i])):
            tile = [i,j]
            pygame.draw.rect(screen, ("#000000"),
                                       [i*32, j*32, 32, 32], 0)
            imp = pygame.image.load("images\minesweeperT.png").convert()
            screen.blit(imp, (i*32+1 ,j*32+1))         
            if tile in revealed:
                if Pboard[i][j] == 9:
                    imp = pygame.image.load("images\minesweeperM.png").convert()
                    screen.blit(imp, (i*32+1 ,j*32+1))
                elif Pboard[i][j] == 1:
                    imp = pygame.image.load("images\minesweeper1.png").convert()
                    screen.blit(imp, (i*32+1 ,j*32+1))
                elif Pboard[i][j] == 2:
                    imp = pygame.image.load("images\minesweeper2.png").convert()
                    screen.blit(imp, (i*32+1 ,j*32+1))
                elif Pboard[i][j] == 3:
                    imp = pygame.image.load("images\minesweeper3.png").convert()
                    screen.blit(imp, (i*32+1 ,j*32+1))
                elif Pboard[i][j] == 4:
                    imp = pygame.image.load("images\minesweeper4.png").convert()
                    screen.blit(imp, (i*32+1 ,j*32+1))
                elif Pboard[i][j] == 5:
                    imp = pygame.image.load("images\minesweeper5.png").convert()
                    screen.blit(imp, (i*32+1 ,j*32+1))
                elif Pboard[i][j] == 6:
                    imp = pygame.image.load("images\minesweeper6.png").convert()
                    screen.blit(imp, (i*32+1 ,j*32+1))
                elif Pboard[i][j] == 7:
                    imp = pygame.image.load("images\minesweeper7.png").convert()
                    screen.blit(imp, (i*32+1 ,j*32+1))
                elif Pboard[i][j] == 8:
                    imp = pygame.image.load("images\minesweeper8.png").convert()
                    screen.blit(imp, (i*32+1 ,j*32+1))
                elif Pboard[i][j] == 0:
                    imp = pygame.image.load("images\minesweeper0.png").convert()
                    screen.blit(imp, (i*32+1 ,j*32+1))
                elif Pboard[i][j] == 10:
                    imp = pygame.image.load("images\minesweeperR.png").convert()
                    screen.blit(imp, (i*32+1 ,j*32+1))
            elif tile in flagged:
                imp = pygame.image.load("images\minesweeperF.png").convert()
                screen.blit(imp, (i*32+1 ,j*32+1))

def reveal(row, column):
    if board[row][column] == 0:
        revealed.append([row,column])
        for i in range(3):
            for j in range(3):
                targetR = row + i - 1
                targetC = column + j - 1 
                if (0 <= targetR < WIDTH) and (0 <= targetC < HEIGHT) and not (i == 1 and j == 1) and ([targetR,targetC] not in revealed):
                    reveal(targetR,targetC)
    else:
        if [row,column] not in revealed:
            revealed.append([row,column])

def die(row,column):
    global dead
    dead = True
    for row in range(len(board)):
        for tile in range(len(board[row])):
            if board[row][tile] == 9:
                revealed.append([row,tile])
    return 10

mouse = pygame.mouse.get_pos()

quitting = False

while not quitting:
    
    for ev in pygame.event.get():
        
        if ev.type == pygame.QUIT:
            pygame.quit()

        #checks if a mouse is clicked
        if ev.type == pygame.MOUSEBUTTONDOWN and not dead:
            if not generated:
                addMines(board,(mouse[0]//32), (mouse[1]//32))
                calcAll(board)
                generated = True
            if board[mouse[0]//32][mouse[1]//32] == 9:
                board[mouse[0]//32][mouse[1]//32] = die((mouse[0]//32), (mouse[1]//32))
            else:
                reveal((mouse[0]//32), (mouse[1]//32))

        if ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_ESCAPE:
                quitting = True
            elif ev.key == pygame.K_f and not dead:
                flagged.append([mouse[0]//32,mouse[1]//32])

    screen.fill("#FFFFFF")
    showBoard(board)
    mouse = pygame.mouse.get_pos()   
    pygame.display.update()
pygame.quit()