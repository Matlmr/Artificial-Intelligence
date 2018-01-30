from noeud import Noeud

class Solver:
    """ Recherche de chemin generique """

    def __init__(self, graphe):
        self.graphe = graphe

    def solve(self, a, b):
        """ Cherche le chemin le plus efficace de a jusqu'a b.

            :param a: le Noeud de depart
            :param b: le Noeud d'arrivee
            :return: le nombres d'iterations pour parvenir a b ou None si pas de chemin
        """
        for n in self.graphe.noeuds:
            n.etat = Noeud.NOT_VISITED

        a.etat = Noeud.OPEN
        queue = [a]
        iterations = 0

        while len(queue) > 0:
            iterations += 1

            n = queue.pop(0)
            n.etat = Noeud.CLOSED
            print('Closed: {}'.format(n))
            if n == b:
                return iterations
            else:
                queue = self.ajoute_voisins(queue, n)

    
    def ajoute_voisins(self, q, n):
        """ Ajoute les voisins de n a la queue (a implementer differement pour DFS, BFS et A*)

            :param q: la queue des noeuds a explorer
            :param n: le Noeud courant
            :return: la queue mise a jour avec les voisins du noeud courant
        """
        #l = q[:]

        #s = self.graphe.voisins(n)
        #s = [x[0] for x in s]
        #for x in s:
        #    x.etat = Noeud.OPEN

        #l.extend(s)

        #return l
