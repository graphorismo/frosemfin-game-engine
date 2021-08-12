from common_classes import *


class PlayerActionTypeEnum(Enum):

    NOTHING = 0,
    MOVE = 1,
    SHOOT = 2


class PlayerAction:

    direction: DirectionEnum = DirectionEnum.NO_DIRECTION
    action_type: PlayerActionTypeEnum = PlayerActionTypeEnum.NOTHING


class IKeyboard:

    def get_the_last_player_action(self) -> PlayerAction:
        raise RuntimeError("Can't find override for function"
                           " get_the_last_player_action(...) from interface IKeyboard")

class PlayerController:

     keyboard: IKeyboard

     def __init__(self, keyboard: IKeyboard):
         self.keyboard = keyboard

     def react_to_the_last_players_action(self, player_data : BodyData):
         last_player_action = self.keyboard.get_the_last_player_action()
         if last_player_action.action_type is PlayerActionTypeEnum.NOTHING:
             pass
         elif last_player_action.action_type is PlayerActionTypeEnum.MOVE:
             if last_player_action.direction is DirectionEnum.NO_DIRECTION:
                pass
             elif last_player_action.direction is DirectionEnum.UP:
                player_data.coordinates.y += 1
             elif last_player_action.direction is DirectionEnum.DOWN:
                player_data.coordinates.y += -1
             elif last_player_action.direction is DirectionEnum.RIGHT:
                player_data.coordinates.x += 1
             elif last_player_action.direction is DirectionEnum.DOWN:
                player_data.coordinates.x += 1
         elif last_player_action.action_type is PlayerActionTypeEnum.SHOOT:
             if last_player_action.direction is DirectionEnum.NO_DIRECTION:
                pass
             elif last_player_action.direction is DirectionEnum.UP:
                player_data.coordinates.y += 1
             elif last_player_action.direction is DirectionEnum.DOWN:
                player_data.coordinates.y += -1
             elif last_player_action.direction is DirectionEnum.RIGHT:
                player_data.coordinates.x += 1
             elif last_player_action.direction is DirectionEnum.DOWN:
                player_data.coordinates.x += 1