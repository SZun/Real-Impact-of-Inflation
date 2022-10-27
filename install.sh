jupyter kernelspec remove workingtitleenv
conda env remove -n workingtitleenv
conda env create -f environment.yml
jupyter kernelspec remove dev
conda install -c conda-forge nb_conda_kernels -y
jupyter lab