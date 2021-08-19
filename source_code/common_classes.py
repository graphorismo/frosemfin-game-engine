from enum import Enum


class WorldData:
    high: int = 0
    width: int = 0


class Vector2i:
    x: int = 0
    y: int = 0


class UniqueEntity:
    unique_id: int = -1


class EntityData(UniqueEntity):
    coordinates: Vector2i = Vector2i()


class DirectionEnum(Enum):
    NO_DIRECTION = 0
    UP = 1
    RIGHT = 2
    DOWN = 3
    LEFT = 4


class BodyActionTypeEnum(Enum):
    NOTHING = 0,
    MOVE = 1,
    SHOOT = 2


class BodyAction:
    direction: DirectionEnum = DirectionEnum.NO_DIRECTION
    action_type: BodyActionTypeEnum = BodyActionTypeEnum.NOTHING


class ProjectileData(EntityData):
    direction: DirectionEnum = DirectionEnum.NO_DIRECTION


class BodyData(EntityData):
    hit_points: int = 0
