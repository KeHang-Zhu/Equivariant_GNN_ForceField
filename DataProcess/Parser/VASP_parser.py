import os
import ase.io
import numpy as np
from ase.io import read

def parse_outcar_to_xyz(outcar_path, xyz_path):
    # Read the OUTCAR file using ASE
    frames = read(outcar_path, index=':', format='vasp-out')

    # Write the frames to an XYZ file with energy and forces information
    with open(xyz_path, 'w') as f:
        for frame in frames:
            num_atoms = len(frame)
            f.write(f"{num_atoms}\n")
            
            energy = frame.get_potential_energy()
            f.write(f"Energy: {energy} eV\n")

            positions = frame.get_positions()
            forces = frame.get_forces()
            symbols = frame.get_chemical_symbols()
            
            for i in range(num_atoms):
                pos = positions[i]
                force = forces[i]
                symbol = symbols[i]
                f.write(f"{symbol} {pos[0]} {pos[1]} {pos[2]} {force[0]} {force[1]} {force[2]}\n")


if __name__ == "__main__":
    outcar_path = "/n/holyscratch01/kozinsky_lab/Kehang/Recrystalization/flare-runs/crys_runs/600K/OUTCAR"
    xyz_path = "./li3po4_crys_600K.xyz"

    parse_outcar_to_xyz(outcar_path, xyz_path)