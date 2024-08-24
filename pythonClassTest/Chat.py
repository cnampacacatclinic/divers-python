class Chat:
    # Attribut de classe
    noms = ("siamois", "autre", "sauvage")
    positions = {}

    def __init__(self, nom):
        # Attribut d'instance
        self.nom = nom
        # On saura ou est le chat uniquement si il est à cette position
        self.pos = (3, 4)

        # On accède à l'attribut de classe "positions" avec Chat.
        Chat.positions[self.pos] = self.nom

    @classmethod
    def trouver_le_chat(cls, pos):
        # Renvoie la position du chat
        if pos in cls.positions:
            #Si le chat est à la position par defaut, on affiche son nom
            return f"Le chat est un : {cls.positions[pos]}"
        #Sinon on ne sait pas qui il est
        return "On ne sait pas où il est"
    
    #methode statique
    @staticmethod
    def chat_description():
        #Description d'un chat
        return (
        "Le chat domestique est une espèce de mammifères carnivores, de la famille des Félidés."
        )
    
##########################################################################

#On affiche la description
print(Chat.chat_description())

# On accede aux variables de classe sans instanciation
print(Chat.noms)
print(Chat.positions)
#On quoi que l'on mette sur sa postion, on ne saura pas son nom
print(Chat.trouver_le_chat((3, 4)))

# On instancie un chat
chaton = Chat("Siamois")
#On ne change pas sa position donc on sait son nom
print(Chat.trouver_le_chat((3, 4)))
