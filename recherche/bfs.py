from solver import Solver
from noeud import Noeud

class BFSSolver(Solver):
    """ Recherche de chemin avec BFS """
    def ajoute_voisins(self, q, n):
        l = q[:]
        s = self.graphe.voisins(n)

        # Pour la recherce BFS, il sufit d'ajouter les voisins pas encore
        # ouverts (deja dans la queue) ou fermes (deja visites)
        s = [x[0] for x in s if x[0].etat == Noeud.NOT_VISITED]
        for x in s:
            x.etat = Noeud.OPEN

        l.extend(s)

        return l
