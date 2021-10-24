# Implementation of Meeple Class

import Lib
import numpy
import random

class Meeple():
    def __init__(self, id: int) -> None:
        self.id = id
        self.name = Lib.random_name()
        self.hunger = 100
        self.health = 100
        self.intelligence: float = numpy.random.normal(Lib.INTELLIGENCE_MEAN, Lib.INTELLIGENCE_STDEV)
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
    def __init__(self, id: int) -> None:
        super().__init__(id)
        self.food_production_rate = Lib.MIN_FARM_KNOWLEDGE
    def __repr__(self) -> str:
        return super().__repr__() + ' : farmer'
    # TODO
    def produce(self) -> int:
        return Lib.net_production(self.food_production_rate, self.hunger, self.health)
    def boost(self) -> None:
        self.food_production_rate += Lib.boost_amounts(Lib.MAX_FARM_KNOWLEDGE-Lib.MIN_FARM_KNOWLEDGE)

class Doctor(Meeple):
    def __init__(self, id) -> None:
        super().__init__(id)
        self.healing_power = Lib.MIN_HEALTH_KNOWLEDGE
    def __repr__(self) -> str:
        return super().__repr__() + ' : doctor'
    # TODO
    def heal(self, meeples) -> None:
        pass
    def boost(self) -> None:
        self.healing_power += int(Lib.boost_amounts(Lib.MAX_HEALTH_KNOWLEDGE-Lib.MIN_HEALTH_KNOWLEDGE))

class Researcher(Meeple):
    def __init__(self, id) -> None:
        super().__init__(id)
        self.farm_research_rate = Lib.MIN_FARM_RESEARCH_RATE
        self.health_research_rate = Lib.MIN_HEALTH_RESEARCH_RATE
        self.escape_research_rate = Lib.MIN_ESCAPE_RESEARCH_RATE
    def __repr__(self) -> str:
        return super().__repr__() + ' : researcher'
    def research(self) -> tuple:
        return Lib.research_amounts(self.intelligence, self.farm_research_rate, self.health_research_rate, self.escape_research_rate)
    def boost(self) -> None:
        self.farm_research_rate += Lib.boost_amounts(Lib.MAX_FARM_RESEARCH_RATE-Lib.MIN_FARM_RESEARCH_RATE)        
        self.health_research_rate += Lib.boost_amounts(Lib.MAX_HEALTH_RESEARCH_RATE-Lib.MIN_HEALTH_RESEARCH_RATE) 
        self.escape_research_rate += Lib.boost_amounts(Lib.ESCAPE_POINT) 

    