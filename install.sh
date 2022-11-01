conda deactivate
jupyter kernelspec remove real_impact_of_inflation_env -y
conda env remove -n real_impact_of_inflation_env
conda create -n real_impact_of_inflation_env anaconda -y
conda activate real_impact_of_inflation_env
conda install -c conda-forge pandas -y
pip install plotly
conda deactivate
python -m ipykernel install --user --name real_impact_of_inflation_env