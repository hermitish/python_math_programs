'''
sa_vol_defs.py
Contains definitions of methods to find surface areas and volumes of the following figures:
    1. Cone
    2. Sphere
    3. Cylinder
    4. Cude
    5. Cuboid
    6. Tetrahedron (Regular)
'''

from math import pi, pow, sqrt
r2 = sqrt(2)
r3 = sqrt(3)


def cone_sa(r, h):
    l = sqrt(pow(r, 2) + pow(h, 2))
    return pi * r * (l + r)
def cone_vol(r, h):
    return (1/3) * pi * pow(r, 2) * h

def sphere_sa(r):
    return 4 * pi * pow(r, 2)
def sphere_vol(r):
    return (4/3) * pi * pow(r, 3)

def cylinder_sa(r, h):
    return 2 * pi * r * (r + h)
def cylinder_vol(r, h):
    return pi * pow(r, 2) * h

def cube_sa(a):
    return 6 * pow(a, 2)
def cube_vol(a):
    return pow(a, 3)

def cuboid_sa(l, b, h):
    return 2 * ((l * b) + (b * h) + (l * h))
def cuboid_vol(l, b, h):
    return l * b * h

def tetrahedron_sa(a):
    return r3 * pow(a, 2)
def tetrahedron_vol(a):
    return pow(a, 3) / (6 * r2)
