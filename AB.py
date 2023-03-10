import tkinter as tk
from math import *

class AB:
    def __init__(self,racine=None,gauche=None,droite=None):
        self.setRacine(racine)  # Initialisation de la racine
        self.setGauche(gauche)  # Initialisation du fils gauche
        self.setDroite(droite)  # Initialisation du fils droit

    def setRacine(self,racine):
        self.racine = [racine]  # Stockage de la racine dans une liste pour la mutabilité

    def setGauche(self,gauche):
        self.gauche = gauche  # Stockage du fils gauche

    def setDroite(self,droite):
        self.droite = droite  # Stockage du fils droit

    def estVide(self):
        return self.racine[0] == None  # Si la racine est nulle, l'arbre est vide
    
    def taille(self):
        if self.estVide():
            return 0  # Si l'arbre est vide, la taille est nulle
        else:
            taille = 1  # Initialisation de la taille à 1 (pour la racine)
            if self.gauche is not None:  # Si le fils gauche n'est pas nul
                if isinstance(self.gauche, AB):  # Si le fils gauche est un arbre, on ajoute sa taille
                    taille += self.gauche.taille()
                else:  # Sinon, on ajoute 1 (pour le nœud)
                    taille += 1
            if self.droite is not None:  # Si le fils droit n'est pas nul
                if isinstance(self.droite, AB):  # Si le fils droit est un arbre, on ajoute sa taille
                    taille += self.droite.taille()
                else:  # Sinon, on ajoute 1 (pour le nœud)
                    taille += 1
        return taille
    
    def __str__(self):
        line = f'PREFIX : {self.prefix()}\n'  # Récupération de l'ordre préfixe
        line += f'INFIX : {self.infix()}\n'  # Récupération de l'ordre infixe
        line += f'POSTFIX : {self.postfix()}\n'  # Récupération de l'ordre postfixe
        line += f'TAILLE : {self.taille()}\n'  # Récupération de la taille de l'arbre
        line += f'HAUTEUR : {self.hauteur()}\n'  # Récupération de la hauteur de l'arbre
        line += f'ABR : {self.estABR()}\n'  # Vérification si l'arbre est un ABR
        line += f'EQUILIBRE : {self.estEquilibre()}'  # Vérification si l'arbre est équilibré
        return line
    
    def prefix(self):
        if self.gauche is not None:  # Si le fils gauche n'est pas nul
            if isinstance(self.gauche, AB):  # Si le fils gauche est un arbre, gauche vaudra son préfix
                gauche = self.gauche.prefix()
            else: gauche = str(self.gauche) # Sinon gauche vaudra sa valeur
        else: gauche = "None" # Si le fils est nul alors gauche vaut None

        if self.droite is not None:  # Si le fils droite n'est pas nul
            if isinstance(self.droite, AB):  # Si le fils droite est un arbre, droite vaudra son préfix
                droite = self.droite.prefix()
            else: droite = str(self.droite) # Sinon droite vaudra sa valeur
        else: droite = "None" # Si le fils est nul alors droite vaut None

        return f'({self.racine},{gauche},{droite})' # On retourne la chaîne comme suit : RACINE, GAUCHE, DROITE
    
    def infix(self):
        if self.gauche is not None:  # Si le fils gauche n'est pas nul
            if isinstance(self.gauche, AB):  # Si le fils gauche est un arbre, gauche vaudra son préfix
                gauche = self.gauche.infix()
            else: gauche = str(self.gauche) # Sinon gauche vaudra sa valeur
        else: gauche = "None" # Si le fils est nul alors gauche vaut None

        if self.droite is not None:  # Si le fils droite n'est pas nul
            if isinstance(self.droite, AB):  # Si le fils droite est un arbre, droite vaudra son préfix
                droite = self.droite.infix()
            else: droite = str(self.droite) # Sinon droite vaudra sa valeur
        else: droite = "None" # Si le fils est nul alors droite vaut None

        return f'({gauche},{self.racine},{droite})' # On retourne la chaîne comme suit : GAUCHE, RACINE, DROITE
    
    def postfix(self):
        if self.gauche is not None:  # Si le fils gauche n'est pas nul
            if isinstance(self.gauche, AB):  # Si le fils gauche est un arbre, gauche vaudra son préfix
                gauche = self.gauche.postfix()
            else: gauche = str(self.gauche) # Sinon gauche vaudra sa valeur
        else: gauche = "None" # Si le fils est nul alors gauche vaut None
        
        if self.droite is not None:  # Si le fils droite n'est pas nul
            if isinstance(self.droite, AB):  # Si le fils droite est un arbre, droite vaudra son préfix
                droite = self.droite.postfix()
            else: droite = str(self.droite) # Sinon droite vaudra sa valeur
        else: droite = "None" # Si le fils est nul alors droite vaut None

        return f'({gauche},{droite},{self.racine})' # On retourne la chaîne comme suit : GAUCHE, DROITE, RACINE
    
    def hauteur(self):
        if self.estVide():  # Si l'arbre est vide, sa hauteur est 0
            return 0
        if self.gauche is None and self.droite is None:  # Si l'arbre a seulement la racine, sa hauteur est 1
            return 1
        # Sinon, on calcule la hauteur récursivement en prenant le maximum des hauteurs de ses fils (si ils existent)
        return 1 + max(self.gauche.hauteur() if isinstance(self.gauche, AB) else 0,  # Hauteur du fils gauche s'il existe
                    self.droite.hauteur() if isinstance(self.droite, AB) else 0)  # Hauteur du fils droit s'il existe
    
    def estABR(self):
        if isinstance(self.gauche,AB): # Si le noeud gauche est un arbre binaire
            # Si la valeur de la racine du sous-arbre gauche est supérieure à celle de la racine de l'arbre courant
            # ou si le sous-arbre gauche n'est pas un ABR, retourne False
            if self.gauche.racine[0] > self.racine[0] or not self.gauche.estABR(): return False
        else:
            # Si le noeud gauche est une feuille, vérifie que sa valeur
            # est inférieure à celle de la racine de l'arbre courant
            if self.gauche is not None and self.gauche > self.racine[0]: return False

        if isinstance(self.droite,AB): # Si le noeud gauche est un arbre binaire
            # Si la valeur de la racine du sous-arbre droite est inférieure à celle de la racine de l'arbre courant
            # ou si le sous-arbre droite n'est pas un ABR, retourne False
            if self.droite.racine[0] < self.racine[0] or not self.droite.estABR(): return False
        else:
            # Si le noeud droite est une feuille, vérifie que sa valeur
            # est supérieure à celle de la racine de l'arbre courant
            if self.droite is not None and self.droite < self.racine[0]: return False

        # Si toutes les conditions sont vérifiées, retourne True (l'arbre est un ABR)
        return True

    def estEquilibre(self):
        # si l'arbre est vide, il est équilibré
        if self.estVide():
            return True
        
        # calculer la hauteur de l'arbre gauche
        if self.gauche is not None:
            hauteur_gauche = 1 + self.gauche.hauteur() if isinstance(self.gauche, AB) else 0
        else:
            hauteur_gauche = -1

        # calculer la hauteur de l'arbre droite
        if self.droite is not None:
            hauteur_droite = 1 + self.droite.hauteur() if isinstance(self.droite, AB) else 0
        else:
            hauteur_droite = -1

        # si la différence de hauteur entre l'arbre gauche et l'arbre droit 
        # est supérieure à 1, alors l'arbre n'est pas équilibré
        # Vérification que la différence de hauteur est au plus égale à 1
        if abs(hauteur_gauche - hauteur_droite) <= 1:
            # Vérification que les sous-arbres gauche et droit sont équilibrés
            if isinstance(self.gauche,AB) and not self.gauche.estEquilibre():
                return False
            if isinstance(self.droite,AB) and not self.droite.estEquilibre():
                return False
            return True
        else:
            return False
        
    def dessiner(self, canvas, x, y, x_step, y_step):
        # Dessiner le noeud actuel
        canvas.create_oval(x-20, y-20, x+20, y+20, fill='white', width=2)
        canvas.create_text(x, y, text=self.racine[0])
        
        # Dessiner la branche gauche, si elle existe
        if self.gauche is not None:
            # Dessiner la ligne reliant le noeud actuel à son fils gauche
            canvas.create_line(x-x_step, y+y_step, x - 15, y + 15)
            if isinstance(self.gauche, AB):
                # Si le fils gauche est un arbre binaire, dessiner récursivement cet arbre
                Yg = self.gauche.dessiner(canvas, x-x_step, y+y_step, x_step/2, y_step) # On récupère la valeur de y à la fin du dessin
            else:
                # Sinon, dessiner un noeud simple pour représenter la valeur du fils gauche
                xg = x-x_step
                yg = y+y_step
                canvas.create_oval(xg-20, yg-20, xg+20, yg+20, fill='white', width=2)
                canvas.create_text(xg, yg, text=self.gauche)
                Yg = yg # On récupère la valeur de y à la fin du dessin
        else : Yg = 0 # On récupère la valeur de y à la fin du dessin
        
        # Dessiner la branche droite, si elle existe
        if self.droite is not None:
            # Dessiner la ligne reliant le noeud actuel à son fils droit
            canvas.create_line(x+x_step, y+y_step, x + 15, y + 15)
            if isinstance(self.droite, AB):
                # Si le fils droit est un arbre binaire, dessiner récursivement cet arbre
                Yd = self.droite.dessiner(canvas, x+x_step, y+y_step, x_step/2, y_step) # On récupère la valeur de y à la fin du dessin
            else:
                # Sinon, dessiner un noeud simple pour représenter la valeur du fils droit
                xd = x+x_step
                yd = y+y_step
                canvas.create_oval(xd-20, yd-20, xd+20, yd+20, fill='white', width=2)
                canvas.create_text(xd, yd, text=self.droite)
                Yd = yd # On récupère la valeur de y à la fin du dessin
        else: Yd = 0 # On récupère la valeur de y à la fin du dessin
        return max(Yg,Yd) # On renvoie la valeur de y à la fin du dessin
    

    
    def afficher(self,width:int=800,height:int=600,name:str="ARBRE DE DONNÉES"):
        # Création du canvas
        root = tk.Tk()
        root.title(name)
        canvas = tk.Canvas(root, width=width, height=height)
        canvas.pack()

        # Dans un arbre binaire : h <= n - 1

        # On dessine l'arbre et on récupère la valeur de y à la fin du dessin
        y = self.dessiner(canvas, width/2, 50, width / 4, height / 6)

        # On ajoute au dessin les informations de l'arbre 
        # en les positionnant 10 pixels après le dessin
        canvas.create_text(width/4, y + 100, text=self.__str__())       

        # Affichage du canvas 
        root.mainloop()   

    @classmethod
    def initFromPrefix(cls, prefix):
        # Si la liste est vide, on retourne None
        if len(prefix) == 0:
            return None
        
        # Le premier élément de la liste est la valeur 
        # du nœud parent
        father = prefix[0]
        
        # Les éléments restants sont les valeurs 
        # des nœuds enfants
        sons = prefix[1:]
        
        # Si la liste contient un seul élément, 
        # on crée un nœud avec cet élément comme fils 
        # gauche ou droit selon sa valeur
        if len(sons) == 1:
            if sons[0] < father:
                return cls(father, sons[0], None)
            else:
                return cls(father, None, sons[0])
        
        # Si la liste contient deux éléments 
        # et que le second est bien supérieur au père, 
        # on crée un nœud avec ces deux éléments 
        # comme fils gauche et droit
        if len(sons) == 2 and sons[1] > father:
            return cls(father, sons[0], sons[1])
        
        # Sinon, on cherche l'indice à partir duquel 
        # les valeurs de la liste sont supérieures 
        # à celle du nœud parent
        index = len(sons)
        for i in range(index):
            if sons[i] > father:
                index = i
                break
        
        # On crée un sous-arbre avec les éléments 
        # de la liste avant l'indice trouvé comme fils gauche
        # et les éléments après l'indice comme fils droit
        left = cls.initFromPrefix(sons[:index])
        right = cls.initFromPrefix(sons[index:])
        
        # On crée le nœud parent avec les sous-arbres 
        # gauche et droit créés précédemment
        return cls(father, left, right)