
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
        return self.fait == fait.fait


    def __hash__(self):
        """Redefinition de la methode de hashing d'un objet fait

        Doit-etre redefini si __eq__ est redefini (notamment pour l'utilisation dans des sets)
        """
        sum = 0
        for i in self.fait:
            sum += ord(i)
        return sum

    def __repr__(self):
        """Representation d'un fait sous forme de string
        """
        return self.fait
