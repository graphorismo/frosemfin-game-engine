from common_classes import *


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
