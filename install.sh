conda env create -f environment.yml
jupyter kernelspec remove dev
conda activate workingtitleenv
conda install -c conda-forge nb_conda_kernels -y
conda deactivate