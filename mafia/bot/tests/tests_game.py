import unittest
from mafia.bot.functions.game import MafiaManager
from mafia.bot.functions.player import Player

class TestMafiaManager(unittest.TestCase):

    def setUp(self):
        self.manager = MafiaManager()

    def test_append_player(self):
        # Проверим, что добавление игрока работает корректно
        self.manager.append_player(user_id=1, name="Player1")
        self.assertEqual(len(self.manager._players), 1)
        self.assertEqual(self.manager._players[0].name, "Player1")
        self.assertEqual(self.manager._players[0].user_id, 1)

    def test_remove_player(self):
        self.manager.append_player(user_id=1, name="Player1")
        self.manager.remove_player(1)
        self.assertEqual(len(self.manager._players), 0)

    def test_kill_player(self):
        self.manager.append_player(user_id=1, name="Player1")
        self.manager._players[0].is_alive = True
        result = self.manager.kill_player(user_id=1)
        self.assertFalse(self.manager._players[0].is_alive)
        self.assertIn("Player1", result)



if __name__ == '__main__':
    unittest.main()