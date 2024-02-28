# nom, prix, ingredients, vegetarienne

class Pizza:
    def __init__(self, nom, prix, ingredients, vegetarienne=False):
        self.nom = nom
        self.prix = prix
        self.ingredients = ingredients
        self.vegetarienne = vegetarienne

    def Afficher(self):
        veg_str = ""
        if self.vegetarienne:
            veg_str = "-> VEGETARIENNE "

        print(f"PIZZA {self.nom} : {self.prix}€ {veg_str}")
        print(", ".join(self.ingredients))
        print()

class PizzaPersonnalisee(Pizza): #classe herité du classe pizza
    PRIX_DE_BASE = 7
    PRIX_PAR_ING = 1.2
    dernier_numero = 0
    def __init__(self):
        PizzaPersonnalisee.dernier_numero += 1
        self.numero = PizzaPersonnalisee.dernier_numero
        super().__init__("Personnalisée " + str(self.numero), 0, [])
        self.demander_ingredients_utilisateur()
        self.calculer_le_prix()

    def demander_ingredients_utilisateur(self):
        print()
        print(f"Ingredients pour la pizza personnalisée {self.numero}")
        while True:
            ingredient = input("Ajouter un ingredient (ou ENTRER pour terminer) : ")
            if ingredient == "":
                return
            self.ingredients.append(ingredient)
            print(f"Vous avez {len(self.ingredients)} ingredient(s) : {','.join(self.ingredients)}")

    def calculer_le_prix(self):
        self.prix = self.PRIX_DE_BASE + len(self.ingredients)*self.PRIX_PAR_ING

pizzas = [
    Pizza("4 fromages", 8.5, ("brie", "emmental", "compté", "parmesan"), True),
    Pizza("Hawai", 9, ("tomate", "steak", "oignons", "ail"), False),
    Pizza("4 saison", 11.4, ("oeuf", "emmental", "jambon", "parmesan"), False),
    Pizza("Vegetariens", 7.8, ("champignon", "tomate", "oignons", "poivrons"), True),
    PizzaPersonnalisee(),
    PizzaPersonnalisee()
]
#afficher tous les pizzas
print( "Les pizzas sont :")
for i in pizzas:
    i.Afficher()

#afficher tous les pizzas vegetariennes
print( "Les pizzas vegetariennes sont :")
for i in pizzas:
    if i.vegetarienne:
        i.Afficher()

#afficher tous les pizzas non vegetariennes
print( "Les pizzas non vegetariennes sont :")
for i in pizzas:
    if not i.vegetarienne:
        i.Afficher()

#afficher tous les pizzas avec des ingredients tomates 
print( "Les pizzas qui ont des ingredients tomates sont :")
for i in pizzas:
    if "tomate" in i.ingredients:
        i.Afficher()

#afficher tous les pizzas moins de 10€ 
print( "Les pizzas moins de 10€ sont :")
for i in pizzas:
    if i.prix < 10:
        i.Afficher()
    
#afficher tous les pizzas par ordre alphabetique
def tri(e) :
    return e.prix

pizzas.sort(key=tri, reverse=True)

print( "Les pizzas par ordre alphabetique sont :")
for i in pizzas:
    i.Afficher()