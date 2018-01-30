class MoteurChainageAvant:
    """ Un moteur d'inference a chainage avant sans variables
    """
    @staticmethod
    def chaine(faits, regles):
        """ Effectue une resolution par chainage avant sur une liste de faits

        :param list faits: objets Fait representant les premisses
        :param list regles: les regles d'inference a utiliser
        :return: (etat, trace): etat est l'ensemble des faits au moment ou la queue est vide. trace est l'ordre dans lequel les faits et regles ont ete inferes
        """

        queue = faits
        trace = []
        etat = []

        while queue:
            q = queue.pop(0)
            trace.append(q)
            if not (q in etat):
                etat.append(q)
                print(q)
                for r in regles:
                    if r.satisfaite_par(q) and r.satisfaite(etat):
                        queue.append(r.conclusion)
                        trace.append(r)

        return (etat,trace)