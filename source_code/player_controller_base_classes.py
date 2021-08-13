from source_code.common_classes import *


class IKeyboard:

    def get_the_last_player_action(self) -> BodyAction:
        raise RuntimeError("Can't find override for function"
                           " get_the_last_player_action(...) from interface IKeyboard")


class PlayerController:
    keyboard: IKeyboard

    def __init__(self, keyboard: IKeyboard):
        self.keyboard = keyboard

    def react_to_the_last_players_action(self, player_data: BodyData):
        action = self.keyboard.get_the_last_player_action()
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
