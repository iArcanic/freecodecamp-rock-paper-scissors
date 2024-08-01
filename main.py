# This entrypoint file to be used in development. Start by reading README.md
from RPS_game import play, mrugesh, abbey, quincy, kris, human, random_player
from RPS import player
from unittest import main

# print("Testing against Quincy...")
# play(player, quincy, 1000)

# print("\nTesting against Abbey...")
# play(player, abbey, 1000)

# print("\nTesting against Kris...")
# play(player, kris, 1000)

# print("\nTesting against Mrugesh...")
# play(player, mrugesh, 1000)

# Uncomment line below to play interactively against a bot:
# play(human, abbey, 20, verbose=True)

# Uncomment line below to play against a bot that plays randomly:
# play(human, random_player, 1000)

# Uncomment line below to run unit tests automatically
print("\nRunning test_module class...")
main(module='test_module', exit=False)
