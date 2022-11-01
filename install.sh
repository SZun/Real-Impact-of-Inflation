jupyter kernelspec remove real_impact_of_inflation_env
conda env remove -n real_impact_of_inflation_env
conda env create -f environment.yml
jupyter kernelspec remove dev
conda install -c conda-forge nb_conda_kernels -y
jupyter lab