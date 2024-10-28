# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 15:12:47 2024

@author: Reza Farzam 20137189
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 14:59:49 2024

@author: rezaf
"""

import unittest

from as2 import  main ,add_value , delete_value, sort_value, add_value2, delete_value2, sorting_list, searching_value2

class Testlistfunctions(unittest.TestCase):
    
    def setUp(self):
        self.movie_stars = ["Reza","Bailey","Aleks","Hong","Tatenda"]
        self.movies = ["Forrest Gump", "The Dark Knight", "The Godfather"]
        self.games = ["The Witcher 3", "God of War", "Minecraft"]
    
    def test_add_value(self):
        new_value = "Alice"
        result = add_value(self.movie_stars, new_value)
        self.assertIn(new_value, result)
    
    def test_sort_value_ascending(self):
        result = sort_value(self.movie_stars)
        self.assertEqual(result, sorted(self.movie_stars) )
    
    def test_sort_value_descending(self):
        self.games.sort(reverse=True)
        result = self.games
        self.assertEqual(result, sorted(self.games, reverse=True))
        
    def test_delete_value(self):
        delete_game = "God of War" 
        result = delete_value(self.games,delete_game)
        self.assertNotIn(delete_game, result)
        
    def test_search_value(self):
        # Testing search (searching is in the I(searching) section)
        search_item = "Forrest Gump"
        self.assertIn(search_item, self.movies)  
        search_item = "Nonexistent Movie"
        self.assertNotIn(search_item, self.movies)       
        
###############################################################################        

class TestDictionaryFunctions2(unittest.TestCase):

    def setUp(self):
        """Sets up initial data for testing"""
        self.actors_birthdays = {
            "Leonardo DiCaprio": "1974-11-11",
            "Natalie Portman": "1981-06-09",
            "Brad Pitt": "1963-12-18"
        }
        
        self.favorite_movies = {
            "Inception": 2010,
            "The Dark Knight": 2008,
            "The Matrix": 1999
        }
        
        self.favorite_games = {
            'The Last of Us': 2013,
            'God of War': 2018,
            'Red Dead Redemption 2': 2018
        }

    # Test adding values to a dictionary
    def test_add_value2(self):
        add_value2(self.actors_birthdays, "Tom Hanks", "1956-07-09")
        self.assertIn("Tom Hanks", self.actors_birthdays)
        self.assertEqual(self.actors_birthdays["Tom Hanks"], "1956-07-09")
    
    # Test deleting values from a dictionary
    def test_delete_value2(self):
        delete_value2(self.actors_birthdays, "Leonardo DiCaprio")
        self.assertNotIn("Leonardo DiCaprio", self.actors_birthdays)
     
    def test_search_value(self):
         # Testing search (searching is in the I(searching) section)
         search_item = "Inception"
         self.assertIn(search_item, self.favorite_movies)  
         search_item = "Nonexistent Movie"
         self.assertNotIn(search_item, self.favorite_movies) 
    
    # Test sorting (ascending) keys in a dictionary
    def test_sorting_list(self):
        sorted_list = sorted(self.favorite_games)
        self.assertEqual(sorted_list, ['God of War', 'Red Dead Redemption 2', 'The Last of Us'])


if __name__ == "__main__":
    unittest.main()