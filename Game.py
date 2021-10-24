# Game engine implementation

from Lib import DAYS_PER_WEEK, ESCAPE_POINT, MIN_HEALTH_TO_WORK, healing_schedule, ration_system
from Meeple import Doctor, Farmer, Researcher
from Village import Village

# returns True if game over
def advance_day(village: Village) -> bool:
    village.report += 'Day ' + str(village.day) + '\n'
    # make meeples hungry
    req_food = 0
    for m in village.meeples:
        m.hunger -= m.diet
        req_food += m.diet
    village.report += str(req_food) + ' food needed\n'
    # feed meeples
    fed = village.feed_meeples(ration_system(village.meeples, village.food))
    village.report += str(fed) + ' food eaten\n'
    # determine health
    sick, died = village.analyze_health()
    village.report += str(sick) + ' sick meeples\n'
    village.report += str(died) + ' meeples died\n'
    # check to make sure all meeples haven't died
    if len(village.meeples) == 0:
        return end_game(False)
    # healthy meeples work
    food = 0
    for m in village.meeples:
        if m.health > MIN_HEALTH_TO_WORK:
            if isinstance(m, Farmer):
                this_food = m.produce()
                village.food += this_food
                food += this_food
            if isinstance(m, Doctor):
                m.heal(healing_schedule(village.meeples, m.healing_power))
            if isinstance(m, Researcher):
                f, h, e = m.research()
                village.farm_knowledge += f
                village.health_knowledge += h
                village.escape += e
    village.report += str(food) + ' food produced\n'
    # check if meeples can escape
    if village.escape == ESCAPE_POINT:
        return end_game(True)
    village.day += 1
    village.report += '-- end day --\n\n'
    return False


# returns True if game over
def week(village: Village) -> bool:
    week = int(village.day/DAYS_PER_WEEK + 1)
    input("Press Enter to run week " + str(week))
    village.report = "\nWeek " + str(week) + '\n\n'
    for i in range(DAYS_PER_WEEK):
        if advance_day(village): return True
    # apply knowledge boosts to meeples
    for m in village.meeples:
        m.boost()
    village.report += str(village)
    print(village.report)
    return False

def end_game(win: bool) -> bool:
    if win: 
        print("Meeples have escaped")
    else:
        print("All Meeples have died :(")
    return True