" A basic reaction pathway class"

from typing import List, Optional

from rxn_network.core import Pathway, Reaction


class BasicPathway(Pathway):
    """
    Simple pathway class for storing multiple ComputedReaction objects which form a single
    reaction pathway with no constraints on stoichiometry
    """

    def __init__(self, reactions: List[Reaction], costs: Optional[List[float]] = None):
        """
        Args:
            rxns ([ComputedReaction]): list of ComputedReaction objects in pymatgen
                which occur along path.
            costs ([float]): list of corresponding costs for each reaction.
        """
        self._reactions = reactions

        if not costs:
            costs = []

        self.costs = costs

    def __repr__(self):
        path_info = ""
        for rxn in self.reactions:
            path_info += f"{rxn} (dG = {round(rxn.energy_per_atom, 3)} eV/atom) \n"

        path_info += f"Total Energy: {round(self.energy_per_atom,3)}"

        return path_info

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return all(
                [
                    other_rxn == rxn
                    for other_rxn, rxn in zip(other.reactions, self.reactions)
                ]
            )

        return False

    def __hash__(self):
        return hash(tuple(self.reactions))
