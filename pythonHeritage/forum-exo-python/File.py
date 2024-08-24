class File:
    def __init__(self,name,Size):
        self.name=name
        self.Size=Size

    def display(self):
        print(f"Fichier '{self.name}'.")