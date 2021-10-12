# Meeple Escape

Using Python 3.10 to create Meeple Escape Simulation

## Outline

### Meeple Escape Simulation

An implementation of Meeples, which are Villager-like characters that are stuck in a Village and must advance their technology to escape. Researchers can advance technology for other professions as well as learn how to escape the village. Once the *escape_knowledge* of the Village is at 100, the Meeples can sucessfully escape! The Village must produce enough food for the Meeples, otherwise they will be more prone to illnesses, and won't be able to perform their jobs. Doctors can heal Meeples, but only so many a per day, and only by so much. At the end of each week, the user may reassign Meeples to different jobs. Having more Researchers improves the ability of the other Meeples to do their jobs and helps bring the Village closer to escape, but the user must make sure there are still enough Farmers and Doctors to feed and heal the Village. 

#### Meeples

##### Types

* **Farmer** - Grows food to feed to other Meeples
    * food_production_rate - how much food produced per day
        * int -> 30 to &LeftFloor; *farm_knowledge* &RightFloor;
* **Doctor** - Heals sick Meeples
    * healing_power - how much health can restore per day
* **Researcher** - Researches advancements for farm and health technology, while also researching a way for the Meeples to escape the village
    * farm_research_rate - how much improvement of farm production per day
        * float -> 0.5 to 50.0
    * health_research_rate - how much improvement of health power per day
        * TODO
    * escape_research_rate - how much increase to escape ability per day
        * float -> 0.01 to 1.0

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
    * int -> 10 to 20

#### Village

##### Traits

* meeples
    * list -> 5 to 100 determined by user
* farm_knowledge - maximum individual food production rate
    * float -> 40.0 (feeds 2-4 people) to 1000.0 (feeds 50-100 people)
* health_knowledge - maximum individual healing power
    * TODO
* escape_knowledge - how close to being able to escape the Village
    * float -> 0.0 (no knowledge) to 100.0 (can escape)
* day
    * int -> 0 to int_max
* food - amount of food available for Meeples
    * int -> 0 to int_max

#### Functions

* create_village() - creates Village and populates with Meeples
    * start farm & health knowledge randomly in the low end of each range
        * *farm_knowledge* random in 40 to 100
        * *health_knowledge* random in TODO
    * start *day* & *escape* knowledge at 0
    * populate Village with new Meeples according to user specification
        * prompt user for number of Farmers, Doctors, and Researchers
        * at least 1 of each, total at least 5
    * set food to random in 50% sum of Meeples' diets to 150%

* create_meeple(*job*) - creates new meeple with given job
    * initialize new Meeple
    * generate name
    * randomly choose diet in range
    * set health to full
    * set intelligence randomly in range with about normal distribution (suggested: mean 0.5, std 0.2)
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
    * healthy Meeples perform jobs - if *health* > 60
        * Farmers add to Village.food
        * Doctors care for sick Meeples
        * Researchers increase Village knowledge
    * apply knowledge boosts to Meeples
    * Meeples can escape if Village has full *escape_knowledge*
    * advance Village day counter

* feed_meeples() - feed Village of Meeples based on how much food is available
    * use a ration system to feed Meeples
    * ration systems determines the order in which food is distributed, and how much each Meeple gets

* analyze_health() - decrease if Meeple doesn't have enough food and/or if health is already low, Meeple has a small random chance of getting sick
    * func (*hunger*, *health*) -> how much *health* to decrease

* die() - Meeple dies if health gets to 0

* produce() - Farmers produce food based on *food_production_rate*, *hunger*, and *health*
    * func (*food_production_rate*, *hunger*, *health*) -> how much food to produce

* heal() - Doctors heal sick Meeples (those too unhealthy to work) based on *healing_power*, *hunger*, and *health*
    * func (*healing_power*, *hunger*, and *health*) -> available healing power to use
    * use healing schedule to determine order in which Meeples are healed, and how much each Meeple is healed

* research() - Researchers increase Village knowledge based on based on *intelligence*, *hunger*, and *health*
    * func (*intelligence*, *hunger*, *health*) -> increments to *farm_knowledge*, *health_knowledge*, *escape_knowledge*

* farmer_boost() - random chance to boost Farmer's *food_production_rate* based on *farm_knowledge* and *intelligence*

* doctor_boost() - random chance to boost Doctor's *healing_power* based on *health_knowledge* and *intelligence*

* researcher_boost() - small random chance to boost Researcher's research rates based on *intelligence*

* weekend_review() - show report of week's activities to user, let user reassign jobs
    * print report
    * list Meeples
    * allow user to choose a Meeple and reassign until user is satisfied

* assign_job(*job*) - assign Meeple to a job
    * change job assignment of Meeple to given job
    * set paramaters based on Meeple intelligence and Village knowledge of the subject


