#this is my first github file

import Rhino.Geometry as rg 

def add(a,b):
    return a + b 


def make_circle(radius):
    return rg.Circle(rg.Plane.World, radius)