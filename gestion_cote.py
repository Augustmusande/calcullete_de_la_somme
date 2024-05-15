class Etudiant:
    def __init__(self,nom,cote1,cote2):
        self.nom=nom
        self.cote1=cote1
        self.cote2=cote2

    def calcul_moyenne(self):
        self.moyenne=(self.cote1+self.cote2)/2
        return(self.cote1+self.cote2)/2

    def affichage (self):
        print(f" nom: ", self.nom,"a pour moyenne: ",self.moyenne)
nom=input("Entrez le nom de l'etudiant: ")
cote1=float(input("saisissez la cote numero 1: "))
cote2=float(input("saisissez la cote numero 2: "))
etudiant=Etudiant(nom,cote1,cote2)
etudiant.calcul_moyenne()
etudiant.affichage()