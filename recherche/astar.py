from solver import Solver
from noeud import Noeud

class AStarSolver(Solver):
    """ Recherche de chemin avec AStar """

    def __init__(self, graphe):
        """
            :param graphe: le Graphe de recherche
        """
        super(AStarSolver, self).__init__(graphe)
        # l'heuristique a utiliser (typiquement: lambda n: n.distance(but))
        self.h = lambda x: 0

    def solve(self, a, b):
        self.h = lambda x: x.distance(b)
        for n in self.graphe.noeuds:
            n.cout = None
            n.cout_f = None

        a.cout = 0
        a.cout_f = self.h(a)

        return super(AStarSolver, self).solve(a, b)

    def ajoute_voisins(self, q, n):
        l = q[:]

        # pour la recherce astar on teste tous les voisins
        s = self.graphe.voisins(n)
        for v in s:
            # cout jusqu'au noeud courant = cout jusqu'au noeud precedent + cout entre les deux noeuds
            cout = n.cout + v[1]
            # cout estime = cout jusqu'au noeud courant + cout estime entre le noeud courant et le but
            cout_f = cout + self.h(v[0])
            # si le voisin n'est pas dans la queue ni fermé ou
            # si un chemin moins couteux est decouvert alors
            # met a jour le cout et ajoute le voisin dans la queue
            if (v[0].cout_f is None or cout_f < v[0].cout_f) :
                v[0].cout = cout
                v[0].cout_f = cout_f
                v[0].etat = Noeud.OPEN

                if not v[0] in l:
                    l.append(v[0])

        l = sorted(l, key=lambda x: x.cout_f)

        return l