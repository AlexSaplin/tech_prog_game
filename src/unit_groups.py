import abc

from src.units import Fighter, AllySmallFighter, AllyMiddleFighter, AllyBigFighter


class UnitArmyBase:

    __metaclass__ = abc.ABCMeta

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, parent):
        self._parent = parent

    def add(self, component):
        pass

    def remove(self, component):
        pass

    @abc.abstractmethod
    def operation(self):
        pass


class ArmyLeaf(UnitArmyBase):

    def __init__(self, fighter: Fighter):
        self._fighter = fighter

    def operation(self):
        return [self._fighter]


class UnitArmy(UnitArmyBase):

    def __init__(self):
        self._children = []

    def add(self, component: UnitArmyBase):
        self._children.append(component)
        component.parent = self

    def remove(self, component: UnitArmyBase):
        self._children.remove(component)
        component.parent = None

    def operation(self):
        units = []
        for child in self._children:
            units.extend(child.operation())
        return units


if __name__ == '__main__':
    a = AllySmallFighter()
    b = AllyMiddleFighter()
    c = AllyBigFighter()
    army = UnitArmy()
    a_leaf = ArmyLeaf(a)
    b_leaf = ArmyLeaf(b)
    c_leaf = ArmyLeaf(c)
    army.add(a_leaf)
    army.add(b_leaf)
    army1 = UnitArmy()
    army1.add(c_leaf)
    print(army1.operation())
    print(army.operation())
    army.add(army1)
    print(army.operation())
