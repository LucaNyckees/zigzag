
# Levelset Zigzag Persistent Homology Computations

This project is supervised by Kathryn Hess Bellwald, from the [Laboratory of Topology and Neuroscience at EPFL](https://www.epfl.ch/labs/hessbellwald-lab/).

## Table of Content 🗃

* [People](#people)
* [Description](#description)
* [Project Organization](#project-organization)
* [Related Articles and Useful References](#refs)

## People 👤

[Nicolas Berkouk](https://people.epfl.ch/nicolas.berkouk),
[Luca Nyckees](https://people.epfl.ch/luca.nyckees)

## Description 💡

Zigzag persistence, as introduced by Carlsson and De Silva [[1]](https://arxiv.org/abs/0812.0197), offers a way to better understand the persistence of topological features observed in a family of spaces or pointclouds by generalizing the setting of persistent homology. In this project, we aim at providing a tool to compute levelset zigzag persistence. The idea is to deduce the results from computations on extended persistence, which are already implemented in C++. To this end, we make use of Python bindings.

## Project Organization 📄🗂
------------

    ├── README.md          <- Top-level README.
    │
    ├── notebooks          <- Jupyter notebooks.
    │
    ├── articles           <- Related articles and useful references.
    │
    ├── reports            <- Notes and report (Latex, pdf).
    │   └── figures        <- Optional graphics and figures to be included in the report.
    │
    ├── requirements.txt   <- Requirements file for reproducibility.
    └── src                <- Project source code.
   
--------

## Related Articles and Useful References 📗🔍

[[1]](https://arxiv.org/abs/0812.0197) - Zigzag Persistence\
[[2]](https://arxiv.org/abs/2105.00518) - Computing Optimal Persitent Cycles for Levelset Zigzag on Manifold-like Complexes\
[[3]](https://arxiv.org/abs/0911.2142) - Quantifying Transversality by Measuring the Robustness of Intersections\
[[4]](https://www.mrzv.org/publications/robustness-levelsets/esa/) - The Robustness of Level Sets
