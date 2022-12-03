#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 15:14:18 2020

@author: jam
"""

#%% basic imports

import scipy.stats as sps
import numpy as np
import pandas as pd


#%% local functions

script_path = ""

import os
try:
    script_path = os.path.dirname(__file__)
    os.chdir(script_path)
except FileNotFoundError:
    script_path = os.getcwd()
else:
    script_path = os.getcwd()

import sys
sys.path.append("..")

def gini_index(vec):
    agent_wealths = sorted(vec)
    N = len(vec)
    #return sum([(2*(i+1)-N-1)*x for i,x in enumerate(agent_wealths) ])/(N*sum(agent_wealths))
    
    return sum([abs(xi-xj) for xi in agent_wealths for xj in agent_wealths ]) /(2*N*sum(agent_wealths))

def hoover_index(vec):
    agent_wealths = sorted(vec)
    N = len(vec)
    mean_wealth = sum(agent_wealths)/N
    return sum([abs(xi-mean_wealth) for xi in agent_wealths])/(2*sum(agent_wealths))

def theil_index(vec):
    agent_wealths = sorted(vec)
    N = len(vec)
    mean_wealth = sum(agent_wealths)/N
    return 1/N*sum([(xi/mean_wealth)*np.log(xi/mean_wealth) for xi in filter(lambda x:x>0,agent_wealths)])

#%% deriviation of the shape parameters
# lambda_ - inverse temperature
# N - {0,1,..,N} -support of the distribution

# number of agents, 
# each agent has m_i=2+i money, i-1,2,3,..,num_agents 

#%% main loop
ineq_index_data_bg = pd.DataFrame([],columns=['num_agents',
                                              'min_gini', 'max_gini', 'median_gini', 'mean_gini',
                                              'min_hoover', 'max_hoover', 'median_hoover', 'mean_hoover',
                                              'min_theil', 'max_theil', 'median_theil', 'mean_theil'])

for num_agents in range(120, 121, 20):
   
    initial_capital = 20
    sum_money = (1+num_agents)*(2*initial_capital+num_agents)//2
     
    lambda_, N = num_agents/sum_money, sum_money
    print("agents: "+str(num_agents))
    print("money: "+str(sum_money))
    sample = [ sps.boltzmann.rvs(lambda_, N, size=num_agents) for _ in range(10000)]
    sample_gini = list(map(gini_index,sample))
    sample_hoover = list(map(hoover_index,sample))
    sample_theil = list(map(theil_index,sample))
    
    tmp_df = pd.DataFrame(
        [(num_agents, min(sample_gini), max(sample_gini),  np.mean(sample_gini),  np.median(sample_gini),
          min(sample_hoover), max(sample_hoover),  np.mean(sample_hoover),  np.median(sample_hoover),
          min(sample_theil), max(sample_theil),  np.mean(sample_theil),  np.median(sample_theil))],
        columns=['num_agents','min_gini','max_gini', 'median_gini', 'mean_gini',
                 'min_hoover', 'max_hoover', 'median_hoover', 'mean_hoover',
                 'min_theil', 'max_theil', 'median_theil', 'mean_theil'])
    ineq_index_data_bg = ineq_index_data_bg.append(tmp_df,ignore_index=True)

  
#%% data saving
ineq_index_data_bg.to_csv("data/ineq_index_values-boltzmann-gibbs_v2.zip", index=False, compression=dict(method='zip', archive_name='data.csv'))