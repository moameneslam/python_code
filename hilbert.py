import ariturtle
import math
import copy
import Image, ImageDraw
import sys
usrS = int(raw_input('Enter Image Size: '))
depth = int(raw_input('Enter Recursion Depth: '))

img = Image.new('RGB', (usrS, usrS))
imageSize = img.size
draw = ImageDraw.Draw(img)

sys.setrecursionlimit(1000)

global size

def drawBasic(turtle, level, angle = 90):

	global size

	if level == 0:
		return

	ariturtle.turn(turtle, angle) 
	drawBasic(turtle, level - 1, -angle)
	
	ariturtle.move(turtle, size)
	ariturtle.turn(turtle, -angle)
	drawBasic(turtle, level - 1, angle)

	ariturtle.move(turtle, size)
	drawBasic(turtle, level - 1, angle)

	ariturtle.turn(turtle, -angle)
	ariturtle.move(turtle, size)
	drawBasic(turtle, level - 1, -angle)

	ariturtle.turn(turtle, angle)

def hilbert(level):
	

	if not(type(level) == int) or (level<1):
		print 'invalid value'
		return

	global size
	
	startPoint = imageSize[0]/math.pow(2,level+1)

	size = 2*startPoint

	tL = ariturtle.the_turtle()

	ariturtle.init(tL, draw, position=[startPoint, startPoint])
	

	ariturtle.penDown(tL)  #facing right
	
	ariturtle.turn(tL, -90)
	
	drawBasic(tL, level)


hilbert(depth)
img.show()
