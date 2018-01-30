from psc.variable import Variable
from psc.contrainte import ContrainteUnaire, ContrainteBinaire

from psc.psc import PSC

if __name__ == '__main__':
    v = [
        Variable('a', [2, 3]),
        Variable('b', list(range(12))),
        Variable('c', list(range(3))),
        Variable('d', list(range(3))),
        Variable('e', list(range(12))),
    ]

    c = [
        ContrainteUnaire(v[1], lambda x: x < 4),
        ContrainteBinaire(v[0], v[1], lambda x,y: x != y),
        ContrainteBinaire(v[1], v[2], lambda x,y: x != y),
        ContrainteBinaire(v[1], v[3], lambda x,y: x != y),
        ContrainteBinaire(v[1], v[4], lambda x,y: x != y),
        ContrainteBinaire(v[2], v[3], lambda x,y: x != y),
        ContrainteBinaire(v[2], v[4], lambda x,y: x != y),
        ContrainteBinaire(v[3], v[4], lambda x,y: x != y),
        ContrainteBinaire(v[4], v[0], lambda x,y: x < y),
    ]

    p = PSC(v, c)
    p.consistance_noeuds()
    p.consistance_arcs()
    p.variable_ordering()
    p.backtrack()

    print('Backtrack avec variable ordering termine en {} iterations.'.format(p.iterations))
    for s in p.solutions:
        print('Solution')
        print( '========')
        for (k, val) in sorted(s.items()):
            print('\tVariable {}: {}'.format(k, val))

    p = PSC(v, c)
    p.consistance_noeuds()
    p.consistance_arcs()
    for v in p.variables:
        v.label = v.domaine[:]
    p.forward_checking()

    print('Forward checking termine en {} iterations.'.format(p.iterations))
    for s in p.solutions:
        print('Solution')
        print('========')
        for (k, v) in sorted(s.items()):
            print('\tVariable {}: {}'.format(k, v))
