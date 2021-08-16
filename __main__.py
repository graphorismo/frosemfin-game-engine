from source_code.game_engine_base_classes import *


def make_and_configure_a_game_engine_builder() -> GameEngineBuilder:
    new_game_engine_builder = GameEngineBuilder()

    # Attach interfaces realisations here
    new_game_engine_builder.data_storage = None
    new_game_engine_builder.keyboard_reader = None
    new_game_engine_builder.world_logic_core = None
    new_game_engine_builder.bot_ai_core = None
    new_game_engine_builder.gui_core = None

    return new_game_engine_builder


# Main script
print("Attaching cores of engines")
game_engine_builder = make_and_configure_a_game_engine_builder()
print("Build the game engine")
game_engine = game_engine_builder.build_a_game_engine()
print("Initialise the game engine")
game_engine.initialize()
print("Running the game engine")
# TODO add a stop flag to the GameEngine to break main while loop with it
while True:
    game_engine.process_a_single_full_game_tick()
print("Shutdown the game engine")
game_engine.shutdown()
print("Game engine stopped. You can exit safely.")







