import abc

from game_state import GameState


class Fighter:

    __metaclass__ = abc.ABCMeta

    __slots__ = ('armour',
                 'damage',
                 'hp',
                 'price',
                 'reward',
                 'tag')

    def __init__(self):
        pass

    @abc.abstractmethod
    def attack(self, enemy):
        pass

    @abc.abstractmethod
    def death(self):
        pass

    def upgrade_attribute(self, attribute, value):
        if not hasattr(self, attribute):
            raise AttributeError('Fighter doesn\'t have that attribute')
        self.__dict__[attribute] += value


class SmallFighter(Fighter):

    def __init__(self):
        super().__init__()
        self.armour = 2
        self.damage = 5
        self.hp = 15
        self.price = 2
        self.reward = 1

    def attack(self, enemy: Fighter):
        