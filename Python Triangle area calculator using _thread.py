# -*- coding: utf-8 -*-
"""
Created on Sun May 23 10:34:35 2021

@author: Ishika
"""

"""
Threads are sometimes called light-weight processes and they do not require much memory overhead; they are cheaper than processes.
A thread has a beginning, an execution sequence, and a conclusion. It has an instruction pointer that keeps track of where within its context is it currently running.


In this article, I will show how to implement a simple triangle area calculator with given
sides

Function definitions:
    areaTriangle: This function is responsible for calculating the area of a triangle.
    check: This function is responsible for checking if the sides are valid or not.
    main: This function is responsible for taking user input of 3 sides and
    calling check funciton using thread.

The code explanation is available after the code.

Source Code: https://github.com/Ishikashah2510/cppsecrets_articles
"""



import _thread


def areaTriangle(side1,side2,side3):
    p = (side1+side2+side3)/2
    area = (p*(p-side1)*(p-side2)*(p-side3))**0.5
    print("Area is : ", area)
    
def check(side1,side2,side3):
    if (side1<side2+side3) and (side3<side2+side1) and (side2<side1+side3):
        areaTriangle(side1, side2, side3)
    else:
        print("Invalid value of sides")
    
if __name__ == "__main__":    
    side1, side2, side3 = map(int, input("Enter 3 sides ").split())
    okay = _thread.start_new_thread(check, (side1, side2, side3,))


"""
Explanation:
    areaTriangle: We calculate the area using its overall perimeter.
    check: We check if the sum of any two sides is greater than the third side alone.
    If all conditions are satisfied we calculate and display the area of the triangle.
    main: we take user input for the three sides, and start a thread for
    checking the sides.
    
Alternatives:
    You can make a area calculator for all shapes and integrate them together.
"""