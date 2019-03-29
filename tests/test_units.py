from src.game_state import GameState


class Test:

    def test_singleton(self):
        a = GameState()
        b = GameState()
        assert id(a) == id(b)
        a.update_ally_coins(5)
        assert b.get_ally_coins() == 5
        a.update_ally_coins(-5)
