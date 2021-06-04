# -*- coding: utf-8 -*-
"""
Created on Tue May 18 21:15:47 2021

@author: Ishika
"""


"""
Writing questions with options and correct answer for 2 difficulty levels
"""

import json


def json_writer_easy():
    data = [{'Question1': {
            "Ques": "How many days are in a week?",
            "a": "8",
            "b": "6",
            "c": "7",
            "d": "9",
            "correct_answer": "c"
            },
            'Question2': {
            "Ques": "How many letters are in the english alphabet?",
            "a": "28",
            "b": "26",
            "c": "27",
            "d": "29",
            "correct_answer": "b"
            },
            'Question3': {
            "Ques": "How many colors are in the rainbow?",
            "a": "8",
            "b": "6",
            "c": "7",
            "d": "9",
            "correct_answer": "c"
            },
            'Question4': {
            "Ques": "How many days are in a year?",
            "a": "365",
            "b": "368",
            "c": "367",
            "d": "379",
            "correct_answer": "a"
            },
            'Question5': {
            "Ques": "How many hours are in a day?",
            "a":"28",
            "b": "26",
            "d": "29",
            "c": "24",
            "correct_answer": "d"
            }}]
    print("Writing data in json file")
    with open("easy_ques.json", "w") as fileobj:
        json.dump(data, fileobj, indent=4)


def json_writer_difficult():
    data = [{'Question1': {
            "Ques": "What is the capital of India?",
            "a": "Nagpur",
            "b": "Mumbai",
            "c": "Delhi",
            "d": "Bangalore",
            "correct_answer": "c"
            },
            'Question2': {
            "Ques": "How many continents are in the world?",
            "a": "8",
            "b": "7",
            "c": "6",
            "d": "9",
            "correct_answer": "b"
            },
            'Question3': {
            "Ques": "Which direction does the sun set in?",
            "a": "north",
            "b": "east",
            "c": "west",
            "d": "south",
            "correct_answer": "c"
            },
            'Question4': {
            "Ques": "How many years are there in a millenium?",
            "a": "1000",
            "b": "100",
            "c": "10000",
            "d": "500",
            "correct_answer": "a"
            },
            'Question5': {
            "Ques": "Which is the smallest continent?",
            "a":"North America",
            "b": "Asia",
            "c": "Africa",
            "d": "Australia",
            "correct_answer": "d"
            }}]
    print("Writing data in json file")
    with open("difficult_ques.json", "w") as fileobj:
        json.dump(data, fileobj, indent=4)


if __name__ == '__main__':
    
    # creating json file for easy questions
    json_writer_easy()
    
    # creating json file for difficult questions
    json_writer_difficult()