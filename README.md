# pysc2 Ladder Bot Example
This is a StarCraft 2 example bot using DeepMind's [PySC2 - StarCraft II Learning Environment](https://github.com/deepmind/pysc2) that has the ability to integrate with the [LadderManager](https://github.com/Cryptyc/Sc2LadderServer) so that it can run against other bots on the [SC2 AI Ladder](http://sc2ai.net).

This bot can be run either locally against a computer opponent, or through the [LadderManager](https://github.com/Cryptyc/Sc2LadderServer). The file "run.py" is used for both variants. The example bot itself does nothing.

## Requirements
* [PySC2 - StarCraft II Learning Environment](https://github.com/deepmind/pysc2)

## Usage

### Run a basic game 
```
python run.py
```
You can modify run.py to load your own bot or change the computer opponent.

### Run a LadderManager game
If you want to run LadderManager yourself to test the bot against other ladder bots, you must first download and compile [LadderManager](https://github.com/Cryptyc/Sc2LadderServer). Then extract pysc2-ladderbot into LadderManager/Bots/pysc2bot and add the following to LadderManager/Bots/LadderBots.json:
```
"SimpleAgent": {
			"Race": "Protoss",
			"Type": "Python",
			"RootPath": "C:/Ladder/Bots/pysc2bot/",
			"FileName": "run.py"
		},
```
You should now be able to configure LadderManager to start a game with "pysc2bot" as one of the opponents (by modifying LadderManager/matchupList).

## Additional resources
For more info check out the [sc2ai.net wiki](http://wiki.sc2ai.net/Main_Page). If you have questions, this [Discord](https://discord.gg/qTZ65sh) is the best place to ask them.

## Pull requests
I am very new to Python in general. If you see some glaring mistakes or think you can improve this interface, please make a PR. Thank you.

