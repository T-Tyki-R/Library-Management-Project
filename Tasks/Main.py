'''#
Main file for testing
'''
from BooksOperation import Books
from AuthorOperation import Authors
from UserOperation import Userdata
from GenreOperation import Genre
u_o = Userdata()

class MainMenu:
    def main_menu():
        u_o.exisiting_users_checker()
        print(f"Hello {u_o.get_name()}. Welcome to the Library Management System!\n\n\tMain Menu\n1. Book Operation\n2. User Operation\n3. Author Operation\n4. Genre Operation\n5. Exit\n")
        while True:
            user_choice = int(input("Enter a number corresponding with your choice: "))
            match user_choice:
                case 1:
                    if __name__ == "__main__":
                       ui = Books()
                       ui.book_menu()
                case 2:
                    if __name__ == "__main__":
                       ui = Userdata()
                       ui.user_database_menu()
                       pass
                case 3:
                   if __name__ =="__main__":
                        ui = Authors()
                        ui.author_menu()
                case 4:
                    if __name__ == "__main__":
                       ui = Genre()
                       ui.genre_menu()
                       pass
                case 5:
                    print("Thank you for using the Library Managment System. Good bye!")
                    break

    print(main_menu())
