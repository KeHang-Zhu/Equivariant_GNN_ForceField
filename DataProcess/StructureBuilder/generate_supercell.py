from ase import Atoms
import ase.io
from ase import build
import numpy as np
from ase.build.tools import sort

atoms = ase.io.read("/n/home09/zkh/li3po4-joint-together.xyz", index=-1)
# now atoms is a list of ase.Atoms objects each representing a frame

#save the unit cell
ase.io.write('./li3_test.data', atoms, format='lammps-data')

# create the supercell
# supercell = ase.build.make_supercell(atoms,np.eye(3) * 4, wrap=True, tol=1e-05)

# # sort the atoms
# super_sorted = sort(supercell)

# #write the atoms
# #save the supercell
# ase.io.write('./li3_amorp_1w.data', super_sorted, format='lammps-data')
