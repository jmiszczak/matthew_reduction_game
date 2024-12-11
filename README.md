[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.5541170.svg)](https://doi.org/10.5281/zenodo.5541170)


# matthew_reduction_game

This software provides implementation of games on networks for controlling the inequalities in the capital
distribution (a.k.a. Janosik model).

Software and data in this repository were used in the manuscript:

J.A. Miszczak, *Constructing games on networks for controlling the inequalities in the capital distribution*, Physica A: Statistical Mechanics and its Applications, Volume 594, 15 May 2022, 126997 DOI:[10.1016/j.physa.2022.126997](https://doi.org/10.1016/j.physa.2022.126997), arXiv:[2201.10913](https://arxiv.org/abs/2201.10913).

This version was created using Mesa 0.8, and it will not work with the current version. For running the specific version fof mesa, it is recommend to use ```venv``` module.

## Quick start

Main functionality is contained within `src/model` folder. To run a simulation of the base model with capital
distribution initialized using constant difference of capital, run

    python Janosik_grid2d_batch.py uniform

Here the last parameter can be `uniform` or `boltzmann`.

Example of the model with Parrondo's game used for policy selection can be run as

    python JanosikParrondo_grid2d_batch.py nagents

where the parameter `nagents` is used to define a number of agents in the network. Please note tha only equal difference
methods (i.e. uniform) is used for this case.

In all case simulation is executed using parallel capabilities of Mesa library. The number of cored used in the
simulation is controlled by the `nr_processes` parameter of `BatchRunnerMP` class.

## Package organization and installation

The provided files can be used to reproduce all the results presented in the accompanying manuscript. They can be also
used to extend the models and run simulations using random graphs models.

### Description of subdirectories

* `src/model` includes model used in the manuscript,
* `src/scripts` contains some extra scripts used in the manuscript,
* `data` is used to store simulation results and can be used to store graphs generated for running simulations,
* `plots` is used to store final plots.

## Running the code

### Anaconda environment

You can use to install most of the required packages
	
	conda env create -f matthew_reduction_game.yml

and 

	pip install -e git+https://github.com/projectmesa/mesa#egg=mesa

to install the latest version of Mesa library.

This software was tested with

* Python 3.9.7
* Mesa 0.8.9
* NetworkX 2.6.3
* Pandas 1.3.3
* conda 4.10.3
* Ubuntu 20.04.3 LTS

### Using venv

To use the specific version of Mesa with a virtual environment, use the following commands:

    python3 -m venv ~/VEnvs/mesa-0.8
    . ~/VEnvs/mesa-0.8/bin/activate
    pip install mesa==0.8.9
    pip install ipython scipy matplotlib


## Publication

The presented results were published in

J.A. Miszczak, *Constructing games on networks for controlling the inequalities in the capital distribution*, Physica A: Statistical Mechanics and its Applications, Vol. 594 (2022), 126997, DOI:[10.1016/j.physa.2022.126997](https://doi.org/10.1016/j.physa.2022.126997), arXiv:[2201.10913](https://arxiv.org/abs/2201.10913) 


```
@article{miszczak2022constructing,
  title = {Constructing games on networks for controlling the inequalities in the capital distribution},
  author = {Miszczak, Jaros{\l}aw Adam},
  journal = {Physica A: Statistical Mechanics and its Applications},
  volume = {594},
  pages = {126997},
  year = {2022},
  doi = {10.1016/j.physa.2022.126997}
}
```

### Contact information

Responsible person: Jarosław Miszczak
