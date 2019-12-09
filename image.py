#! usr/bin/python
import Image, ImageDraw, math

import ImageFile, ImageFilter

#user defined image
IM=raw_input('Please enter the filename of the image to convert: ')
img = Image.open(IM)



#read image size
size=img.size
image_width=size[0]
image_height=size[1]

#draw new object on top of the image
Draw=ImageDraw.Draw(img)

# user defined sample 
sample=int(raw_input('Enter the sample size, values between 5 and 100 pixels are advised: '))
sample_size=sample

#just a small definition - returns an image size tuple - can be useful approximating the time it takes to evaluate the image data
print size

#these 2 nested loops dividie the image into imaginary sample grid
for x in range (0,(image_width/sample_size)+1):
	for y in range (0,(image_height/sample_size)+1):
		
		#make a list that will contain all the colour data for each given sample
		colourValues = []

		'''source from Stefan Tsvetkov starts here '''
		#these 2 loops take each sample and push the pixel data into the colourValues list
		for samplex in range(x*sample_size, x*sample_size+sample_size):
			for sampley in range(y*sample_size, y*sample_size+sample_size):
			#the if statement fixes the problem when amount of samples in an image is not a natural number, e.g.: 8.4
				if (samplex <image_width) and (sampley <image_height):
						pix = img.getpixel((samplex,sampley))
						colourValues.append(pix)
		#declare colour values
		R = 0
		G = 0
		B = 0
		for colour in colourValues:
			R = R + colour[0]
			G = G + colour[1]
			B = B + colour[2]

		avR=0
		avG=0
		avB=0
		#this piece returns  an average value of each channel in a sample square
		if not(len(colourValues) == 0):	

			avR = R/len(colourValues)
			avG = G/len(colourValues)
			avB = B/len(colourValues)

		'''source from Stefan Tsvetkov ends here '''


             	#method that I tried to use that samples the 4 corner pixels of every sample then averages them out
		#xs=(x*sample_size)
		#ys=(y*sample_size)
		#P1 = pix[xs,ys]
		#P2 = pix[xs+sample_size,ys]
		#P3 = pix[xs,ys+sample_size]		
		#P4 = pix[xs+sample_size,ys+sample_size]'''

		#print("P1 = " + str(P1) + "coordinate: " + str(xs) + "-" + str(ys))
		#print("P2 = " + str(P1) + "coordinate: " + str(xs+sample_size) + "-" + str(ys))
		#print("P3 = " + str(P1) + "coordinate: " + str(xs) + "-" + str(ys + ys+sample_size))
		#print("P4 = " + str(P1) + "coordinate: " + str(xs+sample_size) + "-" + str(ys+sample_size))

		#p1,p2, anchor1x etc i used as palce holder simply to make the  if statements shorter and easier to read
		p1 = (x*sample_size,y*sample_size)
		p2 = ((x*sample_size) + sample_size,(y*sample_size)+sample_size)

		Draw.rectangle((p1, p2), outline=None, fill="white")
		anchor1x = (x*sample_size)
		anchor1y = (y*sample_size)
		anchor2x = ((x*sample_size)+sample_size)
		anchor2y = ((y*sample_size)+sample_size)
		average = (avR+avG+avB)/3
		if(average>=0 and average<=5):
			Draw.ellipse((anchor1x,anchor1y, anchor2x,anchor2y), fill="black", outline=None)
		if(average>=5 and average<=40):
			Draw.ellipse((anchor1x+sample_size/18,anchor1y+sample_size/18, anchor2x-sample_size/18,anchor2y-sample_size/18), fill="black", outline=None)
		if(average>=41 and average<=50):
			Draw.ellipse((anchor1x+sample_size/9,anchor1y+sample_size/9, anchor2x-sample_size/9,anchor2y-sample_size/9), fill="black", outline=None)
		if(average>=51 and average<=70):
			Draw.ellipse((anchor1x+sample_size/8,anchor1y+sample_size/8, anchor2x-sample_size/8,anchor2y-sample_size/8), fill="black", outline=None)
		if(average>=71 and average<=100):
			Draw.ellipse((anchor1x+sample_size/7,anchor1y+sample_size/7, anchor2x-sample_size/7,anchor2y-sample_size/7), fill="black", outline=None)
		if(average>=101 and average<=150):
			Draw.ellipse((anchor1x+sample_size/5,anchor1y+sample_size/5, anchor2x-sample_size/5,anchor2y-sample_size/5), fill="black", outline=None)
		if(average>=151 and average<=200):
			Draw.ellipse((anchor1x+sample_size/3,anchor1y+sample_size/3, anchor2x-sample_size/3,anchor2y-sample_size/3), fill="black", outline=None)
		if(average>=201 and average<=220):
			Draw.ellipse((anchor1x+sample_size/2.7,anchor1y+sample_size/2.7, anchor2x-sample_size/2.7,anchor2y-sample_size/2.7), fill="black", outline=None)
		if(average>=221 and average<=230):
			Draw.ellipse((anchor1x+sample_size/2.5,anchor1y+sample_size/2.5, anchor2x-sample_size/2.5,anchor2y-sample_size/2.5), fill="black", outline=None)
		if(average>=231 and average<=240):
			Draw.ellipse((anchor1x+sample_size/2.4,anchor1y+sample_size/2.4, anchor2x-sample_size/2.4,anchor2y-sample_size/2.4), fill="black", outline=None)
		if(average>=241 and average<=246):
			Draw.ellipse((anchor1x+sample_size/2.2,anchor1y+sample_size/2.2, anchor2x-sample_size/2.2,anchor2y-sample_size/2.2), fill="black", outline=None)

img.show()
img.save('imagenew.bmp')

