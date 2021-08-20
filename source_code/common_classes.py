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

class UniqueIDPool:
    pool_of_free_ids: set[int]
    pool_of_locked_ids: set[int]
    size: int

    def __init__(self, size: int):
        self.pool_of_free_ids = set()
        self.pool_of_locked_ids = set()
        for i in range(1, size+1):
            self.pool_of_free_ids.add(i)

    def pop_unique_id(self) -> int:
        poped_id = self.pool_of_free_ids.pop()
        self.pool_of_locked_ids.add(poped_id)
        return poped_id


class UniqueEntity:
    unique_id: int

    def __init__(self, unique_id: int):
        self.unique_id = unique_id

    def __hash__(self):
        return hash(self.unique_id)


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
