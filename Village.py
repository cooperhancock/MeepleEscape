# Implementation of Village class

import Lib
import Meeple
import numpy
import random

class Village():
    def __init__(self) -> None:
        self.meeples = []
        self.farm_knowledge = random.uniform(Lib.MIN_FARM_KNOWLEDGE, Lib.MAX_INITIAL_FARM_KNOWLEDGE)
        self.health_knowledge = random.uniform(Lib.MIN_HEALTH_KNOWLEDGE, Lib.MAX_INITIAL_HEALTH_KNOWLEDGE)
        self.day = 0
        self.escape = 0.0
        self.food = 0
        self.report = []

    def __repr__(self) -> str:
        s = 'Village:\n'
        s += 'day: ' + str(self.day)
        s += ', food: ' + str(self.food)
        s += ', rates: ' + str(self.farm_knowledge) + ' ' + str(self.health_knowledge) + ' ' + str(self.escape)
        s += '\nPeople:\n'
        for m in self.meeples:
            s += str(m) + '\n'
        return s

    def new_farmer(self, id) -> Meeple.Farmer:
        farmer = Meeple.Farmer(id)
        farmer.food_production_rate = Lib.calc_new_farmer_rate(farmer.intelligence, self.farm_knowledge)
        return farmer

    def new_doctor(self, id) -> Meeple.Doctor:
        doctor = Meeple.Doctor(id)
        doctor.healing_power = Lib.calc_new_doctor_rate(doctor.intelligence, self.health_knowledge)
        return doctor 

    def new_researcher(self, id) -> Meeple.Researcher:
        researcher = Meeple.Researcher(id)
        research_rates = Lib.calc_new_researcher_rates(researcher.intelligence, self.farm_knowledge, self.health_knowledge, self.escape)
        researcher.farm_research_rate = research_rates[0]
        researcher.health_research_rate = research_rates[1]
        researcher.escape_research_rate = research_rates[2]
        return researcher

    def populate(self, farmers, doctors, researchers) -> None:
        i = 0
        for f in range(farmers):
            self.meeples.append(self.new_farmer(i))
            i+=1
        for d in range(doctors):
            self.meeples.append(self.new_doctor(i))
            i+=1
        for r in range(researchers):
            self.meeples.append(self.new_researcher(i))
            i+=1
        for m in self.meeples:
            self.food += m.diet

    def reassign(self, id, job):
        old_meeple = self.meeples[id]
        if job == 'f':
            self.meeples[id] = self.new_farmer(id)
        if job == 'd':
            self.meeples[id] = self.new_doctor(id)
        if job == 'r':
            self.meeples[id] = self.new_researcher(id)
        new_meeple = self.meeples[id]
        new_meeple.name = old_meeple.name
        new_meeple.hunger = old_meeple.hunger
        new_meeple.health = old_meeple.health
        new_meeple.intelligence = old_meeple.intelligence
        new_meeple.diet = old_meeple.diet

if __name__ == "__main__":
    village = Village()
    village.populate(3,3,3)
    print(village)
    village.reassign(8, 'f')
    print(village)