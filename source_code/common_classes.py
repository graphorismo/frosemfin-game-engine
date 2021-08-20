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

    def __init__(self, *, x: int = 0, y: int = 0):
        self.x = x
        self.y = y


class UniqueIDPool:
    _pool_of_free_ids: set[int]
    _pool_of_locked_ids: set[int]
    _size: int

    def __init__(self, *, size: int = 10):
        self._pool_of_free_ids = set()
        self._pool_of_locked_ids = set()
        for i in range(1, size+1):
            self._pool_of_free_ids.add(i)
        self._size = size

    def pop_unique_id(self) -> int:
        poped_id = self._pool_of_free_ids.pop()
        self._pool_of_locked_ids.add(poped_id)
        return poped_id

    def push_an_unique_id_back(self, pushed_id: int):
        if pushed_id in self._pool_of_locked_ids:
            self._pool_of_locked_ids.remove(pushed_id)
            self._pool_of_free_ids.add(pushed_id)
        else:
            raise RuntimeError("Tried to push back an id were not in the id-pool before"
                               "or is already freed")


class UniqueEntity:
    unique_id: int

    def __init__(self, unique_id: int):
        self.unique_id = unique_id

    def __hash__(self):
        return hash(self.unique_id)


class EntityData(UniqueEntity):
    coordinates: Vector2i

    def __init__(self, unique_id: int, *, x: int = 0, y: int = 0):
        super().__init__(unique_id)
        self.coordinates = Vector2i(x=x, y=y)


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

    def __init__(self, unique_id: int, *, x: int = 0, y: int = 0,
                 direction: DirectionEnum = DirectionEnum.NO_DIRECTION):
        super().__init__(unique_id, x=x, y=y)
        self.direction = direction


class BodyData(EntityData):
    hit_points: int

    def __init__(self, unique_id: int, *, x: int = 0, y: int = 0,
                 hp: int = 1):
        super().__init__(unique_id, x=x, y=y)
        self.hit_points = hp
