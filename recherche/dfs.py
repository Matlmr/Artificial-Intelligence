from solver import Solver
from noeud import Noeud

class DFSSolver(Solver):
    """ Recherche de chemin avec DFS """
    def ajoute_voisins(self, q, n):
        l = q[:]
        s = self.graphe.voisins(n)
        # pour la recherce DFS, il faut ajouter tous les voisins pas encore fermes
        s = [x[0] for x in s if x[0].etat != Noeud.CLOSED]
        for x in s:
            # si un voisin est deja ouvert (deja dans la queue) il faut le deplacer
            # en tete de la queue
            if x.etat == Noeud.OPEN:
                l.remove(x)
            x.etat = Noeud.OPEN

        l.reverse()
        s.reverse()

        l.extend(s)
        l.reverse()

        return l