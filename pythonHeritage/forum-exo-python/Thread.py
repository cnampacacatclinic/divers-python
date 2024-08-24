class Thread:
    def __init__(self,title,time_posted,post):
        self.posts = [post]
        self.title=title
        self.time_posted=time_posted
    
    def display(self):
        """Affiche le fil de discussion."""
        print("----- THREAD -----")
        print(f"titre: {self.title}, date: {self.time_posted}")
        print()#saute laligne
        for post in self.posts:
            post.display()
            print()#saute laligne
        print("------------------")

    def add_post(self, post):
        """Ajoute un post."""
        self.posts.append(post)