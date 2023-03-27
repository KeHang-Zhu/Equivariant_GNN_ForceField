#!/bin/sh
#SBATCH --job-name=Li3PO4_md
#SBATCH -p gpu
#SBATCH -N 1
#SBATCH -n 1
#SBATCH -t 5-00:00    
#SBATCH --mem-per-cpu=40000
#SBATCH --gres=gpu:1
#SBATCH --constraint=a100
#SBATCH -e %x_%j.err
#SBATCH -o %x_%j.out
# load modules + env
module load Anaconda3/2020.11
module load cmake/3.23.2-fasrc01
module load cuda/11.1.0-fasrc01
module load gcc/10.2.0-fasrc01
module load openmpi/4.1.0-fasrc01
module load intel-mkl/2019.5.281-fasrc01
module load cudnn/8.1.0.77_cuda11.2-fasrc01
source activate allegro-nov23

date
nvidia-smi 
# paths
    
srun -n $SLURM_NTASKS /n/home09/zkh/lammps/build/lmp -var SEED $RANDOM  -in md_li3_input.in
