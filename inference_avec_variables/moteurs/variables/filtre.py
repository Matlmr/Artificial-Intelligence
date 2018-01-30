__author__ = 'Clement Humbert'
__date__ = '19.02.2015'

from .exceptions import MatchingException


class Filtre:
    """Classe statique implementant les methodes de filtrage de propositions avec variables
    """
    @staticmethod
    def est_atomique(el):
        """
        Vérifie si l'argument est un atome
        :return: True si l'argument est une string
        """
        return isinstance(el, str)

    @staticmethod
    def est_variable(el, marqueur='?'):
        """
        Vérifie si l'argument est une variable (dans le cours: vrai s'il commence par '?')
        :param marqueur: marqueur de variable. Valeur par défaut '?'
        :return: True si el[0] == marqueur
        """
        return el[0] == marqueur

    @staticmethod
    def substitue(pattern, matches):
        """
        Effectue des substitutions de variables par leur valeur dans un pattern
        :param pattern: un pattern dans lequel remplacer les variables
        :param dict matches: un dictionnaire de substitutions
        :return: un pattern sans variables
        """
        for p in pattern:
            if Filtre.est_atomique(p):
                for key in matches.keys():
                    if Filtre.est_variable(p) and p == key:
                        p = matches.get(key)
            else:
                Filtre.substitue(p,matches)

        return pattern


    @staticmethod
    def filtre(datum, pattern):
        """
        Algorithme 3.3 du livre de reference

 #       >>> Filtre.filtre(['Superman', 'a', 'une', '?x', '?y'], ['Superman', 'a', 'une', 'cape', 'rouge']) == {'?x': 'cape', '?y': 'rouge'}
        True

        :param list datum: Une collection d'atomes sans variables
        :param list pattern: Une collection d'atomes pouvant contenir des variables
        :return: Un dictionnaire variable -> atome
        """
        if pattern == [] and datum == []:
            return {}

        elif pattern == [] or datum == []:
            raise MatchingException()

        elif Filtre.est_atomique(pattern):
            if pattern == datum:
                return {}
            elif Filtre.est_variable(pattern):
                return {pattern:datum}
            else:
                raise MatchingException()

        elif Filtre.est_atomique(datum):
            raise MatchingException()

        else:
            datum_tete = datum.pop(0)
            pattern_tete = pattern.pop(0)
            tete_substitution = Filtre.filtre(datum_tete, pattern_tete)

            pattern = Filtre.substitue(pattern_tete,tete_substitution)
            reste_substitutions = Filtre.filtre(datum,pattern)

            reste_substitutions.update(tete_substitutions)
            return reste_substitutions



    @staticmethod
    def pattern_match(datum, pattern, env=None):
        """
        Effectue un filtrage en tenant compte d'un environnement initial
        :param list datum: Une collection d'atomes sans variables
        :param list pattern: Une collection d'atomes pouvant contenir des variables
        :return: Un dictionnaire variable -> atome
        """
        if env is None:
            env = {}

        pattern = Filtre.substitue(pattern,env)

        env.update(Filtre.filtre(datum.copy(), pattern.copy()))
        return env