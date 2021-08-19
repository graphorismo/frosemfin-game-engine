from source_code.common_classes import *
from source_code.data_storage_base_classes import IDataStorage

import copy


class BotAction(BodyAction):
    corresponded_bot: EntityData


class IBotAiCore:

    # Functions to override in inherited classes:

    def consider_obstacles_data(self, obstacles_data: list[BodyData]):
        raise RuntimeError("Can't find override for function"
                           " consider_obstacle_data(...) from interface IBotAiCore")

    def consider_bots_data(self, bots_data: list[BodyData]):
        raise RuntimeError("Can't find override for function"
                           " consider_bots_data(...) from interface IBotAiCore")

    def consider_player_data(self, player_data: BodyData):
        raise RuntimeError("Can't find override for function"
                           " consider_player_data(...) from interface IBotAiCore")

    def get_actions_of_considered_bots(self) -> list[BotAction]:
        raise RuntimeError("Can't find override for function"
                           " get_action_for_bots(...) from interface IBotAiCore")


class BotAiEngine:
    _data_storage: IDataStorage = None
    _ai_core: IBotAiCore = None

    projectiles_to_spawn: list[ProjectileData]

    def __init__(self, data_storage: IDataStorage, ai_core: IBotAiCore):
        self._data_storage = data_storage
        self._ai_core = ai_core
        # Checks for None
        if self._data_storage is None:
            raise RuntimeError("Get None instead of an IDataStorage exemplar "
                               "in the _data_storage field due BotAiEngine constructing")
        if self._ai_core is None:
            raise RuntimeError("Get None instead of an IBotAiCore exemplar "
                               "in the _ai_core field due BotAiEngine constructing")

    def load_data_to_consider_by_ai(self):
        bots_data_to_consider = self._data_storage.get_data_of_all_bodies_of_bots()
        self._ai_core.consider_bots_data(bots_data_to_consider)
        obstacles_data_to_consider = self._data_storage.get_data_of_all_bodies_of_obstacles()
        self._ai_core.consider_obstacles_data(obstacles_data_to_consider)
        player_data_to_consider = self._data_storage.get_data_of_the_body_of_the_player()
        self._ai_core.consider_player_data(player_data_to_consider)

    def calculate_and_perform_bots_actions(self):
        actions = self._ai_core.get_actions_of_considered_bots()
        for next_action in actions:
            if next_action.action_type is BodyActionTypeEnum.NOTHING:
                pass
            elif next_action.action_type is BodyActionTypeEnum.MOVE:
                self._move_the_body_correspond_to_the_move_action(next_action)
            elif next_action.action_type is BodyActionTypeEnum.SHOOT:
                self._spawn_a_projectile_correspond_to_the_shoot_action(next_action)

    def _move_the_body_correspond_to_the_move_action(self, move_action: BotAction):
        body_to_move = move_action.corresponded_bot
        if move_action.direction is DirectionEnum.NO_DIRECTION:
            pass
        elif move_action.direction is DirectionEnum.UP:
            body_to_move.coordinates.y += 1
        elif move_action.direction is DirectionEnum.DOWN:
            body_to_move.coordinates.y -= 1
        elif move_action.direction is DirectionEnum.RIGHT:
            body_to_move.coordinates.x += 1
        elif move_action.direction is DirectionEnum.LEFT:
            body_to_move.coordinates.y -= 1

    def _spawn_a_projectile_correspond_to_the_shoot_action(self, shoot_action: BotAction):
        new_projectile = ProjectileData()
        new_projectile.coordinates = copy.deepcopy(shoot_action.corresponded_bot.coordinates)
        new_projectile.direction = copy.deepcopy(shoot_action.direction)
        if shoot_action.direction is DirectionEnum.NO_DIRECTION:
            pass
        elif shoot_action.direction is DirectionEnum.UP:
            new_projectile.coordinates.y += 1
        elif shoot_action.direction is DirectionEnum.DOWN:
            new_projectile.coordinates.y -= 1
        elif shoot_action.direction is DirectionEnum.RIGHT:
            new_projectile.coordinates.x += 1
        elif shoot_action.direction is DirectionEnum.LEFT:
            new_projectile.coordinates.y -= 1

        self._data_storage.add_data_of_projectiles([new_projectile])

