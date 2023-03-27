from ase.io import read, write
import numpy as np
import matplotlib.pyplot as plt

def parity_force(dft_path, mlff_path):
    '''Assume input format as .xyz and 
    each frame can have different #atoms'''
    trj_dft = read(dft_path, index=":")
    trj_nn = read(mlff_path, index=":")
    forces_dft = np.array([])
    for step in trj_dft: 
        forces_dft = np.append(forces_dft, step.get_forces().reshape(-1))
    forces_nn = np.array([])
    for step in trj_nn: 
        forces_nn = np.append(forces_nn, step.get_forces().reshape(-1))
   
    return forces_dft, forces_nn



if __name__ == "__main__":
    # your input
    lim = 11
    dft_path = "/n/home09/zkh/Li3PO4_project/Post/li3po4_crys_600K.xyz"
    mlff_path = "/n/holyscratch01/kozinsky_lab/Kehang/Recrystalization/ML/test_model/predict.xyz" 
    forces_dft,forces_nn = parity_force(dft_path, mlff_path)
    # plot
    plt.figure(figsize=(8, 5))
    plt.rcParams['font.size'] = 14
    plt.plot(np.linspace(-lim,lim),np.linspace(-lim,lim),'r')
    plt.scatter(forces_dft,forces_nn, color='C0',s=4)
    plt.xlabel('DFT forces [eV/A]')
    plt.ylabel('NN forces [eV/A]')
    plt.axis([-lim,lim,-lim,lim])
    #plt.savefig('parity_CDP_l2.png')
    plt.savefig('parity_CDP_l2NVT.png')
    plt.show()