#!/bin/sh
#SBATCH --job-name=ML-test
#SBATCH -p gpu
#SBATCH -o OUT.out
#SBATCH -e Err.err
#SBATCH -n 1
#SBATCH -N 1
#SBATCH -t 0-03:00
#SBATCH --mem-per-cpu=30000
#SBATCH --gres=gpu:1
##SBATCH --mail-type=ALL
##SBATCH --mail-user=kehang_zhu@fas.harvard.edu
#SBATCH --no-requeue

module load Anaconda3/2020.11
module load cmake/3.23.2-fasrc01
module load cuda/11.1.0-fasrc01
module load gcc/10.2.0-fasrc01
module load openmpi/4.1.0-fasrc01
module load intel-mkl/2019.5.281-fasrc01
module load cudnn/8.1.0.77_cuda11.2-fasrc01
source activate allegro-nov23

date
# paths

nequip-evaluate --model /n/holyscratch01/kozinsky_lab/Kehang/Recrystalization/high-speed5/Li-deployed.pth --dataset-config new-data.yaml --metrics-config metric.yaml
# srun -n $SLURM_NTASKS /n/home09/zkh/lammps/build/lmp -var SEED $RANDOM  -in md_li3_input.in
