from collections import defaultdict
from PIL import Image
import operator

image = Image.open("images\\test.png")

pixel_map = image.load()

initial_coordinate = tuple(int(x.strip())
                           for x in input("Initial coordinates: ").split(','))

pixel_list = []

directions = [(1, 0), (0, -1), (1, -1), (-1, 0), (-1, 1), (0, 1)]


def store_pixel(current_pixel):
    if(
        current_pixel[0] == image.size[0] or
        current_pixel[1] == image.size[1] or
        current_pixel[0] < 0 or
        current_pixel[1] < 0 or
        current_pixel in pixel_list or
        pixel_map[current_pixel][3] == 0
    ):
        return

    pixel_list.append(current_pixel)

    for direction in directions:
        store_pixel(tuple(map(operator.add, current_pixel, direction)))


store_pixel(initial_coordinate)

print(pixel_list)

object_image = Image.new('RGBA', image.size, (0, 0, 0, 0))
object_image_pixel_map = object_image.load()

line_image = Image.new('RGBA', (1, len(pixel_list)), (0, 0, 0, 0))
line_image_pixel_map = line_image.load()

for index, pixel in enumerate(pixel_list):
    object_image_pixel_map[pixel] = pixel_map[pixel]
    line_image_pixel_map[0, index] = pixel_map[pixel]
    object_image.save(f"out/{index}.png")
line_image.save(f"out/line.png")
