from src.utils import Singleton


class GameState(metaclass=Singleton):

    def __init__(self):
        self._ally_coins = 0
        self._enemy_coins = 0
        self._ally_hp = 0
        self._enemy_hp = 0

    def update_ally_coins(self, delta):
        self._ally_coins += delta

    def update_enemy_coins(self, delta):
        self._enemy_coins += delta

    def update_ally_hp(self, delta):
        self._ally_hp += delta

    def update_enemy_hp(self, delta):
        self._enemy_hp += delta

    def get_ally_coins(self):
        return self._ally_coins

    def get_enemy_coins(self):
        return self._enemy_coins

    def get_ally_hp(self):
        return self._ally_hp

    def get_enemy_hp(self):
        return self._enemy_hp
