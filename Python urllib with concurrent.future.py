# -*- coding: utf-8 -*-
"""
Created on Wed May 26 10:09:39 2021

@author: Ishika
"""

"""
The concurrent.futures module provides a high-level interface for asynchronously executing callables.

The asynchronous execution can be performed with threads, using ThreadPoolExecutor, or separate processes, using ProcessPoolExecutor. Both implement the same interface, which is defined by the abstract Executor class.

In this article, we will see how to use urllib with threadpoolexecutor

Source Code: https://github.com/Ishikashah2510/cppsecrets_articles
"""


import concurrent.futures
import urllib.request

URLS = ['http://www.foxnews.com/',
        'http://www.cnn.com/',
        'http://europe.wsj.com/',
        'http://www.bbc.co.uk/',
        'http://some-made-up-domain.com/',
        'https://cppsecrets.com/']


def load_url(url, timeout):
    with urllib.request.urlopen(url, timeout=timeout) as conn:
        return conn.read()

def tpe_urllib():
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        future_to_url = {executor.submit(load_url, url, 60): url for url in URLS}
        for future in concurrent.futures.as_completed(future_to_url):
            url = future_to_url[future]
            try:
                data = future.result()
            except Exception as exc:
                print('%r generated an exception: %s' % (url, exc))
            else:
                print('%r page is %d bytes' % (url, len(data)))


if __name__ == "__main__":
    tpe_urllib()


"""
Explanation:
    we define a set of urls, and use threadpoolexecutor to load url and read the
    number of bytes or the error thrown, and then print it.
    
Observation:
    Here we see that even though the max_workers defined are 5, the program works
    for 6 links as well. That's because ThreadPoolExecutor reuses the threads which have
    completed their assigned task.
"""