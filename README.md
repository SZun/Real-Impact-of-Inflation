# Real Impact of Inflation

Our project is to uncover the difference between the reported and actual urban inflation. We will be using the CPI data, from the Bureau of Labor Statistics, with and without food and energy costs to answer this question. Additionally, we will also be analyzing the differences in inflation between the various US regions, compared to the national average, over time.

## [Notebook](./Real-Impact-of-Inflation.ipynb)

<!-- Images Here -->
<!-- []() -->


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

### Installation
```
$ git clone git@github.com:SZun/Real-Impact-of-Inflation.git
$ cd Real-Impact-of-Inflation
$ conda activate base
$ jupyter kernelspec remove real_impact_of_inflation_env -y
$ conda env remove -n real_impact_of_inflation_env
$ conda create -n real_impact_of_inflation_env anaconda -y
$ conda activate real_impact_of_inflation_env
$ conda install -c conda-forge pandas panel geoviews hvplot cartopy -y
$ pip install plotly==5.11.0
$ conda activate base
$ conda remove nb_conda_kernels -y
$ conda install -c conda-forge nb_conda_kernels -y
```

## Built With

- [Plotly](https://plotly.com/python/) - Visualization library
- [Pandas](https://pandas.pydata.org/docs/#) - Data maniupulation library
- [Numpy](https://numpy.org/) - Multi-dimensional array library
- [Matplotlib](https://matplotlib.org/stable/index.html) - Visualization library

## Authors
- **Gabriel Millan** - [LinkedIn](https://www.linkedin.com/in/millangabriel/) | [Github](https://github.com/gjmillan)
- **Samuel Farrell** - [LinkedIn](https://www.linkedin.com/in/samuelcfarrell/) | [Github](https://github.com/SamCFarrell)
- **Sami Naeem** - [LinkedIn](https://www.linkedin.com/in/sami-naeem/) | [Github](https://github.com/SZun)
- **Sam G Zun** - [LinkedIn](https://www.linkedin.com/in/szun/) | [Github](https://github.com/SZun)
