import tkinter as tk
from ..gui_engine_base_classes import IGUIDrawer
from ..common_classes import *


class DrawBuffer:
    lines: list[str]
    high: int = 10
    width: int = 10

    basic_filler_symbol = '.'

    def __str__(self):
        return '\n'.join([self.lines[i] for i in range(self.high)])

    def fill_all_lines_with_basic_filler_symbol(self):
        for h in range(self.high):
            self.lines[h] = self.basic_filler_symbol[0]*self.width

    def fill_the_area_with_symbol(self, area_defining_vector_1: Vector2i, area_defining_vector_2: Vector2i,
                                  area_filler_symbol: str) -> str:
        top_line_index: int
        bottom_line_index: int
        left_edge_column_index: int
        right_edge_column_index: int
        # Define purposes of coordinates of vectors
        if area_defining_vector_1.y >= area_defining_vector_2.y:
            top_line_index = area_defining_vector_1.y
            bottom_line_index = area_defining_vector_2.y
        else:
            top_line_index = area_defining_vector_2.y
            bottom_line_index = area_defining_vector_1.y
        if area_defining_vector_1.x >= area_defining_vector_2.x:
            right_edge_column_index = area_defining_vector_1.x
            left_edge_column_index = area_defining_vector_2.x
        else:
            right_edge_column_index = area_defining_vector_2.x
            left_edge_column_index = area_defining_vector_1.x
        # Snapping of coordinates of vectors
        top_line_index = self._clip_number_to_fit_the_high_and_return_copy(top_line_index)
        bottom_line_index = self._clip_number_to_fit_the_high_and_return_copy(bottom_line_index)
        left_edge_column_index = self._clip_number_to_fit_the_width_and_return_copy(left_edge_column_index)
        right_edge_column_index = self._clip_number_to_fit_the_width_and_return_copy(right_edge_column_index)
        # Filling the area
        area_width = right_edge_column_index - left_edge_column_index
        for line_index in range(bottom_line_index, top_line_index):
            line_old_data = self.lines[line_index]
            self.lines[line_index] = line_old_data[0:left_edge_column_index] + \
                                     area_filler_symbol * area_width + \
                                     line_old_data[right_edge_column_index:]

    def _clip_number_to_fit_the_width_and_return_copy(self, number_to_clip: int) -> int:
        clipped_number: int
        if number_to_clip >= self.width:
            clipped_number = self.width - 1
        elif number_to_clip < 0:
            clipped_number = 0
        else:
            clipped_number = number_to_clip
        return clipped_number

    def _clip_number_to_fit_the_high_and_return_copy(self, number_to_clip: int) -> int:
        clipped_number: int
        if number_to_clip >= self.high:
            clipped_number = self.high - 1
        elif number_to_clip < 0:
            clipped_number = 0
        else:
            clipped_number = number_to_clip
        return clipped_number


class SimpleWindow(tk.Frame):
    text_graphics_field: tk.Text

    def __init__(self, master=None):
        tk.Frame.__init__(self, master, bg='thistle1')
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        self.text_graphics_field = tk.Text(self, bg='black', fg='white')
        self.text_graphics_field.grid()

    def show_draw_buffer(self, draw_buffer: DrawBuffer):
        self.text_graphics_field.insert(str(draw_buffer))


class TextModeGraphicTkinterGUIDrawer(IGUIDrawer):
    _window: SimpleWindow
    _draw_buffer: DrawBuffer = DrawBuffer()
    _text_draw_buffer: str = ""

    # Resolution scale the side of square of draw units that image 1 coordinate unit.
    # For example, if resolution set to 3, then square defined with vectors {0, 0} and {1, 1}
    # will be drawn as as square of symbols defined with vectors {0, 0} and {3, 3}
    _resolution_of_draw: int = 1

    def initialize(self):
        window = SimpleWindow()
        window.master.title('Sample application')

    def add_an_obstacle_to_the_draw_buffer(self, obstacle_data: BodyData):
        self._raise_an_exception_if_an_entity_have_negative_coordinates(obstacle_data)
        vector1, vector2 = \
            self._get_two_vectors_defining_draw_area_with_center_on_coordinates(obstacle_data.coordinates)
        self._draw_buffer.fill_the_area_with_symbol(vector1, vector2, '\u25a6')


    def add_a_projectile_to_the_draw_buffer(self, projectile_data: ProjectileData):
        self._raise_an_exception_if_an_entity_have_negative_coordinates(projectile_data)
        vector1, vector2 = \
            self._get_two_vectors_defining_draw_area_with_center_on_coordinates(projectile_data.coordinates)
        self._draw_buffer.fill_the_area_with_symbol(vector1, vector2, '\u2600')

    def add_a_bot_to_the_draw_buffer(self, bot_data: BodyData):
        self._raise_an_exception_if_an_entity_have_negative_coordinates(bot_data)
        vector1, vector2 = \
            self._get_two_vectors_defining_draw_area_with_center_on_coordinates(bot_data.coordinates)
        self._draw_buffer.fill_the_area_with_symbol(vector1, vector2, '\u25cf')

    def add_a_player_to_the_draw_buffer(self, player_data: BodyData):
        self._raise_an_exception_if_an_entity_have_negative_coordinates(player_data)
        vector1, vector2 = \
            self._get_two_vectors_defining_draw_area_with_center_on_coordinates(player_data.coordinates)
        self._draw_buffer.fill_the_area_with_symbol(vector1, vector2, '\u25c9')

    def set_the_draw_resolution(self, units_of_picture_per_one_unit_of_coordinates: int):
        if units_of_picture_per_one_unit_of_coordinates <= 0:
            raise RuntimeError(f"Receive a draw resolution less or equal to zero on the "
                               f"input of TextModeGraphicTkinterGUIDrawer::set_the_draw_resolution(...)")
        self._draw_buffer.resolution_in_units_of_picture_per_one_unit_of_coordinates \
            = units_of_picture_per_one_unit_of_coordinates

    def set_the_draw_area_size_in_draw_units(self, high: int, width: int):
        if high <= 0 or width <= 0:
            raise RuntimeError(f"Receive a draw area size number less or equal to zero on the "
                               f"input of TextModeGraphicTkinterGUIDrawer::set_the_draw_area_size_in_draw_units(...)")
        self._draw_buffer.high_in_draw_units = high
        self._draw_buffer.width_in_draw_units = width

    def draw_the_draw_buffer_on_screen(self):
        self._window.show_draw_buffer(self._draw_buffer)
        self._window.update_idletasks()
        self._window.update()

    def clear_the_draw_buffer(self):
        self._draw_buffer.fill_all_lines_with_basic_filler_symbol()

    def finish_work_and_die(self):
        self._window.destroy()

    def _raise_an_exception_if_an_entity_have_negative_coordinates(self, entity: EntityData):
        if entity.coordinates.x < 0 or entity.coordinates.y < 0:
            raise RuntimeError(f"Receive an entity with negative coordinates "
                               f"{entity.coordinates.x, entity.coordinates.y} "
                               f"on the input of TextModeGraphicTkinterGUIDrawer")

    def _get_two_vectors_defining_draw_area_with_center_on_coordinates\
                                                (self, center: Vector2i) -> (Vector2i, Vector2i):
        res_div_2, res_mod_2 = divmod(self._resolution_of_draw, 2)
        vector1 = Vector2i()
        vector1.y = center.y - res_div_2 + (1 - res_mod_2)
        vector1.x = center.x - res_div_2 + (1 - res_mod_2)
        vector2 = Vector2i()
        vector2.y = center.y + res_div_2
        vector2.x = center.x + res_div_2
        return vector1, vector2

