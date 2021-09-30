#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 18:48:04 2020

@author: jam
"""


#%% local functions
import os
script_path = ""

try:
    script_path = os.path.dirname(__file__)
    os.chdir(script_path)
except FileNotFoundError:
    script_path = os.getcwd()
else:
    script_path = os.getcwd()

import sys
sys.path.append("..")

from IPython.core.display import display

import matplotlib as mpl
mpl.rc('text', usetex = True)
mpl.rc('font', size = 10)
import numpy as np
import pandas as pd


#%% plot of the Gini and Hoover index for the constant difference initialization

def gini_index_const_calc(init_wealth,num_agents):
    agents_capital = [init_wealth+i for i in range(num_agents)]
    return sum([abs(xi-xj) for xi in agents_capital for xj in agents_capital ]) /(2*num_agents*sum(agents_capital))


def hoover_index_const_calc(init_wealth,num_agents):
    agents_capital = [init_wealth+i for i in range(num_agents)]
    mean_capital = (1/num_agents)*sum(agents_capital)
    
    return (0.5/sum(agents_capital))*sum([abs(xi - mean_capital) for xi in agents_capital])

# data for selected initial_capital
initial_capital = 20

gini_data_const = [gini_index_const_calc(initial_capital,n) for n in range(20,201,20)]
hoover_data_const = [hoover_index_const_calc(initial_capital,n) for n in range(20,201,20)]

np.savetxt(script_path + "/data/gini_index_values-constant.dat",gini_data_const)


# %% Gini, Hoover and Theil

fig = mpl.figure.Figure(figsize=(3.25,2.4375))
axs = fig.add_subplot()

# axs.set_xlim((15,145))
axs.set_xticks(range(20,206,20))

axs.grid(alpha=0.75,ls=':')

axs.set_ylim((0.1,0.8))
axs.set_yticks(np.arange(0.0,0.81,0.1))
axs.set_ylabel('Inequality index')
axs.set_xlabel('Number of agents')
axs.plot(list(np.arange(20,202,20)),gini_data_const,'b.--',label="Gini",markersize='12',fillstyle='none')
axs.plot(list(np.arange(20,202,20)),hoover_data_const,'g+:', label="Hoover")

# axs.plot(list(np.arange(20,142,20)),theil_data_conts[20:141:20],'rx-.', label="Theil")

fig.legend(loc='upper center',ncol=1,bbox_to_anchor=(0.7,0.85))

display(fig)

fig.tight_layout()
fig.savefig("plots/indices_values-constant.pdf")

# # %%  Gini index only
# fig = mpl.figure.Figure(figsize=(3.25,2.4375))
# axs = fig.add_subplot()

# axs.set_xlim((15,145))
# axs.set_xticks(range(25,146,20))

# axs.grid(alpha=0.75,ls=':')

# axs.set_ylim((0.1,0.8))
# axs.set_yticks(np.arange(0.1,0.81,0.1))
# axs.set_ylabel('Inequality index')
# axs.set_xlabel('Number of agents')
# axs.plot(list(np.arange(20,142,10)),gini_data_const,'x:')

# display(fig)

# fig.tight_layout()
# fig.savefig("../plots/gini_index_values-constant.pdf")


#%% plot of the Gini index for the constant initialization

# gini_data_bg = pd.read_csv(script_path + "data/gini_index_values-boltzmann-gibbs.zip")

ineq_data_bg =  pd.read_csv(script_path + "/data/ineq_index_values-boltzmann-gibbs.zip")
                         
#%%

                         
fig = mpl.figure.Figure(figsize=(3.25,2.4375))
axs = fig.add_subplot()

# axs.set_xlim((15,145))
axs.set_xticks(range(20,206,20))

axs.set_yticks(np.arange(0.0,0.81,0.1))
axs.grid(alpha=0.75,ls=':')
axs.set_ylim((0.1,0.8))
# axs.set_ylabel('Gini index')
axs.set_xlabel('Number of agents')
# axs.plot(gini_data_bg['num_agents'], gini_data_bg['min'],'bx:', label="min")
# axs.plot(gini_data_bg['num_agents'], gini_data_bg['max'],'r+:', label="max")
axs.plot(ineq_data_bg['num_agents'], ineq_data_bg['mean_gini'],'b.--', label="Gini",markersize='12',fillstyle='none')
axs.fill_between(ineq_data_bg['num_agents'],ineq_data_bg['min_gini'], ineq_data_bg['max_gini'],alpha=0.3, color='darkblue',linestyle='--')

axs.plot(ineq_data_bg['num_agents'], ineq_data_bg['mean_hoover'],'g+:', label="Hoover",color='darkgreen')
axs.fill_between(ineq_data_bg['num_agents'],ineq_data_bg['min_hoover'], ineq_data_bg['max_hoover'],alpha=0.3, color='green',linestyle=':')
# 
# axs.plot(ineq_data_bg['num_agents'], ineq_data_bg['mean_theil'],'rx-', label="Theil")
# axs.fill_between(ineq_data_bg['num_agents'],ineq_data_bg['min_theil'], ineq_data_bg['max_theil'],alpha=0.25,color='red',capstyle='round')


# axs.legend(ncol=3,loc='lower right',  fontsize=10, labelspacing=0, columnspacing=1)
display(fig)

fig.tight_layout()
fig.savefig("plots/ineq_values-boltzman-gibbs.pdf")

#%% plot of the Gini index for both initilizations
# fig = mpl.figure.Figure(figsize=(3.25,2.4375))
# axs = fig.add_subplot()

# axs.set_xlim((15,145))
# axs.grid()
# axs.set_ylim((0.1,0.8))
# axs.set_ylabel('Gini index')
# axs.set_xlabel('Number of agents')
# axs.plot(gini_data_bg['num_agents'], gini_data_bg['min'],'bx--', label="B-G (min)")
# axs.plot(gini_data_bg['num_agents'], gini_data_bg['max'],'r+-.', label="B-G (max)")
# axs.plot(gini_data_bg['num_agents'], gini_data_bg['mean'],'g.:', label="B-G (mean)")

# # axs.plot(gini_data_bg['num_agents'], gini_data_bg['mean'],'k.:', label="mean")
# axs.plot(list(np.arange(20,142,10)),gini_data_conts[20:141:10],'k:', label="const.", linewidth=2)

# axs.legend(ncol=2,loc='best', fontsize=10, labelspacing=0, columnspacing=1)
# display(fig)

# fig.tight_layout()
# fig.savefig("../plots/gini_values.pdf")
