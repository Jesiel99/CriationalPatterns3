import abc
import copy
from abc import ABC


class EnterprisePrototype(abc.ABC):

    @abc.abstractmethod
    def shares_value(self):
        pass

    @abc.abstractmethod
    def clone(self):
      pass


class Petrobras(EnterprisePrototype):

    shares_value = 0

    def __init__(self, share):
        shares_value = share

    def clone(self):
        return copy.copy(self)


class Spotify(EnterprisePrototype):

    shares_value = 0

    def __init__(self, share):
        shares_value = share

    def clone(self):
       return copy.copy(self)