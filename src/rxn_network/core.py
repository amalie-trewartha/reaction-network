from abc import ABCMeta, abstractmethod, abstractproperty
from typing import List

from monty.json import MSONable

from rxn_network.core.reaction import Reaction
from pymatgen.entries import Entry


class Reaction(MSONable, metaclass=ABCMeta):
    " Base definition for a Reaction "

    @abstractproperty
    def energy(self):
        " The energy of this reaction in eV per ??"

    @abstractproperty
    def coefficients(self) -> np.array:
        """
        Coefficients of the reaction
        """

    @abstractproperty
    def compositions(self) -> List[Composition]:
        """
        List of all compositions in the reaction.
        """

    @abstractproperty
    def elements(self) -> List[Element]:
        """
        List of elements in the reaction
        """


class CostFunction(MSONable, metaclass=ABCMeta):
    " Base definition for a cost function "

    @abstractmethod
    def evaluate(self, rxn: Reaction) -> float:
        " Evaluates the cost function on a reaction "


class Enumerator(MSONable, metaclass=ABCMeta):
    " Base definition for a reaction enumeration methodology "

    @abstractmethod
    def enumerate(self, entries) -> List[Reaction]:
        " Evaluates the cost function on a reaction "


class Pathway(MSONable, metaclass=ABCMeta):
    " Base definition for a reaction pathway "

    @abstractproperty
    def number_intermediates(self):
        " The number of intermediates in the total pathway "


class ReactionNetwork(MSONable, metaclass=ABCMeta):
    " Base definition for a reaction network "

    def __init__(self, entries: List[Entry], enumerators, cost_function):

        self.entries = entries
        self.enumerators = enumerators
        self.cost_function = cost_function

    @abstractmethod
    def find_best_rxn_pathways(self, precursors, targets, num=15):
        " Find the N best reaction pathways "
