'''#
Book file with vital data
'''
from GenreOperation import Genre
from AuthorOperation import Authors
from UserOperation import Userdata
from random import randint
class Books:
    '''#
    Module Functionality
    '''
    def __init__(self):
        self.library_books = {}
        self.user_books = {}
        self.author = ""
        self.title = ""
        self.isbn = ""
        self.publication_date = ""

    g_o = Genre()
    a_o = Authors()
    u_o = Userdata()
    

    def add_books(self):
        book_number = len(self.library_books.keys()) + 1
        self.title = input("What is the name of the book?: ").title()
        self.author = self.a_o.add_author()
        book_isbn_length = 7
        self.isbn = ''.join("{}".format(randint(0, 9)) for i in range(book_isbn_length))
        self.publication_date = input("What year was the book published?: ")
        self.library_books[f"Book {book_number}"] = {"Title": self.title, "Author": self.author, "ISBN": self.isbn, "Publication Date": self.publication_date}
        return f"This book was saved under Book 00{book_number}"

    def borrow_books(self):
        book_number = len(self.user_books.keys()) + 1
        if len(self.library_books) == 0:
            return "The library is closed"
        book_num = input("Which book are you trying to borrow?: ").capitalize()
        if book_num not in self.library_books.keys():
            return f"This book is not in stock..."
        else:
            self.user_books[f"Book {book_number}"] = self.library_books[book_num]
            self.library_books.pop(book_num)
        return self.library_books, self.user_books

    def return_books(self):
        book_number = len(self.user_books.keys()) + 1
        book_num = input("Which book are you trying to return?: ").capitalize()
        if book_num not in self.user_books.keys():
            return f"You don't have this book checked out..."
        else:
            self.library_books[f"Book {book_number}"] = self.user_books[book_num]
            self.user_books.pop(book_num)
        return self.library_books, self.user_books
    
    def search_books(self):
        book_num = input("Please enter the book you wish to search up?: ").capitalize()
        for num, book in self.library_books.items():
            if book_num == num:
                print(f"{num}\n")
                for data in book:
                    print(f"{data}: {book[data]}\n")

    def display_books(self):
        if len(self.library_books) == 0:
            print(f"The library is, surprising, out of books...")
        else:
            for num, book in self.library_books.items():
                print(f"{num}\n")
                for data in book:
                    print(f"{data}: {book[data]}\n")

    def book_menu(self):
        print("\n\tBook Operations\n1. Add New Book\n2. Borrow a Book\n3. Return a Book\n4. Search for a Book\n5. Display All Books\n")
        while True:
            user_choice = int(input("Enter a number corresponding with your choice: "))
            match user_choice:
                case 1:
                   print(self.add_books())
                case 2:
                    print(self.borrow_books())
                case 3:
                    print(self.return_books())
                case 4:
                    self.search_books()
                case 5:
                    self.display_books()