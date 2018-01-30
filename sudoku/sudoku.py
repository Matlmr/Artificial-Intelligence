from psc import Variable, ContrainteBinaire, PSC

class Sudoku:
    """ Representation et resolution d'une grille de sudoku"""

    def __init__(self, grille, taille=9, sous_taille=3):
        """
            :param taille: taille de la grille de sudoku
            :param sous_taille: taille des sous-grilles du probleme
        """
        if taille % sous_taille != 0:
            raise ValueError('Taille et sous-taille de grille incompatibles.')
        self.taille = taille
        self.sous_taille = sous_taille

        # genere une variable par case
        self.variables = [ Variable('{}{}'.format(i, j), list(range(1, self.taille+1)))
            for i in range(0, self.taille) for j in range(0, self.taille) ]

        # initialise les cases dont les valeurs sont connues
        for i in range(0, self.taille):
            for j in range(0, self.taille):
                # si la case est instanciee avec une valeur valide
                # assigne la variable et restreint son domaine a la valeur initiale
                if isinstance(grille[i][j], int):
                    if not (0 < grille[i][j] <= self.taille):
                        raise ValueError('Valeur invalide dans la grille de depart.')
                    v = self.variables[i * self.taille + j]
                    v.val = grille[i][j]
                    v.domaine = [grille[i][j]]
                    v.label = [grille[i][j]]

        self.contraintes =  []
        self.genere_contraintes()

    def genere_contraintes(self):
        """Genere toutes les contraintes d'une grille de sudoku """

        def genere_contraintes_sous_grille(x, y):
            """Genere les contraintes de la sous grille dont le coin est situe en (x,y)"""
            # parcours de la sous-grille
            for i in range(x, x + self.sous_taille):
                for j in range(y, y + self.sous_taille):
                    # pour chaque case qui n'est ni dans la meme ligne i ni la meme colonne j
                    # on ajoute une contrainte (les autres cases sont couvertes par les contraintes
                    # de lignes et de colonnes)
                    for k in range(x, x + self.sous_taille):
                        for l in range(y, y + self.sous_taille):
                            if i != k and j !=l:
                                self.contraintes.append(ContrainteBinaire(self.variables[i * self.taille + j],
                                                                          self.variables[k * self.taille + l],
                                                                          lambda x,y: x != y))

        self.contraintes = []

        for i in range(0, self.taille):
            for j in range(0, self.taille):
                # contraintes sur les case d'une ligne
                for k in range(j+1, self.taille):
                    self.contraintes.append(ContrainteBinaire(self.variables[i * self.taille + j],
                                                              self.variables[i * self.taille + k],
                                                              lambda x,y: x != y))
                # contraintes sur les cases d'une colonne
                for k in range(j+1, self.taille):
                    self.contraintes.append(ContrainteBinaire(self.variables[j * self.taille + i],
                                                              self.variables[k * self.taille + i],
                                                              lambda x,y: x != y))

        # contrainte sur les cases d'une sous-grille
        # le troisieme argument de range permet de regler l'increment
        # ex: range(0, 5, 2) genere la sequence 0, 3
        #     range(10, 5, -1) genere la sequence 10, 9, 8, 7, 6
        # // est l'operateur de division entiere
        for i in range(0, self.taille, self.taille // self.sous_taille):
            for j in range(0, self.taille, self.taille // self.sous_taille):
                genere_contraintes_sous_grille(i, j)

    def resoudre(self, methode='forward_checking'):
        """ Lance l'algorithme de resolution choisi sur la grille.

            :param methode: methode de resolution, forward_checking ou backtracking.
        """

        p = PSC(list(self.variables), self.contraintes)
        p.consistance_noeuds()
        p.consistance_arcs()

        if methode == 'forward_checking':
            for v in p.variables:
                v.label = v.domaine[:]
            #p.variable_ordering()
            p.forward_checking(True)
            print(p.iterations)
        else:
            p.variable_ordering()
            p.backtrack(True)
            print(p.iterations)

        for i in range(0, self.taille):
            for j in range(0, self.taille):
                nom = '{}{}'.format(i, j)
                self.variables[i * self.taille + j].val = p.solutions[0][nom]

    def __repr__(self):
        """ Convertit les variables du probleme en grille a afficher."""
        def val(e):
            """ Methode locale pour la mise en forme des valeurs absentes."""
            if e is None:
                return '-'
            else:
                return e

        ret = ''
        for i in range(0, self.taille):
            for j in range(0, self.taille):
                ret += '{} '.format(val(self.variables[i * self.taille + j].val))
            ret += '\n'

        return ret
