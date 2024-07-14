'''#
Author file
'''

class Authors:
    # Hooks and Constructors
    def __init__(self, name, bio) -> None:
        self.__author_name = name
        self.bio = bio
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
        author_add = len(self.author_database.keys()) + 1
        author_name = input("What is the author's name?: ").title()
        self.__author_name = self.set_name(author_name)
        author_bio = input(f"Provide a short bio about {author_name}: ").capitalize()
        self.bio = self.set_bio(author_bio)
        self.author_database[f"Author 00{author_add}"] = {"Name" : self.get_name(), "Bio" : self.get_bio()}
        return f"This author was saved under the ticket: Author 00{author_add}"
         
    def view_details(self):
        author_num = input("Please enter the author ticket you wish to search up?: ").capitalize()
        for num, person in self.author_database.items():
            if author_num == num:
                print(f"{num}\n")
                for data in person:
                    print(f"{data}: {person[data]}\n")

    def display_author(self):
        for num, person in self.author_database.items():
                print(f"{num}\n")
                for data in person:
                    print(f"{data}: {person[data]}\n")

    def author_menu(self):
        print("\n\tAuthor Operation\n1. Add a New Author\n2. View Author Details\n3. Display all Author")
        while True:
            user_choice = int(input("Enter a number corresponding with your choice: "))
            match user_choice:
                case 1:
                    print(self.add_author())
                case 2:
                    self.view_details()
                case 3:
                    self.display_author()
    
