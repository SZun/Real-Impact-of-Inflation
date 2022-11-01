conda deactivate
jupyter kernelspec remove real_impact_of_inflation_env -y
conda env remove -n real_impact_of_inflation_env
conda create -n real_impact_of_inflation_env anaconda -y
conda activate real_impact_of_inflation_env
conda install -c conda-forge pandas -y
pip install plotly
conda deactivate
conda remove nb_conda_kernels -y
conda install -c conda-forge nb_conda_kernels -y