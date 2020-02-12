import abc

from src.game_state import GameState
from src.utils import Team


class Fighter:

    __metaclass__ = abc.ABCMeta

    __slots__ = ('armour',
                 'damage',
                 'hp',
                 'price',
                 'reward',
                 'team',
                 'alive')

    def __init__(self):
        pass

    def death(self):
        if self.alive:
            GameState().update_warriors(self.team, -1)
            GameState().update_coins(self.team ^ 1, self.reward)
            self.alive = False

    def upgrade_attribute(self, attribute: str, value: int):
        if not hasattr(self, attribute) or not isinstance(getattr(self, attribute), int):
            raise AttributeError('You can\'t change that')
        setattr(self, attribute, getattr(self, attribute) + value)
        if self.hp <= 0:
            self.death()

    def __repr__(self):
        return f'Fighter(armour={self.armour}, damage={self.damage}, hp={self.hp}, price={self.price},' \
               f'reward={self.reward}, alive={self.alive})'


class SmallFighter(Fighter):

    def __init__(self):
        super().__init__()
        self.armour = 2
        self.damage = 5
        self.hp = 15
        self.price = 2
        self.reward = 1
        self.alive = True


class AllySmallFighter(SmallFighter):

    def __init__(self):
        self.team = Team.ALLY.value
        super().__init__()
        GameState().update_warriors(self.team, 1)
        GameState().update_coins(self.team, -self.price)


class EnemySmallFighter(SmallFighter):

    def __init__(self):
        self.team = Team.ENEMY.value
        super().__init__()
        GameState().update_warriors(self.team, 1)
        GameState().update_coins(self.team, -self.price)


class MiddleFighter(Fighter):

    def __init__(self):
        super().__init__()
        self.armour = 3
        self.damage = 8
        self.hp = 25
        self.price = 3
        self.reward = 2
        self.alive = True


class AllyMiddleFighter(MiddleFighter):

    def __init__(self):
        self.team = Team.ALLY.value
        super().__init__()
        GameState().update_warriors(self.team, 1)
        GameState().update_coins(self.team, -self.price)


class EnemyMiddleFighter(SmallFighter):

    def __init__(self):
        self.team = Team.ENEMY.value
        super().__init__()
        GameState().update_warriors(self.team, 1)
        GameState().update_coins(self.team, -self.price)


class BigFighter(Fighter):

    def __init__(self):
        super().__init__()
        self.armour = 5
        self.damage = 12
        self.hp = 40
        self.price = 7
        self.reward = 5
        self.alive = True


class AllyBigFighter(MiddleFighter):

    def __init__(self):
        self.team = Team.ALLY.value
        super().__init__()
        GameState().update_warriors(self.team, 1)
        GameState().update_coins(self.team, -self.price)


class EnemyBigFighter(SmallFighter):

    def __init__(self):
        self.team = Team.ENEMY.value
        super().__init__()
        GameState().update_warriors(self.team, 1)
        GameState().update_coins(self.team, -self.price)
