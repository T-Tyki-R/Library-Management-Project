'''#
Main file for testing
'''
from UserOperation import Userdata
u_o = Userdata()

class Genre:
    def __init__(self):
        self.description = ""
        self.category = ""
        self.genre_list = {}

    def set_description(self, description):
        self.description = description
    def set_category(self, category):
        self.category = category
    def get_description(self):
        return self.description
    def get_category(self):
        return self.category

    def add_genre(self):  
        genre_name = input("What is the name of genre you wish to add?: ").title()
        self.set_category(genre_name)
        genre_description = input(f"What is the {self.get_category().lower()} genre about?: ").capitalize()
        self.set_description(genre_description)
        self.genre_list[f"{self.get_category()} Genre"] = {"Description" : self.get_description()}
        return self.genre_list
         
    def view_genre(self):
        if len(self.genre_list) == 0:
            print("This page is empty")
        else:
            for key, value in self.genre_list.items():
                print(f"{key}\n")
            search_genre = input("Please enter the genre you wish to search up?: ").title()
            for name, line in self.genre_list.items():
                if search_genre in self.genre_list.keys():
                    print(f"{name}\n")
                    for data in line:
                        print(f"{data}: {line[data]}\n")
                else:
                    print(f"{search_genre} is not listed here..")  

    def display_genre(self):
        if len(self.genre_list) == 0:
            print("This page is empty")
        else:
            for name, line in self.genre_list.items():
                print(f"{name}\n")
                for data in line:
                    print(f"{line[data]}\n")
    
    def genre_menu(self):
        print("\n\tGenre Operation\n1. Add a New Genre\n2. View Genre Details\n3. Display all Genres\n4. Return to Homescreen\n")
        while True:
            user_choice = int(input("Enter a number corresponding with your choice: "))
            match user_choice:
                case 1:
                    print(self.add_genre())
                case 2:
                    self.view_genre()
                case 3:
                    self.display_genre()
                case 4:
                    pass