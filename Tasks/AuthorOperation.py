'''#
Author file
'''
from random import randint
from UserOperation import Userdata
u_o = Userdata()

class Authors:
    # Hooks and Constructors
    def __init__(self):
        self.__author_name = ""
        self.bio = ""
        self.author_database = {}


    def set_name(self, name):
        self.__author_name = name
    def get_name(self):
        return self.__author_name
    def set_bio(self, bio):
        self.bio = bio
    def get_bio(self):
        return self.bio
    
    '''#
        Module Functionality
    '''
    def add_author(self):
        author_id_length = 4 
        author_id = ''.join("{}".format(randint(0, 9)) for i in range(author_id_length))
        author_name = input("What is the author's name?: ").title()
        self.set_name(author_name)
        author_bio = input(f"Provide a short bio about {author_name}: ").capitalize()
        self.set_bio(author_bio)
        self.author_database[f"{str(author_id)}"] = {"Name" : self.get_name(), "Bio" : self.get_bio()}
        return self.author_database
    
         
    def view_details(self):
        if len(self.author_database) == 0:
            print("This page is empty")
        else:
            for key, value in self.author_database.items():
                print(f"Author ID {key}\n")
            author_num = input("Please enter the 4-digit author ID you wish to search up?: ").capitalize()
            if author_num in self.author_database.keys():
                for info, line in self.author_database.items():
                    print(f"Author ID {info}\n")
                    for data in line:
                        print(f"\t {data} - {line[data]}\n")
            else:
                print("This ID does not exist.")  
            

    def display_author(self):
        if len(self.author_database) == 0:
            print("This page is empty")
        else:
            for num, person in self.author_database.items():
                print(f"{num}\n")
                for data in person:
                    print(f"{data}: {person[data]}\n")

    def author_menu(self):
        print("\n\tAuthor Operation\n1. Add a New Author\n2. View Author Details\n3. Display all Author\n return to Homescreen")
        while True:
            user_choice = int(input("Enter a number corresponding with your choice: "))
            match user_choice:
                case 1:
                    print(self.add_author())
                case 2:
                    self.view_details()
                case 3:
                    self.display_author()
                case 4:
                    pass

    
