
class Regle:
    """Representation d'une regle d'inference"""

    def __init__(self, conditions, conclusion):
        """
        :param list conditions: les faits necessaires a declencher la regle
        :param Fait conclusion: le fait resultant du declenchement de la regle
        """
        self.conditions = frozenset(conditions)
        self.conclusion = conclusion

    def satisfaite_par(self, fait):
        """
        :return: True si "fait" fait partie des conditions de declenchement
        """
        for i in self.conditions:
            if i == fait:
                return True
        return False

    def satisfaite(self, faits):
        """
        :return: True si les faits en parametres suffisent a dechlencher la regle
        """
        if self.conditions.issubset(faits):
            return True
        return False

    @property
    def __repr__(self):

        return self.conditions + self.conclusions