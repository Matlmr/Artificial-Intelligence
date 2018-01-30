from copy import copy

class Graphe:
    """ Graphe non-dirige avec poids sur les arcs """
    def __init__(self, noeuds=None, arcs=None):
        """
        :param list noeuds: Une liste de Noeuds
        :param list arcs: Une liste de paires de Noeuds (sous forme de tuples (a, b, poids))
        """
        if noeuds is not None:
            self.noeuds = list(noeuds)
        else:
            self.noeuds = []

        self.arcs = []

        if arcs is not None:
            self.ajoute_arcs(arcs)

    def ajoute_arcs(self, arcs):
        """
        :param list arcs: Une liste de paires de Noeuds (sous forme de tuples (a, b, poids))
        """
        for (u, v, w) in arcs:
            if not u in self.noeuds:
                self.noeuds.append(u)
            if not v in self.noeuds:
                self.noeuds.append(v)

            if not (u, v, w) in self.arcs:
                self.arcs.append((u, v, w))

    def voisins(self, vertice):
        """
        :return: Les voisins d'un vertice accompagnes du poids de l'arc qui les lie [(a, 2), (b, 1), etc.]
        """
        voisins = []

        for (u, v, w) in self.arcs:
            if u == vertice:
                voisins.append((v, w))
            if v == vertice:
                voisins.append((u, w))

        return voisins

    def __repr__(self):
        s = ''
        for n in self.noeuds:
            s += '{}\n'.format(n)
            s += 'Voisins:\n'
            for v in self.voisins(n):
                s += '\t{}\n'.format(v)
        return s

