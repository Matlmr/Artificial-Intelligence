__author__ = 'Clement Humbert'
__date__ = '19.02.2015'

from .exceptions import MatchingException
from .filtre import Filtre

class Unifieur(Filtre):
    """Classe statique pour l'unification de propositions avec variables"""

    @staticmethod
    def substitue(pattern, matches):
        print("a completer")
    
    @staticmethod
    def unifie(prop1, prop2):
        # utiliser == pour comparer des collections dans le doctest évite d'avoir a les trier
        """
        Filtrage dans lequel les deux propositions peuvent contenir des variables

        >>> Unifieur.unifie(['Superman', 'a', 'une', 'cape', '?z'], ['?x', 'a', 'une', '?y', 'rouge']) == {'?x': 'Superman', '?y': 'cape', '?z': 'rouge'}
        True

        :param list prop1: Une collection d'atomes pouvant contenir des variables
        :param list prop2: Une collection d'atomes pouvant contenir des variables
        :return: Un dictionnaire variable -> atome
        """
        print("a completer")

    @staticmethod
    def pattern_match(prop1, prop2, env=None):
        """
        Effectue une unification en tenant compte d'un environnement initial
        :param list prop1: Une collection d'atomes pouvant contenir des variables
        :param list prop2: Une collection d'atomes pouvant contenir des variables
        :param dict env: Un dictionnaire contenant un environnement initial
        :return: Un dictionnaire variable : atome
        """
        print("a completer")

