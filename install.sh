conda deactivate
conda update --all -y
jupyter kernelspec remove real_impact_of_inflation_env -y
conda env remove -n real_impact_of_inflation_env
conda create -n real_impact_of_inflation_env anaconda -y
conda activate real_impact_of_inflation_env
conda install -c conda-forge pandas panel geoviews hvplot cartopy -y
pip install --upgrade pip
pip install plotly==5.11.0
conda deactivate
conda remove nb_conda_kernels -y
conda install -c conda-forge nb_conda_kernels -y
jupyter lab