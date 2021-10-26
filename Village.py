# Implementation of Village class

import Lib
import Meeple
import numpy
import random

class Village:
    def __init__(self) -> None:
        self.meeples = []
        self.farm_knowledge = random.uniform(Lib.MIN_FARM_KNOWLEDGE, Lib.MAX_INITIAL_FARM_KNOWLEDGE)
        self.health_knowledge = random.uniform(Lib.MIN_HEALTH_KNOWLEDGE, Lib.MAX_INITIAL_HEALTH_KNOWLEDGE)
        self.day = 0
        self.escape = 0.0
        self.food = 0
        self.report = ""
        self.end_report = ""

    def __repr__(self) -> str:
        s = 'Village:\n'
        s += 'day: ' + str(self.day)
        s += ', food: ' + str(self.food)
        s += ', rates: ' + str("{:.2f}".format(self.farm_knowledge)) + ' ' + str("{:.2f}".format(self.health_knowledge)) + ' ' + str("{:.2f}".format(self.escape))
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
        doctor.healing_power = int(Lib.calc_new_doctor_rate(doctor.intelligence, self.health_knowledge))
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

    def feed_meeples(self, rations) -> int:
        food_spent = 0
        for i in range(len(rations)):
            self.meeples[i].hunger += int(rations[i])
            food_spent += int(rations[i])
        self.food -= food_spent
        return food_spent

    def kill_meeple(self, id):
        dead = self.meeples.pop(id)
        for i in range(id,len(self.meeples)):
            self.meeples[i].id = i

    def analyze_health(self) -> tuple:
        sick_meeples = 0
        died = 0
        for m in self.meeples:
            dec = Lib.health_decrement(m.hunger, m.health)
            m.health -= dec
            if m.health < Lib.MIN_HEALTH_TO_WORK:
                sick_meeples += 1
            if m.health <= 0:
                died += 1
                sick_meeples -= 1
                self.kill_meeple(m.id)
        return sick_meeples, died

if __name__ == "__main__":
    village = Village()
    village.populate(3,3,3)
    print(village)
    village.reassign(8, 'f')
    print(village)
    village.kill_meeple(8)
    print(village)
