#!/bin/sh
#SBATCH --job-name=Li3PO4_flare
#SBATCH -p gpu
#SBATCH -N 1
#SBATCH -n 1
#SBATCH -t 4-00:00    
#SBATCH --mem-per-cpu=20000
#SBATCH --gres=gpu:1
#SBATCH --constraint=a100
#SBATCH -e %x_%j.err
#SBATCH -o %x_%j.out
# load modules + env
module load Anaconda3/2020.11
module load cmake/3.17.3-fasrc01
module load gcc/9.3.0-fasrc01 intel-mkl/2017.2.174-fasrc01 openmpi/4.0.5-fasrc01
source activate flare

date
nvidia-smi

export ASE_VASP_COMMAND="srun -n ${SLURM_NTASKS} --mpi=pmi2 /n/holystore01/LABS/kozinsky_lab/Lab/Software/VASP6.3/vasp.6.3.0/bin/vasp_std"  #vasp exec
export VASP_PP_PATH="/n/holystore01/LABS/kozinsky_lab/Lab/Software/VASP6.3/Potentials_54"
export LD_PRELOAD=/n/sw/intel-cluster-studio-2017/mkl/lib/intel64/libmkl_def.so:/n/sw/intel-cluster-studio-2017/mkl/lib/intel64/libmkl_avx2.so:/n/sw/intel-cluster-studio-2017/mkl/lib/intel64/libmkl_intel_thread.so:/n/sw/intel-cluster-studio-2017/mkl/lib/intel64/libmkl_core.so:/n/sw/intel-cluster-studio-2017/lib/intel64_lin/libiomp5.so

export OMP_NUM_THREADS=$SLURM_NTASKS_PER_NODE

flare-otf Li3PO4_flare.yaml
