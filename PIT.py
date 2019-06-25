import math
import meep as mp
from meep import mpb
num_bands = 8
k_points = [mp.Vector3(),               # Gamma
            mp.Vector3(y=0.5),          # M
            mp.Vector3(-1 / 3, 1 / 3),  # K
            mp.Vector3()]               # Gamma

k_points = mp.interpolate(4, k_points)
geometry = [mp.Cylinder(center=mp.Vector3(),radius=0.2,height=0.1,axis=mp.Vector3(0,0,1), material=mp.Medium(epsilon=12))]
geometry_lattice = mp.Lattice(size=mp.Vector3(5, 5, 0.1))
mp.geometric_objects_lattice_duplicates(geometry_lattice, geometry, 1,1,0.1)
resolution = 20
ms = mpb.ModeSolver(num_bands=num_bands,
                    k_points=k_points,
                    geometry=geometry,
                    geometry_lattice=geometry_lattice,
                    resolution=resolution)
ms.run_tm()
ms.output_epsilon()