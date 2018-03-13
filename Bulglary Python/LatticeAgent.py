from mesa import *
from BurglaryModel import *
import random

from Burgler import Burgler


class LatticeAgent(Agent):
    burglers = []
    attractiveness = 0.
    burglerDynamic = 0.
    occurredBurgs = 0
    pos = (0, 0)

    def __init__(self, uniqueID, model, burglers, pos):
        """

        :type model: BurglaryModel
        """
        super().__init__(uniqueID, model)
        self.attractiveness = model.A0
        self.burglers = burglers
        self.burglerDynamic = model.avgBD
        self.pos = pos

    def step(self):
        self.attractiveness = self.model.A0 + self.burglerDynamic
        self.criminalActivity()

    '''
    def move(self):
        possible_steps = self.model.grid.get_neighborhood(
            self.pos,
            moore=False,  # Using Von Neumann neighborhood
            include_center=False,
            torous=True)

        new_position = random.choice(possible_steps)  # TODO implementare reale movimento dei ladri
        self.model.grid.move_agent(self, new_position)  # TODO ^
        '''

    def criminalActivity(self):
        for badGuy in self.burglers:
            if badGuy.steal(self.attractiveness, self.model.DELTA_T):
                self.burglers.remove(badGuy)
                self.occurredBurgs += 1
            else:
                b = badGuy
                neighbors = self.model.grid.get_neighbors(
                    self.pos,
                    moore=False,  # Using Von Neumann neighborhood
                    include_center=False)#,
                    #torous=True)
                stillHere = True
                attrNeig = 0

                for n in neighbors:
                    attrNeig += n.attractiveness

                for n in neighbors:
                    qMove = n.attractiveness/attrNeig
                    if random.random() < qMove and stillHere:
                        stillHere = False
                        n.burglers.append(b)

                if stillHere:
                    newLattice = random.choice(neighbors)
                    newLattice.burglers.append(b)
                self.burglers.remove(badGuy)


    def updateVariables(self):
        eta = self.model.eta
        theta = self.model.theta
        omega = self.model.OMEGA
        gamma = self.model.gamma
        self.occurredBurgs = 0
        sumNeighbors = 0.
        neighbors = self.model.grid.get_neighbors(
            self.pos,
            moore=False,  # Using Von Neumann neighborhood
            include_center=False)#,
            #torous=True)
        for n in neighbors:
            sumNeighbors += n.burglerDynamic
        self.burglerDynamic = (((((1 - eta) * self.burglerDynamic) + ((eta / 4)  *
                                sumNeighbors)) * (1 - omega * self.model.DELTA_T)) + (theta * self.occurredBurgs))
        if random.random() < gamma :
            self.burglers.append(Burgler())

