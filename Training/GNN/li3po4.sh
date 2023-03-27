#!/bin/sh
#SBATCH --job-name=20230301_Li
#SBATCH -p gpu
#SBATCH -N 1
#SBATCH -n 1
#SBATCH -t 3-00:00    
#SBATCH --mem-per-cpu=100000
#SBATCH --gres=gpu:1
#SBATCH --constraint=a100
#SBATCH -e %x_%j.err
#SBATCH -o %x_%j.out
#SBATCH --mail-user=kehangzhu@gmail.com
# load modules + env
module load Anaconda3/2020.11 
module load cmake/3.23.2-fasrc01
module load cuda/11.1.0-fasrc01
module load gcc/10.2.0-fasrc01
module load openmpi/4.1.0-fasrc01
module load intel-mkl/2019.5.281-fasrc01
module load cudnn/8.1.0.77_cuda11.2-fasrc01 
source activate allegro-nov23

# run allegro to train the potential
nequip-train li3.yaml
