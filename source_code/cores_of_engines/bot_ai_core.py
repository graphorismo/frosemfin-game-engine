from ..common_classes import *
from ..bot_ai_engine_base_classes import IBotAiCore, BotAction
import random


# Just make bots do random actions in random directions
class SimpleBotAiCore(IBotAiCore):
    _obstacles_data: list[BodyData]
    _bots_data: list[BodyData]
    _player_data: BodyData

    def consider_obstacles_data(self, obstacles_data: list[BodyData]):
        if obstacles_data is None:
            raise RuntimeError("Get None instead of an list[BodyData] "
                               "on the input of SimpleBotAiCore::consider_obstacles_data(...)")

        self._obstacles_data = obstacles_data

    def consider_bots_data(self, bots_data: list[BodyData]):
        if bots_data is None:
            raise RuntimeError("Get None instead of an list[BodyData] "
                               "on the input of SimpleBotAiCore::consider_bots_data(...)")

        self._bots_data = bots_data

    def consider_player_data(self, player_data: BodyData):
        if player_data is None:
            raise RuntimeError("Get None instead of an list[BodyData] "
                               "on the input of SimpleBotAiCore::consider_player_data(...)")

        self._player_data = player_data

    def get_actions_of_considered_bots(self) -> list[BotAction]:
        actions_of_bots: list[BotAction] = list()
        for current_bot in self._bots_data:
            bot_action = BotAction()
            bot_action.corresponded_bot = current_bot
            bot_action.direction = self._get_random_direction()
            bot_action.action_type = self._get_random_action_type()
            actions_of_bots += bot_action
        return actions_of_bots

    def _get_random_direction(self) -> DirectionEnum:
        random_index = random.randint(0, len(DirectionEnum) - 1)
        return DirectionEnum(random_index)

    def _get_random_action_type(self) -> BodyActionTypeEnum:
        random_index = random.randint(0, len(BodyActionTypeEnum) - 1)
        return BodyActionTypeEnum(random_index)
