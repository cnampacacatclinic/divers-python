#J'importe un package deja existant comme par ex Request
import requests

if __name__== '__main__':
    #j'utilise la fonction get
    page = requests.get("https://google.fr")
    #on affiche le code html de la page
    print(page.content)

    #je souhaite parser le html avec le package BeautifulSoup
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(page.content, 'html.parser')

    