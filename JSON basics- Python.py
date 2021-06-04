# -*- coding: utf-8 -*-
"""
Created on Mon May 17 19:01:37 2021

@author: Ishika
"""

"""
JSON stands for JavaScript Object Notation. JSON is a lightweight format for storing
and transporting data. JSON is said to be "self describing" and easy to understand.
In this article, I will demonstrate the storing of objects using JSON library
in python.

class definition 
json_string : This class is simply for converting a string type object 
              to a json type object with a method meant for printing it
              
json_dictionary : This class is simply for converting a list of dictionary type objects
                  to a json type object with a method meant for printing it

Source code : https://github.com/Ishikashah2510/cppsecrets_articles
"""

# importing necessary libraries

import json


class json_string:
    def __init__(self, indent_val=2):
        self.x = '{"firstName": "Ishika", "lastName":"Shah", "Age": "20", "Country": "India", "convertedFrom": "string"}'
        self.y = json.dumps(self.x, indent=indent_val)
    
    def pretty_print(self):
        print(self.y)
        
    def class_definition(self):
        definition = """This class is simply for converting a string type object
        to a json type object with a method meant for printing it"""
        print(definition)


class json_dictionary:
    def __init__(self, indent_val=2):
        self.x = [{'Person 1': {
            "firstName": "Ishika",
            "lastName":"Shah",
            "Age": "20",
            "Country": "India",
            "convertedFrom": "dictionary"
            }},
            {'Person 2': {
            "firstName": "Aadar",
            "lastName": "Jain",
            "Age": "18",
            "Country": "India",
            "convertedFrom": "dictionary"
            }}]
        self.y = json.dumps(self.x, indent=indent_val)
    
    def pretty_print(self):
        print(self.y)
    
    def class_definition(self):
        definition = """This class is simply for converting a list of dictionary type objects
        to a json type object with a method meant for printing it"""
        print(definition)


if __name__ == '__main__':
    print("""Creating an object of converting a string 
          object to json format with default indent (2)""")
    str_conv = json_string()
    print(""""Creating an object of converting a dictionary 
          object to json format with default indent (2)""")
    dict_conv = json_dictionary()
    
    # calling pretty print for str_conv object
    str_conv.pretty_print()
    # calling pretty print for dict_conv object
    dict_conv.pretty_print()
    

