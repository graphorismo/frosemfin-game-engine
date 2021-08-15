from source_code.common_classes import *

from source_code.data_storage_base_classes import IDataStorage


class IKeyboardReader:

    def get_the_last_player_action(self) -> BodyAction:
        raise RuntimeError("Can't find override for function"
                           " get_the_last_player_action(...) from interface IKeyboard")


class PlayerController:
    keyboard_reader: IKeyboardReader
    data_storage: IDataStorage

    def __init__(self, data_storage: IDataStorage, keyboard: IKeyboardReader):
        self.keyboard_reader = keyboard
        self.data_storage = data_storage

    def react_to_the_last_players_action(self):
        player_data = self.data_storage.get_data_of_the_body_of_the_player()
        action = self.keyboard_reader.get_the_last_player_action()
        action_type = action.action_type
        action_direction = action.direction
        if action_type is BodyActionTypeEnum.NOTHING:
            pass
        elif action_type is BodyActionTypeEnum.MOVE:
            if action_direction is DirectionEnum.NO_DIRECTION:
                pass
            elif action_direction is DirectionEnum.UP:
                player_data.coordinates.y += 1
            elif action_direction is DirectionEnum.DOWN:
                player_data.coordinates.y += -1
            elif action_direction is DirectionEnum.RIGHT:
                player_data.coordinates.x += 1
            elif action_direction is DirectionEnum.DOWN:
                player_data.coordinates.x += 1
        elif action_type is BodyActionTypeEnum.SHOOT:
            if action_direction is DirectionEnum.NO_DIRECTION:
                pass
            elif action_direction is DirectionEnum.UP:
                player_data.coordinates.y += 1
            elif action_direction is DirectionEnum.DOWN:
                player_data.coordinates.y += -1
            elif action_direction is DirectionEnum.RIGHT:
                player_data.coordinates.x += 1
            elif action_direction is DirectionEnum.DOWN:
                player_data.coordinates.x += 1
