from src.utils import Singleton, Team


class GameState(metaclass=Singleton):

    def __init__(self):
        self._coins = [0, 0]
        self._warriors = [0, 0]

    def update_coins(self, team, delta):
        self._coins[team] += delta

    def update_warriors(self, team, delta):
        self._warriors[team] += delta

    def get_ally_warriors_count(self):
        return self._warriors[Team.ALLY.value]

    def get_enemy_warriors_count(self):
        return self._warriors[Team.ENEMY.value]

    def get_ally_coins(self):
        return self._coins[Team.ALLY.value]

    def get_enemy_coins(self):
        return self._coins[Team.ENEMY.value]

    def clear(self):
        self._coins = [0, 0]
        self._warriors = [0, 0]

    def __repr__(self):
        return f"Current Game State:\n" \
               f"COINS\n" \
               f"ALLY {self._coins[0]} : {self._coins[1]} ENEMY\n" \
               f"WARRIORS\n" \
               f"ALLY {self._warriors[0]} : {self._warriors[1]} ENEMY"
