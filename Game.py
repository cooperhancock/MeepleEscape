# Game engine implementation

from Lib import MIN_HEALTH_TO_WORK, ration_system
from Meeple import Doctor, Farmer, Researcher
from Village import Village



def advance_day(village: Village) -> None:
    # make meeples hungry
    for m in village.meeples:
        m.hunger -= m.diet
    # feed meeples
    village.feed_meeples(ration_system(village.meeples, village.food))
    # TODO
    # determine health
    village.analyze_health()
    # healthy meeples work
    for m in village.meeples:
        if m.health > MIN_HEALTH_TO_WORK:
            if isinstance(m, Farmer):
                village.food += m.produce()
            if isinstance(m, Doctor):
                m.heal()
            if isinstance(m, Researcher):
                f, h, e = m.research()
                village.farm_knowledge += f
                village.health_knowledge += h
                village.escape += e

# TODO
def report() -> None:
    pass

# TODO
def week() -> None:
    pass
