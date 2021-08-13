from enum import Enum

from common_classes import *


class IDataStorage:

    # Functions to override in inherited classes:

    def get_data_of_all_entities(self) -> list[EntityData]:
        raise RuntimeError("Can't find override for function"
                           " get_data_of_all_entities(...) from interface IDataStorage")

    def get_data_of_all_projectiles(self) -> list[ProjectileData]:
        raise RuntimeError("Can't find override for function"
                           " get_data_of_projectiles(...) from interface IDataStorage")

    def add_data_of_projectiles(self, projectiles: list[ProjectileData]):
        raise RuntimeError("Can't find override for function"
                           " edit_or_create_data_of_projectiles(...) from interface IDataStorage")

    def get_data_of_all_bodies_of_bots(self) -> list[BodyData]:
        raise RuntimeError("Can't find override for function"
                           " get_data_of_bodies_of_bots(...) from interface IDataStorage")

    def add_data_of_bodies_of_bots(self, bodies_of_bots: list[BodyData]):
        raise RuntimeError("Can't find override for function"
                           " edit_or_create_data_of_bodies_of_bots(...) from interface IDataStorage")

    def get_data_of_all_bodies_of_obstacles(self) -> list[BodyData]:
        raise RuntimeError("Can't find override for function"
                           " get_data_of_all_bodies_of_obstacles(...) from interface IDataStorage")

    def add_data_of_bodies_of_obstacles(self, bodies_of_bots: list[BodyData]):
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

