from unittest import TestCase

from noeud import Noeud
from graphe import Graphe
from astar import AStarSolver


class TestAStar(TestCase):

    def setUp(self):
        self.n = {
            'a': Noeud(0, 0, 'a'),
            'b': Noeud(0, 2, 'b'),
            'c': Noeud(2, 2, 'c'),
            'd': Noeud(3, 4, 'd'),
            'e': Noeud(4, 2, 'e'),
            'f': Noeud(4, 4, 'f'),
        }

        self.g1 = Graphe([self.n['a'], self.n['b'], self.n['c'], self.n['d'], self.n['e'], self.n['f']],
                [(self.n['a'], self.n['b'], self.n['a'].distance(self.n['b'])),
                 (self.n['a'], self.n['c'], self.n['a'].distance(self.n['c'])),
                 (self.n['b'], self.n['d'], self.n['b'].distance(self.n['d'])),
                 (self.n['d'], self.n['f'], self.n['d'].distance(self.n['f'])),
                 (self.n['c'], self.n['d'], self.n['c'].distance(self.n['d'])),
                 (self.n['c'], self.n['e'], self.n['c'].distance(self.n['e'])),
                 (self.n['e'], self.n['f'], self.n['e'].distance(self.n['f']))])

    def test_ajoute_voisins(self):
        s = AStarSolver(self.g1)
        s.h = lambda x: x.distance(self.n['f'])

        self.n['a'].cout = 0
        self.n['a'].cout_f = self.n['a'].distance(self.n['f'])
        
        q = s.ajoute_voisins([], self.n['a'])
        self.n['a'].etat = Noeud.CLOSED
        q = s.ajoute_voisins(q[1:], q.pop(0))
        self.n['c'].etat = Noeud.CLOSED
        q = s.ajoute_voisins(q[1:], q.pop(0))
        
        self.assertAlmostEqual(self.n['d'].cout_f, 6.064495, places=4)
        # verifie que la liste soit correctement triee
        self.assertEqual(q, sorted(q, key=lambda x: x.cout_f))

    def test_astar(self):
        s = AStarSolver(self.g1)
        i = s.solve(self.n['a'], self.n['f'])
        self.assertEqual(i, 4)
