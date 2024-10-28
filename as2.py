# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 15:11:34 2024

@author: Reza Farzam 20137189
"""

"""
Part A

In this part we have to create three list and test some function on them. 
"""
# coding


# Lists for different categories

movie_stars = ["Robert Downey Jr.", "Scarlett Johansson", "Leonardo DiCaprio", 
                   "Tom Hanks", "Meryl Streep", "Denzel Washington", 
                   "Cate Blanchett", "Brad Pitt", "Emma Stone", 
                   "Johnny Depp", "Natalie Portman", "Chris Hemsworth"] 

movies = ["Inception", "Avengers: Endgame", "The Matrix", 
              "Forrest Gump", "The Dark Knight", "The Godfather", 
              "Titanic", "The Lord of the Rings", "The Shawshank Redemption", 
              "Gladiator", "Pulp Fiction", "Fight Club"]

games = ["The Witcher 3", "God of War", "Minecraft", 
             "The Last of Us", "Red Dead Redemption 2", "GTA V", 
             "Fortnite", "Cyberpunk 2077", "Doom", 
             "Halo", "The Legend of Zelda", "Overwatch"]

actors_birthdays = {
        "Leonardo DiCaprio": "1974-11-11",
        "Natalie Portman": "1981-06-09",
        "Brad Pitt": "1963-12-18",
        "Scarlett Johansson": "1984-11-22",
        "Johnny Depp": "1963-06-09",
        "Angelina Jolie": "1975-06-04",
        "Robert Downey Jr.": "1965-04-04",
        "Emma Watson": "1990-04-15",
        "Tom Hanks": "1956-07-09",
        "Meryl Streep": "1949-06-22",
        "Hugh Jackman": "1968-10-12",
        "Anne Hathaway": "1982-11-12"
    }

favorite_movies = {
        "Inception": 2010,
        "The Dark Knight": 2008,
        "The Matrix": 1999,
        "Interstellar": 2014,
        "Titanic": 1997,
        "Avatar": 2009,
        "Pulp Fiction": 1994,
        "Forrest Gump": 1994,
        "Gladiator": 2000,
        "The Avengers": 2012,
        "Iron Man": 2008,
        "The Wolf of Wall Street": 2013
    }

favorite_games = {
        'The Last of Us': 2013,
        'God of War': 2018,
        'Red Dead Redemption 2': 2018,
        'Grand Theft Auto V': 2013,
        'The Witcher 3': 2015,
        'Cyberpunk 2077': 2020,
        'Horizon Zero Dawn': 2017,
        'Fortnite': 2017,
        'Overwatch': 2016,
        'Dark Souls III': 2016,
        'Resident Evil 2': 2019,
        'Minecraft': 2011
    }

    # Function to add value to a list
def add_value(list_name, value):
    list_name.append(value)
    return list_name

    # Function to sort a list
def sort_value(list_name):
    list_name.sort()
    return list_name

    # Function to delete a specific value from the list
def delete_value(list_name, value):
    list_name.remove(value)
    return list_name

    # Function to search for a specific value in the list
def searching_value(listname, value):
    if value in listname:
        print(f"{value} is in this list")
    else:
        print(f"{value} is not in this list!!!")

    # Function to add a key-value pair to a dictionary
def add_value2(listname, name, value):
    listname[name] = value

    # Function to delete a specific key from a dictionary
def delete_value2(listname, name):
    if name in listname:
        del listname[name]

    # Function to sort the dictionary by keys or values
def sorting_list(listname, by_values=False, reverse=False):
    if by_values:
        sorted_list = sorted(listname.items(), key=lambda x: x[1], reverse=reverse)
    else:
        sorted_list = sorted(listname.items(), reverse=reverse)
    return sorted_list

    # Function to search for a specific key in a dictionary
def searching_value2(listname, value):
    if value in listname:
        print(f"{value} is in this list")
    else:
        print(f"{value} is not in this list!!!")
        
        
        
def main():
    # Input to select category type (S: Stars, M: Movies, G: Games, E: End program)
    category_type = input("Please Enter category type e.g., S(tars), M(ovie), G(ames), E(nd) => ")

    if category_type == 'E':
        print("Thanks you. You are now exiting the program ")
        return
    else:
        if category_type == 'S':
            list_type = movie_stars
        elif category_type == 'M':
            list_type = movies
        else:
            list_type = games

        instruction_type = input("Please enter instruction type e.g., A(dd), D(elete), S(orting), I(searching), P(revious menu) => ")

        if instruction_type == "P":
            return
        else:
            if instruction_type == "A":
                value = input("Please Enter Value :")
                list_type = add_value(list_type, value)

            elif instruction_type == "D":
                value = input("Enter the Value you want to Delete: ")
                list_type = delete_value(list_type, value)

            elif instruction_type == "S":
                sort_type = input("Please enter sorting type e.g, A(scending), D(escending) => ")
                if sort_type == "A":
                    list_type = sort_value(list_type)
                elif sort_type == "D":
                    list_type.sort(reverse=True)
                else:
                    print("Invalid input!!!")
                    return

            elif instruction_type == "I":
                value = input("Enter the Name you want to find: ")
                list_type = searching_value(list_type, value)

    # Input to select category type (A: Actors' birthdays, M: Favorite movies, G: Favorite games, E: Exit program)
    category = input("Enter A(Actors_birthday), M(Favorite movies), G(Favorite games) E(xit)=> ")

    if category == "E":
        print("Thanks for choosing our program you are now exiting the program.")
        return
    else:
        if category == "A":
            listname = actors_birthdays
        elif category == "M":
            listname = favorite_movies
        elif category == "G":
            listname = favorite_games
        else:
            print("The value you entered is not valid!!")
            return

    # Input for function type (A: Add, D: Delete, S: Sort, I: Search, E: Exit program)
    function_type = input(" Please enter A(dd),D(elete),S(ort),I(search) or E(xit)=>  ")
    if function_type == "A":
        name = input("Enter the name that you want: ")
        value = input("Enter the date of the product: ")
        add_value2(listname, name, value)

    elif function_type == "D":
        name = input("Enter the value you want to delete: ")
        delete_value2(listname, name)

    elif function_type == "S":
        sorting_type = input("Enter your sorting method: A(scending), D(escending): ")
        sort_by = input("Sort by Keys or Values? Enter K or V: ").upper()

        reverse = False
        if sorting_type == "D":
            reverse = True

        if sort_by == "K":
            sorted_list = sorting_list(listname, by_values=False, reverse=reverse)
        elif sort_by == "V":
            sorted_list = sorting_list(listname, by_values=True, reverse=reverse)
        else:
            print("Invalid sorting option!!")
            return

        print(f"Sorted List: {sorted_list}")

    elif function_type == "I":
        value = input("Enter the Name you want to find: ")
        searching_value2(listname, value)

    elif function_type == "E":
        print("Thank You!! You are now exiting this program!!")
    else:
        print("Invalid parameter!!!")



if __name__ == "__main__":
    main() 





