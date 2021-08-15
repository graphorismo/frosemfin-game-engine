from source_code.common_classes import *

from source_code.bot_ai_engine_base_classes import *
from source_code.data_storage_base_classes import *
from source_code.gui_engine_base_classes import *
from source_code.player_controller_base_classes import *
from source_code.world_logic_engine_base_classes import *


class GameEngine:
    data_storage: IDataStorage
    gui_engine: GUIEngine
    player_controller: PlayerController
    world_logic_engine: WordLogicEngine
    bot_ai_engine: BotAiEngine

    def initialize(self):
        self.gui_engine.init_gui()

    def process_a_single_full_game_tick(self):
        self.world_logic_engine.process_world_logic_effects()

        self.player_controller.react_to_the_last_players_action()

        self.bot_ai_engine.load_data_to_consider_by_ai()
        self.bot_ai_engine.calculate_and_perform_bots_actions()

        self.gui_engine.update_frame()

    def shutdown(self):
        self.gui_engine.kill_gui()


class GameEngineBuilder:
    data_storage: IDataStorage
    gui_core: IGUIDrawer
    keyboard_reader: IKeyboardReader
    world_logic_core: IWorldLogicCore
    bot_ai_core: IBotAiCore

    def build_a_game_engine(self) -> GameEngine:
        self._do_checks_for_Nones_in_fields()
        game_engine = GameEngine()
        game_engine.data_storage = self.data_storage
        game_engine.gui_engine = GUIEngine(self.data_storage, self.gui_core)
        game_engine.player_controller = PlayerController(self.data_storage, self.keyboard_reader)
        game_engine.world_logic_engine = WordLogicEngine(self.data_storage, self.world_logic_core)
        game_engine.bot_ai_engine = BotAiEngine(self.data_storage, self.bot_ai_core)
        return game_engine

    def _do_checks_for_Nones_in_fields(self):
        # Checks for None
        if self.data_storage is None:
            raise RuntimeError("Get None instead of an IDataStorage exemplar "
                               "in the data_storage field due GameEngineBuilder::build_a_game_engine()")
        if self.gui_core is None:
            raise RuntimeError("Get None instead of an IGUIDrawer exemplar "
                               "in the gui_core field due GameEngineBuilder::build_a_game_engine()")
        if self.keyboard_reader is None:
            raise RuntimeError("Get None instead of an IKeyboardReader exemplar "
                               "in the keyboard_reader field due GameEngineBuilder::build_a_game_engine()")
        if self.world_logic_core is None:
            raise RuntimeError("Get None instead of an IWorldLogicCore exemplar "
                               "in the world_logic_core field due GameEngineBuilder::build_a_game_engine()")
        if self.bot_ai_core is None:
            raise RuntimeError("Get None instead of an IBotAiCore exemplar "
                               "in the bot_ai_core field due GameEngineBuilder::build_a_game_engine()")
