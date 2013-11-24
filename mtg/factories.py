import factory
from factory.fuzzy import FuzzyInteger

from creature import CreatureType
from creature_state import CreatureState
from battleground_state import BattlegroundState
from game_state import GameState
from turn_phase import TurnPhase


class CreatureTypeFactory(factory.Factory):

    FACTORY_FOR = CreatureType

    power = FuzzyInteger(0, 6)
    toughness = FuzzyInteger(1, 7)


class CreatureStateFactory(factory.Factory):

    FACTORY_FOR = CreatureState

    creature_type = factory.SubFactory(CreatureTypeFactory)
    controlling_player = FuzzyInteger(0, 1)


class BattlegroundStateFactory(factory.Factory):

    FACTORY_FOR = BattlegroundState

    # TODO - how can we better integrate nr_creatures?
    @classmethod
    def build_with_creatures(cls, nr_creatures):
        obj = cls.build()
        for i in range(nr_creatures):
            obj.add_creature(CreatureStateFactory())
        return obj