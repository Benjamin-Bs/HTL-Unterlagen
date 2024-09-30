from PIL import Image
import sys

with open(sys.argv[1], 'r') as f:
    ascii_data = f.read()

image = Image.new('L', (128, 64))

# read every hex char and convert to grayscale value
for i in range(len(ascii_data)):
    px = int(ascii_data[i], 16) # reads 0..15
    px *= 17 # scales to 0..255
    x = (i % 128)
    y = (i // 128)
    image.putpixel((x, y), px)

image.show()