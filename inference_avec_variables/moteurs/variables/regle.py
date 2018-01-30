from .filtre import Filtre
from .unifieur import Unifieur
from .exceptions import MatchingException

class Regle:
    """Representation d'une regle d'inference"""

    def __init__(self, conditions, conclusion):
        """
        :param list conditions: les faits necessaires a declencher la regle
        :param Fait conclusion: le fait resultant du declenchement de la regle
        """
        self.conditions = frozenset(conditions)
        self.conclusion = conclusion

    def satisfaite_par(self, fait, method=Filtre):
        """
        :param fait: le fait qui doit faire partie des conditions
        :param method: Unifieur ou Filtre, selectionne le type de filtrage a appliquer
        :return: True si "fait" fait partie des conditions de declenchement
        """
        satisfaite = False
        envs_satisfaisants = []

        for c in self.conditions:
            try:
                e = method.pattern_match(fait.fait, c.fait, {})
                envs_satisfaisants.append(e)
                # si au moins une des conditions retourne un environnement le fait satisfait une des conditions
                satisfaite = True
            except MatchingException:
                continue

        if satisfaite:
            return envs_satisfaisants
        else:
            return False
    
    def satisfaite(self, faits, env, method=Filtre):
        """
        :param list faits: la liste des faits de la base
        :param env: l'environnement déjà établi par satisfaite_par
        :param method: Unifieur ou Filtre, selectionne le type de filtrage a appliquer
        :return: True si les faits en parametres suffisent a dechlencher la regle
        """
        satisfaite = True
        envs_satisfaisants = [env]

        for c in self.conditions:
            c_satisfaite = False
            nouveaux_envs = []

            for f in faits:
                for e in envs_satisfaisants:
                    ecopie  = {}
                    if e is not None:
                        ecopie = e.copy()

                    try:
                        ecopie.update(method.pattern_match(f.fait,c.fait,ecopie))
                        nouveaux_envs.append(ecopie)
                        c_satisfaite = True
                    except MatchingException:
                        pass

            if not c_satisfaite:
                satisfaite = False
                break

            envs_satisfaisants = nouveaux_envs
        if satisfaite:
            return envs_satisfaisants
        else:
            return False

    
    def __repr__(self):
        """Representation d'une regle sous forme de string"""
        return '[' + ', '.join(map(str, self.conditions)) + '] => ' + str(self.conclusion)
