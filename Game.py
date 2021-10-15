# Game engine implementation

from Lib import ration_system
from Village import Village


def advance_day(village: Village) -> None:
    # make meeples hungry
    for m in village.meeples:
        m.hunger -= m.diet
    # feed meeples
    village.feed_meeples(ration_system(village.meeples, village.food))
    # TODO

# TODO
def week():
    pass
