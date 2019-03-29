from src.game_state import GameState
from src.units_factory import AllyFactory, EnemyFactory
from src.utils import Team


class Test:

    def test_singleton(self):
        a = GameState()
        b = GameState()
        assert id(a) == id(b)
        a.update_coins(Team.ALLY.value, 5)
        assert b.get_ally_coins() == 5
        a.update_coins(Team.ALLY.value, -5)

    def test_creating_units(self):
        unit = AllyFactory().get_big_fighter()
        assert GameState().get_ally_warriors_count() == 1
        unit.death()
        assert GameState().get_ally_warriors_count() == 0

    def test_getting_reward(self):
        GameState().clear()
        unit = AllyFactory().get_big_fighter()
        unit.death()
        assert GameState().get_enemy_coins() == unit.reward

    def test_getting_reward_twice(self):
        GameState().clear()
        unit = AllyFactory().get_big_fighter()
        unit.death()
        unit.death()
        assert GameState().get_enemy_coins() == unit.reward

    def test_upgrade(self):
        GameState().clear()
        unit = AllyFactory().get_big_fighter()
        print(unit)
        old_hp = unit.hp
        unit.upgrade_attribute('hp', 12)
        assert unit.hp == old_hp + 12

