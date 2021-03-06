# Memory puzzle by Archimedes on 4-3=19
import random, pygame, sys
from pygame.locals import *

FPS = 30 # frames per second, the general speed of the program
WINDOWWIDTH = 640 # size of window's width in pixels
WINDOWHEIGHT = 480 # size of window's height in pixels
REVEALSPEED = 8 # speed boxes's sliding reveals and covers
BOXSIZE = 40 # size of box height and width in pixels
GAPSIZE = 10 # size of gap between boxes in pixels 
BOARDWIDTH = 10 # number of columns of icons
BOARDHEIGHT = 7 # number of rows of icons
assert (BOARDWIDTH* BOARDHEIGHT) % 2 == 0, 'Board needs to an even number of boxes for pairs of matches.'
XMARGIN = int((WINDOWWIDTH - (BOARDWIDTH * (BOXSIZE + GAPSIZE))) / 2)
YMARGIN = int((WINDOWHEIGHT - (BOARDHEIGHT * (BOXSIZE + GAPSIZE))) / 2)

#             R     G    B
GRAY       = (100, 100, 100)
NAVYBLUE   = ( 60,  60, 100)
WHITE      = (255  255, 255)
RED        = (255,   0,   0)
GREEN      = (  0  255,   0)
BLUE       = (  0,   0, 255)
YELLOW     = (255, 255,   0)
ORANGE     = (255, 128,   0)
PURPLE     = (255,  0,  255)
CYAN       = (  0, 255, 255)

BGCOLOR = NAVYBLUE
LIGHTBGCOLOR = GRAY
BOXCOLOR = WHITE
HIGHLIGHTCOLOR = BLUE

DONUT = 'donut'
SQUARE = 'square'
DIAMOND = 'diamond'
LINES = 'lines'
OVAL = 'oval'

ALLCOLORS = (RED, GREEN, BLUE, YELLOW, ORANGE, PURPLE, CYAN)
ALLSHAPES = (DONUT, SQUARE, DIAMOND, LINES, OVAL)
assert len(ALLCOLORS) * len(ALLSHAPES) * 2 >= BOARDWIDTH * BOARDHEIGHT, 'Board is too big for the number of shapes/colors defined.'

def main():
    global FPSCLOCK, DISPLAYSURF
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    mousex = 0
    mousey = 0
    pygame.display.set_caption('Memory Game')
    mainBoard = getRandomizedBoard()
    revealBoxes = generateRevealedBoxesData(False)
    firstSelection = None
    DISPLAYSURF.fill(BGCOLOR)
    startGameAnimation(mainBoard)

    while True:
        mouseClicked = False
        DISPLAYSURF.fill(BGCOLOR)
        drawBoard(mainBoard, revealedBoxes)
        for event in pygame.event.get():
                if event.type == QUIT or(event.type==KEYUP and K_ESCAPE):
                        pygame.quit()
                        sys.exit()
                elif event.type == MOUSEMOTION:
                        mousex, mousey = event.pos
                elif event.type == MOUSEBUTTONUP:
                        mousex, mousey = event.pos
                        mouseClicked =  True
        boxx, boxy = getBoxAtPixel(mousex,mousey)
        if boxx != None and boxy != None:
                if not revealBoxes[boxx][boxy]:
                        drawHighlightBox(boxx, boxy)
                if not revealBoxes[boxx][boxy] and mouseClicked:
                        revealBoxesAnimation(mainBoard, [(boxx, boxy)])
                        revealBoxes[boxx][boxy] = True
                        if firstSelection == None:
                                firstSelection = (boxx, boxy)
                        else:
                                icon1shape, icon1color = getShapeAndColor(mainBoard,firstSelection[0], firstSelection[1])
                                icon2shape, icon2color = getShapeAndColor(mainBoard, boxx, boxy)
                                if icon1shape != icon2shape or icon1color != icon2color:
                                        pygame.time.wait(100)
                                        coverBoxesAnimaition(mainBoard, [(firstSelection[0], firstSelection[1]), (boxx, boxy)])
                                        revealBoxes[firstSelection[0]][firstSelection[1]] = False
                                        revealBoxes[boxx][boxy] = False
                                        elif hasWon(revealBoxes):
                                                gameWonAnimation(mainBoard)
                                                pygame.time.wait(2000)
                                                mainBoard = getRandomizedBoard()
                                                revealBoxes = generateRevealedBoxesData(False)
                                                drawBoard(mainBoard, revealBoxes)
                                                pygame.display.update()
                                                pygame.time.wait(1000)
                 FPSCLOCK.tick.FPS
def generateRevealdBoxesData(val):
        revealBoxes = []
        for i in range(BOARDWIDTH):
                revealedBoxes.append([val]) * BOARDHEIGHT)
        return revealedBoxes
def getRandomizedBoard():
        
        icons = []
        for color in ALLCOLORS:
                for shape in ALLSHAPES:
                        icons.append((shape, color))
        random.shuffle(icons)
        numIconsUsed = int(BOARDWIDTH *BOARDHEIGHT /2)

        icons = icons:[:numIconsUsed] * 2
        random.shuffle(icons)
        board = []
        for x in range(BOARDWIDTH):
                column = []
                for y in range(BOARDHEIGHT):
                        column.append(icon[0])
                        del icons[0]
                        board.append(column)
        return board
def splitIntoGroupOf(groupSize, theList):
        result = []
        for i in range(0, len(theList), groupSize):
                resul.append(theList[i.i + groupSize])
                return result
def leftTopCoordsOfBox(boxx, boxy):
        left = boxx * (BOXSIZE + GAPSIZE) + XMARGIN
        top = boxy * (BOXSIZE + GAPSIZE) + YMARGIN
        return (left, top)


def getBoxAtPixel(x, y):
        for boxx in range(BOARDHEIGHT):
                left, top = leftTopCoordsOfBox(boxx, boxy)
                boxRect = pygame.Rect(left,top, BOXSIZE,BOXSIZE)
                if boxRect.collidepoint(x, y):
                        return (boxx, boxy)
                        return(None, None)
def drawIcon(shape, color, boxx, boxy):
        quarter = int(BOXSIZE * 0.25)
        half = int(BOXSIZE * 0.5)
        left, top = leftTopCoordsOfBox(boxx, boxy)
        if shape == DONUT:
                pygame.draw.circle(DISPLAYSURF, color, (left + half, top + half), half -5)
                pygame.draw.circle(DISPLAYSURF,BGCOLOR,(left + half, top + half), quarter -5)
        elif shape == SQUARE:
                pygame.draw.rect(DISPLAYSURF, color,(left + quarter, top + quarter,  BOXSIZE - half, BOXSIZE - half))
        elif shape == DIAMOND:
                pygame.draw.polygon(DISPLAYSURF, color,((left+ half, top), (left + BOXSIZE - 1 , top + half), (left + half, top + BOXSIZE - 1),(left, top + half)))
        elif shape == LINES:
                for i in range(0, BOXSIZE, 4):
                        pygame.draw.line(DISPLAYSURF, color, (left, top + i),(left + i),(left + i, top))
                        pygame.draw.line(DISPLAYSURF, color,(left + i, top + BOXSIZE - 1, (left + BOXSIZE - 1, top + i))
        elif shape == OVAL:
                pygame.draw.ellipse(DISPLAYSURF, color,(left, top + quarter, BOXSIZE, half))

def getShapeAndColor(board, boxx, boxy):
        return board[boxx][0], board[boxx][boxy][1]


def drawBoxCovers(board, boxes, coverage):
        for box in boxes:
                left, top = leftTopCoordsOfBox(box[0], box[1])
                pygame.draw.rec(DISPLAYSURF, BGCOLOR, (left,top, BOXSIZE, BOXSIZE))
                shape, color = getShapeAndColor(board, box[0], box[1])
                drawIcon(shape, color, box[0], box[1])
                if coverage > 0:
                        pygame.draw.rect(DISPLAYSURF, BOXCOLOR,(left, top, coverage, BOXSIZE))
        pygame.display.update()
        FPSCLOCK.tick(FPS)

def revealBoxesAnimatiion(board,boxesToReveal):

        for coverage in range(BOXSIZE, (-REVEALSPEED )- 1, - REVEALSPEED):
                drawBoxCovers(board, boxesToReveal, coverage)

def coverBoxesAnimaition(board, boxesToCover):

        for coverage in range(0, BOXSIZE + REVEALSPEED, REVEALSPEED):
                drawBoxCovers(board, board, boxesToCover, coverage)

def drawBoard(board, revealed):
        for boxx in range(BOARDWIDTH):
                for boxy in range(BOARDHEIGHT):
                        left, top = leftTopCoordsOfBox(boxx, boxy)
                        if not revealed[boxx][boxy]:
                                pygame.draw.rect(DISPLAYSURF, BOXCOLOR, (left, top, BOXSIZE, BOXSIE))
                        else:
                                shape, color = getShapeAndColor(board, boxx, boxy)
                                drawIcon(shape, color, boxx, boxy)
def startGameAnimation(board):

        coveredBoxes = generateRevealedBoxesData(False)
        boxes = []
        for x in range(BOARDWIDTH):
                for y in range(BOARDHEIGHT):
                        boxes.append( (x, y) )
                random.shuffle(boxes)
                boxGroups = splitIntoGroupOf(8, boxes)
                
                drawBoard(board, coveredBoxes)
                for boxGroup in boxGroups:
                        revealBoxesAnimatiion(board, boxGroup)
                        coverBoxesAnimaition(board, boxGroup)
                        
def gameWonAnimation(board):
        coveredBoxes = generateRevealedBoxesData(True)
        color1 = LIGHTBGCOLOR
        color2 = BGCOLOR
        for i in range(13):
                color1, color2 = color2, color1
                DISPLAYSURF.fill(color1)
                drawBoard(board, coveredBoxes)
                pygame.display.update()
                pygame.time.wait(300)
def hasWon(revealedBoxes):
        for i in revealedBoxes:
                if False in i:
                        return False
        return True



if __name__== '_main_':
        main()

        






                
                                

























                



                                        

                                                
                                        







                

        















