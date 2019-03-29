import abc


class UnitFactory:

    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_small_fighter(self):
        pass

    @abc.abstractmethod
    def get_middle_fighter(self):
        pass

    @abc.abstractmethod
    def get_big_fighter(self):
        pass


class AllyFactory(UnitFactory):

    def get_small_fighter(self):
        return AllySmallFighter()

    def get_middle_fighter(self):
        return AllyMiddleFighter()

    def get_big_fighter(self):
        return AllyBigFighter()


class EnemyFactory(UnitFactory):

    def get_small_fighter(self):
        return EnemySmallFighter()

    def get_middle_fighter(self):
        return EnemyMiddleFighter()

    def get_big_fighter(self):
        return EnemyBigFighter()
