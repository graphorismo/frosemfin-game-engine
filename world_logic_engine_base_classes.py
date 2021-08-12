from common_classes import *

class IWorldLogicEngine:

    # Functions to override in inherited classes:

    def set_world_border_size(self, high: int, width: int):
        raise RuntimeError("Can't find override for function"
                           " set_world_border_size(...) from interface IWorldLogicEngine")

    def get_all_collisions_between_entities(self, entities_list: list[EntityData]):
        raise RuntimeError("Can't find override for function"
                           " get_all_collisions_between_entities(...) from interface IWorldLogicEngine")

    def bounce_back_entities_collided_with_world_border(self, entities_list: list[EntityData]):
        raise RuntimeError("Can't find override for function"
                           " bounce_back_entities_collided_with_world_border(...) from interface IWorldLogicEngine")