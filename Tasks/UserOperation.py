'''#
Main file for testing
'''
from random import randint

class Userdata:
    def __init__(self):
        self.__name = ""
        self.__id = ""
        self.user_books = {}
        self.user_database = {}
        self.current_account = {}

    def set_name(self, name):
        self.__name = name
    def set_id(self, id):
        self.__id = id
    def get_name(self):
        return self.__name
    def get_id(self):
        return self.__id
         
    def add_users(self):
        id_length = 5
        user_name = input("Enter the name of the new user of this account: ").title()
        self.set_name(user_name)
        library_id = ''.join("{}".format(randint(0, 9)) for i in range(id_length))
        self.set_id(library_id)
        self.current_account = self.user_database[f"{self.get_name()}"] = {"ID" : self.get_id(), "List of Books" : self.user_books}
        return f"{self.get_name()}, your library ID number is {self.get_id()}"

    def add_switch_account(self):
        if len(self.user_database) == 0:
            print("There aren't any user accounts active. Please add a user to get started")
            self.add_users()
        else:
            for key, value in self.user_database.items():
                print(f"{key}\n")  
            print("\n1. Add a User\n2. Switch Account\n3. Go Back")
            while(True):
                user_option = int(input("Enter a number corresponding with your choice: "))
                match user_option:
                    case 1:
                        self.add_users()
                    case 2:
                        if len(self.user_database) == 1:
                            print("There's only 1 account active. You need 2 or more accounts to use this feature.")
                        else:
                            search_name = input("Please enter the user's name of the account you wish to use: ").title()
                            if search_name in self.user_database.keys():
                                self.current_account = self.user_database[search_name]
                                for key, value in self.user_database.items():
                                        print(f"You're currently using {key}'s account.")
                    case 3:
                        break

    def view_user(self):
        if len(self.user_database) == 0:
            print("This page is empty")
        else:
            for key, value in self.user_database.items():
                print(f"{key}\n")
            search_name = input("Please enter the owner of the account  you wish to search up: ").title()
            for name, line in self.user_database.items():
                if search_name in self.user_database.keys():
                    print(f"{name}\n")
                    for data in line:
                        print(f"{data}: {line[data]}\n")
                else:
                    print(f"{search_name} is not listed here..")  
                

    def display_user(self):
        if len(self.user_database) == 0:
            print("This page is empty")
        else: 
            for name, line in self.user_database.items():
                print(f"Library ID - {name}\n")
                for data in line:
                    print(f"{data}: {line[data]}\n")
        
         
    def user_database_menu(self): 
        print("\n\tUser Operation\n1. Add a User\n2. View User Details\n3. Display all Users\n4. Return to Homescreen")
        while True:
            user_choice = int(input("Enter a number corresponding with your choice: "))
            match user_choice:
                case 1:
                    print(self.add_switch_account())
                case 2:
                    self.view_user()
                case 3:
                    self.display_user()
                case 4:
                    print(f"Welcome to the Library Management System!\n\n\tMain Menu\n1. Book Operation\n2. User Operation\n3. Author Operation\n4. Genre Operation\n5. Exit\n")
                    break