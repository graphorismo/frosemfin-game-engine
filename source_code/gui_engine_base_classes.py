from source_code.common_classes import *

from source_code.data_storage_base_classes import IDataStorage


class IGUIDrawer:

    # Functions to override in inherited classes:

    def initialize(self):
        raise RuntimeError("Can't find override for function"
                           " initialize(...) from interface IGUIDrawer")

    def add_an_obstacle_to_the_draw_buffer(self, obstacle_data: BodyData):
        raise RuntimeError("Can't find override for function"
                           " draw_an_obstacle(...) from interface IGUIDrawer")

    def add_a_projectile_to_the_draw_buffer(self, projectile_data: ProjectileData):
        raise RuntimeError("Can't find override for function"
                           " draw_a_projectile(...) from interface IGUIDrawer")

    def add_a_bot_to_the_draw_buffer(self, bot_data: BodyData):
        raise RuntimeError("Can't find override for function"
                           " draw_a_bot(...) from interface IGUIDrawer")

    def add_a_player_to_the_draw_buffer(self, player_data: BodyData):
        raise RuntimeError("Can't find override for function"
                           " draw_a_player(...) from interface IGUIDrawer")

    def set_the_draw_resolution(self, units_of_picture_per_one_unit_of_coordinates: int):
        raise RuntimeError("Can't find override for function"
                           " set_the_draw_resolution(...) from interface IGUIDrawer")

    def set_the_draw_area_size_in_draw_units(self, high: int, width: int):
        raise RuntimeError("Can't find override for function"
                           " set_the_draw_area_size_in_draw_units(...) from interface IGUIDrawer")

    def draw_the_draw_buffer_on_screen(self):
        raise RuntimeError("Can't find override for function"
                           " update_screen(...) from interface IGUIDrawer")

    def clear_the_draw_buffer(self):
        raise RuntimeError("Can't find override for function"
                           " clear_screen(...) from interface IGUIDrawer")

    def finish_work_and_die(self):
        raise RuntimeError("Can't find override for function"
                           " stop(...) from interface IGUIDrawer")


class GUIEngine:

    _data_storage: IDataStorage
    _gui_drawer: IGUIDrawer

    def __init__(self, data_storage: IDataStorage, gui_drawer: IGUIDrawer):
        self._data_storage = data_storage
        self._gui_drawer = gui_drawer
        # Checks for None
        if self._data_storage is None:
            raise RuntimeError("Get None instead of an IDataStorage exemplar "
                               "in the _data_storage field due PlayerController constructing")
        if self._gui_drawer is None:
            raise RuntimeError("Get None instead of an IGUIDrawer exemplar "
                               "in the _gui_drawer field due PlayerController constructing")

    def init_gui(self):
        self._gui_drawer.initialize()

    def update_frame(self):
        self._gui_drawer.clear_the_draw_buffer()
        self._draw_all_obstacles()
        self._draw_all_projectiles()
        self._draw_all_bots()
        self._draw_player()
        self._gui_drawer.draw_the_draw_buffer_on_screen()

    def _draw_all_obstacles(self):
        obstacles = self._data_storage.get_data_of_all_bodies_of_obstacles()
        for next_obstacle in obstacles:
            self._gui_drawer.add_an_obstacle_to_the_draw_buffer(next_obstacle)

    def _draw_all_projectiles(self):
        projectiles = self._data_storage.get_data_of_all_projectiles()
        for next_projectile in projectiles:
            self._gui_drawer.add_a_projectile_to_the_draw_buffer(next_projectile)

    def _draw_all_bots(self):
        bots = self._data_storage.get_data_of_all_bodies_of_bots()
        for next_bot in bots:
            self._gui_drawer.add_a_bot_to_the_draw_buffer(next_bot)

    def _draw_player(self):
        player = self._data_storage.get_data_of_the_body_of_the_player()
        self._gui_drawer.add_a_player_to_the_draw_buffer(player)

    def kill_gui(self):
        self._gui_drawer.finish_work_and_die()