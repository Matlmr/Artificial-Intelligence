from .variable import Variable
from .contrainte import ContrainteUnaire, ContrainteBinaire

from .exceptions import NonSatisfiable


class PSC:
    def __init__(self, variables, contraintes):
        """
            :param list variables: les variables du probleme
            :param list contraintes: les contraintes du probleme
        """
        self.variables = list(variables)
        self.contraintes = contraintes

        self.iterations = 0
        self.solutions = []

    def consistance_noeuds(self):
        """ Applique la consistance des noeuds sur les contraintes unaires du probleme

            L'algorithme consiste a enlever des domaines de definitions toutes les valeurs
            qui violent les contraintes unaires.

            .. seealso:: Chapitre 8.5.1
        """

        for c in self.contraintes:
            if c.dimension() == 1:
                # /!\ iterer sur domaine[:], sinon on ne peut pas supprimer d'elements
                for v in c.variables[0].domaine[:]:
                    if not c.est_valide(v):
                        c.variables[0].domaine.remove(v)
                        c.variables[0].label.remove(v)

    def consistance_arcs(self):
        """ Applique la consistance des arcs sur les contraintes binaires du probleme

        L'algorithme utiliser la methode REVISER vue en cours. Il supprime les valeurs interdisant
        la satisfaction d'une contrainte.
        """

        refaire = False
        for c in self.contraintes:
            if c.dimension() == 2 and c.reviser():
                refaire = True

        if refaire:
            self.consistance_arcs()

    def consistance_avec_vars_precedentes(self, k):
        """ Verifie si toutes les contraintes concernant les variables deja
            instanciees sont satisfaites.

            :param k: la profondeur actuelle de la recherche
            :return: True si la valeur de la derniere variable instanciee satisfait toutes les conditions concernant les variables deja instanciees
        """

        for c in self.contraintes:
            # si la variables courante est concernee
            if self.variables[k] in c.variables:
                for i in range(0, k):
                    # si n'importe laquelle des variables precedentes est concernee
                    if self.variables[i] in c.variables:
                        if c.est_valide(self.variables[k], self.variables[k].val):
                            break
                        else:
                            return False
        # toutes les contraintes sont valides
        return True

    def variable_ordering(self):
        """ Trie les variables par ordre croissant de taille de domaine."""
        self.variables.sort(key=lambda x: len(x.domaine))

    def backtrack(self, k=0, une_seule_solution=False):
        """ Algorithme de backtracking simple
            
            Tente d'assigner une valeur a chaque variable. A chaque assignation,\
            verifie que toutes les contraintes des variables instanciees sont satisfaites.\
            Si non, retourne en arriere pour essayer une autre valeur\
            
            :param k: la profondeur de la recherche
            :param une_seule_solution: indique a l'algorithme s'il faut s'arreter apres avoir trouve la premiere solution
            """
        
        if len(self.solutions) == 1 and une_seule_solution:
            return
        
        self.iterations += 1
        # on est parvenu a une solution
        if k >= len(self.variables):
            sol = {}
            for v in self.variables:
                sol[v.nom] = v.val
            if len(self.solutions) == 0 or not une_seule_solution:
                self.solutions.append(sol)
        else:
            var = self.variables[k]
            for val in var.domaine:
                var.val = val
                if self.consistance_avec_vars_precedentes(k):
                    try:
                        # continue l'algorithme sur la variable k+1
                        self.backtrack(k+1, une_seule_solution)
                    except NonSatisfiable as e:
                        # on essaie d'autres valeurs pour la variable courante
                        continue
            if len(self.solutions) == 0:
                # la variable k ne possede pas de valeurs qui menent a une solution
                raise NonSatisfiable('Contraintes non satisfiables')

    def dynamic_variable_ordering(self, k):
        """ Place en k eme position la variable non instanciee ayant le label le plus restreint.

            :param k: profondeur actuelle de la recherche
        """

        index = k
        taille_plus_petit_label = len(self.variables[index].label)

        for i in range(k+1, len(self.variables)):
            if len(self.variables[i].label) < taille_plus_petit_label:
                index = i
                taille_plus_petit_label = len(self.variables[i].label)

        if k != index:
            self.variables[k], self.variables[index] = self.variables[index], self.variables[k]

    def propagation_consistante(self, k):
        """ Propage la valeur de la variable actuelle aux variables suivantes.

            Pour chaque contrainte sur la variable courante et sur une ou plus des variables non
            instanciee, appelle la methode propage() de la contrainte pour reduire le label de la
            deuxieme variable.

            :param k: profondeur actuelle de la recherche
            :return: True si la valeur de la derniere variable instanciee n'empeche pas l'instanciation des variables suivantes
        """

        # pour chaque contrainte portant sur la variable courante
        for c in self.contraintes:
            if self.variables[k] in c.variables:
                # si la contrainte porte sur une des variables suivantes
                for i in range(k+1, len(self.variables)):
                    if self.variables[i] in c.variables:
                        # propage la nouvelle assignation
                        if c.propage(self.variables[k]):
                            break
                        else:
                            # la contrainte ne peut pas etre satisfaite
                            return False
        return True

    def forward_checking(self, une_seule_solution=False, k=0):
        """ Algorithme de Forward Checking

            Le forward checking essaie de limiter les retours en arriere
            en limitant les domaines des variables non instanciees (consistance des arcs
            a chaque iteration).

            :param une_seule_solution: retourne apres avoir atteint la premiere solution
            :param k: la profondeur actuelle de la recherhe
        """

        if len(self.solutions) == 1 and une_seule_solution:
            return
        
        self.iterations += 1
        if k >= len(self.variables):
            sol = {}
            for v in self.variables:
                sol[v.nom] = v.val
            self.solutions.append(sol)
        else:
            self.dynamic_variable_ordering(k)
            var = self.variables[k]

            # garde une copie des labels de depart
            sauvegarde_labels = { v: v.label[:] for v in self.variables }
            
            for val in sauvegarde_labels[var]:
                var.val = val
                var.label = [val]
                if self.propagation_consistante(k):
                    try:
                        # continue l'algorithme sur la variable k+1
                        self.forward_checking(une_seule_solution, k+1)
                    except NonSatisfiable as e:
                        # on essaie d'autres valeurs pour la variable courante
                        pass
                    for v in self.variables:
                        v.label = sauvegarde_labels[v]
            if len(self.solutions) == 0:
                # la variable k ne possede pas de valeurs qui menent a une solution
                raise NonSatisfiable('Contraintes non satisfiables')

    def print_etat(self):
        """ Methode pour afficher l'etat courant de l'algorithme, a utiliser pour debugger."""

        print('Etat de la recherche:')
        print('=====================')
        print('Iteration #{}'.format(self.iterations))

        for v in self.variables:
            print('Variable {}: '.format(v.nom), end='')
            print(v.val, end='')
            print(' domaine: ', end='')
            print(v.domaine, end='')
            print(' label: ', end='')
            print(v.label)

        if len(self.solutions) != 0:
            print('Solutions trouvees:')
            for s in self.solutions:
                print(s)

