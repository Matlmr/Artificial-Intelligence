from unittest import TestCase
from moteurs.variables import MoteurChainageAvantVariables, Regle, Fait, Filtre, Unifieur


class TestMoteurChainageAvant(TestCase):

    def setUp(self):
        self.faits = [
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

        self.regles = [
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


    def test_chainage(self):

        buts = [
            Fait(['reduc', '300', 'Paul']),
            Fait(['reduc', '250', 'Marc']),
            Fait(['reduc', '100', 'Jean'])
        ]

        resultat = MoteurChainageAvantVariables(method=Filtre).chaine(self.faits, self.regles)

        for but in buts:
            self.assertTrue(but in resultat[1])

    def test_instancie_conclusion(self):
        moteur = MoteurChainageAvantVariables(method=Filtre)

        conclusions = moteur.instancie_consequence(self.regles[0], [{'?x': 'Dupont'}, {'?x': 'Dupond'}])
        self.assertEqual(conclusions, [Fait(['reduc-enfant', '0', 'Dupont']), Fait(['reduc-enfant', '0', 'Dupond'])])
