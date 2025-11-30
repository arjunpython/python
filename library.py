class library:
    def __init__(self,books=None):
        self.books={"Python Essentials": {"author": "John Deo", "copies": 5},
            "AI for Beginners": {"author": "Lara Ray", "copies": 2},
            "Data Science 101": {"author": "Emily Clark", "copies": 3},
            "Machine Learning Pro": {"author": "Alex Stone", "copies": 4},
            "Deep Learning Guide": {"author": "Ravi Kumar", "copies": 1},}
    def display(self):
        if not self.books:
            print("There are currently no books available in the library.")
        else:
            print("Available books")
        for title,info in self.books.items():
            print(f"{title} : the author and number copies for this book are {info}")
    def borrow_book(self, member, title):
        if title not in self.books:
            print("Book not found.")
            return
        if not member.can_borrow():
            print("Borrowing limit reached!")
            return
        if self.books[title] ["copies"]<= 0:
            print("No copies left.")
            return
        self.books[title]["copies"] -= 1
        member.borrowed_books.append(title)
        print(f"✅ '{title}' borrowed successfully!")

class member:
    def __init__(self, name, is_premium):
        self.name=name
        self.is_premium=is_premium
        slef.borrowed_books=[]
    def can_borrow(self):
        limit=5 if self.is_premium else 3
        return len(self.borrowed_books)<limit