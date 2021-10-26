# Library of game-wide Constants and Functions

import names
import random

# Constants

MIN_FARM_RESEARCH_RATE = 0.5
MAX_FARM_RESEARCH_RATE = 50.0
MIN_HEALTH_RESEARCH_RATE = 0.05 #TODO
MAX_HEALTH_RESEARCH_RATE = 2.0 #TODO
MIN_ESCAPE_RESEARCH_RATE = 0.01
MAX_ESCAPE_RESEARCH_RATE = 1.0
MIN_DIET = 10
MAX_DIET = 20
MIN_VILLAGE_POPULATION = 5
MAX_VILLAGE_POPULATION = 100
MIN_FARM_KNOWLEDGE = 40.0
MAX_FARM_KNOWLEDGE = 1000.0
MIN_HEALTH_KNOWLEDGE = 1 #TODO 
MAX_HEALTH_KNOWLEDGE = 100 #TODO
ESCAPE_POINT = 100.0
MAX_INITIAL_FARM_KNOWLEDGE = 100.0
MAX_INITIAL_HEALTH_KNOWLEDGE = 2 #TODO
MIN_INITIAL_FOOD_MULTIPLIER = 0.5
MIN_INITIAL_FOOD_MULTIPLIER = 1.5
INTELLIGENCE_MEAN = 0.5
INTELLIGENCE_STDEV = 0.2
DAYS_PER_WEEK = 7
MIN_HEALTH_TO_WORK = 50
ADVANCE_RATE = 0.01

# Utility functions

def random_name():
    return names.get_full_name()

def validated_input(str: str, type: type):
    while True:
        try:
            val = type(input(str))
        except ValueError:
            print("invalid, try again")
            continue
        else:
            break
    return val

def restricted_input(str: str, lst: list):
    while True:
        val = input(str)
        print(val)
        print(lst)
        if val in lst:
            break
        else:
            print("invalid, try again")
            continue
    return val

# Functions

def calc_new_farmer_rate(intelligence, farm_knowledge) -> float:
    return random.uniform(MIN_FARM_KNOWLEDGE, farm_knowledge)

def calc_new_doctor_rate(intelligence, health_knowledge) -> float:
    return random.uniform(MIN_HEALTH_KNOWLEDGE, health_knowledge)

def calc_new_researcher_rates(intelligence, farm_knowledge, health_knowledge, escape_knowledge) -> tuple:
    return (MIN_FARM_RESEARCH_RATE, MIN_HEALTH_RESEARCH_RATE, MIN_ESCAPE_RESEARCH_RATE)

def ration_system(meeples, food) -> list:
    per_meeple = food / len(meeples)
    rations = [min(100-meeples[i].hunger,per_meeple) for i in range(len(meeples))]
    return rations

# TODO
def health_decrement(hunger, health) -> int:
    dec = 0
    if hunger < 80:
        dec += 5
    if health < 50:
        dec += 5
    if random.randrange(0,100) < 5:
        dec += 10 * random.randrange(1,5)
    return dec

# TODO
def net_production(fpr, hunger, health) -> int:
    return int(fpr)

# TODO
def net_healing(hp, hunger, health) -> int:
    return int(hp)

# TODO
def healing_schedule(meeples, hp) -> list:
    hs = []
    healing_indicies = []
    for i in range(len(meeples)):
        if meeples[i].health < 80:
            healing_indicies.append(i)
        hs.append(0)
    if len(healing_indicies) > 0:
        hp_per_meeple = int(hp/len(healing_indicies))
        for i in healing_indicies:
            hs[i] = hp_per_meeple
    return hs

# TODO
def research_amounts(intelligence, f_rate, h_rate, e_rate) -> tuple:
    return (f_rate, h_rate, e_rate)

# TODO
def boost_amounts(range) -> float:
    return range * ADVANCE_RATE