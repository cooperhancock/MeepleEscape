# Meeple Escape

Using Python 3.10 to create Meeple Escape Simulation

## Initial Outline

### Meeple Escape Simulation

An implementation of Meeples, which are Villager-like characters that are stuck in a Village and must advance their technology to escape. Researchers can advance technology for other professions as well as learn how to escape the village. Once the *escape_knowledge* of the Village is at 100, the Meeples can sucessfully escape! The Village must produce enough food for the Meeples, otherwise they will be more prone to illnesses, and won't be able to perform their jobs. Doctors can heal Meeples, but only so many a per day, and only by so much. At the end of each week, the user may reassign Meeples to different jobs. Having more Researchers improves the ability of the other Meeples to do their jobs and helps bring the Village closer to escape, but the user must make sure there are still enough Farmers and Doctors to feed and heal the Village. 

#### Constants & Effect Functions

List of constants used for bounds of attributes, and multipliers for effects. Functions for determining these multipliers/modifiers based on input. Suggested values included in some places.

##### Constants

* MIN_FARM_RESEARCH_RATE - 0.5
* MAX_FARM_RESEARCH_RATE - 50.0
* MIN_HEALTH_RESEARCH_RATE
* MAX_HEALTH_RESEARCH_RATE
* MIN_ESCAPE_RESEARCH_RATE - 0.01
* MAX_ESCAPE_RESEARCH_RATE - 1.0
* MIN_DIET - 10
* MAX_DIET - 20
* MIN_VILLAGE_POPULATION - 5
* MAX_VILLAGE_POPULATION - 100
* MIN_FARM_KNOWLEDGE - 40.0
* MAX_FARM_KNOWLEDGE - 1000.0
* MIN_HEALTH_KNOWLEDGE 
* MAX_HEALTH_KNOWLEDGE
* ESCAPE_POINT - 100.0
* MAX_INITIAL_FARM_KNOWLEDGE - 100.0
* MAX_INITIAL_HEALTH_KNOWLEDGE
* MIN_INITIAL_FOOD_MULTIPLIER - 0.5
* MIN_INITIAL_FOOD_MULTIPLIER - 1.5
* INTELLIGENCE_MEAN - 0.5
* INTELLIGENCE_STDEV - 0.2

##### Functions

* calc_new_farmer_rate(*intelligence*, *farm_knowledge*) -> *food_production_rate*
* calc_new_doctor_rate(*intelligence*, *health_knowledge*) -> *healing_power*
* calc_new_researcher_rates(*intelligence*, *farm_knowledge*, *health_knowledge*, *escape_knowledge*) -> *farm_research_rate*, *health_research_rate*, *escape_research_rate*
* ration_system(Meeples, *food*) -> how much food each Meeple gets (probably an ordered list of food amounts)
* health_decrement(*hunger*, *health*) -> how much to decrement *health*
* net_production(*food_production_rate*, *hunger*, *health*) -> amount of food to produce
* net_healing(*healing_power*, *hunger*, and *health*) -> amount of healing power available to use
* healing_schedule(Meeples, amount of healing power available) -> how much health increase each Meeple gets (probably an ordered list of healing amounts)
* research_amounts(*intelligence*, *farm_research_rate*, *health_research_rate*, *escape_research_rate*, *hunger*, *health*) -> increments to *farm_knowledge*, *health_knowledge*, *escape_knowledge*
* boost_amounts(?) -> amount to level up

#### Meeples

##### Types

* **Farmer** - Grows food to feed to other Meeples
    * food_production_rate - how much food produced per day
        * float -> *MIN_FARM_KNOWLEDGE* to *farm_knowledge*
* **Doctor** - Heals sick Meeples
    * healing_power - how much health can restore per day
        int -> *MIN_HEALTH_KNOWLEDGE* to *health_knowledge*
* **Researcher** - Researches advancements for farm and health technology, while also researching a way for the Meeples to escape the village
    * farm_research_rate - how much improvement of farm production per day
        * float -> *MIN_FARM_RESEARCH_RATE* to *MAX_FARM_RESEARCH_RATE*
    * health_research_rate - how much improvement of health power per day
        * float -> *MIN_HEALTH_RESEARCH_RATE* to *MAX_HEALTH_RESEARCH_RATE*
    * escape_research_rate - how much increase to escape ability per day
        * float -> *MIN_ESCAPE_RESEARCH_RATE* to *MAX_ESCAPE_RESEARCH_RATE*

##### Traits

* id
    * int -> unique identifier/index
* name
    * string -> Firstname Lastinitial.
* hunger
    * int -> 0 (starving) to 100 (full)
* health 
    * int -> 0 (dead) to 100 (perfect health)
* intelligence - amount of knowledge able to learn about a given subject
    * float -> 0.0 (can't learn anything) to 1.0 (can learn all available knowledge)
* diet - how much *hunger* "spent" per day
    * int -> *MIN_DIET* to *MAX_DIET*

#### Village

##### Traits

* meeples
    * list -> *MIN_VILLAGE_POPULATION* to *MAX_VILLAGE_POPULATION* determined by user
* farm_knowledge - maximum individual food production rate
    * float -> *MIN_FARM_KNOWLEDGE* to *MAX_FARM_KNOWLEDGE*
* health_knowledge - maximum individual healing power
    * float -> *MIN_HEALTH_KNOWLEDGE* to *MAX_HEALTH_KNOWLEDGE*
* escape_knowledge - how close to being able to escape the Village
    * float -> 0.0 (no knowledge) to *ESCAPE_POINT*
* day
    * int -> 0 to int_max
* food - amount of food available for Meeples
    * int -> 0 to int_max

#### Functions

* populate() - creates Village and populates with Meeples
    * start farm & health knowledge randomly in the low end of each range
        * *farm_knowledge* random in *MIN_FARM_KNOWLEDGE* to *MAX_INITIAL_FARM_KNOWLEDGE*
        * *health_knowledge* random in *MIN_HEALTH_KNOWLEDGE* to *MAX_INITIAL_HEALTH_KNOWLEDGE*
    * start *day* & *escape* knowledge at 0
    * populate Village with new Meeples according to user specification
        * prompt user for number of Farmers, Doctors, and Researchers
    * set food to random in *MIN_INITIAL_FOOD_MULTIPLIER* to *MAX_INITIAL_FOOD_MULTIPLIER* times sum of Meeples' diets

* create_meeple(*job*) - creates new meeple with given job
    * initialize new Meeple
    * generate name
    * randomly choose diet in range
    * set health to full
    * set intelligence randomly in range with about normal distribution (mean *INTELLIGENCE_MEAN*, std *INTELLIGENCE_STDEV*)
    * assign Meeple to given job

* new_farmer() 
    * func *calc_new_farmer_rate* -> *food_production_rate* 

* new_doctor() 
    * func *calc_new_doctor_rate* -> *healing_power*

* new_researcher() 
    * func *calc_new_researcher_rates* -> *farm_research_rate*, *health_research_rate*, *escape_research_rate*

* week() - simulate one week passing in the Village
    * pass *DAYS_PER_WEEK* days
    * print report to user
    * allow user to reassign jobs

* advance_day() - simulate one day passing in the Village
    * feed Meeples
    * determine health of Meeples
    * healthy Meeples perform jobs
        * Farmers add to Village food
        * Doctors care for sick Meeples
        * Researchers increase Village knowledge
    * apply knowledge boosts to Meeples
    * Meeples can escape if Village has full *escape_knowledge*
    * advance Village day counter

* feed_meeples() - feed Village of Meeples based on how much food is available
    * use *ration_system* to feed Meeples

* analyze_health() - decrease if Meeple doesn't have enough food and/or if health is already low, Meeple has a small random chance of getting sick
    * func *health_decrement* -> how much *health* to decrease

* die() - Meeple dies if *health* gets to 0

* produce() - Farmers produce food based on *food_production_rate*, *hunger*, and *health*
    * func *net_production* -> how much food to produce

* heal() - Doctors heal sick Meeples (those too unhealthy to work) based on *healing_power*, *hunger*, and *health*
    * func *net_healing* -> available healing power to use
    * use *healing_schedule* to determine order in which Meeples are healed, and how much each Meeple is healed

* research() - Researchers increase Village knowledge
    * func *research_amounts* -> increments to *farm_knowledge*, *health_knowledge*, *escape_knowledge*

* farmer_boost() - random chance to boost Farmer's *food_production_rate*
    * func *boost_amount* -> level up amount

* doctor_boost() - random chance to boost Doctor's *healing_power*
    * func *boost_amount* -> level up amount

* researcher_boost() - small random chance to boost Researcher's research rates
    * func *boost_amount* -> level up amount

* report() - show report of week's activities to user
    * show enough data for user to make reasonable job reassignments

* assign_job(*job*) - assign Meeple to a job
    * change job assignment of Meeple to given job
    * set paramaters based on new job functions


