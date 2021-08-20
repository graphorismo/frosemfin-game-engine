from ..common_classes import *
from ..world_logic_engine_base_classes import IWorldLogicCore


class SimpleWorldLogicCore(IWorldLogicCore):
    _high: int = 0
    _width: int = 0

    _cached_projectiles_to_remove: list[ProjectileData] = []

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
                    new_collision_second_layer_list.append(entity_j)
                are_there_collision_for_entity_i = len(new_collision_second_layer_list) > 1
                if are_there_collision_for_entity_i:
                    collisions_list.extend(new_collision_second_layer_list)
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

    def process_projectiles_logic(self, all_projectiles: list[ProjectileData]):
        directed_projectiles, undirected_projectiles \
            = self._split_projectiles_to_directed_and_undirected(all_projectiles)
        # Remove undirected projectiles
        self._cached_projectiles_to_remove.extend(undirected_projectiles)
        # Move directed projectiles
        for moving_projectile in directed_projectiles:
            direction = moving_projectile.direction
            if direction is DirectionEnum.UP:
                moving_projectile.coordinates.y += 1
            elif direction is DirectionEnum.DOWN:
                moving_projectile.coordinates.y -= 1
            elif direction is DirectionEnum.RIGHT:
                moving_projectile.coordinates.x += 1
            elif direction is DirectionEnum.LEFT:
                moving_projectile.coordinates.x -= 1

    def pop_a_list_of_projectiles_to_remove(self) -> list[ProjectileData]:
        poped_list: list[ProjectileData] = []
        poped_list.extend(self._cached_projectiles_to_remove)
        self._cached_projectiles_to_remove = []
        return poped_list

    def _split_projectiles_to_directed_and_undirected\
                    (self, all_projectiles: list[ProjectileData]) -> (list[ProjectileData], list[ProjectileData]):
        undirected_projectiles: list[ProjectileData] = []
        directed_projectiles: list[ProjectileData] = []
        for current_projectile in all_projectiles:
            if current_projectile.direction is DirectionEnum.NO_DIRECTION:
                undirected_projectiles.append(current_projectile)
            else:
                directed_projectiles.append(current_projectile)
        return directed_projectiles, undirected_projectiles


