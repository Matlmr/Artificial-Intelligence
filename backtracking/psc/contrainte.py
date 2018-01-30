

class Contrainte:
    """Modelisation d'une contrainte (abstraite)"""
    
    def __init__(self, variables):
        """
            :param list variables: les variables concernees par la contrainte
        """
        self.variables = tuple(variables)
    
    def dimension(self):
        """
            :return: le nombre de variables concernees par la contrainte
        """
        return len(self.variables)
    
    def est_valide(self):
        """ Teste si la contrainte est repectee par les valeurs actuelles
            
            :return: ``True`` si la contrainte e valide
        """
        return False
    
    def __repr__(self):
        return 'Contrainte: {}'.format(self.variables)
    
    def __eq__(self, that):
        return self.variables == that.variables
    
    def __hash__(self):
        return sum([v.__hash__ for v in self.variables])


class ContrainteUnaire(Contrainte):
    """ Contrainte imposant une restriction sur la valeur d'une variable
        
        Exemples: x > 0, y = 5, etc
    """
    
    def __init__(self, var, op):
        """
            
            Exemples d'op: ``lambda x: x > 5``, ``lambda x: x > 5 and x < 10``
            
            :param var: variable concernee par la contrainte
            :param op: fonction ou lambda expression permettant de verifier la contrainte
        """
        Contrainte.__init__(self, (var,))
        self.op = op
    
    def est_valide(self, val):
        """ Teste si la contrainte est valide quand la variable ``var`` prend la valeur ``val``
            
            :note: La contrainte unaire est respectee si l'operateur applique au operand\
            ``val``  retourne ``True``
            
            :return: ``True`` si la contrainte e valide
        """
        return self.op(val)


class ContrainteBinaire(Contrainte):
    """ Contrainte imposant une restriction sur deux variables
        
        Exemple: x > y
    """
    
    def __init__(self, x1, x2, op):
        """
            
            Exemples d'op: ``lambda x,y: x != y``, ``lambda x,y: x < y``
            
            :param x1: premiere variable concernee par la contrainte
            :param x2: deuxieme variable concernee par la contrainte
            :param op: fonction ou lambda expression permettant de verifier la contrainte
        """
        Contrainte.__init__(self, (x1, x2))
        self.op = op
    
    def est_valide(self, var, val):
        """ Teste si la contrainte est valide quand la variable ``var`` (une de ``x1`` ou ``x2``)\
            prend la valeur ``val``
            
            :note: La contrainte unaire est respectee si l'operateur applique aux operands\
            ``val, x2.val`` (si ``var`` est ``x1``) ou ``x1.val, val`` (si ``var`` est ``x2``)\
            retourne ``True``
            
            :return: ``True`` si la contrainte e valide
        """
        x1, x2 = self.variables

        if x1 == var:
            return self.op(val, x2.val)
        else:
            return self.op(x1.val, val)
    
    def est_possible(self, var):
        """ Teste si le domaine de var contient au moins une valeur satisfaisant la contrainte
            
            :return: ``True`` s'il existe au moins une valeur satisfaisant la contrainte
        """
        # pas ou plus de valeurs possibles a tester pour cette variable
        if var.taille_domaine() == 0:
            return False

        for v in var.domaine:
            if self.est_valide(var, v):
                # il suffit d'une valeur valide
                return True

        # aucune valeur du domaine n'a retourne True pour est_valide(var, d)
        return False
    
    def reviser(self):
        """ Algorithme de revision des domaines
            
            Pour chaque variable, verifie chaque valeur du domaine. Supprime les valeurs\
            qui empechent la contrainte d'etre satisfaite du domaine. (cf: Algorithme de Waltz\
            et REVISER dans le livre du cours)
            
            :return: True si un des domaines a ete modifie
        """
        domaines_modifies = False

        # l'indice [::-1] est une astuce pour obtenir l'inverse d'une liste ou d'un tuple
        # les paires sont donc (x1, x2) et (x2, x1)
        # (/!\ les tuples ne sont pas identiques mais ils contiennent des references sur les
        # memes objets Variable (modifier x1 dans le premier tuple, modifie x1 dans le second)
        for x1, x2 in (self.variables, self.variables[::-1]):
            ancienne_valeur = x1.val
            for v in x1.domaine:
                x1.val = v

                if not self.est_possible(x2):
                    x1.domaine.remove(v)
                    domaines_modifies = True
            x1.val = ancienne_valeur

        return domaines_modifies