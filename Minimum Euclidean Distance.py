import itertools
import math

def euclideanDistance(point1, point2):
    return math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)

points = [(1, 2), (3, 5), (6, 8), (2, 1), (7, 3)]

distances = []

for point1, point2 in itertools.combinations(points, 2):
    distances.append(euclideanDistance(point1, point2))

min_distance = min(distances)
print(f"The minimum Euclidean distance is: {min_distance}")
