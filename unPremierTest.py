titre ="truc muche"
print("{titre} est le titre du livre")

liste1 = [10, "chose", "truc"]
liste1[0]
liste1[2]

fruit=[]
fruit.append("pomme")
fruit.append("banane")
fruit.append("orange")
print(fruit)

nouvelle_campagne = {
"responsable_de_campagne": "Jeanne d'Arc",
"nom_de_campagne": "Campagne nous aimons les chiens",
"date_de_début": "01/01/2020",
"influenceurs_importants": ["@MonAmourDeChien", "@MeilleuresFriandisesPourChiens"]
}

taux_de_conversion = {}
taux_de_conversion['facebook'] = 3.4
taux_de_conversion['instagram'] = 1.2
taux_de_conversion = dict()
taux_de_conversion['facebook'] = 3.4
taux_de_conversion['instagram'] = 1.2

ensoleille = True
if ensoleille:
    print("soleil")
else:
    print("pas de soleil")

ensoleille = False
neige = True
if ensoleille:
    print("on va à la plage !")
elif neige:
    print("on fait un bonhomme de neige")
else:
    print("on reste à la maison !")

avec_soleil =True
en_semaine =False

if avec_soleil and not en_semaine:
    print("plage")
else:
    print("maison")

num1 = 6
if num1 == 0:
    print("zéro")
else:
    print(num1)

nombre_a_gauche =9
nombre_a_droite =4
symbole="-"
resultat=0
print(isinstance(nombre_a_droite, int))
if nombre_a_gauche ==0 or nombre_a_droite==0:
    False
else:
    match symbole:
        case "+":
            print("+")
            resultat=nombre_a_gauche+nombre_a_droite
        case "-":
            print("-")
            resultat=nombre_a_gauche-nombre_a_droite
        case "*":
            print("*")
            resultat=nombre_a_gauche*nombre_a_droite
        case "/":
            print("/")
            resultat=nombre_a_gauche/nombre_a_droite
        case _: 
            print("Error")

print(f"{nombre_a_gauche}{symbole}{nombre_a_droite}={resultat}")
    
capacite_maximale = 9
capacite_actuelle = 4
while capacite_actuelle < capacite_maximale:
    capacite_actuelle += 1

races_de_chien = ["golden retriever", "chihuahua", "terrier", "carlin"]
for chien in races_de_chien:
    print(chien)

for i in range(10):
    if i == 5:
        break
    print(i)

for i in range(15):
    if i == 5:
        continue
    print(i)

# affiche un input
input_str = input("Tapez une liste de nombres séparé par une virgule : ")

# Sépare la chaîne avec une virgule
str_list = input_str.split(',')

# Convertit chaque en un entier
num_list = [int(num) for num in str_list]

# nombre de nombres pairs dans la liste grace au modulo
even_count = sum(1 for num in num_list if num % 2 == 0)

# Affiche le nombre de nombres pairs
print("Le nombre de nombres pairs dans la liste est :", even_count)

annuel=100000

#exemple de fonction
def salaire_mensuel(a):
    resultatat=a/12
    return resultatat

mensuel=salaire_mensuel(annuel)
print("le salaire mensuel est : " +str(mensuel))

def salaire_hebdomadaire(b):
    resultatat=b/4
    return resultatat

hebdomadaire=salaire_hebdomadaire(mensuel)
print("le salaire hebdomadaire est : " + str(hebdomadaire))

heures_travaillees=35

def salaire_horaire(a, b):
    resultatat=a/b
    return resultatat

horaire=salaire_horaire(hebdomadaire, heures_travaillees)
print("le salaire horaire est : "+str(horaire))

#try erreur
#On cherche un entier
def test_entier(e):
    try:
        reponse = int(e)
        print(reponse)
    # ValueError: on peut ajouter ValueError: après except pour preciser l'erreur
    except:
        print("Erreur")

num3 = input("Tapez un entier: ")
test_entier(num3)

#maintenant on va ameliorer le code car on veut egalement que le num ne soit pas egale à zero

def test_division():
    try:
        reponse = input("Tapez un nombre entier: ")
        
        # On convertit en entier
        num = int(reponse)
        
        # On divise 2000 par la reponse
        resultat = 2000 / num
        
        # On affiche le résultat de la division
        print(f"Le résultat de 2000 divisé par {num} est {resultat}")
    
    # on affiche l'erreur si ce n'est pas un entier
    except ValueError:
        print("Erreur ce n'est pas un nombre entier.")
    
    # On affiche l'erreur si ce n'est pas egale à zero
    except ZeroDivisionError:
        print("Erreur, on  ne peut pas diviser par zero.")

# On utilise la fonction pour tester le chiffre pour diviser
test_division()

