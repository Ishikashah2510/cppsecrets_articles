# -*- coding: utf-8 -*-
"""
Created on Wed May 19 19:57:49 2021

@author: Ishika
"""


"""
JSON stands for JavaScript Object Notation. JSON is a lightweight format for storing
and transporting data. JSON is said to be "self describing" and easy to understand.
In this article, I will demonstrate how to use pandas in python with json files.

About json_normalize function:
    It is used to Normalize semi-structured JSON data into a flat table.
"""

import pandas as pd
import json
from pandas import json_normalize


if __name__ == '__main__':
    # reading json file using pandas
    print("Reading json file using pandas")
    
    df = pd.read_json('easy_ques.json')
    print(df.to_string())
    
    
    # converting data frame to json file
    print()
    print("Converting data frame to json format")
    df = pd.DataFrame([['a', 'b'], ['c', 'd']],
                      index =['row 1', 'row 2'],
                      columns =['col 1', 'col 2'])
    print(df.to_json(orient ='split'))
  
    print(df.to_json(orient ='index'))
    
    # Using json_normalize function
    print()
    print("Using json_normalize function")
    print("Reading data ")
    with open('D:/codes/python_codes/cppsecrets_internship_may-july-2021/raw_nyc_phil.json') as f:
        d = json.load(f)
     

    # lets put the data into a pandas df
    # clicking on raw_nyc_phil.json under "Input Files"
    # tells us parent node is 'programs'
    nycphil = json_normalize(d['programs'])
    print()
    print(nycphil.head(3))
    works_data = json_normalize(data = d['programs'],
                            record_path ='works', 
                            meta =['id', 'orchestra', 'programID', 'season'])
    print(works_data.head(3))
    
    print()
    # Let’s flatten the ‘soloists’ data here by passing a list. Since soloists is nested in work
    print("Let’s flatten the ‘soloists’ data here by passing a list. Since soloists is nested in work")
    soloist_data = json_normalize(data = d['programs'],
                              record_path =['works', 'soloists'],
                              meta =['id'])

    print(soloist_data.head(3))