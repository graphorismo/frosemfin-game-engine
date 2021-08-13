from enum import Enum


class Vector2i:
    x: int = 0
    y: int = 0


class UniqueEntity:
    unique_id: int = -1


class EntityData(UniqueEntity):
    coordinates: Vector2i


class DirectionEnum(Enum):
    NO_DIRECTION = 0
    UP = 1
    RIGHT = 2
    DOWN = 3
    LEFT = 4


class ProjectileData(EntityData):
    direction: DirectionEnum = DirectionEnum.NO_DIRECTION


class BodyData(EntityData):
    hit_points: int = 0
