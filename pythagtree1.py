import Image, ImageDraw
import math
# global settings
W = int(raw_input('Enter Image Width: '))
H = int(raw_input('Enter Image Height: '))
Sz = int(raw_input('Enter Initial Polygon Size: '))
Ang = int(raw_input('Enter Tree Angle: '))
Rec = int(raw_input('Enter Recursion Level: '))

colProfile = raw_input('Select from Azure, Autumn, Winter, and MintberryCrunch: ')
#colour profiles
#INITIALIZE------------------------------------------------------------------------------------------------
R=0
G=0
B=0
BckgrColourProfile = (0, 0, 0)
#----------------------------------------------------------------------------------------------------------
if colProfile == 'Azure' or colProfile =='azure' or colProfile == 'AZURE':
	R = 51
	G = 161
	B = 201
	BckgrColourProfile = (240, 255, 255)

elif colProfile == 'Autumn' or  colProfile == 'autumn' or colProfile == 'AUTUMN' or colProfile == 'autum' or colProfile == 'Autum' or colProfile == 'Fall' or colProfile == 'fall':
	R = 255		
	G = 193
	B = 37
	BckgrColourProfile = (205, 133, 0)

elif colProfile == 'Winter' or  colProfile == 'winter' or colProfile == 'WINTER':
	R = 30		
	G = 144
	B = 255
	BckgrColourProfile = (135, 206, 235)

elif colProfile == 'MintberryCrunch' or  colProfile == 'mintberrycrunch' or colProfile == 'MINTBERRYCRUNCH':
	R = 238		
	G = 121
	B = 159
	BckgrColourProfile = (34, 139, 34)

# DefaultSettings-------------------------------------------------------------------------------------------

else:
	R = 120 #Default
	G = 66
	B = 101
	BckgrColourProfile = (0, 0, 0)
#------------------------------------------------------------------------------------------------------------
#print 'you chose:'colProfile


#------------------------------------------------------------------------------------------------------------

width = W #width/height in px to be specified by the user
height = H

im = Image.new("RGB",(width,height), BckgrColourProfile)
draw = ImageDraw.Draw(im)

polySize = Sz #initial polygon side
AngleL = Ang  # increment angle
AngleJ = 90 - AngleL # derivative of the increment angle will help to calculate the transformation

x1 =  (width/2) - (polySize/2) #"centers" the initial polygon in x-direction
y1 = 100 # since pil counts pixels from top left subs this number from height will place the tree at 100px up from the bottom edge of the image. eg: height = 1000; so 1000 - y1 = 900px  


recursion = Rec # recursion level for the tree to be set as raw-input

r = R # initial colour; can do couple of colour profiles
g = G
b = B

# globals end here---------------------------------------



def DrawSquare (x1,y1,x2,y2,x3,y3,x4,y4,r,g,b): # draw initial poly from set globals
	draw.polygon([(x1, height-y1),(x2,height-y2),(x3,height-y3),(x4,height-y4)],fill = (r,g,b),outline = (255,255,255))

def CalcPoints (x1, y1, side): #this makes a list of usable coordiantes for the initial polygon
	x2 = x1+side           #they are passed into DrawSquare which substracts the height of the image from y1,y2,y3,y4 thus making a perfect square
	y2 = y1                    #seems to be the only way to deal with the problem of origin being top left
	x3 = x1+side
	y3 = y1+side
	x4 = x1
	y4 = y1+side

	listofCoords = [x1,y1,x2,y2,x3,y3,x4,y4] #here they are passed in to a neat list
	return listofCoords

def CalculateOldLength(x1,y1,x2,y2): #Calculates the length of the old side
	x = math.fabs(x2 - x1)        
	y = math.fabs(y2 - y1)
	side = math.sqrt(math.pow(x,2) + math.pow(y,2))
	return side

def CalculateNewLength(Angle,side): #Calculate the len of the incremented square side
	Angle = math.radians(Angle)
	return math.sin(Angle) * side

def VectorSubtract(x4,y4,x3,y3): #Returns a vector calculated by substracting two points' coordinates of the Square
	x = x3 - x4
	y = y3 - y4
	vectorList = [x,y]
	return vectorList         # this vector is positioned at the origin and is equal to the length of the original polygon

def VectorScale(x,y,SideOld,SideNew): #Scales the vector at the origin by the ratio between the OldSide and the NewSide
	Ratio = SideRatio(SideOld,SideNew)
	x = x * Ratio
	y = y * Ratio
	vectorList = [x,y]
	return vectorList

def SideRatio(SideOld,SideNew): #Calculates the ratio between the New and the Old Length.
	return SideNew/SideOld

def TranslateBack(pX,pY,x1,y1): #Scaled vetor is then translated back to its original location.
	x = pX + x1                 #pX and pY are the original positions where the program moves the vector.these numbers are to be varied since each time its going to be a recursion calculation
	y = pY + y1
	vectorList = [x,y]
	return vectorList #The returned list contains the Coordinates of the scaled vector in the tree.

def CVRotation(pX,pY,X1,Y1,Angle): #Rotates X1 and Y1 Coordinates by the Angle around pX and pY
        
	Angle = math.radians(Angle)    

    # matrix a
	a11 = CorrectCos(Angle)                                         #rotation matrix:   @ is an angle
	a12 = -(math.sin(Angle))                                        #|x'|   |cos@ -sin@||x|
	a13 = (pX * (1 - CorrectCos(Angle)) + (pY * math.sin(Angle)))   #|y'|=  |sin@ cos@ ||y|
	a21 = math.sin(Angle)                                           #therefore the coords of x',y' od the points x,y after the rotation are:
	a22 = CorrectCos(Angle)                                         #x'= xCos@ - ySin@,
	a23 = (pY * (1 - CorrectCos(Angle)) - (pX * math.sin(Angle)))   #y'= xSin@ - yCos@.
										a = [[a11,a12,a13],
	     [a21,a22,a23],
             [0.0,0.0,1.0]]

    #Set the matrix b        
	b = [X1,Y1,1.0]

	return MMultiplication(a,b) #Multiplies the two matrixes and returns it

def MMultiplication(a,b): #Procedure for matrix multiplication a,b are 2 matrices
	new_matrix = [0,0,0]    #initialize
	for i in range(len(a)): #Row number is 3
		t = 0 #Set to 0 because the loop goes to the a new row in a
		for j in range(len(a[0])): #Column number is 3
			t = t + a[i][j] * b[j]   #Multiplies a[i][j] and b[j] and summs them together 
		new_matrix[i] = t 
	rMatrix = [new_matrix[0],new_matrix[1]] #Returns the x,y Coordinates of multiplied matrix
	return rMatrix

             #Thankyou to Attila Torok for this next procedure
def CorrectCos(Angle): # I had to write this procedure becasue the math.cos(x) at x = 90 and x = -90
	a = math.cos(Angle) #returned the value 6.12323399574e-17. This procedure changes this value to 0.
	if (a<0.01 and a>0):
		a = 0.0
	if (a>-0.01 and a<0):
		a = 0.0
	return a

def CalculateThirdPoint(x4,y4,x3,y3,SideOld,SideNew,Angle): #This Procedure calculates the Coordinates of the top of the 'triangle'.||'Triangle' is the negative shape  that appears between 2 levels 
	a = VectorSubtract(x4,y4,x3,y3)    #takes a vector of a side  moves to the origin                                               || of the pythagorian tree squares where hypotenuse is the top edge of the previous 
	b = VectorScale(a[0],a[1],SideOld,SideNew)  #scales at the origin                                                               || level square adjacent is the bottom edge of the left branch and opposite
	c = TranslateBack(x4,y4,b[0],b[1])       # moves back                                                                           || is a bottom edge of the right branch
	d = CVRotation(x4,y4,c[0],c[1],Angle) #Rotate the scaled vector by the given angle of the triangle.
	return d #The returned list contains the Third point's Coordinate in the triangle.

#________________________________________________________________________________________________________________________________________________________________________________________________________________________
# RUNNING THE PROGRAM


PolygonINIT = [x1,y1] #list with first square's coordinates

PolygonINIT = CalcPoints(PolygonINIT[0],PolygonINIT[1],polySize) #calculating the first polygon
DrawSquare(PolygonINIT[0],PolygonINIT[1],PolygonINIT[2],PolygonINIT[3],PolygonINIT[4],PolygonINIT[5],PolygonINIT[6],PolygonINIT[7],r,g,b) #draw the first poly

VlistSide = [PolygonINIT[6],PolygonINIT[7],PolygonINIT[4],PolygonINIT[5]] # the list of coordinates of the side where the 'triangle' needs to be built (initially this is the top edge)
VlistSideNew = []                                                         # points x3y3, and x4y4 this is the side that's going to be taken and transformed into a vector then rotated.
VlistTriangle = [] # the list of the triangle coordinates

for i in range(1,recursion):
	k = 0   #coordinates of each polygon (x3y3, x4y4) are stored in a list after each other this variable is used to acces the list elements.
            #every iteration 4 values are added since each vertex has 2 oordinates and to access x3y3 and x4y4  2 vertices are skipped.
	r = r + 5 # changing the red and greeen channels
	g = g + 10
    
	for l in range(int(math.pow(2,i-1))):
		
		SideOld = CalculateOldLength(VlistSide[k],VlistSide[k+1],VlistSide[k+2],VlistSide[k+3]) #Calculates the length between x3y3 and x4y4, where the 'triangle' needs to be built.
        	SideNew = CalculateNewLength(AngleJ,SideOld) #From the OldSide and the Triangle's AngleL angle it calculates the triangle's opposite side

		TriangleTop = CalculateThirdPoint(VlistSide[k],VlistSide[k+1],VlistSide[k+2],VlistSide[k+3],SideOld,SideNew,AngleL) #Calculates where the triangle's third point is.
        	VlistTriangle = [] #Set it to zero, because every time it runs in the loop it is going to be a new triangle
       		 #List of the triangle's vertexes
        	VlistTriangle.append(VlistSide[k])   #0x
        	VlistTriangle.append(VlistSide[k+1]) #1y
        	VlistTriangle.append(TriangleTop[0]) #2x
        	VlistTriangle.append(TriangleTop[1]) #3y
       		VlistTriangle.append(VlistSide[k+2]) #4x
        	VlistTriangle.append(VlistSide[k+3]) #5y

		#Rotates one point of the triangle around the other point of the triangle by 90 to get the new Cube.in case of the first iteration it's the top point which then becomes a side between vertices 1 and 4
        	NewXY4Left = CVRotation(VlistTriangle[0],VlistTriangle[1],VlistTriangle[2],VlistTriangle[3],90)  #LEFT SIDE BRANCH
        	NewXY3Left = CVRotation(VlistTriangle[2],VlistTriangle[3],VlistTriangle[0],VlistTriangle[1],-90) #
		#Same rotation for the Square on the right side
        	NewXY4Right = CVRotation(VlistTriangle[2],VlistTriangle[3],VlistTriangle[4],VlistTriangle[5],90)
        	NewXY3Right = CVRotation(VlistTriangle[4],VlistTriangle[5],VlistTriangle[2],VlistTriangle[3],-90)

		 #draw out the Square
        	DrawSquare(VlistTriangle[0],VlistTriangle[1],VlistTriangle[2],VlistTriangle[3],NewXY3Left[0],NewXY3Left[1],NewXY4Left[0],NewXY4Left[1],r,g,b) #Left branch
		DrawSquare(VlistTriangle[4],VlistTriangle[5],NewXY3Right[0],NewXY3Right[1],NewXY4Right[0],NewXY4Right[1],VlistTriangle[2],VlistTriangle[3],r,g,b) #right 

		#Stores the new top sides
        	VlistSideNew.append(NewXY4Left[0])
        	VlistSideNew.append(NewXY4Left[1])
        	VlistSideNew.append(NewXY3Left[0])
        	VlistSideNew.append(NewXY3Left[1])
		VlistSideNew.append(NewXY4Right[0])
        	VlistSideNew.append(NewXY4Right[1])
        	VlistSideNew.append(NewXY3Right[0])
        	VlistSideNew.append(NewXY3Right[1])


		
        	k = k + 4
    	VlistSide = VlistSideNew 
    	VlistSideNew = []

im.save('pythagoras.jpg')
im.show ()
