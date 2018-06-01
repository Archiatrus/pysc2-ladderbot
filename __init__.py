import sys
from absl import app
from absl import logging
from absl import flags
import platform

from pysc2.env import remote_sc2_env
from pysc2.env import run_loop
from pysc2.maps.lib import get_maps

FLAGS = flags.FLAGS
flags.DEFINE_integer("GamePort", None,"GamePort")
flags.DEFINE_integer("StartPort", None,"StartPort")
flags.DEFINE_string("LadderServer","127.0.0.1","LadderServer")

# Run ladder game
def run_ladder_game(agent,race,step_mul,agent_interface_format):
    
    #Setting up ports
    if FLAGS.LadderServer != "127.0.0.1":
        host = "127.0.0.1"
    else:
        host = FLAGS.LadderServer
		
    #The environment expects a map even though it is not used
    #So just use an arbitrary one
    available_maps = get_maps()
    map=list(available_maps.keys())[0]

    # Join ladder game
    with remote_sc2_env.RemoteSC2Env(
            map_name=map,
            host=host,
			host_port=FLAGS.GamePort,
            lan_port=FLAGS.StartPort + 2, #s2client-api and pysc2 have different opinions what "startport" means,
            race=race,
            step_mul=step_mul,
            agent_interface_format=agent_interface_format,
            visualize=platform.system() == "Linux") as env:
        agents = [agent]
        logging.info("Connected, starting run_loop.")
        try:
            run_loop.run_loop(agents, env)
        except remote_sc2_env.RestartException:
            pass
    logging.info("Done.")
