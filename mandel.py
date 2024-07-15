from PIL import Image, ImageDraw
import math

# User input for image dimensions
width = int(input('Enter Image width in pixels: '))
height = int(input('Enter Image height in pixels: '))

# Create a new image
im = Image.new("RGB", (width, height), (255, 255, 255))
draw = ImageDraw.Draw(im)

MinReal = -2.0
MaxReal = 1.0
MinImaginary = -1.2
MaxImaginary = MinImaginary + (MaxReal - MinReal) * height / width
Real_factor = (MaxReal - MinReal) / (width - 1)
Imaginary_factor = (MaxImaginary - MinImaginary) / (height - 1)
MaxIterations = 100

for y in range(0, height):
    for x in range(0, width):
        c_real = MinReal + x * Real_factor
        c_imaginary = MaxImaginary - y * Imaginary_factor

        Z_real = 0
        Z_imaginary = 0
        isInside = True

        for n in range(MaxIterations):
            Z_real2 = Z_real * Z_real
            Z_imaginary2 = Z_imaginary * Z_imaginary

            if Z_real2 + Z_imaginary2 > 4:
                isInside = False
                break

            Z_imaginary = 2 * Z_real * Z_imaginary + c_imaginary
            Z_real = Z_real2 - Z_imaginary2 + c_real

        if isInside:
            draw.point((x, y), fill=(0, 0, 0))  # Black inside Mandelbrot set
        else:
            # Compute color based on the escape number
            escapeNumber = math.sqrt(Z_real2 + Z_imaginary2)
            color = int(255 * escapeNumber / MaxIterations)
            draw.point((x, y), fill=(color, color, color))

im.save('mandelbrot.jpg')
im.show()
