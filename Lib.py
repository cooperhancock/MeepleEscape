# Library of game-wide Constants and Functions

import names
import random

# Constants

MIN_FARM_RESEARCH_RATE = 0.5
MAX_FARM_RESEARCH_RATE = 50.0
MIN_HEALTH_RESEARCH_RATE = 0 #TODO
MAX_HEALTH_RESEARCH_RATE = 0 #TODO
MIN_ESCAPE_RESEARCH_RATE = 0.01
MAX_ESCAPE_RESEARCH_RATE = 1.0
MIN_DIET = 10
MAX_DIET = 20
MIN_VILLAGE_POPULATION = 5
MAX_VILLAGE_POPULATION = 100
MIN_FARM_KNOWLEDGE = 40.0
MAX_FARM_KNOWLEDGE = 1000.0
MIN_HEALTH_KNOWLEDGE = 0 #TODO 
MAX_HEALTH_KNOWLEDGE = 0 #TODO
ESCAPE_POINT = 100.0
MAX_INITIAL_FARM_KNOWLEDGE = 100.0
MAX_INITIAL_HEALTH_KNOWLEDGE = 0 #TODO
MIN_INITIAL_FOOD_MULTIPLIER = 0.5
MIN_INITIAL_FOOD_MULTIPLIER = 1.5
INTELLIGENCE_MEAN = 0.5
INTELLIGENCE_STDEV = 0.2
DAYS_PER_WEEK = 7
MIN_HEALTH_TO_WORK = 50

# Utility functions

def random_name():
    return names.get_full_name()

# Functions

def calc_new_farmer_rate(intelligence, farm_knowledge) -> float:
    return random.uniform(MIN_FARM_KNOWLEDGE, farm_knowledge)

def calc_new_doctor_rate(intelligence, health_knowledge) -> float:
    return random.uniform(MIN_HEALTH_KNOWLEDGE, health_knowledge)

def calc_new_researcher_rates(intelligence, farm_knowledge, health_knowledge, escape_knowledge) -> tuple:
    return (MIN_FARM_RESEARCH_RATE, MIN_HEALTH_RESEARCH_RATE, MIN_ESCAPE_RESEARCH_RATE)

def ration_system(meeples, food) -> list:
    per_meeple = food / len(meeples)
    rations = [per_meeple for i in range(len(meeples))]
    return rations

# TODO
def health_decrement(hunger, health) -> int:
    pass

# TODO
def net_production(fpr, hunger, health) -> int:
    pass

# TODO
def net_healing(hp, hunger, health) -> int:
    pass

# TODO
def healing_schedule(meeples, hp) -> list:
    pass

# TODO
def research_amounts(intelligence, f_rate, h_rate, e_rate) -> tuple:
    pass

# TODO
def boost_amounts():
    pass