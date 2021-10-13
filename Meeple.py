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
        self.diet = random.randint(Lib.MIN_DIET, Lib.MAX_DIET)

class Farmer(Meeple):
    def __init__(self, id) -> None:
        super().__init__(id)
        self.food_production_rate = Lib.MIN_FARM_KNOWLEDGE

class Doctor(Meeple):
    def __init__(self, id) -> None:
        super().__init__(id)
        self.healing_power = Lib.MIN_HEALTH_KNOWLEDGE

class Researcher(Meeple):
    def __init__(self, id) -> None:
        super().__init__(id)
        self.farm_research_rate = Lib.MIN_FARM_RESEARCH_RATE
        self.health_research_rate = Lib.MIN_HEALTH_RESEARCH_RATE
        self.escape_research_rate = Lib.MIN_ESCAPE_RESEARCH_RATE

    