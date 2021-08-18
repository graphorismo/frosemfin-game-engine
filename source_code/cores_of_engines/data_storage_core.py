from ..common_classes import *
from ..data_storage_base_classes import IDataStorage
from copy import copy


class SimpleDataStorage(IDataStorage):

    _projectiles: list[ProjectileData] = []
    _bots: list[BodyData] = []
    _obstacles: list[BodyData] = []
    _player: BodyData = []
    _collision_events: list[list[EntityData]] = []

    def get_data_of_all_entities(self) -> list[EntityData]:
        all_entities_data = list[EntityData]
        all_entities_data += self._projectiles
        all_entities_data += self._bots
        all_entities_data += self._obstacles
        all_entities_data += self._player
        return copy(all_entities_data)

    def get_data_of_all_projectiles(self) -> list[ProjectileData]:
        return copy(self._projectiles)

    def add_data_of_projectiles(self, projectiles: list[ProjectileData]):
        self._projectiles += projectiles

    def get_data_of_all_bodies_of_bots(self) -> list[BodyData]:
        return copy(self._bots)

    def add_data_of_bodies_of_bots(self, bodies_of_bots: list[BodyData]):
        self._bots += bodies_of_bots

    def get_data_of_all_bodies_of_obstacles(self) -> list[BodyData]:
        return copy(self._obstacles)

    def add_data_of_bodies_of_obstacles(self, bodies_of_obstacles: list[BodyData]):
        self._obstacles += bodies_of_obstacles

    def get_data_of_the_body_of_the_player(self) -> BodyData:
        return copy(self._player)

    def add_the_player_body_data(self, player_body_data: BodyData):
        self._player = player_body_data

    def push_collisions_data(self, collisions_data: list[list[EntityData]]):
        self._collision_events += collisions_data

    def pop_collisions_data(self, collisions_data: list[list[EntityData]]):
        poped_events = self._collision_events
        self._collision_events = []
        return poped_events