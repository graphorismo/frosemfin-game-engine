from ..common_classes import *
from ..world_logic_engine_base_classes import IWorldLogicCore


class SimpleWorldLogicCore(IWorldLogicCore):
    _high: int = 0
    _width: int = 0

    def set_world_border_size(self, high: int, width: int):
        if (high is None or high <= 0) or (width is None or width <= 0):
            raise RuntimeError("Get None or number that less or equal then 0 "
                               "on the input of SimpleBotAiCore::set_world_border_size(...)")
        self._high = high
        self._width = width

    def get_all_collisions_between_entities(self, entities_list: list[EntityData]) -> list[list[EntityData]]:
        collisions_list: list[list[EntityData]] = []
        all_available_indexes = range(len(entities_list))
        for i in all_available_indexes:
            entity_i = entities_list[i]
            indexes_from_i_to_the_last_index = range(i, len(entities_list))
            new_collision_second_layer_list = [entity_i]
            for j in indexes_from_i_to_the_last_index:
                entity_j = entities_list[j]
                if entity_i.coordinates == entity_j.coordinates:
                    new_collision_second_layer_list += entity_j
                are_there_collision_for_entity_i = len(new_collision_second_layer_list) > 1
                if are_there_collision_for_entity_i:
                    collisions_list += new_collision_second_layer_list
        return collisions_list

    def bounce_back_entities_collided_with_world_border(self, entities_list: list[EntityData]):
        for current_entity in entities_list:
            if current_entity.coordinates.x >= self._high:
                current_entity.coordinates.x = self._high-1
            elif current_entity.coordinates.x < 0:
                current_entity.coordinates.x = 0

            if current_entity.coordinates.y >= self._width:
                current_entity.coordinates.y = self._width - 1
            elif current_entity.coordinates.y < 0:
                current_entity.coordinates.y = 0
