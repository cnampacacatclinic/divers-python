class Post:
    def __init__(self,user,time_posted,content):
        self.user=user
        self.time_posted=time_posted
        self.content=content
    
    def display(self):
        """Affiche le message."""
        print(f"Message posté par {self.user} le {self.time_posted}:")
        print(self.content)