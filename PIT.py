import math
import meep as mp
from meep import mpb
num_bands = 10
ax = math.sqrt(2)/2.0
ay = math.sqrt(6)/2.0
az = math.sqrt(3)
L = math.sqrt(3)/4.0
hs = math.sqrt(3)/12.0
na = 1
r = 0.0725
geometry_lattice = mp.Lattice(size=mp.Vector3(na,na,na),
                              basis_size=mp.Vector3(ax,ay,az))
#v1 = mp.Vector3(1)

v2 = mp.Vector3(0.5,0.5,0)
v1 = mp.Vector3(0,1.0/3.0,1.0/3.0)
v5 = mp.Vector3(0.5,5.0/6.0,1.0/3.0)
v3 = mp.Vector3(0.5,1.0/6.0,2.0/3.0)
v4 = mp.Vector3(0,2.0/3.0,2.0/3.0)
res0 = mp.Vector3(12,20,28)
n0 = 1.5
mesh_size = 3
n = math.sqrt(32)
r = 0.0725
m = mp.Medium(epsilon=n*n)
c1 = mp.Vector3(0,-math.sqrt(6)/12/ay,-hs/2/az)
c2 = mp.Vector3(math.sqrt(2)/8/ax,math.sqrt(6)/24/ay,-hs/2/az)
c3 = mp.Vector3(-math.sqrt(2)/8/ax,math.sqrt(6)/24/ay,-hs/2/az)
c4 = mp.Vector3(0,0,L/2/az)
geometry = [mp.Cylinder(center=c1,radius=r, material=m, height=L, axis=c1),
            mp.Cylinder(center=c2,radius=r, material=m, height=L, axis=c2),
            mp.Cylinder(center=c3,radius=r, material=m, height=L, axis=c3),
            mp.Cylinder(center=c4,radius=r, material=m, height=L, axis=c4),
            mp.Cylinder(center=c1+v1,radius=r, material=m, height=L, axis=c1),
            mp.Cylinder(center=c2+v1,radius=r, material=m, height=L, axis=c2),
            mp.Cylinder(center=c3+v1,radius=r, material=m, height=L, axis=c3),
            mp.Cylinder(center=c4+v1,radius=r, material=m, height=L, axis=c4),
            mp.Cylinder(center=c1+v2,radius=r, material=m, height=L, axis=c1),
            mp.Cylinder(center=c2+v2,radius=r, material=m, height=L, axis=c2),
            mp.Cylinder(center=c3+v2,radius=r, material=m, height=L, axis=c3),
            mp.Cylinder(center=c4+v2,radius=r, material=m, height=L, axis=c4),
            mp.Cylinder(center=c1+v3,radius=r, material=m, height=L, axis=c1),
            mp.Cylinder(center=c2+v3,radius=r, material=m, height=L, axis=c2),
            mp.Cylinder(center=c3+v3,radius=r, material=m, height=L, axis=c3),
            mp.Cylinder(center=c4+v3,radius=r, material=m, height=L, axis=c4),
            mp.Cylinder(center=c1+v4,radius=r, material=m, height=L, axis=c1),
            mp.Cylinder(center=c2+v4,radius=r, material=m, height=L, axis=c2),
            mp.Cylinder(center=c3+v4,radius=r, material=m, height=L, axis=c3),
            mp.Cylinder(center=c4+v4,radius=r, material=m, height=L, axis=c4),
            mp.Cylinder(center=c1+v5,radius=r, material=m, height=L, axis=c1),
            mp.Cylinder(center=c2+v5,radius=r, material=m, height=L, axis=c2),
            mp.Cylinder(center=c3+v5,radius=r, material=m, height=L, axis=c3),
            mp.Cylinder(center=c4+v5,radius=r, material=m, height=L, axis=c4)]

#geometry2 = mp.geometric_objects_duplicates(v1,1,1,geometry_unit)
#geometry3 = mp.geometric_objects_duplicates(mp.Vector3(0,math.sqrt(6)/2/ay,0),1,1,geometry_unit)
#geometry4 = mp.geometric_objects_duplicates(v3,1,1,geometry_unit)
#geometry5 = mp.geometric_objects_duplicates(v3,1,1,geometry2)
#geometry6 = mp.geometric_objects_duplicates(v2,1,1,geometry4)
geometry = mp.geometric_objects_lattice_duplicates(geometry_lattice, geometry)

#k_points = [mp.Vector3(),
#            mp.Vector3(0,0.5),
#            mp.Vector3(0.5,0.5),
#            mp.Vector3(),
#            mp.Vector3(0,0.5),
#            mp.Vector3(0.5,0.5,0.5),
#            mp.Vector3()]          # Gamma
#k_points = mp.interpolate(4, k_points)
k_points = [mp.Vector3()]
ms = mpb.ModeSolver(num_bands=num_bands,
                    k_points=k_points,
                    geometry=geometry,
                    geometry_lattice=geometry_lattice,
                    resolution=2*res0,
                    mesh_size = mesh_size)
ms.geometry = ms.geometry.append([mp.Cylinder(center=c1,radius=r, material=mp.air, height=L, axis=c1)])
#mpb.ModeSolver.optimize_grid_size()
ms.run()
ms.output_epsilon()
#!h5tovtk epsilon.h5