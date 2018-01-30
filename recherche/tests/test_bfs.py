from unittest import TestCase

from noeud import Noeud
from graphe import Graphe
from bfs import BFSSolver


class TestBFS(TestCase):

    def setUp(self):
        self.n = {
            'a': Noeud(0, 0, 'a'),
            'b': Noeud(0, 1, 'b'),
            'c': Noeud(1, 0, 'c'),
            'd': Noeud(-1, 0, 'd'),
            'e': Noeud(0, -1, 'e'),
        }

        self.g1 = Graphe([self.n['a'], self.n['b'], self.n['c'], self.n['d'], self.n['e']],
                [(self.n['a'], self.n['b'], 1), (self.n['a'], self.n['c'], 1), (self.n['a'], self.n['d'], 1)])

    def test_ajoute_voisins(self):
        s = BFSSolver(self.g1)

        # ajout avec aucun noeud visites (b sera a double dans la liste)
        q = s.ajoute_voisins([self.n['b']], self.n['a'])

        # verifie que les elements deja presents dans la liste soient a la fin
        self.assertEqual(q[0], self.n['b'])
        # verifie que les bons elements soient ajoutes
        self.assertListEqual(sorted(q, key=lambda x: x.label),
                sorted([self.n['b'], self.n['b'], self.n['c'], self.n['d']], key=lambda x: x.label))


        # reset l'etat des noeuds
        for (k, v) in self.n.items():
            v.etat = Noeud.NOT_VISITED
        self.n['b'].etat = Noeud.OPEN

        q = s.ajoute_voisins([self.n['b']], self.n['a'])

        # verifie que les elements deja presents dans la liste soient a la fin
        self.assertEqual(q[0], self.n['b'])
        # verifie que les bons elements soient ajoutes (b pas a double)
        self.assertListEqual(sorted(q, key=lambda x: x.label),
                sorted([self.n['b'], self.n['c'], self.n['d']], key=lambda x: x.label))


    def test_bfs(self):
        self.assertLessEqual(BFSSolver(self.g1).solve(self.n['a'], self.n['b']), 4)
        self.assertLessEqual(BFSSolver(self.g1).solve(self.n['a'], self.n['c']), 4)
        self.assertLessEqual(BFSSolver(self.g1).solve(self.n['a'], self.n['d']), 4)
        self.assertEqual(BFSSolver(self.g1).solve(self.n['a'], self.n['e']), None)
