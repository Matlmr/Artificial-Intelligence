from noeud import Noeud
from graphe import Graphe

from dfs import DFSSolver
from bfs import BFSSolver
from astar import AStarSolver

# les noeuds du graphe
noeuds = {
    'A': Noeud(0, 16, 'A'),
    'B': Noeud(5, 13, 'B'),
    'C': Noeud(0, 10, 'C'),
    'D': Noeud(5, 8, 'D'),
    'E': Noeud(11, 18, 'E'),
    'F': Noeud(15, 13, 'F'),
    'G': Noeud(29, 18, 'G'),
    'H': Noeud(26, 0, 'H'),
    'I': Noeud(12, 10, 'I'),
    'J': Noeud(17, 7, 'J'),
    'K': Noeud(11, 3, 'K'),
    'L': Noeud(22, 16, 'L'),
    'M': Noeud(25, 12, 'M'),
    'N': Noeud(24, 6, 'N'),
    'O': Noeud(20, 0, 'O'),
    'P': Noeud(5, 0, 'P'),
}

# les arcs
arcs = [
    (noeuds['A'], noeuds['B'], noeuds['A'].distance(noeuds['B'])),
    (noeuds['A'], noeuds['E'], noeuds['A'].distance(noeuds['E'])),
    (noeuds['B'], noeuds['C'], noeuds['B'].distance(noeuds['C'])),
    (noeuds['B'], noeuds['E'], noeuds['B'].distance(noeuds['E'])),
    (noeuds['B'], noeuds['D'], noeuds['B'].distance(noeuds['D'])),
    (noeuds['C'], noeuds['D'], noeuds['C'].distance(noeuds['D'])),
    (noeuds['C'], noeuds['P'], noeuds['C'].distance(noeuds['P'])),
    (noeuds['D'], noeuds['I'], noeuds['D'].distance(noeuds['I'])),
    (noeuds['D'], noeuds['K'], noeuds['D'].distance(noeuds['K'])),
    (noeuds['E'], noeuds['F'], noeuds['E'].distance(noeuds['F'])),
    (noeuds['E'], noeuds['L'], noeuds['E'].distance(noeuds['L'])),
    (noeuds['F'], noeuds['I'], noeuds['F'].distance(noeuds['I'])),
    (noeuds['F'], noeuds['L'], noeuds['F'].distance(noeuds['L'])),
    (noeuds['F'], noeuds['M'], noeuds['F'].distance(noeuds['M'])),
    (noeuds['G'], noeuds['H'], noeuds['G'].distance(noeuds['H'])),
    (noeuds['G'], noeuds['L'], noeuds['G'].distance(noeuds['L'])),
    (noeuds['G'], noeuds['M'], noeuds['G'].distance(noeuds['M'])),
    (noeuds['I'], noeuds['J'], noeuds['I'].distance(noeuds['J'])),
    (noeuds['J'], noeuds['K'], noeuds['J'].distance(noeuds['K'])),
    (noeuds['J'], noeuds['N'], noeuds['J'].distance(noeuds['N'])),
    (noeuds['K'], noeuds['O'], noeuds['K'].distance(noeuds['O'])),
    (noeuds['K'], noeuds['P'], noeuds['K'].distance(noeuds['P'])),
    (noeuds['M'], noeuds['N'], noeuds['M'].distance(noeuds['N'])),
    (noeuds['N'], noeuds['O'], noeuds['N'].distance(noeuds['O'])),
    (noeuds['B'], noeuds['I'], noeuds['B'].distance(noeuds['I'])),
    (noeuds['B'], noeuds['F'], noeuds['B'].distance(noeuds['F'])),
    (noeuds['P'], noeuds['O'], noeuds['P'].distance(noeuds['O']))
]

if __name__ == '__main__':

    graphe = Graphe(noeuds.values(), arcs)
    print(graphe)

    print('Recherche DFS:')
    s = DFSSolver(graphe)
    iterations = s.solve(noeuds['A'], noeuds['P'])

    # notez que DFS trouve UN chemin et non pas LE MEILLEUR chemin entre deux noeuds
    print('Nombre d\'iterations: {}'.format(iterations))

    #################################################

    for (k, n) in noeuds.items():
        n.etat = Noeud.NOT_VISITED

    print('Recherche BFS:')
    s = BFSSolver(graphe)
    iterations = s.solve(noeuds['A'], noeuds['P'])

    # notez que BFS trouve UN chemin et non pas LE MEILLEUR chemin entre deux noeuds
    print('Nombre d\'iterations: {}'.format(iterations))

    ##################################################

    for (k, n) in noeuds.items():
        n.etat = Noeud.NOT_VISITED

    print('Recherche AStar:')
    a = AStarSolver(graphe)
    iterations = a.solve(noeuds['A'], noeuds['P'])

    print('Nombre d\'iterations: {}'.format(iterations))

