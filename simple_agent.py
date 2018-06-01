## Inspired by  StevenBrown 
"""A base agent to write custom scripted agents."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from pysc2.lib import actions
from pysc2.agents import base_agent
from pysc2.lib import features 

# Functions
_NOOP = actions.FUNCTIONS.no_op.id

class SimpleAgent(base_agent.BaseAgent):
  


  def step(self, obs):
      super(SimpleAgent, self).step(obs)

      return actions.FunctionCall(_NOOP, [])