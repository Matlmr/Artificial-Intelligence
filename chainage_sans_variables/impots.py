from sys import argv

from moteurs.sansvariables import MoteurChainageAvant, Fait, Regle


if __name__ == '__main__' :
    if len(argv) == 1 or argv[1] == '1':
        faits = [Fait('bas-salaire'), Fait('loyer'), Fait('enfants'), Fait('long-trajet')]
    else:
        faits = [Fait('pas-d-enfants'), Fait('pas-de-loyer'), Fait('haut-salaire'), Fait('long-trajet')]

    regles = [Regle([Fait('pas-d-enfants')], Fait('reduc-enfant-0')),
              Regle([Fait('enfants')], Fait('reduc-enfant-100')),
              Regle([Fait('bas-salaire')], Fait('reduc-loyer-200')),
              Regle([Fait('moyen-salaire')], Fait('reduc-loyer-100')),
              Regle([Fait('haut-salaire')], Fait('reduc-loyer-0')),
              Regle([Fait('pas-de-loyer')], Fait('reduc-loyer-0')),
              Regle([Fait('petit-trajet')], Fait('reduc-trajet-0')),
              Regle([Fait('reduc-enfant-0'), Fait('long-trajet')], Fait('reduc-trajet-100')),
              Regle([Fait('reduc-loyer-0'), Fait('long-trajet')], Fait('reduc-trajet-100')),
              Regle([Fait('reduc-enfant-100'), Fait('reduc-loyer-100'), Fait('long-trajet')], Fait('reduc-trajet-50')),
              Regle([Fait('reduc-enfant-100'), Fait('reduc-loyer-200'), Fait('long-trajet')], Fait('reduc-trajet-0')),
              Regle([Fait('reduc-enfant-0'), Fait('reduc-loyer-0'), Fait('reduc-trajet-0')], Fait('reduc-0')),
              Regle([Fait('reduc-enfant-100'), Fait('reduc-loyer-0'), Fait('reduc-trajet-0')], Fait('reduc-100')),
              Regle([Fait('reduc-enfant-0'), Fait('reduc-loyer-100'), Fait('reduc-trajet-0')], Fait('reduc-100')),
              Regle([Fait('reduc-enfant-100'), Fait('reduc-loyer-100'), Fait('reduc-trajet-0')], Fait('reduc-200')),
              Regle([Fait('reduc-enfant-0'), Fait('reduc-loyer-200'), Fait('reduc-trajet-0')], Fait('reduc-200')),
              Regle([Fait('reduc-enfant-100'), Fait('reduc-loyer-200'), Fait('reduc-trajet-0')], Fait('reduc-300')),
              Regle([Fait('reduc-enfant-0'), Fait('reduc-loyer-0'), Fait('reduc-trajet-50')], Fait('reduc-50')),
              Regle([Fait('reduc-enfant-100'), Fait('reduc-loyer-0'), Fait('reduc-trajet-50')], Fait('reduc-150')),
              Regle([Fait('reduc-enfant-0'), Fait('reduc-loyer-100'), Fait('reduc-trajet-50')], Fait('reduc-150')),
              Regle([Fait('reduc-enfant-100'), Fait('reduc-loyer-100'), Fait('reduc-trajet-50')], Fait('reduc-250')),
              Regle([Fait('reduc-enfant-0'), Fait('reduc-loyer-200'), Fait('reduc-trajet-50')], Fait('reduc-250')),
              Regle([Fait('reduc-enfant-0'), Fait('reduc-loyer-200'), Fait('reduc-trajet-50')], Fait('reduc-250')),
              Regle([Fait('reduc-enfant-100'), Fait('reduc-loyer-200'), Fait('reduc-trajet-50')], Fait('reduc-350')),
              Regle([Fait('reduc-enfant-0'), Fait('reduc-loyer-0'), Fait('reduc-trajet-100')], Fait('reduc-100')),
              Regle([Fait('reduc-enfant-100'), Fait('reduc-loyer-0'), Fait('reduc-trajet-100')], Fait('reduc-200')),
              Regle([Fait('reduc-enfant-0'), Fait('reduc-loyer-100'), Fait('reduc-trajet-100')], Fait('reduc-200')),
              Regle([Fait('reduc-enfant-100'), Fait('reduc-loyer-100'), Fait('reduc-trajet-100')], Fait('reduc-300')),
              Regle([Fait('reduc-enfant-0'), Fait('reduc-loyer-200'), Fait('reduc-trajet-100')], Fait('reduc-300')),
              Regle([Fait('reduc-enfant-100'), Fait('reduc-loyer-200'), Fait('reduc-trajet-100')], Fait('reduc-400')),
              ]

    (etat, trace) = MoteurChainageAvant.chaine(faits, regles)

    for t in trace:
        print(t)
