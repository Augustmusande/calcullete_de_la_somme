class Somme:
    def __init__(self,nombre1,nombre2):
        self.nombre1=nombre1
        self.nombre2=nombre2

    def Somation(self):
        return self.nombre1+self.nombre2
nombre1=int(input("saisissez le premier nombre: "))
nombre2=int(input("saisissez le deuxieme nombre: "))
Somme=Somme(nombre1,nombre2)
valeur=Somme.Somation()
print(f"la somme de {nombre1} + {nombre2} = {valeur}")