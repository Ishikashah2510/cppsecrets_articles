# -*- coding: utf-8 -*-
"""
Created on Sun May 23 11:24:51 2021

@author: Ishika
"""

"""
Threads are sometimes called light-weight processes and they do not require much memory overhead; they are cheaper than processes.
A thread has a beginning, an execution sequence, and a conclusion. It has an instruction pointer that keeps track of where within its context is it currently running.

A Gaussian curve is formally defined as a normalized frequency distribution that is
symmetrical about the line of zero error and in which the frequency and magnitude
of quantities are related by the expression:
    

In this article, I will show how to plot a gaussian curve using _thread module.

Function definitions:
    evaluate: Evaluates the probability density value for a given value, x
    generator: Generates t random numbers from domain (-10, 10) and calculates
    standard deviation, s and mean, m and evaluates probability density value for all
    x in f(sorted input values).
    plotter: plots the gaussian curve
    main: Starts a thread for generator and plotter.

The code explanation is available after the code.

Source Code: https://github.com/Ishikashah2510/cppsecrets_articles
"""


from matplotlib import pyplot as plt
import random
import statistics
import math
import _thread
import pandas as pd


outs = []
ins = set()
f = []


def evaluate(s,x,m):
    e=(-0.5)*(((x-m)/s)**2)
    b=1/(s*((2*3.14)**0.5))
    return b*math.exp(e)


def generator(t):
    global ins
    global f

    for i in range(t):
        ins.add(random.uniform(-10,10))
        
    f=list(ins)
    f.sort()
    # print("Sorted random values generated are : ", f)
    
    s = statistics.stdev(f)
    m = statistics.mean(f)
    for x in f:
        outs.append(evaluate(s,x,m))
    # print("Respective probability density values are : ", outs)
    df = pd.DataFrame(list(zip(f, outs)),
                      columns=['Value generated', 'Probability density values'])
    print(df)
    
    
def plotter():
    global f
    global outs
    
    plt.title("Gaussian curve")
    plt.xlabel("X values")
    plt.ylabel("values")
    plt.plot(f, outs, linestyle="-",color="b")
    plt.show()
    

if __name__=="__main__":
    t = int(input("Enter number of test cases(min 2) : "))
    _thread.start_new_thread(generator, (t,))
    _thread.start_new_thread(plotter, ())


"""
Explanation:
    evaluation: Evaluating probability density value for given x using the formula:
    
    generator: We generate t random numbers in domain (-10, 10), sort these values and
    find their probability density values.
    
    plotter: We plot the gaussian curve for given values.
    
    main: We start two threads to generate and evaluate the values and one for plotting
    the curve.

Observation:
    The more the number of test cases, the more smooth the curve becomes.
"""