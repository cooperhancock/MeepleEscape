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

# Utility functions

def random_name():
    return names.get_full_name()

# Functions

def calc_new_farmer_rate(intelligence, farm_knowledge) -> float:
    return random.random(MIN_FARM_KNOWLEDGE, farm_knowledge)

def calc_new_doctor_rate(intelligence, health_knowledge) -> float:
    return random.random(MIN_HEALTH_KNOWLEDGE, health_knowledge)

def calc_new_researcher_rates(intelligence, farm_knowledge, health_knowledge, escape_knowledge) -> tuple:
    pass
