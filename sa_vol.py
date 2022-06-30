# sa_vol.py
# print surface area and volume of all the listed figures
'''
    1. Cone
    2. Sphere
    3. Cylinder
    4. Cude
    5. Cuboid
    6. Tetrahedron (Regular)

'''
import sa_vol_defs as s

print(s.cone_sa(3, 2.5))
print(s.cone_vol(3, 2.5))
print()
print(s.sphere_sa(2.75))
print(s.sphere_vol(2.75))
print()
print(s.cylinder_sa(3, 2.5))
print(s.cylinder_vol(3, 2.5))
print()
print(s.cube_sa(5.45))
print(s.cube_vol(5.45))
print()
print(s.cuboid_sa(3, 2.5, 4))
print(s.cuboid_vol(3, 2.5, 4))
print()
print(s.tetrahedron_sa(2.5))
print(s.tetrahedron_vol(2.5))
print()
