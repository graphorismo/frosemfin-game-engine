from enum import Enum


class WorldData:
    # Fields have default values
    # because im too lazy to implement
    # the test suit for world init or
    # world edit funcs for now
    high: int = 15
    width: int = 15


class Vector2i:
    x: int
    y: int

    def __init__(self):
        self.x = 0
        self.y = 0


class UniqueEntity:
    unique_id: int

    def __init__(self):
        self.unique_id = -1


class EntityData(UniqueEntity):
    coordinates: Vector2i

    def __init__(self):
        super().__init__()
        self.coordinates = Vector2i()


class DirectionEnum(Enum):
    NO_DIRECTION = 0
    UP = 1
    RIGHT = 2
    DOWN = 3
    LEFT = 4


class BodyActionTypeEnum(Enum):
    NOTHING = 0
    MOVE = 1
    SHOOT = 2


class BodyAction:
    direction: DirectionEnum
    action_type: BodyActionTypeEnum

    def __init__(self):
        self.direction = DirectionEnum.NO_DIRECTION
        self.action_type = BodyActionTypeEnum.NOTHING


class ProjectileData(EntityData):
    direction: DirectionEnum

    def __init__(self):
        super().__init__()
        self.direction = DirectionEnum.NO_DIRECTION


class BodyData(EntityData):
    hit_points: int

    def __init__(self):
        super().__init__()
        self.hit_points = 0
