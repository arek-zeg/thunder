import graphics
from time import sleep
from random import paretovariate, randint
from playsound import playsound


'''
Application that tries to simulate thunder elements.

- simulate one thunder with 3+ (max 10, randomized, loop 'for') segments, from top to bottom - okey
- refactor -> create class - okey
- add ground, clouds - okey


TODO:
add absolute paths to additional files
'''


class Thunder():
    def __init__(self, window: graphics.GraphWin):
        self.window = window
        self.segments = randint(2, 5)
        self.segmentHeight = round(window.getHeight() / self.segments)
        self.lineNumber = []
        x = 0
        # starting points
        self.pt1 = graphics.Point(
            randint(0, window.getWidth()),
            90)
        self.pt2 = graphics.Point(
            abs(randint(self.pt1.x - self.window.getWidth()/4,
                        self.pt1.x + self.window.getWidth()/4)),
            randint(2, self.segmentHeight))

        # draw next segments
        while True:
            self.draw_line(x)
            self.pt1 = self.pt2
            self.pt2Temp = self.pt2
            self.segmentHeight = randint(0.2 * window.getHeight(),
                                         0.8 * window.getHeight())
            self.pt2 = graphics.Point(
                abs(randint(self.pt1.x - self.window.getWidth()/4,
                            self.pt1.x + self.window.getWidth()/4)),
                randint(self.pt2Temp.y + 5, self.pt2Temp.y + self.segmentHeight))
            x += 1
            if self.pt2Temp.y >= 600:  # window.getHeight():
                break
            print(self.pt1, self.pt2)
            sleep(0.01)

    def draw_line(self, x):
        self.lineNumber.append(graphics.Line(self.pt1, self.pt2))
        self.lineNumber[x].setWidth((self.window.getHeight()/70)-x)
        self.lineNumber[x].setFill('yellow')
        self.lineNumber[x].draw(self.window)

    def undraw_thunder(self):
        for i in self.lineNumber:
            i.undraw()


def storm_segment(repetitions, window):
    thunder = []
    for i in range(0, repetitions):
        sleep(1)
        myImageFlash = graphics.Image(graphics.Point(
            740, 400), "d://vsc-python//thunder//3.png")
        myImageFlash.draw(winMain)
        sleep(0.3)
        myImageFlash.undraw()
        thunder.append(Thunder(window))
    sleep(2)
    for i in range(0, repetitions):
        thunder[i].undraw_thunder()


def main():

    myImage = graphics.Image(graphics.Point(
        740, 400), "d://vsc-python//thunder//2.png")
    myImage.draw(winMain)

    while True:
        playsound('d://vsc-python//thunder//thunder1.mp3', block=False)
        storm_segment(3, winMain)
        text1 = graphics.Text(graphics.Point(
            winMain.getWidth()/2, 40), 'Click anywhere to close.')
        text1.setTextColor('white')
        text1.draw(winMain)

        sleep(2)
        text1.undraw()
        if winMain.checkMouse() != None:
            break


winMain = graphics.GraphWin(height=800, width=1400, title='Thunder')
winMain.setBackground('black')

main()
winMain.close()
