import unittest
from RPS_game import play, mrugesh, abbey, quincy, kris
from RPS import player


class UnitTests(unittest.TestCase):
    print()

    def test_player_vs_quincy(self):
        print("\nTesting game against Quincy...")
        actual = play(player, quincy, 1000) >= 60
        self.assertTrue(
            actual,
            'Expected player to defeat Quincy at least 60% of the time.')

    def test_player_vs_abbey(self):
        print("Testing game against Abbey...")
        actual = play(player, abbey, 1000) >= 60
        self.assertTrue(
            actual,
            'Expected player to defeat Abbey at least 60% of the time.')

    def test_player_vs_kris(self):
        print("\nTesting game against Kris...")
        actual = play(player, kris, 1000) >= 60
        self.assertTrue(
            actual, 'Expected player to defeat Kris at least 60% of the time.')

    def test_player_vs_mrugesh(self):
        print("\nTesting game against Mrugesh...")
        actual = play(player, mrugesh, 1000) >= 60
        self.assertTrue(
            actual,
            'Expected player to defeat Mrugesh at least 60% of the time.')


if __name__ == "__main__":
    unittest.main()
