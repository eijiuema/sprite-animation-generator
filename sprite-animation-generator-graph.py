from collections import defaultdict
from PIL import Image
import operator

image = Image.open("images\\test4.png")

pixel_map = image.load()

# Python3 Program to print BFS traversal
# from a given source vertex. BFS(int s)
# traverses vertices reachable from s.

# This class represents a directed graph
# using adjacency list representation


class Graph:

    # Constructor
    def __init__(self):

        # default dictionary to store graph
        self.graph = defaultdict(list)

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    # Function to print a BFS of graph
    def BFS(self, s):

        # Mark all the vertices as not visited
        visited = [False] * (len(self.graph))

        # Create a queue for BFS
        queue = []

        # Create a result list
        result = []

        # Mark the source node as
        # visited and enqueue it
        queue.append(s)
        visited[s] = True

        x = 0

        while queue:

            # Dequeue a vertex from
            # queue and print it
            s = queue.pop(0)
            result.append(s)

            # Get all adjacent vertices of the
            # dequeued vertex s. If a adjacent
            # has not been visited, then mark it
            # visited and enqueue it
            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True

        print(x)

        return result


pixel_list = []

for x in range(0, image.size[0]):
    for y in range(0, image.size[1]):
        if(pixel_map[x, y][3] != 0):
            pixel_list.append((x, y))

g = Graph()

for u, pixel in enumerate(pixel_list):
    for v, pixell in enumerate(pixel_list):
        x = abs(pixel[0]) - abs(pixell[0])
        y = abs(pixel[1]) - abs(pixell[1])
        if(-1 <= x <= 1 and -1 <= y <= 1):
            g.addEdge(u, v)

result = g.BFS(0)

# pixel_list = []

# directions = [(1, 0), (0, -1), (-1, 0), (0, 1)]


# def store_pixel(current_pixel):
#     if(
#         current_pixel[0] == image.size[0] or
#         current_pixel[1] == image.size[1] or
#         current_pixel[0] < 0 or
#         current_pixel[1] < 0 or
#         current_pixel in pixel_list or
#         pixel_map[current_pixel][3] == 0
#     ):
#         return

#     pixel_list.append(current_pixel)

#     for direction in directions:
#         store_pixel(tuple(map(operator.add, current_pixel, direction)))
#         # directions.append(directions.pop(0))


# store_pixel(initial_coordinate)

# print(pixel_list)

object_image = Image.new('RGBA', image.size, (0, 0, 0, 0))
object_image_pixel_map = object_image.load()

line_image = Image.new('RGBA', (1, len(pixel_list)), (0, 0, 0, 0))
line_image_pixel_map = line_image.load()

for index, pixel_id in enumerate(result):
    object_image_pixel_map[pixel_list[pixel_id]] = pixel_map[pixel_list[pixel_id]]
    line_image_pixel_map[0, index] = pixel_map[pixel_list[pixel_id]]
    object_image.save(f"out/{index}.png")
line_image.save(f"out/line.png")
