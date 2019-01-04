# Tarun Mandalapu 2016

from graphics import *
import math
from random import *

#Short method that checks if a number is between two others to make checking button presses on GUIs a bit more straightforward 
def isBet(lower, var, upper):
	if(lower > upper): #This is a stupid proofing for myself because I'm stupid sometimes
		holder = upper
		upper = lower
		lower = holder
	if(var < upper and var > lower):
		return True
	else:
		return False

#Gets user input and plugs into drawKC
def main():
	#Initializing window and coords
	gui = GraphWin("Koch's Fractal Grapher", 300, 200)
	gui.setCoords(-200, -200, 200, 200)
	gui.setBackground("gray95")
	#Line(Point(0,200), Point(0, -200)).draw(gui) #Line for formatting purposes

	#Gui Stuff
	title = Text(Point(0, 175), "Koch Curve Grapher");title.draw(gui)
	ul = Line(Point(-75, 155), Point(75, 155));ul.draw(gui)
	lvlt = Text(Point (-10, 100), "Desired Level:"); lvlt.draw(gui)
	lvlp = Entry(Point(80, 100), 2);lvlp.setText("5");lvlp.draw(gui)
	thetat = Text(Point(-42, 0), "Desired Theta Value:");thetat.draw(gui)
	thetap = Entry(Point(80, 0), 2);thetap.setText("60");thetap.draw(gui)
	drawclearb = Rectangle(Point(-27, -115), Point(29, -83));drawclearb.draw(gui)
	draw = Text(Point(0, -100), "Draw"); draw.draw(gui)
	clear = Text(Point(0, -100), "Clear")
	win = GraphWin("Koch's Snowflake", 600, 600)
	win.setCoords(-10, -10, 10, 10)
	win.setBackground("gray95")
	

	bp = 0 #keeping track of number of times draw/clear button has been pressed
	#Click collecting loop
	while(1):
		click = gui.getMouse();x = click.getX(); y = click.getY() #Get the user's mouseclick and initialize the coordinates
		#If it's the draw button, draw the curve using the user's inputs
		if(isBet(-27, x, 29) and isBet(-115, y, -83) & bp%2 == 0):
			draw.undraw()
			clear.undraw()
			clear.draw(gui)
			drawKC(win, int(lvlp.getText()), Point(-7, 3), int(thetap.getText()), 0, 14)
			drawKC(win, int(lvlp.getText()), Point(7, 3), int(thetap.getText()), 240, 14)
			drawKC(win, int(lvlp.getText()), Point(0, -9.1), int(thetap.getText()), 120, 14)
			sd = getSD(int(thetap.getText()))
			sdt = Text(Point(0, 8), ("similarity dimension: " + str(sd)[0:5]));sdt.draw(win) #this could be simplified
			per = getLength(1, int(lvlp.getText()), int(thetap.getText()))
			pert = Text(Point(0, 9), "Perimeter of Snowflake: " + str(per));pert.draw(win)

			bp += 1
		#If it's the clear button, clear the window and switch to the draw button
		elif(isBet(-27, x, 29) and isBet(-115, y, -83) & bp%2 != 0):
			clear.undraw()
			draw.undraw()
			draw.draw(gui)
			clearwin(win)
			bp += 1

#Very VERY lazy clear method, but it works :)
def clearwin(win):
	clearwindow = Rectangle(Point(-300, -300), Point(300, 300)); clearwindow.setFill("gray95") 
	clearwindow.draw(win)
#draws a line in window "w" starting at point "p0", of length "L", "theta" degrees aboce the horizontal
def drawLine(w, p0, theta, L, color):
	x1 = p0.getX() + L * math.cos(math.pi/180 * theta)
	y1 = p0.getY() + L * math.sin(math.pi/180 * theta)
	p1 = Point(x1, y1)
	line = Line(p0, p1); line.setOutline(color); line.draw(w)
	return p1

#Draws level "lvl" Koch Curve in window "w", starting at point "p", with initial length "L", pointing "phi" degrees above the horizontal
def drawKC(w, lvl, p, theta, phi, L):
	#The scale factor of the length for every level
	colors = ['red', 'blue', 'green', 'purple', 'magenta', 'black']
	sf = 1/(2*(1+math.cos(math.pi/180 * theta)))
	#The resolution of our computers limits the detail we can represent the fractal at, passing 6 lvls adds no noticeable detail, but takes more time
	if(lvl > 6):
		lvl = 6
	#base case: draw a line
	if(lvl == 0):
		p = drawLine(w, p, phi, L, colors[randint(0, 5)])
	#recursive case: calls this method four times for every segment of the level 1 koch
	else:
		p = drawKC(w, lvl - 1, p, theta, phi, L * sf)
		p = drawKC(w, lvl - 1, p, theta, phi + theta, L * sf)
		p = drawKC(w, lvl -1, p, theta, phi - theta, L * sf)
		p = drawKC(w, lvl -1, p, theta, phi, L * sf)
	return p

#returns similarity dimension
def getSD(theta):
    sd = math.log(4)/((math.log(2)+math.log(1+math.cos(theta*math.pi/180))))
    return sd

#returns length of curve (I changed this to the perimeter of the snowlake)
def getLength(length, lvls, theta):
	return (3*(4**lvls)) * (length*3**(-lvls))

main()
