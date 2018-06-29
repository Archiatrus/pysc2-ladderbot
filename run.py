import sys
import platform
from absl import logging
from absl import app
from absl import flags

from pysc2.env import sc2_env
from pysc2.env import run_loop

from pysc2.env import remote_sc2_env

# !!! LOAD YOUR BOT HERE !!!
from simple_agent import SimpleAgent
AGENT = SimpleAgent()
RACE = sc2_env.Race.protoss
STEP_MUL = 8
AGENT_INTERFACE_FORMAT = sc2_env.parse_agent_interface_format(
    feature_screen=84,
    feature_minimap=64,
    rgb_screen=None,
    rgb_minimap=None,
    action_space="FEATURES", #FEATURES or RGB
    use_feature_units=False)

# Flags
FLAGS = flags.FLAGS
flags.DEFINE_integer("GamePort", None, "GamePort")
flags.DEFINE_integer("StartPort", None, "StartPort")
flags.DEFINE_string("LadderServer", "127.0.0.1", "LadderServer")
flags.DEFINE_string("OpponentId", None, "OpponentId")

# Run ladder game
def run_ladder_game():
    # Join ladder game
    with remote_sc2_env.RemoteSC2Env(
        host=FLAGS.LadderServer,
		      host_port=FLAGS.GamePort,
        lan_port=FLAGS.StartPort + 2, #s2client-api and pysc2 have different opinions what "startport" means,
        race=RACE,
        step_mul=STEP_MUL,
        agent_interface_format=AGENT_INTERFACE_FORMAT,
        visualize=platform.system() == "Linux") as env:
        agents = [AGENT]
        logging.info("Connected, starting run_loop.")
        try:
            run_loop.run_loop(agents, env)
        except remote_sc2_env.RestartException:
            pass
    logging.info("Done.")


# Start game
def main(argv):
    if "--LadderServer" in sys.argv:
        # Ladder game started by LadderManager
        logging.info("Starting ladder game...")
        run_ladder_game()
    else:
        # Local game
        logging.info("Starting local game...")
        players = []
        players.append(sc2_env.Agent(RACE))
        players.append(sc2_env.Bot(sc2_env.Race.random, sc2_env.Difficulty.very_easy))

        with sc2_env.SC2Env(
            map_name="Simple64",
            players=players,
            step_mul=STEP_MUL,
            agent_interface_format=AGENT_INTERFACE_FORMAT) as env:
            agents = [AGENT]
            max_steps = 0 #no max steps
            max_episodes = 1
            run_loop.run_loop(agents, env, max_steps, max_episodes)


if __name__ == '__main__':
    app.run(main)
