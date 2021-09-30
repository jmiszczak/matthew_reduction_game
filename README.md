[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.5541170.svg)](https://doi.org/10.5281/zenodo.5541170)


# Package matthew_reduction_game

This software provides implementation of games on networks for controlling the inequalities in the capital
distribution (a.k.a. Janoski model).

Software and data in this repository was used in the manuscript:

J.A. Miszczak, _Constructing games on networks for controlling the inequalities in the capital distribution_, (2021).

## Quick start

Main functionality is contained within `src/model` folder. To run a simulation of the base model with capital
distribution initialized using constant difference of capital, run

    python Janosik_grid2d_batch.py uniform

Here the last parameter can be `uniform` or `boltzmann`.

Example of the model with Parrondo's game used for policy selection can be run as

    python JanosikParrondo_grid2d_batch.py nagents

where the parameter `nagents` is used to define a number of agents in the network. Please note tha only equal difference
methods (i.e. uniform) is used for this case.

In all case simulation is executed using parallel capabilities of Mesa library. The number of cored ussed in the
simulation is controlled by the `nr_processes` parameter of `BatchRunnerMP` class.

## Package organization and installation

The provided files can be used to reproduce all the results presented in the accompanying manuscript. They can be also
used to extend the models and run simulations using random graphs models.

### Description of subdirectories

* `src/model` includes model used in the manuscript,
* `src/scripts` contains some extra scripts used in the manuscript,
* `data` is used to store simulation results and can be used to store graphs generated for running simulations,
* `plots` is used to store final plots.

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
