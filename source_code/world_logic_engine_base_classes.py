from source_code.common_classes import *

from source_code.data_storage_base_classes import IDataStorage


class IWorldLogicCore:

    # Functions to override in inherited classes:

    def set_world_border_size(self, high: int, width: int):
        raise RuntimeError("Can't find override for function"
                           " set_world_border_size(...) from interface IWorldLogicEngine")

    def get_all_collisions_between_entities(self, entities_list: list[EntityData]) -> list[list[EntityData]]:
        raise RuntimeError("Can't find override for function"
                           " get_all_collisions_between_entities(...) from interface IWorldLogicEngine")

    def bounce_back_entities_collided_with_world_border(self, entities_list: list[EntityData]):
        raise RuntimeError("Can't find override for function"
                           " bounce_back_entities_collided_with_world_border(...) from interface IWorldLogicEngine")


class WordLogicEngine:
    data_storage: IDataStorage
    logic_core: IWorldLogicCore

    def __init__(self, data_storage: IDataStorage, logic_core: IWorldLogicCore):
        self.data_storage = data_storage
        self.logic_core = logic_core

    def process_world_logic_effects(self):
        entities = self.data_storage.get_data_of_all_entities()
        self.logic_core.bounce_back_entities_collided_with_world_border(entities)
        collisions = self.logic_core.get_all_collisions_between_entities(entities)
        self.data_storage.push_collisions_data(collisions)



