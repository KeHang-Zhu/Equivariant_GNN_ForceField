from ase import Atoms
import ase.io
from ase import build
import numpy as np
from ase.build.tools import sort

# atoms = ase.io.read("/n/home09/zkh/Li3PO4_project/Post/li3_interface.vasp", index=-1)
atoms = ase.io.read("/n/home09/zkh/Li3PO4_project/Post/Li3Po4_crystal.cif")
# atoms = ase.io.read("/n/holyscratch01/kozinsky_lab/Kehang/Li3PO4/lammps_runs/test1536/melt192/dump.trj", index=1)
# now atoms is a list of ase.Atoms objects each representing a frame

atoms= sort(atoms)
#save the unit cell
ase.io.write('li3_crys16.vasp', atoms, format='vasp')
# ase.io.write('./li3_interface.data', atoms, format='lammps-data')
# create the supercell
matrix = [[3, 0, 0],
          [0, 2, 0],
          [0, 0, 2]]
supercell = ase.build.make_supercell(atoms, matrix, wrap=True, tol=1e-05)

# sort the atoms
super_sorted = sort(supercell)

# #write the atoms
# #save the supercell
ase.io.write('li3_crys192.vasp', super_sorted, format='vasp')
