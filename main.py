#snowThem.py, a graphics program
#Shahir & Maia

from graphics import *


def drawBG(width, height, color, window):
		background = Rectangle(Point(0, 0),Point(width, height))
		background.setFill(color)
		background.setOutline(color)
		background.draw(window)
		hillSide = hill(maxWidth, maxHeight, hillColor, snowWind)

def drawCirc(x, y, radius, color, window):
	 head = Circle(Point(x,y), radius)
	 head.setFill(color)
	 head.setOutline(color)
	 head.draw(window)


def hill(width, height, color, window):
	snowHill = Polygon(Point(0, 0), Point(width, 0), Point(0, height))
	snowHill.setFill(color)
	snowHill.setOutline(color)
	snowHill.draw(window)
	head = drawCirc(startX, startY, headRadius, headColor, snowWind)

headRadius = 6
startX = 20
startY = 480
headColor = color_rgb(200, 200, 200)
maxHeight = 500
maxWidth = 500
bgColor = color_rgb(190, 255, 255)
hillColor = color_rgb(255, 255, 255)

snowWind = GraphWin("Winter is coming", maxHeight, 500)
snowWind.setCoords(0, 0, maxHeight, 500)

blueBackground = drawBG(maxWidth, maxHeight, bgColor, snowWind)


snowWind.getMouse()
snowWind.close()