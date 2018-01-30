
class Fait:
    """Representation d'un fait pour l'inference"""
    def __init__(self, fait):
        """
        :param fait: description du fait (string, list, etc.)
        """
        self.fait = fait

    def __eq__(self, fait):
        """Redefinition de l'egalite pour les faits

        Permet de comparer des faits avec f1 == f2 ou f1 is f2
        """

        if isinstance(fait, Fait):
            return self.fait == fait.fait
        return False

    def __hash__(self):
        """Redefinition de la methode de hashing d'un objet fait

        Doit-etre redefini si __eq__ est redefini (notamment pour l'utilisation dans des sets)
        """

        if type(self.fait) == type(''):
            return sum(map(ord, self.fait))
        if type(self.fait) == type([]):
            return sum([sum(map(ord, e)) for e in self.fait])

    def __repr__(self):
        """Representation d'un fait sous forme de string
        """
        return str(self.fait)

