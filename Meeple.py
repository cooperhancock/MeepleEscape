# Implementation of Meeple Class

import Lib
import numpy
import random

class Meeple():
    def __init__(self, id) -> None:
        self.id = id
        self.name = Lib.random_name()
        self.hunger = 100
        self.health = 100
        self.intelligence = numpy.random.normal(Lib.INTELLIGENCE_MEAN, Lib.INTELLIGENCE_STDEV)
        if self.intelligence > 1: self.intelligence = 1.0
        if self.intelligence < 0: self.intelligence = 0.0
        self.diet = random.randint(Lib.MIN_DIET, Lib.MAX_DIET)
    def __repr__(self) -> str:
        s = '['
        s += str(self.id) + ', '
        s += str(self.name) + ', '
        s += str(self.hunger) + ', '
        s += str(self.health) + ', '
        s += str(self.intelligence) + ', '
        s += str(self.diet) + ']'
        return s

class Farmer(Meeple):
    def __init__(self, id) -> None:
        super().__init__(id)
        self.food_production_rate = Lib.MIN_FARM_KNOWLEDGE
    def __repr__(self) -> str:
        return super().__repr__() + ' : farmer'

class Doctor(Meeple):
    def __init__(self, id) -> None:
        super().__init__(id)
        self.healing_power = Lib.MIN_HEALTH_KNOWLEDGE
    def __repr__(self) -> str:
        return super().__repr__() + ' : doctor'

class Researcher(Meeple):
    def __init__(self, id) -> None:
        super().__init__(id)
        self.farm_research_rate = Lib.MIN_FARM_RESEARCH_RATE
        self.health_research_rate = Lib.MIN_HEALTH_RESEARCH_RATE
        self.escape_research_rate = Lib.MIN_ESCAPE_RESEARCH_RATE
    def __repr__(self) -> str:
        return super().__repr__() + ' : researcher'

    