import random

from mesa import *
from mesa.time import RandomActivation
from mesa.space import SingleGrid

from Burgler import Burgler
from LatticeAgent import LatticeAgent
import math



class BurglaryModel(Model):

    DELTA_T = 1/100
    OMEGA = 1/15
    A0 = 1/30

    eta = 0
    theta = 0
    gamma = 0

    avgA = A0
    varA = 0
    avgBD = theta*gamma/OMEGA
    avgN = (gamma*DELTA_T / (1 - math.exp(- avgA*DELTA_T)))

    id = 0
    """A model with some number of agents."""
    def __init__(self, width, height, eta, theta, gamma):
        super().__init__()
        self.grid = SingleGrid(width, height, True)
        self.schedule = RandomActivation(self)
        self.eta = eta
        self.theta = theta
        self.gamma = gamma
        self.nAgents = width*height

        self.avgA = self.A0
        self.avgBD = theta * gamma / self.OMEGA
        self.avgN = (gamma * self.DELTA_T / (1 - math.exp(- self.avgA * self.DELTA_T)))

        for i in range(width):
            for j in range(height):

                newId =  self.id + 1
                newAgent = LatticeAgent(newId, self, [], (j,i))
                self.schedule.add(newAgent)
                self.grid.position_agent(newAgent, j, i)
                self.id = newId+1

        for k in range(round(self.avgN*width*height)):
            acell = random.choice(self.schedule.agents)
            acell.burglers.append(Burgler())



    def step(self):
        self.schedule.step()
        for agent in self.schedule.agents :
            self.avgA = (self.avgA + agent.attractiveness)/2
            self.avgBD = (self.avgBD + agent.burglerDynamic)/2
            self.avgN = (self.avgN + len(agent.burglers))/2
        sumV = 0
        for agent in self.schedule.agents :
            sumV = (agent.attractiveness - self.avgA)*(agent.attractiveness - self.avgA)
        self.varA = sumV/(len(self.schedule.agents)-1)
