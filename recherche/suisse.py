from noeud import Noeud
from graphe import Graphe

from dfs import DFSSolver
from bfs import BFSSolver
from astar import AStarSolver

# Les villes
villes = {
    'Lausanne': Noeud(110, 260, 'Lausanne'),
    'Geneve': Noeud(40, 300, 'Geneve'),
    'Sion': Noeud(200, 300, 'Sion'),
    'Neuchatel': Noeud(150, 170, 'Neuchatel'),
    'Bern': Noeud(210, 280, 'Bern'),
    'Basel': Noeud(230, 65, 'Basel'),
    'Fribourg': Noeud(175, 200, 'Fribourg'),
    'Zurich': Noeud(340, 90, 'Zurich'),
    'Aarau': Noeud(290, 95, 'Aarau'),
    'Luzern': Noeud(320, 155, 'Luzern'),
    'St-Gallen': Noeud(85, 455,  'St-Gallen'),
    'Thun': Noeud(235, 210, 'Thun'),
}

# Les routes.
routes = [
    (villes['Lausanne'], villes['Geneve'], villes['Lausanne'].distance(villes['Geneve'])),
    (villes['Sion'], villes['Lausanne'], villes['Sion'].distance(villes['Lausanne'])),
    (villes['Neuchatel'], villes['Lausanne'], villes['Neuchatel'].distance(villes['Lausanne'])),
    (villes['Fribourg'], villes['Lausanne'], villes['Fribourg'].distance(villes['Lausanne'])),
    (villes['Fribourg'], villes['Bern'], villes['Fribourg'].distance(villes['Bern'])),
    (villes['Sion'], villes['Thun'], villes['Sion'].distance(villes['Thun'])),
    (villes['Neuchatel'], villes['Bern'], villes['Neuchatel'].distance(villes['Bern'])),
    (villes['Basel'], villes['Bern'], villes['Basel'].distance(villes['Bern'])),
    (villes['Zurich'], villes['Aarau'], villes['Zurich'].distance(villes['Aarau'])),
    (villes['Zurich'], villes['Luzern'], villes['Zurich'].distance(villes['Luzern'])),
    (villes['Bern'], villes['Aarau'], villes['Bern'].distance(villes['Aarau'])),
    (villes['Bern'], villes['Luzern'], villes['Bern'].distance(villes['Luzern'])),
    (villes['Luzern'], villes['Aarau'], villes['Luzern'].distance(villes['Aarau'])),
    (villes['St-Gallen'], villes['Zurich'], villes['St-Gallen'].distance(villes['Zurich'])),
    (villes['Thun'], villes['Bern'], villes['Thun'].distance(villes['Bern'])),
    (villes['Basel'], villes['Zurich'], villes['Basel'].distance(villes['Zurich'])),
]

if __name__ == '__main__':
    graphe = Graphe(villes.values(), routes)

    print(graphe)

    print('Recherche DFS:')
    s = DFSSolver(graphe)
    iterations = s.solve(villes['Lausanne'], villes['Zurich'])

    print('Nombre d\'iterations: {}'.format(iterations))

    #################################################

    for (k, n) in villes.items():
        n.etat = Noeud.NOT_VISITED

    print('Recherche BFS:')
    s = BFSSolver(graphe)
    iterations = s.solve(villes['Lausanne'], villes['Zurich'])

    print('Nombre d\'iterations: {}'.format(iterations))

    ##################################################

    for (k, n) in villes.items():
        n.etat = Noeud.NOT_VISITED

    print('Recherche AStar:')
    a = AStarSolver(graphe)
    iterations = a.solve(villes['Lausanne'], villes['Zurich'])

    print('Nombre d\'iterations: {}'.format(iterations))

