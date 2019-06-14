import math
import meep as mp
from meep import mpb
#!rm *.h5
num_bands = 3

#k_points = [mp.Vector3(),
#            mp.Vector3(0.0  ,0.5  ,0.5  ),  #X
#            mp.Vector3(0.0  ,0.625,0.375),  #U
#            mp.Vector3(0.0  ,0.5  ,0.0  ),  #L
#            mp.Vector3(0.0  ,0.0  ,0.0  ),  #Gamma
#            mp.Vector3(0.0  ,0.5  ,0.5  ),  #X
#            mp.Vector3(0.25 ,0.75 ,0.5  ),  #W
#            mp.Vector3(0.375,0.75 ,0.375),  #K
#            mp.Vector3()]          

k_points = [mp.Vector3(),
            mp.Vector3(0.0  ,0.5  ,0.5  ),  #X
            mp.Vector3(0.5  ,0.625,0.625),  #U
            mp.Vector3(0.5  ,0.5  ,0.5  ),  #L
            mp.Vector3(0.0  ,0.0  ,0.0  ),  #Gamma
            mp.Vector3(0.0  ,0.5  ,0.5  ),  #X
            mp.Vector3(0.25 ,0.75 ,0.5  ),  #W
            mp.Vector3(0.375,0.75 ,0.375),  #K
            mp.Vector3()]  

res0 = 16
n0 = 1.5
tol = 0.001
mesh_size = 3
L = math.sqrt(3)/4
n = math.sqrt(32)
r = 0.0725
m = mp.Medium(epsilon=n*n)

geometry = [mp.Cylinder(center=mp.Vector3(0,0,0),radius=r, material=m, height=L, axis=mp.Vector3(1,1,1)),
           mp.Cylinder(center=mp.Vector3(0.5,0,0),radius=r, material=m, height=L, axis=mp.Vector3(3,-1,-1)),
           mp.Cylinder(center=mp.Vector3(0,0.5,0),radius=r, material=m, height=L, axis=mp.Vector3(-1,3,-1)),
           mp.Cylinder(center=mp.Vector3(0,0,0.5),radius=r, material=m, height=L, axis=mp.Vector3(-1,-1,3))]

#a = math.sqrt(0.5)
#geometry_lattice = mp.Lattice(basis-size=mp.Vector3(a,a,a),
#                                 basis1=mp.Vector3(0,1,1),
#                                 basis2=mp.Vector3(1,0,1),
#                                 basis3=mp.Vector3(1,1,0))

sqrt_half = math.sqrt(0.5)
geometry_lattice = mp.Lattice(
    basis_size=mp.Vector3(sqrt_half, sqrt_half, sqrt_half),
    basis1=mp.Vector3(0, 1, 1),
    basis2=mp.Vector3(1, 0, 1),
    basis3=mp.Vector3(1, 1)
)
k_points = mp.interpolate(4, k_points)

ms = mpb.ModeSolver(num_bands=num_bands,
                    k_points=k_points,
                    geometry=geometry,
                    geometry_lattice=geometry_lattice,
                    resolution=res0*n/n0,
                    mesh_size = mesh_size)
#mpb.ModeSolver.optimize_grid_size()
ms.run()
ms.output_epsilon()