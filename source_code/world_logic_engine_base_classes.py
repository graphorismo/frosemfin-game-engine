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
    _data_storage: IDataStorage = None
    _logic_core: IWorldLogicCore = None

    def __init__(self, data_storage: IDataStorage, logic_core: IWorldLogicCore):
        self._data_storage = data_storage
        self._logic_core = logic_core
        # Checks for None
        if self._data_storage is None:
            raise RuntimeError("Get None instead of an IDataStorage exemplar "
                               "in the _data_storage field due WordLogicEngine constructing")
        if self._logic_core is None:
            raise RuntimeError("Get None instead of an IWorldLogicCore exemplar "
                               "in the _logic_core field due WordLogicEngine constructing")

    def process_world_logic_effects(self):
        entities = self._data_storage.get_data_of_all_entities()
        self._logic_core.bounce_back_entities_collided_with_world_border(entities)
        collisions = self._logic_core.get_all_collisions_between_entities(entities)
        self._data_storage.push_collisions_data(collisions)



