from ..common_classes import *
from ..data_storage_base_classes import IDataStorage
from copy import copy
import pickle


class SimpleDataStorage(IDataStorage):

    _projectiles: list[ProjectileData] = []
    _bots: list[BodyData] = []
    _obstacles: list[BodyData] = []
    _player: BodyData = None
    _collision_events: list[list[EntityData]] = []
    _world_data: WorldData = WorldData()

    def save_all_data_to_a_file(self, file_path: str):
        with open(file_path, "wb") as file_to_save_in:
            file_to_save_in.write(bytearray(pickle.dumps(self._projectiles)))
            file_to_save_in.write(bytearray(pickle.dumps(self._bots)))
            file_to_save_in.write(bytearray(pickle.dumps(self._obstacles)))
            file_to_save_in.write(bytearray(pickle.dumps(self._player)))
            file_to_save_in.write(bytearray(pickle.dumps(self._world_data)))

    def load_all_data_from_a_file(self, file_path: str):
        try:
            with open(file_path, "rb") as file_to_load_from:
                self._projectiles = pickle.load(file_to_load_from.readline())
                self._bots = pickle.load(file_to_load_from.readline())
                self._obstacles = pickle.load(file_to_load_from.readline())
                self._player = pickle.load(file_to_load_from.readline())
                self._world_data = pickle.load(file_to_load_from.readline())
        except FileNotFoundError:
            pass

    def get_data_of_all_entities(self) -> list[EntityData]:
        all_entities_data: list[EntityData] = []
        all_entities_data.extend(self._projectiles)
        all_entities_data.extend(self._bots)
        all_entities_data.extend(self._obstacles)
        all_entities_data.append(self._player)
        return copy(all_entities_data)

    def get_data_of_all_projectiles(self) -> list[ProjectileData]:
        return copy(self._projectiles)

    def add_data_of_projectiles(self, projectiles: list[ProjectileData]):
        self._projectiles.extend(projectiles)

    def remove_data_of_projectiles(self, projectiles: list[ProjectileData]):
        if len(projectiles) > 0:
            for current_projectile in projectiles:
                self._projectiles.remove(current_projectile)

    def get_data_of_all_bodies_of_bots(self) -> list[BodyData]:
        return copy(self._bots)

    def add_data_of_bodies_of_bots(self, bodies_of_bots: list[BodyData]):
        self._bots.extend(bodies_of_bots)

    def get_data_of_all_bodies_of_obstacles(self) -> list[BodyData]:
        return copy(self._obstacles)

    def add_data_of_bodies_of_obstacles(self, bodies_of_obstacles: list[BodyData]):
        self._obstacles.extend(bodies_of_obstacles)

    def get_data_of_the_body_of_the_player(self) -> BodyData:
        return copy(self._player)

    def add_the_player_body_data(self, player_body_data: BodyData):
        self._player = player_body_data

    def push_collisions_data(self, collisions_data: list[list[EntityData]]):
        self._collision_events.extend(collisions_data)

    def pop_collisions_data(self, collisions_data: list[list[EntityData]]):
        poped_events = self._collision_events
        self._collision_events = []
        return poped_events

    def get_world_data(self) -> WorldData:
        return self._world_data

