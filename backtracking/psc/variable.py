

class Variable:
    """Modelisation d'une variable dans un systeme de contraintes"""

    def __init__(self, nom, domaine, val=None):
        """
            :param nom: nom de la variable
            :param list domaine: le domain de definition de la variable
            :param val: valeur de depart
        """

        self.nom = nom
        self.domaine = domaine
        self.val = val

    def taille_domaine(self):
        """ La taille du domaine de definition de la variable

            :return: la taille du domaine
        """
        return len(self.domaine)

    def __eq__(self, that):
        return self.nom == that.nom

    def __hash__(self):
        return sum(map(ord, self.nom))

    def __repr__(self):
        return '{} = {}, domaine: {}'.format(self.nom, self.val, self.domaine)
