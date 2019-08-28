from collections import defaultdict
from PIL import Image
import operator

image = Image.open("images\\test6.png")

pixel_map = image.load()

# Avançar em todas as direções e salvar

# initial_coordinate = tuple(int(x.strip())
#                            for x in input("Initial coordinates: ").split(','))

pixel_list = []
pixels_by_step = []

directions = [(1, 0), (0, -1), (1, -1), (-1, 0), (-1, 1), (0, 1)]

def is_color(pixel):
    x, y = pixel
    w, h = image.size
    return 0 <= x <= w and 0 <= y <= h and pixel_map[pixel][3] != 0


def sort_pixels(center_pixel):

    queue = [center_pixel]
    result = []

    pixels_by_step = []

    while queue:
        x = queue.pop()
        result.append(x)

        pixels_by_step.append(0)

        for direction in directions:
            pixel = tuple(map(operator.add, x, direction))
            if is_color(pixel) and pixel not in queue + result:
                queue.append(pixel)

    return result

pixel_list = sort_pixels((5,5))

object_image = Image.new('RGBA', image.size, (0, 0, 0, 0))
object_image_pixel_map = object_image.load()

line_image = Image.new('RGBA', (1, len(pixel_list)), (0, 0, 0, 0))
line_image_pixel_map = line_image.load()

current_step = 0

for index, pixel in enumerate(pixel_list):
    # for step in range(0, pixels_by_step[current_step]):
    object_image_pixel_map[pixel] = pixel_map[pixel]
    line_image_pixel_map[0, index] = pixel_map[pixel]
    object_image.save(f"out/{index}.png")
line_image.save(f"out/line.png")
