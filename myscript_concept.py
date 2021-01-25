import graphics
from time import sleep
from random import randint
from playsound import playsound


'''
Application that tries to simulate thunder elements.

- simulate one thunder with 3+ (max 10, randomized, loop 'for') segments, from top to bottom - okey
- refactor -> create class *
- add ground, clouds
'''


def draw_line(lineNumber, pt1, pt2, window, lineWidth, x):
    lineNumber.append(graphics.Line(pt1, pt2))
    lineNumber[x].setWidth(lineWidth)
    lineNumber[x].setFill('yellow')
    lineNumber[x].draw(window)


def thunder_draw():
    segments = randint(2, 10)
    segmentHeight = round(winMain.getHeight() / segments)
    lineNumber = []
    x = 0
    # starting points
    pt1 = graphics.Point(
        randint(0, winMain.getWidth()),
        0)
    pt2 = graphics.Point(
        abs(randint(pt1.x - segmentHeight, pt1.x + segmentHeight)),
        randint(2, segmentHeight))

    # draw next segments
    while True:
        draw_line(lineNumber, pt1, pt2, winMain, (winMain.getWidth()/50)-x, x)
        pt1 = pt2
        pt2Temp = pt2
        segmentHeight = randint(0.2 * winMain.getHeight(),
                                0.8 * winMain.getHeight())
        pt2 = graphics.Point(
            abs(randint(pt1.x - segmentHeight, pt1.x + segmentHeight)),
            randint(pt2Temp.y + 5, pt2Temp.y + segmentHeight))
        x += 1
        if pt2Temp.y >= winMain.getHeight():
            break
        print(pt1, pt2)
        sleep(0.01)



winMain = graphics.GraphWin(height=600, width=600, title='Thunder')
winMain.setBackground('black')


sleep(1)
winMain.setBackground('yellow')
sleep(0.1)
#playsound('d://vsc-python//thunder//thunder1.mp3', block=False)
winMain.setBackground('black')
thunder_draw()
winMain.setBackground('yellow')
sleep(0.1)
winMain.setBackground('black')
thunder_draw()


'''
'''

winMain.getMouse()
winMain.close()
