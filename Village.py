# Implementation of Village class

import Lib
import Meeple
import numpy
import random

class Village():
    def __init__(self) -> None:
        self.meeples = []
        self.farm_knowledge = random.random(Lib.MIN_FARM_KNOWLEDGE, Lib.MAX_INITIAL_FARM_KNOWLEDGE)
        self.health_knowledge = random.random(Lib.MIN_HEALTH_KNOWLEDGE, Lib.MAX_INITIAL_HEALTH_KNOWLEDGE)
        self.day = 0
        self.escape = 0.0
        self.food = 0

    def new_farmer(self, id) -> Meeple.Farmer:
        farmer = Meeple.Farmer(id)
        farmer.food_production_rate = Lib.calc_new_farmer_rate(farmer.intelligence, self.farm_knowledge)
        return farmer

    def new_doctor(self, id) -> Meeple.Doctor:
        doctor = Meeple.Doctor(id)
        doctor.healing_power = Lib.calc_new_doctor_rate(doctor.intelligence, self.health_knowledge)
        return doctor 

    def create_village(farmers, doctors, researchers) -> None:
        pass