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
        self.title = ""
        self.isbn = ""
        self.publication_date = ""

    def set_title(self, title):
        self.title = title
    def set_isbn_id(self, id):
        self.isbn = id
    def set_date(self, date):
        self.publication_date = date
    def get_title(self):
        return self.title
    def get_isbn_id(self):
        return self.isbn
    def get_date(self):
        return self.publication_date    

    g_o = Genre()
    a_o = Authors()
    u_o = Userdata()
    # self.u_o.exisiting_users_checker()
    # self.u_o.user_database[[f"{str(self.u_o.get_id())}"]]

    def add_books(self):
        book_number = len(self.library_books.keys()) + 1
        book_isbn_length = 7
        title_res = input("What is the name of the book?: ").title()
        self.set_title(title_res)
        author_info = self.a_o.add_author()
        isbn_id = ''.join("{}".format(randint(0, 9)) for i in range(book_isbn_length))
        self.set_isbn_id(isbn_id)
        publication_date = input("What year was the book published?: ")
        self.set_date(publication_date)
        self.library_books[f"{self.get_isbn_id()}"] = {"Title": self.get_title(), "Author": author_info, "ISBN": self.get_isbn_id(), "Publication Date": self.get_date()}
        return f"This book was saved under it's ISBN, ID #{self.get_isbn_id()}"

    def borrow_books(self):
        if len(self.library_books) == 0:
            return "The library is closed"
        else:
            for key, value in self.library_books.items():
                 print(f"ISBN ID #{key}\n")
            book_num = input("Which book are you trying to borrow? Please enter the 7-digit ISBN: ").capitalize()
            if book_num not in self.library_books.keys():
                return f"This book is not in stock..."
            else:
                self.u_o.current_account["List of Books"] = self.library_books[f"{self.get_isbn_id()}"]
                self.library_books.pop(book_num)
            return f"{self.u_o.get_name()}, you borrowed the book from the library."

    def return_books(self):
        if len(self.user_books) == 0:
            return "You have no books listed..."
        else:
            for key, value in self.user_books.items():
                 print(f"ISBN ID #{key}\n")
            book_num = input("Which book are you trying to return? Please enter the ISBN: ").capitalize()
            if book_num not in self.user_books.keys():
                return f"This book is not in your inventory..."
            else:
                self.library_books[f"{self.get_isbn_id()}"] = self.u_o.current_account["List of Books"][f"{self.get_isbn_id()}"]
                self.u_o.current_account["List of Books"].pop(self.get_isbn_id())
            return f"{self.u_o.get_name()}, you returned the book to the library."
    
    def search_books(self):
        if len(self.library_books) == 0:
            print("Unfortunately, the libraby is out of books...")
        else:
            for key, value in self.library_books.items():
                print(f"ISBN ID #{key}\n")
            search_book = input("Please enter the 7-didgit ISBN of the book you wish to search up: ").title()
            for num, line in self.library_books.items():
                if search_book in self.library_books.keys():
                    print(f"ISBN ID #{num}\n")
                    for data in line:
                        print(f"{data}: {line[data]}\n")
                else:
                    print(f"{search_book} is not listed here..")  
        
    def display_library_books(self):
        if len(self.library_books) == 0:
            print(f"The library is, surprising, out of books...")
        else:
            for num, book in self.library_books.items():
                print(f"ISBN ID #{num}\n")
                for data in book:
                    print(f"{data}: {book[data]}\n")

    def display_user_books(self):
        if len(self.u_o.current_account["List of Books"]) == 0:
            print(f"You have no books in your inventory...")
        else:
            for num, book in self.u_o.current_account["List of Books"].items():
                print(f"ISBN ID #{num}\n")
                for data in book:
                    print(f"{data}: {book[data]}\n")

    def book_menu(self):
        print(f"\n\tBook Operations\n1. Add New Book\n2. Borrow a Book\n3. Return a Book\n4. Search for a Book\n5. Display Library Books\n6. Display {self.u_o.get_name()} Books\n7. Return to Homescreen\n")
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
                    self.display_library_books()
                case 6:
                    self.display_user_books()
                case 7:
                    print(f"Welcome to the Library Management System!\n\n\tMain Menu\n1. Book Operation\n2. User Operation\n3. Author Operation\n4. Genre Operation\n5. Exit\n")
                    break

                    
