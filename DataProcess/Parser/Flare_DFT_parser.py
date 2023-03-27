import os
import re
import ase.io
import numpy as np
from ase.io import read
from ase import Atoms

def read_custom_format(file_path):
    frames = []
    position = []
    with open(file_path, 'r') as f:
        while True:
            line = f.readline()
            if not line:
                break
            num_atoms = int(line.strip())
            header = f.readline().strip()
            
             # Extract lattice parameters from the header
            lattice_str = re.search(r'Lattice="([^"]*)"', header).group(1)
            energy_str = re.search(r'energy=([^\s+]*)', header).group(1)
            lattice = np.array([float(x) for x in lattice_str.split()]).reshape(3, 3)
            # position.append(lattice_str)
            print(energy_str)
            atoms_data = []
            for _ in range(num_atoms):
                atom_data = f.readline().split()
                symbol = atom_data[0]
                pos = [float(x) for x in atom_data[1:4]]
                forces = [float(x) for x in atom_data[4:7]]
                atoms_data.append((symbol, pos, forces))

            frame = Atoms(positions=[pos for _, pos, _ in atoms_data],
                          symbols=[sym for sym, _, _ in atoms_data])
            frame.set_cell(lattice)
            forces = np.array([forces for _, _, forces in atoms_data])
            frame.set_array('forces', forces)
            energy_str = np.array([float(energy_str) for _, _, forces in atoms_data])
            frame.set_array('energy', energy_str)
            frames.append(frame)

    return frames

def parse_custom_to_xyz(input_file, xyz_path):
    

    with open(xyz_path, 'w') as f:
        for input_file in input_files:
            frames = read_custom_format(input_file)
            for frame in frames:
                num_atoms = len(frame)
                f.write(f"{num_atoms}\n")

                cell = frame.get_cell()
                lattice_str = " ".join(f"{cell[i, j]:.6f}" for i in range(3) for j in range(3))
                energy_str = frame.get_array('energy')[0]
                print(cell)
                # lattice_str = position
                # lattice_str = " ".join(f"{c:.6f}" for c in frame.get_cell().flat)
                f.write(f"Lattice=\"{lattice_str}\" Properties=species:S:1:pos:R:3:forces:R:3 energy={energy_str}  pbc=\"T T T\"\n")

                positions = frame.get_positions()
                forces = frame.get_array('forces')
                symbols = frame.get_chemical_symbols()

                for i in range(num_atoms):
                    pos = positions[i]
                    force = forces[i]
                    symbol = symbols[i]
                    f.write(f"{symbol} {pos[0]:.6f} {pos[1]:.6f} {pos[2]:.6f} {force[0]:.6f} {force[1]:.6f} {force[2]:.6f}\n")

if __name__ == "__main__":
    input_files = [
        "/n/holyscratch01/kozinsky_lab/Kehang/Recrystalization/flare-runs/crys_runs/600K/flare_Li3PO4_otf_output_dft.xyz",
        "/n/holyscratch01/kozinsky_lab/Kehang/Recrystalization/flare-runs/crys_runs/700K/flare_Li3PO4_otf_output_dft.xyz", 
        "/n/holyscratch01/kozinsky_lab/Kehang/Recrystalization/flare-runs/crys_runs/800K/flare_Li3PO4_otf_output_dft.xyz",
        "/n/holyscratch01/kozinsky_lab/Kehang/Recrystalization/flare-runs/crys_runs/900K/flare_Li3PO4_otf_output_dft.xyz",
        "/n/holyscratch01/kozinsky_lab/Kehang/Recrystalization/flare-runs/crys_runs/1000K/flare_Li3PO4_otf_output_dft.xyz",
    ]
    xyz_path = "./li3po4_crys_combined.xyz"

    parse_custom_to_xyz(input_files, xyz_path)