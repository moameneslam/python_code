import Image, ImageDraw
import math
# NOTE : doubling the image size quadruples the time of calculation!!!!!
width = int(raw_input('Enter Image width in pixels: '))
height = int(raw_input('Enter Image height in pixels: '))


im = Image.new("RGB",(width,height), (255, 255, 255))
draw = ImageDraw.Draw(im)



MinReal = -2.0 #Left edge of the image X-direction real numbers
MaxReal= 1.0   #right edge of the image
MinImaginary = -1.2  #lower edge of the image y direction, imaginary numbers
MaxImaginary = MinImaginary+(MaxReal-MinReal)*height/width #top edge setting a hard value might stretch the image about 1.2
Real_factor = (MaxReal-MinReal)/(width-1)
Imaginary_factor = (MaxImaginary-MinImaginary)/(height-1)
MaxIterations = 20
y = 0 #initialize x ad y coordinates
x = 0

for y in range (0, height): #y <height
   for x in range (0, width):  
      c_real = MinReal + (x*Real_factor)
      c_imagin = MaxImaginary - (y*Imaginary_factor)
		
      Z_Real = c_real
      Z_Imagin = c_imagin
      isInside = False # if outside do nothing
      n = 0
      for n in range (0, MaxIterations ):  #n<MaxIterations
			Z_Real2 = Z_Real*Z_Real    # Complex number addition
			Z_Imagin2 = Z_Imagin*Z_Imagin
			Z_Imagin = (2*Z_Real*Z_Imagin) + c_imagin
			Z_Real = (Z_Real2 - Z_Imagin2) + c_real  # swap brackets to reverse shape

      if (Z_Real2 + Z_Imagin2  <4):   # sqrt((zreal^2)+(zimgiry^2) < 2)
		   isInside = True  

      if (isInside):draw.point((x, y), fill= (0, 0, 0)) # draws a black pixel if that pixel belongs to the set
    # colours the otside of the set
      r = 255 # initialize rgb values
      g = 0
      b = 0
      #if (isInside == False):
      escapeNumber = 4.0
      numberlist = [4.0, math.pow(4.5, MaxIterations+4), math.pow(5.0, MaxIterations), math.pow(5.5, MaxIterations), math.pow(6.0, MaxIterations), math.pow(7.0, MaxIterations), math.pow(13, MaxIterations), math.pow(16, MaxIterations), math.pow(22, MaxIterations), math.pow(30, MaxIterations), math.pow(40, MaxIterations), math.pow(55, MaxIterations), math.pow(70, MaxIterations), math.pow(120, MaxIterations), math.pow(1000, MaxIterations), math.pow(10000, MaxIterations), math.pow(100000, MaxIterations), math.pow(1000000, MaxIterations)]    #list of escape numbers

      if (isInside == False):
                  draw.point((x, y), fill=(0, 0, 0)) #black background

      for escapeNumber in (numberlist):
            if (Z_Real2 + Z_Imagin2 > escapeNumber): #makes a red gradient based on the escape number list tends to break with high MaxIterations
                  r = r -(255/(len(numberlist))) # changes the red channel
                  draw.point((x, y), fill=(r, g, b))
	
im.save('mandelbrot.jpg')
im.show()
