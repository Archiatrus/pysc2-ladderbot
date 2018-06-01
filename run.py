import sys
import enum
from absl import logging
from absl import app

from pysc2.env import sc2_env
from pysc2.env import run_loop
from pysc2.agents import random_agent


from __init__ import run_ladder_game

from simple_agent import SimpleAgent

agent = SimpleAgent()
race = sc2_env.Race.protoss;
# Start game
def main(argv):
    step_mul = 8
    agent_interface_format=sc2_env.parse_agent_interface_format(
          feature_screen=84,
          feature_minimap=64,
          rgb_screen=None,
          rgb_minimap=None,
          action_space="FEATURES", #FEATURES or RGB
          use_feature_units=False)
    
    if "--LadderServer" in sys.argv:
        # Ladder game started by LadderManager
        logging.info("Starting ladder game...")
        run_ladder_game(agent,race,step_mul,agent_interface_format)
    else:
        # Local game
        logging.info("Starting local game...")
        players = []
        players.append(sc2_env.Agent(race))
        players.append(sc2_env.Bot(sc2_env.Race.random,sc2_env.Difficulty.very_easy))

        with sc2_env.SC2Env(
        map_name="Simple64",
        players=players,
        agent_interface_format=agent_interface_format) as env:
            agents=[agent]
            max_steps = 0 #no max steps
            max_episodes = 1
            run_loop.run_loop(agents, env,max_steps,max_episodes)


if __name__ == '__main__':
    app.run(main)