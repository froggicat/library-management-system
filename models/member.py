import random

class Member():
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.memberid = random.randint(0, 1000)
        self.borrowed_books = []

    def __str__(self):
        return f"Name: {self.name} \nEmail: {self.email} \nMember ID: {self.memberid}"