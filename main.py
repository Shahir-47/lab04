#snowThem.py, a graphics program
#Shahir & Maia

from graphics import *


def drawBG(width, height, color, window):
		background = Rectangle(Point(0, 0),Point(width, height))
		background.setFill(color)
		background.setOutline(color)
		background.draw(window)

def hill(width, height, color, window):
	snowHill = Polygon(Point(0, 0), Point(width, 0), Point(0, height))
	snowHill.setFill(color)
	snowHill.setOutline(color)
	snowHill.draw(window)
		
maxHeight = 500
maxWidth = 500
bgColor = color_rgb(190, 255, 255)
hillColor = color_rgb(255, 255, 255)

snowWind = GraphWin("Winter is coming", maxHeight, 500)
snowWind.setCoords(0, 0, maxHeight, 500)

blueBackground = drawBG(maxWidth, maxHeight, bgColor, snowWind)

hillSide = hill(maxWidth, maxHeight, hillColor, snowWind)

snowWind.getMouse()
snowWind.close()