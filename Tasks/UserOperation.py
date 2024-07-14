'''#
Main file for testing
'''
from random import randint

class Userdata:

    user_database = {}
    user_book_list = {}

    def add_users(self):
        user_name = input("Enter the name of the new user of this account: ").title()
        id_length = 5
        library_id =''.join("{}".format(randint(0, 9)) for i in range(id_length))
        self.user_database[f"ID {str(library_id)}"] = {"Name" : user_name, "List of Books": self.user_book_list}
        return f"{user_name}, your library ID number is {library_id}"

    def view_user(self):
        search_user = input("Please enter the library ID for the user you wish to search up?: ")
        for id_num, line in self.user_database.items():
            search_found = self.user_book_list[search_user]
            if search_user == id_num:
                print(f"Library ID - {id_num}\n")
                for data in line:
                        if not search_found["List of Books"]:
                            print("Your book list is empty")
                        else:
                            for data in line:
                                print(f"{data}: {line[data]}\n")
                

    def display_user(self):
         for id_num, line in self.user_database.items():
                print(f"Library ID - {id_num}\n")
                for data in line:
                    print(f"{data}: {line[data]}\n")
        
         
    def user_database_menu(self): 
        print("\n\tUser Operation\n1. Add a User\n2. View User Details\n3. Display all Users")
        while True:
            user_choice = int(input("Enter a number corresponding with your choice: "))
            match user_choice:
                case 1:
                    print(self.add_users())
                case 2:
                    self.view_user()
                case 3:
                    self.display_user()