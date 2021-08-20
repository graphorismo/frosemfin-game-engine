
from source_code.common_classes import *


class IDataStorage(UniqueIDPool):

    # Functions to override in inherited classes:

    def save_all_data_to_a_file(self, file_path: str):
        raise RuntimeError("Can't find override for function"
                           " save_all_data_to_a_file(...) from interface IDataStorage")

    def load_all_data_from_a_file(self, file_path: str):
        raise RuntimeError("Can't find override for function"
                           " load_all_data_from_a_file(...) from interface IDataStorage")

    def get_data_of_all_entities(self) -> list[EntityData]:
        raise RuntimeError("Can't find override for function"
                           " get_data_of_all_entities(...) from interface IDataStorage")

    def get_data_of_all_projectiles(self) -> list[ProjectileData]:
        raise RuntimeError("Can't find override for function"
                           " get_data_of_projectiles(...) from interface IDataStorage")

    def add_data_of_projectiles(self, projectiles: list[ProjectileData]):
        raise RuntimeError("Can't find override for function"
                           " edit_or_create_data_of_projectiles(...) from interface IDataStorage")

    def remove_data_of_projectiles(self, projectiles: list[ProjectileData]):
        raise RuntimeError("Can't find override for function"
                           " remove_data_of_projectiles(...) from interface IDataStorage")

    def get_data_of_all_bodies_of_bots(self) -> list[BodyData]:
        raise RuntimeError("Can't find override for function"
                           " get_data_of_bodies_of_bots(...) from interface IDataStorage")

    def add_data_of_bodies_of_bots(self, bodies_of_bots: list[BodyData]):
        raise RuntimeError("Can't find override for function"
                           " edit_or_create_data_of_bodies_of_bots(...) from interface IDataStorage")

    def get_data_of_all_bodies_of_obstacles(self) -> list[BodyData]:
        raise RuntimeError("Can't find override for function"
                           " get_data_of_all_bodies_of_obstacles(...) from interface IDataStorage")

    def add_data_of_bodies_of_obstacles(self, bodies_of_obstacles: list[BodyData]):
        raise RuntimeError("Can't find override for function"
                           " edit_or_create_data_of_bodies_of_obstacles(...) from interface IDataStorage")

    def get_data_of_the_body_of_the_player(self) -> BodyData:
        raise RuntimeError("Can't find override for function"
                           " get_data_of_the_body_of_the_player(...) from interface IDataStorage")

    def add_the_player_body_data(self, player_body_data: BodyData):
        raise RuntimeError("Can't find override for function"
                           " edit_the_player_body_data(...) from interface IDataStorage")

    def push_collisions_data(self, collisions_data: list[list[EntityData]]):
        raise RuntimeError("Can't find override for function"
                           " push_collisions_data(...) from interface IDataStorage")

    def pop_collisions_data(self, collisions_data: list[list[EntityData]]):
        raise RuntimeError("Can't find override for function"
                           " pop_collisions_data(...) from interface IDataStorage")

    def get_world_data(self) -> WorldData:
        raise RuntimeError("Can't find override for function"
                           " get_world_data_copy(...) from interface IDataStorage")

