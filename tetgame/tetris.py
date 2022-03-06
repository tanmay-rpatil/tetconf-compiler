import random
import time
import pygame
pygame.init()
from pieces import *
from config import *



# Initialise Screen
screen = pygame.display.set_mode(screenSize)
pygame.display.set_caption('Tetris')
inAnimation = False
score = 0



#  Loading initial screen
def pre(state):
    for i in range(rows):
        state[i][0] = boundaryCell
        state[i][cols-1] = boundaryCell
    for i in range(cols):
        state[rows-1][i] = boundaryCell
    return



def makeColorLighter(color, amount):
    newColor = []
    for i in range(3):
        val = color[i] + (255-color[i])*(100 - amount)/100
        newColor.append(val)
    return newColor



def makeColorDarker(color, amount):
    newColor = []
    for i in range(3):
        val = color[i]*(100 - amount)/100
        newColor.append(val)
    return newColor



# Draw current game state
def draw(state):
    shadow = getDropShadow(state)
    for i in range(rows):
        for j in range(cols):
            if state[i][j][0] == emptyColor:
                rect = (blockSize*j, blockSize*i, blockSize, blockSize)
                pygame.draw.rect(screen, state[i][j][0], rect)
                pygame.draw.rect(screen, borderColor, rect, 1)
                continue

            # state[i][j] = (colors[random.randint(0,6)], state[i][j][1])  #masti

            rect = (blockSize*j+borderThickness, blockSize*i+borderThickness, blockSize-2*borderThickness, blockSize-2*borderThickness)
            pygame.draw.rect(screen, state[i][j][0], rect, 0)

            borderColorUp = makeColorLighter(state[i][j][0], 40)
            borderColorDown = makeColorDarker(state[i][j][0], 75)
            borderColorSide = makeColorDarker(state[i][j][0], 20)

            x1 = blockSize*j
            y1 = blockSize*i
            x2 = x1 + blockSize
            y2 = y1 + blockSize
            rectUp = [(x1,y1), (x2,y1), ((x1+x2)/2, (y1+y2)/2)]
            rectDown = [(x1,y2), (x2,y2), ((x1+x2)/2, (y1+y2)/2)]
            rectLeft = [(x1,y1), (x1,y2), ((x1+x2)/2, (y1+y2)/2)]
            rectRight = [(x2,y1), (x2,y2), ((x1+x2)/2, (y1+y2)/2)]
            pygame.draw.polygon(screen, borderColorUp, rectUp)
            pygame.draw.polygon(screen, borderColorDown, rectDown)
            pygame.draw.polygon(screen, borderColorSide, rectLeft)
            pygame.draw.polygon(screen, borderColorSide, rectRight)
            pygame.draw.rect(screen, state[i][j][0], rect)
            

    for square in shadow:
        if state[square[2]][square[3]] == emptyCell:
            rect = (blockSize*square[3], blockSize*square[2], blockSize, blockSize)
            color = makeColorDarker(state[square[0]][square[1]][0], 50)
            pygame.draw.rect(screen, color, rect, 2)
            # pygame.draw.rect(screen, borderColor, rect, 1)          




def addPiece(state, piece, hinge, color):
    x = cols//2 - 1
    for i in range(len(piece)):
        for j in range(len(piece)):
            if piece[i][j] == 0:
                continue
            if(state[i][x+j][0] != emptyColor):
                return False
            if hinge[i][j] == 1:
                state[i][x+j] = (color,2)
            else:
                state[i][x+j] = (color,1)
    return True



def checkRow(state):
    linesCleared = 0
    for i in range(rows-1):
        flag = 1
        for j in range(cols):
            if state[i][j] == emptyCell:
                flag=0
                break
        if flag:
            linesCleared += 1
            for ii in range(i-1, -1, -1):
                for j in range(1, cols-1):
                    state[ii+1][j] = state[ii][j]
                    state[ii][j] = emptyCell
    
    print('linesCleared' + str(linesCleared))
    global score
    score += points[linesCleared]



def solidify(state):
    for i in range(rows):
        for j in range(cols):
            state[i][j] = (state[i][j][0], 0)
    global inAnimation, score
    inAnimation = False
    score += 5
    checkRow(state)



def moveLeft(state):
    for i in range(rows):
        for j in range(cols):
            if state[i][j][1] > 0:
                if state[i][j-1][0] != emptyColor and state[i][j-1][1] == 0:
                    return

    for i in range(rows):
        for j in range(cols):
            if state[i][j][1] > 0:
                state[i][j-1] = state[i][j]
                state[i][j] = emptyCell



def moveRight(state):
    for i in range(rows):
        for j in range(cols):
            if state[i][j][1] > 0:
                if state[i][j+1][0] != emptyColor and state[i][j+1][1] == 0:
                    return

    for i in range(rows):
        for j in range(cols-1, 0, -1):
            if state[i][j][1] > 0:
                state[i][j+1] = state[i][j]
                state[i][j] = emptyCell

    return state



def moveDown(state):
    for i in range(rows):
        for j in range(cols):
            if state[i][j][1] > 0:
                if state[i+1][j][0] != emptyColor and state[i+1][j][1] == 0:
                    solidify(state)
                    return

    for i in range(rows-1, -1, -1):
        for j in range(cols):
            if state[i][j][1] > 0:
                state[i+1][j] = state[i][j]
                state[i][j] = emptyCell


  
def getDropShadow(state):
    drop = rows
    for j in range(cols):
        rd = rows
        for i in range(rows-1, -1, -1):
            if state[i][j][1] > 0:
                drop = min(drop, rd-i-1)
                break
            elif state[i][j] != emptyCell:
                rd = i

    newState = []
    for i in range(rows):
        for j in range(cols):
            if state[i][j][1] > 0:
                newState.append((i, j, i+drop, j))

    return newState



def hardDrop(state):
    # nextState = getDropShadow(state)
    # for move in nextState:
    #     state[move[2]][move[3]] = state[move[0]][move[1]]
    #     state[move[0]][move[1]] = emptyCell
    # solidify(state)
    while inAnimation:
        moveDown(state)



def rotatePiece(state):
    hinge = []
    for i in range(rows):
        for j in range(cols):
            if state[i][j][1] == 2:
                hinge.append((i,j))
    
    for h in hinge:
        flag = 0
        for i in range(rows):
            for j in range(cols):
                if state[i][j][1] > 0:
                    rx = h[0] + j-h[1]
                    ry = h[1] + h[0]-i
                    if rx not in range(rows) or ry not in range(cols):
                        flag = 1
                        break 
                    elif not (state[rx][ry][1] > 0 or state[rx][ry][0] == emptyColor):
                        flag = 1
                        break
            if flag:
                break

        if not flag:
            newPosition = []
            for i in range(rows):
                for j in range(cols):
                    if state[i][j][1] > 0:
                        rx = h[0] + j-h[1]
                        ry = h[1] + h[0]-i
                        newPosition.append((state[i][j], rx, ry))
                        state[i][j] = emptyCell

            for pos in newPosition:
                state[pos[1]][pos[2]] = pos[0]
            break

    return state



def playMove(move, state):
    # print(move)
    if move == 'U':
        rotatePiece(state)
    elif move == 'D':
        moveDown(state)
    elif move == 'L':
        moveLeft(state)
    elif move == 'R':
        moveRight(state)
    elif move == 'S':
        hardDrop(state)



def showScore():
    font1 = pygame.font.Font('freesansbold.ttf', fontSize)
    text1 = font1.render('Score', True, white)
    text1_rect = text1.get_rect()
    text2 = font1.render(str(score), True, white)
    text2_rect = text2.get_rect()
    text1_rect.center = (cols*blockSize + 100, 6*blockSize)
    text2_rect.center = (cols*blockSize + 100, 7*blockSize)
    screen.blit(text1, text1_rect);
    screen.blit(text2, text2_rect);


def main():
    state = [[emptyCell for _ in range(cols)] for _ in range(rows)]
    # print(len(state[0]))
    global inAnimation
    pre(state)
    start_time = time.time() 
    
    while True:
        for event in pygame.event.get():

            # quit
            if event.type == pygame.QUIT:
                quit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                quit()


            # move left
            if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                moveLeft(state)
                break


            # move right
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                moveRight(state)
                break


            # move left
            if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                moveDown(state)
                break

            # hard drop
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                hardDrop(state)
                break


            # rotate
            if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                rotatePiece(state)


        # Gravity
        if inAnimation:
            curr_time = time.time()
            if curr_time - start_time > speed:
                moveDown(state)
                start_time = curr_time


        # Load new piece
        if not inAnimation:
            ind = random.randint(0,6)
            color = random.choice(colors)
            if addPiece(state, pieces[ind], hinges[ind], color) == False:
                quit()
            inAnimation = True


        # Update Screen
        screen.fill(black)
        draw(state)
        showScore()
        pygame.display.update()
        pygame.time.delay(tickInterval)




def quit():
    pygame.quit()
    exit()



main()




# Things to Add:
# Start page
# Play Again screen
# Teleport down key
# Rotate piece
# Shadow down
# Delete filled row (preferably with a bit of animation)





