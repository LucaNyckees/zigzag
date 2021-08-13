
# Levelset Zigzag Persistent Homology Computations

## Table of Content

* [People](#people)
* [Project Organization](#project-organization)
* [Description](#description)
* [Useful References](#refs)

## People

[Nicolas Berkouk](https://people.epfl.ch/nicolas.berkouk),
[Luca Nyckees](https://people.epfl.ch/luca.nyckees)

## Description

In this project we aim at providing a tool to compute levelset zigzag persistence. The idea is to deduce the results from computations on extended persistence, which are already implemented in C++. To this end, we make use of Python bindings.

Project Organization
------------

    ├── LICENSE
    ├── Makefile           <-- Makefile facilitating multiple commands
    ├── README.md          <- Top-level README.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for ML/modelling.
    │   └── raw            <- The original, immutable data dump. Do not modify these datas, as they contribute to the experiment reproducibility
    │
    ├── docs               <- Future Sphinx documentation
    │
    ├── models             <- Trained and serialized (saved) models
    │
    ├── notebooks          <- Jupyter notebooks.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Future report (Latex, pdf)
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment.
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    └── src                <- Source code for use in this project.
        ├── __init__.py    <- Makes src a Python package (and not just a module)
        │
        ├── data           <- Scripts to download or generate data
        │
        ├── features       <- Scripts to turn raw data into features for modeling
        │   └── build_features.py
        │
        ├── models         <- Scripts to train models and use trained models to make
        │
        └── visualization  <- Scripts to create exploratory and results oriented visualizations
--------

## Useful References
