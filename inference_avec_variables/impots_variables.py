from moteurs.variables import MoteurChainageAvantVariables
from moteurs.variables import Fait, Regle, Filtre, Unifieur

if __name__ == '__main__':
    faits = [
        Fait(['add','0','0','0','0']),
        Fait(['add','100','100','0','0']),
        Fait(['add','100','0','100','0']),
        Fait(['add','200','100','100','0']),
        Fait(['add','200','0','200','0']),
        Fait(['add','300','100','200','0']),
        Fait(['add','50','0','0','50']),
        Fait(['add','150','100','0','50']),
        Fait(['add','150','0','100','50']),
        Fait(['add','250','100','100','50']),
        Fait(['add','250','0','200','50']),
        Fait(['add','350','100','200','50']),
        Fait(['add','100','0','0','100']),
        Fait(['add','200','100','0','100']),
        Fait(['add','200','0','100','100']),
        Fait(['add','300','100','100','100']),
        Fait(['add','300','0','200','100']),
        Fait(['add','400','100','200','100']),
        ##Paul
        Fait(['bas-salaire', 'Paul']),
        Fait(['loyer', 'Paul']),
        Fait(['enfants', 'Paul']),
        Fait(['long-trajet', 'Paul']),
        ##Marc
        Fait(['moyen-salaire', 'Marc']),
        Fait(['loyer', 'Marc']),
        Fait(['enfants', 'Marc']),
        Fait(['long-trajet', 'Marc']),
        ##Jean
        Fait(['haut-salaire', 'Jean']),
        Fait(['pas-de-loyer', 'Jean']),
        Fait(['pas-d-enfants', 'Jean']),
        Fait(['long-trajet', 'Jean']),
    ]

    regles = [
        ##Reduction enfants
        Regle([Fait(['pas-d-enfants', '?x'])],Fait(['reduc-enfant', '0','?x'])),
        Regle([Fait(['enfants', '?x'])],Fait(['reduc-enfant', '100','?x'])),

        ##Reduction loyer
        Regle([Fait(['bas-salaire', '?x']), Fait(['loyer', '?x'])],Fait(['reduc-loyer', '200', '?x'])),
        Regle([Fait(['moyen-salaire', '?x']),Fait(['loyer', '?x'])],Fait(['reduc-loyer', '100', '?x'])),
        Regle([Fait(['haut-salaire', '?x']),Fait(['loyer', '?x'])],Fait(['reduc-loyer', '0', '?x'])),
        Regle([Fait(['pas-de-loyer', '?x'])],Fait(['reduc-loyer', '0','?x'])),

        ##Reduction transport
        Regle([Fait(['petit-trajet', '?x'])],Fait(['reduc-trajet', '0', '?x'])),
        Regle([Fait(['reduc-enfant', '0','?x']),Fait(['long-trajet', '?x'])],Fait(['reduc-trajet', '100', '?x'])),
        Regle([Fait(['reduc-loyer', '0','?x']),Fait(['long-trajet', '?x'])],Fait(['reduc-trajet', '100', '?x'])),
        Regle([Fait(['reduc-enfant', '100','?x']),Fait(['reduc-loyer', '100', '?x']),Fait(['long-trajet', '?x'])],Fait(['reduc-trajet', '50', '?x'])),
        Regle([Fait(['reduc-enfant', '100','?x']),Fait(['reduc-loyer', '200', '?x']),Fait(['long-trajet', '?x'])],Fait(['reduc-trajet', '0', '?x'])),

        ##Reduction totale
        Regle([Fait(['reduc-enfant', '?a','?x']),Fait(['reduc-loyer', '?b', '?x']),Fait(['reduc-trajet','?c', '?x']),Fait(['add','?res','?a','?b','?c'])],Fait(['reduc', '?res', '?x'])),
    ]

    m = MoteurChainageAvantVariables(Filtre)#Unifieur)
    (trace, etat) = m.chaine(faits, regles)

    for el in trace:
        if el not in faits:
            print(el)

    ##Nouveau faits deduits (fin de la trace)
    ##['reduc-loyer', '200', 'Paul']
    ##['reduc-enfant', '100', 'Paul']
    ##['reduc-loyer', '100', 'Marc']
    ##['reduc-enfant', '100', 'Marc']
    ##['reduc-loyer', '0', 'Jean']
    ##['reduc-enfant', '0', 'Jean']
    ##['reduc-trajet', '0', 'Paul']
    ##['reduc-trajet', '50', 'Marc']
    ##['reduc-trajet', '100', 'Jean']
    ##['reduc', '300', 'Paul']
    ##['reduc', '250', 'Marc']
    ##['reduc', '100', 'Jean']
