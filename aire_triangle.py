class Forme:
    def __init__ (self,largeur,hauteur):
        self.largeur=largeur
        self.hauteur=hauteur
class Triangle(Forme):
    def Aire(self):
        return  (self.largeur * self.hauteur)/2 
class Rectangle(Forme):
      def Aire(self):
        return self.largeur * self.hauteur
rectangle=Rectangle(5,5)
print(f"le rectangle a pour aire de:{rectangle.Aire()}")
triangle=Triangle(8,3)
print(f"le triangle a pour aire de:{triangle.Aire()}") 

