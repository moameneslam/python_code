import Image, ImageDraw
import math

width = 1000
height = 1000

im = Image.new("RGB",(width,height), (255, 255, 255))
draw = ImageDraw.Draw(im)



MinReal = -2.0 #Left edge of the image X-direction real numbers
MaxReal= 1.0   #right edge of the image
MinImaginary = -1.2  #lower edge of the image y direction, imaginary numbers
MaxImaginary = MinImaginary+(MaxReal-MinReal)*height/width #top edge setting a hard value might stretch the image about 1.2
Real_factor = (MaxReal-MinReal)/(width-1)
Imaginary_factor = (MaxImaginary-MinImaginary)/(height-1)
MaxIterations = 40
y = 0
x = 0

for y in range (0, height): #y <height
	c_imagin = MaxImaginary - (y*Imaginary_factor)
	for x in range (0, width):   #x< width
		c_real = MinReal + (x*Real_factor)
		
		(Z,i) = (c_real) + (c_imagin)
		#Z_Real = c_real  # complex Z = c_real + c_imagin
		#Z_Imagin = c_imagin  # Z = c   Zn with c being c_real +c_imaginary *i
		isInside = True
		n = 0

		for n in range (0, MaxIterations ):  #n<MaxIterations
			(Z2,j) = (complex (Z)) * (complex (Z))
			#Z_Real2 = Z_Real*Z_Real   #complex(Z2) = complex Z ^2 
			#Z_Imagin2 = Z_Imagin*Z_Imagin
			if (complex (Z2,j) > 4):
			#if (Z_Real2 + Z_Imagin2 > 4):    # or  if (sqrt(complex(Z2)) > 2)  // if absolute value of z > 2
				isInside = False
				break
			(C,k) = (c_real) + (c_imagin)  
			 
			Z.imag = (2*Z2.real*Z.imag) + C.imag   # Z = Z^2 + c
			Z.real = (Z2.real - Z2.imag) + C.real  # swap brackets to reverse shape
		if (isInside):draw.point((x, y), fill= (0, 0, 0))

im.show()
