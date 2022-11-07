# Real Impact of Inflation

Our project is to uncover the difference between the reported and actual urban inflation. We will be using the CPI data, from the Bureau of Labor Statistics, with and without food and energy costs to answer this question. Additionally, we will also be analyzing the differences in inflation between the various US regions, compared to the national average, over time.

## Notebooks
- [Data Exploration](./Data-Exploration.ipynb)
- [Final Data Analysis](./Final-Data-Analysis.ipynb)

## Plots
![Plot1](./assets/images/average_regional_consumer_price_percentage_change_2012-2019.png)
![Plot2](./assets/images/average_regional_consumer_price_percentage_change_2020-2022.png)
![Plot3](./assets/images/categorical_consumer_price_correlations_2012-2019_plot.png)
![Plot4](./assets/images/categorical_consumer_price_correlations_2020-2022_plot.png)
![Plot5](./assets/images/monthly_regional_consumer_prices_january_2012_to_september_2022.png)
![Plot6](./assets/images/nationa_and_regional_consumer_prices_2012-2022_plot.png)
![Plot7](./assets/images/national_&_regional_consumer_prices_correlation_plot.png)
![Plot8](./assets/images/national_consumer_prices_2012-2022_plot.png)
![Plot9](./assets/images/national_consumer_prices_vs_national_consumer_prices_minus_food_&_energy_percent_changes_2012-2019_plot.png)
![Plot10](./assets/images/national_consumer_prices_vs_national_consumer_prices_minus_food_&_energy_percent_changes_2020-2022_plot.png)
![Plot11](./assets/images/national_price_vs_national_price_less_f&e_correlation_2012-2022_plot.png)
![Plot12](./assets/images/national_prices_vs_national_prices_less_f&e_-_consumer_prices_2012-2019_plot.png)
![Plot13](./assets/images/national_prices_vs_national_prices_less_f&e_-_consumer_prices_2012-2022_plot.png)
![Plot14](./assets/images/national_prices_vs_national_prices_less_f&e_-_consumer_prices_2020-2022_plot.png)
![Plot15](./assets/images/national_prices_vs_national_prices_less_f&e_-_percent_change_2012-2022_plot.png)
![Plot16](./assets/images/national_prices_vs_national_prices_less_f&e_-_percent_change_2012_2019_plot.png)
![Plot17](./assets/images/national_prices_vs_national_prices_less_f&e_-_percent_change_2020-2022_plot.png)
![Plot18](./assets/images/regions_consumer_prices_2012-2022_plot.png)


## Getting Started

### Prerequisites

You must have anaconda and conda installed

```
$ anaconda --version
```
*# EXAMPLE OUTPUT: "anaconda Command line client (version 1.11.0)"*
```
$ conda --verison
```
*# EXAMPLE OUTPUT: "conda 22.9.0"*

### Install Environmnet
```
conda create -n real_impact_of_inflation_env anaconda -y
conda activate real_impact_of_inflation_env
conda install -c conda-forge pandas panel geoviews hvplot cartopy pandas-profiling python-kaleido selenium -y
pip install plotly==5.11.0
python -m ipykernel install --user --name real_impact_of_inflation_env
```

### Clone Repository
```
git clone git@github.com:SZun/Real-Impact-of-Inflation.git
cd Real-Impact-of-Inflation
```

## Built With

- [Pandas](https://pandas.pydata.org/docs/#) - Data maniupulation library
- [Numpy](https://numpy.org/) - Multi-dimensional array library
- [Pandas Profiling](https://github.com/ydataai/pandas-profiling) - Generative reporting library
- [Panel](https://panel.holoviz.org/) - Visualization library for dashboards
- [Plotly](https://plotly.com/python/) - Visualization library for plots
- [Hvplot](https://hvplot.holoviz.org/) - Visualization library for Pandas-based plots
- [Geoviews](https://geoviews.org/#) - Visualization library for geographic data
- [Cartopy](https://scitools.org.uk/cartopy/docs/latest/) - Geospacial data processing library
- [Seaborn](https://seaborn.pydata.org/) - Visualization library
- [Pathlib](https://plotly.com/python/) - Python module for paths
- [Datetime](https://plotly.com/python/) - Python module for dates


## Authors
- **Gabriel Millan** - [LinkedIn](https://www.linkedin.com/in/millangabriel/) | [Github](https://github.com/gjmillan)
- **Samuel Farrell** - [LinkedIn](https://www.linkedin.com/in/samuelcfarrell/) | [Github](https://github.com/SamCFarrell)
- **Sami Naeem** - [LinkedIn](https://www.linkedin.com/in/samimuhammad/) | [Github](https://github.com/SZun)
- **Sam G Zun** - [LinkedIn](https://www.linkedin.com/in/szun/) | [Github](https://github.com/SZun)