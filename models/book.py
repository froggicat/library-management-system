class Book():
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

    def __str__(self):
        if self.available == True:
            return f"{self.title} by {self.author} is available to borrow."
        else: 
            return f"{self.title} by {self.author} has been taken out by someone else."