from source_code.common_classes import *

from source_code.data_storage_base_classes import IDataStorage


class IGUIDrawer:

    # Functions to override in inherited classes:

    def initialize(self):
        raise RuntimeError("Can't find override for function"
                           " initialize(...) from interface IGUIDrawer")

    def draw_an_obstacle(self, obstacle_data: BodyData):
        raise RuntimeError("Can't find override for function"
                           " draw_an_obstacle(...) from interface IGUIDrawer")

    def draw_a_projectile(self, projectile_data: ProjectileData):
        raise RuntimeError("Can't find override for function"
                           " draw_a_projectile(...) from interface IGUIDrawer")

    def draw_a_bot(self, bot_data: BodyData):
        raise RuntimeError("Can't find override for function"
                           " draw_a_bot(...) from interface IGUIDrawer")

    def draw_a_player(self, player_data: BodyData):
        raise RuntimeError("Can't find override for function"
                           " draw_a_player(...) from interface IGUIDrawer")

    def clear_screen(self):
        raise RuntimeError("Can't find override for function"
                           " clear_screen(...) from interface IGUIDrawer")

    def stop(self):
        raise RuntimeError("Can't find override for function"
                           " stop(...) from interface IGUIDrawer")


class GUIEngine:

    data_storage: IDataStorage
    gui_drawer: IGUIDrawer

    def __init__(self, data_storage: IDataStorage, gui_drawer: IGUIDrawer):
        self.data_storage = data_storage
        self.gui_drawer = gui_drawer

    def init_gui(self):
        self.gui_drawer.initialize()

    def update_frame(self):
        self.gui_drawer.clear_screen()
        self._draw_all_obstacles()
        self._draw_all_projectiles()
        self._draw_all_bots()
        self._draw_player()

    def _draw_all_obstacles(self):
        obstacles = self.data_storage.get_data_of_all_bodies_of_obstacles()
        for next_obstacle in obstacles:
            self.gui_drawer.draw_an_obstacle(next_obstacle)

    def _draw_all_projectiles(self):
        projectiles = self.data_storage.get_data_of_all_projectiles()
        for next_projectile in projectiles:
            self.gui_drawer.draw_a_projectile(next_projectile)

    def _draw_all_bots(self):
        bots = self.data_storage.get_data_of_all_bodies_of_bots()
        for next_bot in bots:
            self.gui_drawer.draw_a_bot(next_bot)

    def _draw_player(self):
        player = self.data_storage.get_data_of_the_body_of_the_player()
        self.gui_drawer.draw_a_player(player)

    def kill_gui(self):
        self.gui_drawer.stop()