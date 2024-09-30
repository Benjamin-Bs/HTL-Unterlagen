from PIL import Image
import sys

with open(sys.argv[1], 'rb') as f:
    raw_data = f.read()

image = Image.new('L', (128, 64))

# Process each byte to extract two 4-bit grayscale pixels
for i in range(len(raw_data)):
    byte = raw_data[i]
    high = byte >> 4
    low = byte & 0x0F
    high *= 17
    low *= 17
    x = (i % 64) * 2
    y = (i // 64)
    image.putpixel((x, y), high)
    image.putpixel((x + 1, y), low)

image.show()
