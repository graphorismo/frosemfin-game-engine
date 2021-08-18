from ..common_classes import *
from ..player_controller_base_classes import IKeyboardReader
import random


class SimpleKeyboardReader(IKeyboardReader):

    def get_the_last_player_action(self) -> BodyAction:
        player_action = BodyAction()
        player_action.direction = self._get_random_direction()
        player_action.action_type = self._get_random_action_type()
        return  player_action

    def _get_random_direction(self) -> DirectionEnum:
        random_index = random.randint(0, len(DirectionEnum)-1)
        return DirectionEnum(random_index)

    def _get_random_action_type(self) -> BodyActionTypeEnum:
        random_index = random.randint(0, len(BodyActionTypeEnum)-1)
        return BodyActionTypeEnum(random_index)
