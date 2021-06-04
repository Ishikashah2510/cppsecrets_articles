# -*- coding: utf-8 -*-
"""
Created on Tue May 18 20:33:34 2021

@author: Ishika
"""

"""
JSON stands for JavaScript Object Notation. JSON is a lightweight format for storing
and transporting data. JSON is said to be "self describing" and easy to understand.
In this article, I will demonstrate how to fetch json data from a given site.

function definitions
json_using_urllib => using urllib library to fetch json data
json_using_requests => using requests library to fetch json data

Source code : https://github.com/Ishikashah2510/cppsecrets_articles
"""

# importing necessary libraries

import requests, json, urllib, time


def json_using_urllib(url):
    
    # fetching and decoding data from given url
    data = urllib.request.urlopen(url).read().decode('utf-8', errors='ignore')
    # waiting for 5 seconds
    time.sleep(5)
    # loading the data into json type
    obj = json.loads(data)
    # printing the data loaded
    print(obj)


def json_using_requests(url):
    
    # using requests library to get data from given url
    r = requests.get(url)
    # getting json data
    data_json = r.json()
    # printing the data loaded
    print(data_json)


if __name__ == '__main__':
    
    # url to be considered
    url = 'http://httpbin.org/stream/1'
    
    print("Data using urllib library")
    # calling json_using_urllib
    json_using_urllib(url)

    print("\nData using requests library")    
    # calling json_using_requests
    json_using_requests(url)
