from .fait import Fait
from .regle import Regle
from .unifieur import Filtre

from .exceptions import MatchingException

class MoteurChainageAvantVariables:
    """ Un moteur d'inference a chainage avant avec variables
    """

    def __init__(self, method=Filtre):
        """
        :param method: Unifieur ou Filtre, selectionne le type de filtrage a appliquer
        """
        self.method = method

    def instancie_consequence(self, regle, envs):
        """ Instancie la conséquence d'une règle pour tous les environnements

        :param regle: la regle dont la consequence doit etre instanciee
        :param envs: les environnements servant a instancier la consequence
        :return: une liste de Faits correspondants aux differentes instances de la consequence
        """

        faits = []
        for e in self.environnements:
            faits.append(Filtre.substitue(regle.consequence.fait, e))
        return faits

    
    def chaine(self, faits, regles):
        """ Effectue une resolution par chainage avant sur une liste de faits

        :param list faits: objets Fait representant les premisses
        :param list regles: les regles d'inference a utiliser
        :return etat: l'ensemble des faits au moment ou la queue est vide.
        """

        queue = faits
        etat = []
        trace = []

        while queue:
            q = queue.pop(0)

            if q not in etat:
                etat.append(q)
                trace.append(q)

                # verifie si des regles sont declenchees par le nouveau fait
                for r in regles:
                    envs = r.satisfaite_par(q, self.method)
                    if not envs:
                        continue

                    for e in envs[:]:
                        envs_satisfaisants = r.satisfaite(etat, e, self.method)
                        if not envs_satisfaisants:
                            # l'environnement courant ne peut pas satifsaire la regle, on passe au suivant
                            continue
                        # remplace l'environnement par celui qui satisfait la regle et pas juste la premiere condition
                        # ajoute la consequence de la regle instanciee pour tous les environnements possibles
                        queue.extend(self.instancie_consequence(r, envs_satisfaisants))

            return(trace, etat)

