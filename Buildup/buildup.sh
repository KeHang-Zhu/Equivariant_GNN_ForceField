salloc -p gpu_requeue -t 0-01:00 --mem 8000 --gres=gpu:1
module load Anaconda3/2020.11 cuda/11.1.0-fasrc01 
conda create --name allegro-nov23 python=3.9
source activate allegro-nov23
conda install pytorch==1.11 cudatoolkit=11.1 -c pytorch -c nvidia

cd ~
mkdir nequip-v0.5.5-pt1.11
cd nequip-v0.5.5-pt1.11

pip install wandb
git clone https://github.com/mir-group/nequip.git


cd nequip/
pip install -e .

cd ~
mchrokdir allegro-nov23-22
cd allegro-nov23-22/
git clone --depth 1 https://github.com/mir-group/allegro.git
cd allegro
pip install -e . 
