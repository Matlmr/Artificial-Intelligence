from unittest import TestCase
from moteurs.sansvariables import MoteurChainageAvant, Regle, Fait


class TestMoteurChainageAvant(TestCase):

    def test_chainage(self):

        but = Fait('hors-taxe')

        faits = [Fait('vin'), Fait('<-2-litres'), Fait('<-100-Euro'), Fait('adulte')]
        regles = [Regle([Fait('vin'), Fait('<-2-litres')], Fait('petite-quantite')),
                 Regle([Fait('cognac'), Fait('<-1-litre')], Fait('petite-quantite')),
                 Regle([Fait('<-100-Euro')], Fait('petite-quantite')),
                 Regle([Fait('petite-quantite'), Fait('adulte')], but)]

        resultat = MoteurChainageAvant.chaine(faits, regles)

        self.assertTrue(but in resultat[0])

    def test_pas_de_faits(self):
        regles = [Regle([Fait('vin'), Fait('<-2-litres')], Fait('petite-quantite')),
                 Regle([Fait('cognac'), Fait('<-1-litre')], Fait('petite-quantite')),
                 Regle([Fait('<-100-Euro')], Fait('petite-quantite'))]

        resultat = MoteurChainageAvant.chaine([], regles)

        self.assertEqual(set(), resultat[0])
        self.assertEqual([], resultat[1])

    def test_faits_redondants(self):

        but = Fait('hors-taxe')

        faits = [Fait('vin'), Fait('vin'), Fait('<-2-litres'), Fait('<-100-Euro'), Fait('adulte')]
        regles = [Regle([Fait('vin'), Fait('<-2-litres')], Fait('petite-quantite')),
                 Regle([Fait('cognac'), Fait('<-1-litre')], Fait('petite-quantite')),
                 Regle([Fait('<-100-Euro')], Fait('petite-quantite')),
                 Regle([Fait('petite-quantite'), Fait('adulte')], but)]

        resultat = MoteurChainageAvant.chaine(faits, regles)

        self.assertTrue(but in resultat[0])
