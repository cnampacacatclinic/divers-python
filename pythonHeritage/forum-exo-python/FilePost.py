import Post.py
"""Message comportant un fichier."""
class FilePost(Post):


    def __init__(self, user, time_posted, content, file):
        """Initialise le fichier."""
        self.user = user
        self.time_posted = time_posted
        self.content = content
        self.file = file

    def display(self):
        """Affiche le contenu et le fichier."""
        super().display()
        print("pièce jointe:")
        self.file.display()
