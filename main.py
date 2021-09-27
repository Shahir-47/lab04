#snowThem.py, a graphics program
#Shahir & Maia

from graphics import *

def draw_eyes(eX, eY, eRadius, eWindow):
	for i in range (2) :
		eye = Circle(Point((eX-eRadius) + (eRadius*0.7)+(i * 0.6 * eRadius),eY + (0.275*eRadius)), 0.1 * eRadius)
		eye.setFill(color_rgb(0, 0, 0))
		eye.setOutline(color_rgb(0, 0, 0))
		eye.draw(eWindow)
		draw_nose(eX, eY, eRadius, eWindow)

def draw_nose(nX, nY, nRadius, nWindow):
	nose = Polygon(Point(nX - (0.2 * nRadius), nY), Point(nX + (0.2 * nRadius), nY), Point(nX, nY - (0.5 * nRadius)))
	nose.setFill(color_rgb(255, 165, 0))
	nose.setOutline(color_rgb(255, 165, 0))
	nose.draw(nWindow)



def drawBG(width, height, color, window):
		background = Rectangle(Point(0, 0),Point(width, height))
		background.setFill(color)
		background.setOutline(color)
		background.draw(window)


def drawCirc(x, y, radius, color, window):
	 head = Circle(Point(x,y), radius)
	 head.setFill(color)
	 head.setOutline(color)
	 head.draw(window)
	 bodyCircle(x, y, radius, color, window)

def bodyCircle(x, y, radius, color, window):
	for i in range(1, 3):
		head = Circle(Point(x, y - (i * 2 * radius)), radius + (radius * 0.3 * i))
		head.setFill(color)
		head.setOutline(color)
		head.draw(window)

	draw_eyes(x, y, radius, window)



def hill(width, height, color, window):
	snowHill = Polygon(Point(0, 0), Point(width, 0), Point(0, height))
	snowHill.setFill(color)
	snowHill.setOutline(color)
	snowHill.draw(window)
	head = drawCirc(startX, startY, headRadius, headColor, snowWind)

headRadius = 20
startX = 200
startY = 200
headColor = color_rgb(200, 200, 200)
maxHeight = 500
maxWidth = 500
bgColor = color_rgb(190, 255, 255)
hillColor = color_rgb(255, 255, 255)

snowWind = GraphWin("Winter is coming", maxHeight, 500)
snowWind.setCoords(0, 0, maxHeight, 500)

blueBackground = drawBG(maxWidth, maxHeight, bgColor, snowWind)
drawCirc(startX, startY, headRadius, headColor, snowWind)

snowWind.getMouse()
snowWind.close()