import mesa
import mesa.time as mt
import mesa.space as ms
import mesa.datacollection as md

import numpy.random as rnd
import scipy.stats as sps
import networkx as nx

import sys

sys.path.append('..')

import indicators

from JanosikAgent import JanosikAgent


class JanosikGraphModel(mesa.Model):
    """
    Model of with the agent implementing inequality reduction policies. 
    
    Positions of the agnets are defined using NetworkX graph.
    """

    def __init__(self, num_agents, graph_spec, init_capital,init_capital_dist, default_eps, default_boost):
        self.num_agents = num_agents
        self.agent_init_capital = []
        if init_capital_dist == "uniform":
            # assuming that init_capital is explicitly given
            self.agent_init_capital = init_capital
        elif init_capital_dist == "boltzmann":
            # assuming that only avergae is give as a string
            self.agent_init_capital = sps.boltzmann.rvs(1/int(init_capital), num_agents*int(init_capital), size=num_agents)
        else:
            raise("[ERROR] Unknown type of capital distribution.")
        
        self.running = True

        # chech if the graph is given as a path or as NetworkX graph
        if type(graph_spec) == nx.classes.graph.Graph:
            self.graph = ms.NetworkGrid(graph_spec)
        elif type(graph_spec) == str:
            self.graph = ms.NetworkGrid(nx.readwrite.read_gexf(graph_spec))

        # use random activation policy
        self.schedule = mt.RandomActivation(self)

        # create and add agents 
        for aid in range(self.num_agents):
            # select a graph node
            position = list(self.graph.G.nodes)[rnd.choice(range(len(list(self.graph.G.nodes))))]
            # create an agent
            agent = JanosikAgent(aid, self, position, default_eps, default_boost)
            # add it to the scheduler
            self.schedule.add(agent)
            # assign it to a location
            self.graph.place_agent(agent, position)

        # add data collector
        self.datacollector = md.DataCollector(
            model_reporters={"Gini index": indicators.gini_index,
                             "Total capital": indicators.total_capital,
                             "Mean capital": indicators.mean_capital,
                             "Median capital": indicators.median_capital,
                             "Min capital": indicators.min_capital,
                             "Max capital": indicators.max_capital
                             },
            agent_reporters={"Capital": "capital"}
        )

    def step(self):
        """Execute one step for all agents"""
        self.datacollector.collect(self)
        self.schedule.step()
