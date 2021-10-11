# Meeple Escape

Using Python 3.10 to create Meeple Escape Simulation

## Outline

### Meeple Escape Simulation

An implementation of Meeples, which are Villager-like characters that are stuck in a Village and must advance their technology to escape. Researchers can advance technology for other professions as well as learn how to escape the village. Once the *escape_knowledge* of the Village is at 100, the Meeples can sucessfully escape! The Village must produce enough food for the Meeples, otherwise they will be more prone to illnesses, and won't be able to perform their jobs. Doctors can heal Meeples, but only so many a per day, and only by so much. At the end of each week, the user may reassign Meeples to different jobs. Having more Researchers improves the ability of the other Meeples to do their jobs and helps bring the Village closer to escape, but the user must make sure there are still enough Farmers and Doctors to feed and heal the Village. 

#### Meeples

##### Types

* **Farmer** - Grows food to feed to other Meeples
    * food_production_rate - how much food produced per day
* **Doctor** - Heals sick Meeples
    * healing_power - how much health can restore per day
* **Researcher** - Researches advancements for farm and health technology, while also researching a way for the Meeples to escape the village
    * farm_kresearch_rate - how much improvement of farm production per day
    * health_research_rate - how much improvement of health power per day
    * escape_research_rate - how much increase to escape ability per day

##### Traits

* name
* hunger - how much food required per day
* health 
* intelligence - amount of knowledge able to learn about a given subject

#### Village

##### Traits

* meeples
* farm_knowledge - maximum individual food production rate
* health_knowledge - maximum individual healing power
* escape_knowledge - how close to being able to escape the Village
* day
* food - amount of food available for Meeples

#### Functions

* create_village() - creates Village and populates with Meeples
    * start farm & health knowledge randomly in the low 25% of each range
    * start day & escape knowledge at 0
    * populate Village with new Meeples according to user specification
    * set food to total one day worth of food for Village

* create_meeple(*job*) - creates new meeple with given job
    * initialize new Meeple
    * generate name
    * randomly choose hunger in range
    * set health to full
    * set intelligence randomly in range
    * assign Meeple to given job

* new_farmer() 
    * set *food_production_rate* based on Meeple intelligence and Village farm knowledge

* new_doctor() 
    * set *healing_power* based on Meeple intelligence and Village health knowledge

* new_researcher() 
    * set each knowledge randomly based on Meeple intelligence and overall Village knowledge

* advance_day() - simulate one day passing in the Village
    * feed Meeples
    * determine health of Meeples
    * healthy Meeples perform jobs
        * Farmers add to Village.food
        * Doctors care for sick Meeples
        * Researchers increase Village knowledge
    * apply knowledge boosts to Meeples
    * Meeples can escape if Village has full *escape_knowledge*
    * advance Village day counter

* feed_meeples() - feed Village of Meeples based on how much food is available

* analyze_health() - decrease if Meeple doesn't have enough food and/or if health is already low, Meeple has a small random chance of getting sick

* die() - Meeple dies if health gets to 0

* produce() - Farmers produce food based on *food_production_rate*, *hunger*, and *health*

* heal() - Doctors heal sick Meeples (those too unhealthy to work) based on *healing_power*, *hunger*, and *health*

* research() - Researchers increase Village knowledge based on based on research rates, *hunger*, and *health*

* farmer_boost() - random chance to boost Farmer's *food_production_rate* based on *farm_knowledge* and *intelligence*

* doctor_boost() - random chance to boost Doctor's *healing_power* based on *health_knowledge* and *intelligence*

* researcher_boost() - small random chance to boost Researcher's research rates based on *intelligence*
