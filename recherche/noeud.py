from math import sqrt

class Noeud:
    """ Noeud d'un graphe """
    NOT_VISITED = 0
    OPEN = 1
    CLOSED = 2

    
    def __init__(self, x, y, label=''):
        """
            :param x: coordonnee x du Noeud
            :param y: coordonnee y du Noeud
            :param label: nom du Noeud
        """
        self.x = x
        self.y = y
        self.label = label

        self.etat = Noeud.NOT_VISITED
        self.cout = None
        self.cout_f = None

    def distance(self, n):
        """ Distance euclidienne entre le Noeud courant et n """
        return sqrt((self.x - n.x)**2 + (self.y - n.y)**2)

    def __eq__(self, n):
        return self.x == n.x and self.y == n.y and self.label == n.label

    def __hash__(self):
        return self.x + self.y + sum(map(ord, self.label))

    def __repr__(self):
        if self.cout is not None:
            return '(Cout: {}, cout_f: {}): {}'.format(self.cout, self.cout_f, self.label)
        return '({}, {}): {}'.format(self.x, self.y, self.label)