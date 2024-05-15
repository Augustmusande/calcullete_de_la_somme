class Account:
    def __init__(self,SoldeInitial=0):
        self.SoldeInitial=SoldeInitial
        self.soldeActuel=SoldeInitial
    def getBalance(self):
        return self.soldeActuel
    def deposer(self,montantAdeposer):
        self.soldeActuel= self.soldeActuel+montantAdeposer
    def retirer(self,montantAretirer):
        self.soldeActuel=self.soldeActuel-montantAretirer
    def ajouterInteret(self,tauxInteret):
        self.soldeActuel=self.soldeActuel*(1+tauxInteret)

new_account=Account()
new_account.deposer(200)
new_account.retirer(50)
new_account.ajouterInteret(4)
print(f"la balance est de :{new_account.getBalance()}")


