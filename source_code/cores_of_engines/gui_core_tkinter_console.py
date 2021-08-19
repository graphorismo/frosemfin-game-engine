import tkinter as tk
from ..gui_engine_base_classes import IGUIDrawer
from ..common_classes import *


class DrawBuffer:
    lines: list[str] = [str() for _ in range(10)]
    _high: int
    _width: int

    basic_filler_symbol = '.'

    def __str__(self):
        return '\n'.join([self.lines[i] for i in range(self._high)])

    def update_size_and_clear(self, high: int, width: int):
        self._high = high
        self._width = width
        self.lines = [str() for _ in range(high)]
        self.fill_all_lines_with_basic_filler_symbol()

    def fill_all_lines_with_basic_filler_symbol(self):
        for h in range(self._high):
            self.lines[h] = self.basic_filler_symbol[0]*self._width

    def draw_a_symbol_on_coordinates(self, symbol: str, coordinates: Vector2i):
        line_old_data = self.lines[coordinates.y]
        self.lines[coordinates.y] = line_old_data[0 : coordinates.x - 1] + \
                                 symbol[0] +\
                                 line_old_data[coordinates.x+1 : ]


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
        area_width = right_edge_column_index - left_edge_column_index + 1
        for line_index in range(bottom_line_index, top_line_index+1):
            line_old_data = self.lines[line_index]
            self.lines[line_index] = line_old_data[0:left_edge_column_index-1] + \
                                     area_filler_symbol[0] * area_width + \
                                     line_old_data[right_edge_column_index+1:]

    def _clip_number_to_fit_the_width_and_return_copy(self, number_to_clip: int) -> int:
        clipped_number: int
        if number_to_clip >= self._width:
            clipped_number = self._width - 1
        elif number_to_clip < 0:
            clipped_number = 0
        else:
            clipped_number = number_to_clip
        return clipped_number

    def _clip_number_to_fit_the_high_and_return_copy(self, number_to_clip: int) -> int:
        clipped_number: int
        if number_to_clip >= self._high:
            clipped_number = self._high - 1
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
        self.text_graphics_field.delete('0.0')
        self.text_graphics_field.insert('0.0', str(draw_buffer))


class TextModeGraphicTkinterGUIDrawer(IGUIDrawer):
    _window: SimpleWindow
    _draw_buffer: DrawBuffer = DrawBuffer()
    _text_draw_buffer: str = ""

    # Resolution scale the side of square of draw units that image 1 coordinate unit.
    # For example, if resolution set to 3, then square defined with vectors {0, 0} and {1, 1}
    # will be drawn as as square of symbols defined with vectors {0, 0} and {3, 3}
    _resolution_of_draw: int = 1

    def initialize(self):
        self._window = SimpleWindow()
        self._window.master.title('Sample application')

    def add_an_obstacle_to_the_draw_buffer(self, obstacle_data: BodyData):
        self._raise_an_exception_if_an_entity_have_negative_coordinates(obstacle_data)
        if self._resolution_of_draw > 1:
            vector1, vector2 = \
                self._get_two_vectors_defining_draw_area_with_center_on_coordinates(obstacle_data.coordinates)
            self._draw_buffer.fill_the_area_with_symbol(vector1, vector2, '\u25a6')
        else:
            self._draw_buffer.draw_a_symbol_on_coordinates('\u25a6', obstacle_data.coordinates)

    def add_a_projectile_to_the_draw_buffer(self, projectile_data: ProjectileData):
        self._raise_an_exception_if_an_entity_have_negative_coordinates(projectile_data)
        if self._resolution_of_draw > 1:
            vector1, vector2 = \
                self._get_two_vectors_defining_draw_area_with_center_on_coordinates(projectile_data.coordinates)
            self._draw_buffer.fill_the_area_with_symbol(vector1, vector2, '\u2600')
        else:
            self._draw_buffer.draw_a_symbol_on_coordinates('\u2600', projectile_data.coordinates)

    def add_a_bot_to_the_draw_buffer(self, bot_data: BodyData):
        self._raise_an_exception_if_an_entity_have_negative_coordinates(bot_data)
        if self._resolution_of_draw > 1:
            vector1, vector2 = \
                self._get_two_vectors_defining_draw_area_with_center_on_coordinates(bot_data.coordinates)
            self._draw_buffer.fill_the_area_with_symbol(vector1, vector2, '\u25cf')
        else:
            self._draw_buffer.draw_a_symbol_on_coordinates('\u25cf', bot_data.coordinates)

    def add_a_player_to_the_draw_buffer(self, player_data: BodyData):
        self._raise_an_exception_if_an_entity_have_negative_coordinates(player_data)
        if self._resolution_of_draw > 1:
            vector1, vector2 = \
                self._get_two_vectors_defining_draw_area_with_center_on_coordinates(player_data.coordinates)
            self._draw_buffer.fill_the_area_with_symbol(vector1, vector2, '\u25c9')
        else:
            self._draw_buffer.draw_a_symbol_on_coordinates('\u25c9', player_data.coordinates)

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
        self._draw_buffer.update_size_and_clear(high, width)

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


