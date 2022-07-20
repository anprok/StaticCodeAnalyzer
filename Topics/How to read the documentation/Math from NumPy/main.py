# import the required library
import math


def calculate_cosine(angle_in_degrees):
    # do not forget to round the result and print it
    i = 180
    angle_in_radians = angle_in_degrees * math.pi / i
    print(round(math.cos(angle_in_radians), 2))