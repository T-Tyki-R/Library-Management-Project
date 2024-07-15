'''#
Main file for testing
'''
from random import randint

class Userdata:
    def __init__(self):
        self.__name = ""
        self.__id = ""
        self.user_database = {}

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
        self.user_database[f"{str(self.get_id())}"] = {"Name" : user_name}
        return f"{self.get_name()}, your library ID number is {self.get_id()}"
    
    def exisiting_users_checker(self):
        if len(self.user_database) == 0:
            print("There aren't any users added to the list. Please add a user to get started")
            self.add_users()
        else:
            for key, value in self.user_database.items():
                print(f"{key}\n")
            search_id = input("Please enter the 5-digit ID number of the account you wish to use: ").title()
            if search_id in self.user_database.keys():
                user_account = input(f"{self.get_name}, do you want to switch over to account {search_id}? Y/N: ").capitalize()
                if user_account == "Y":
                    self.user_database[search_id] = Userdata(self.__name)
                elif user_account == "N":
                    return f"{self.get_name()}, your library ID number is {self.get_id()}"

    def view_user(self):
        if len(self.user_database) == 0:
            print("This page is empty")
        else:
            for key, value in self.user_database.items():
                print(f"{key}\n")
            search_id = input("Please enter the 5-digit ID number for the user you wish to search up: ").title()
            for name, line in self.user_database.items():
                if search_id in self.user_database.keys():
                    print(f"{name}\n")
                    for data in line:
                        print(f"{data}: {line[data]}\n")
                else:
                    print(f"{search_id} is not listed here..")  
                

    def display_user(self):
         for id_num, line in self.user_database.items():
                print(f"Library ID - {id_num}\n")
                for data in line:
                    print(f"{data}: {line[data]}\n")
        
         
    def user_database_menu(self): 
        print("\n\tUser Operation\n1. Add a User\n2. View User Details\n3. Display all Users\n4. Return to Homescreen")
        while True:
            user_choice = int(input("Enter a number corresponding with your choice: "))
            match user_choice:
                case 1:
                    print(self.exisiting_users_checker())
                case 2:
                    self.view_user()
                case 3:
                    self.display_user()
                case 4:
                    pass