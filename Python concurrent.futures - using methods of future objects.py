# -*- coding: utf-8 -*-
"""
Created on Thu May 27 11:49:23 2021

@author: Ishika
"""

"""
The concurrent.futures module provides a high-level interface for asynchronously executing callables.

The asynchronous execution can be performed with threads, using ThreadPoolExecutor, or separate processes, using ProcessPoolExecutor. Both implement the same interface, which is defined by the abstract Executor class.

In this article, we will see the methods of future objects(the outputs returned by a
 threadpoolexecutor.submit() call).

Source Code: https://github.com/Ishikashah2510/cppsecrets_articles
"""

import concurrent.futures as cf
import urllib.request


def cube_calc(x):
    return x**3


def check(res):
    if res.cancel():
        print("Cancelled")
    else:
        print("Not able to cancel since call being executed")
    if res.cancelled():
        print("Cancelled checking with cancelled")
    else:
        print("Not cancelled yet")
    if res.done():
        print("Done")
    else:
        print("Not done yet")


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
    with cf.ThreadPoolExecutor(max_workers=5) as executor:
        future_to_url = {}
        for url in URLS:
            res = executor.submit(load_url, url, 60)
            check(res)
            future_to_url[res] = url
        # future_to_url = {executor.submit(load_url, url, 60): url for url in URLS}
        for future in cf.as_completed(future_to_url):
            
            url = future_to_url[future]
            try:
                data = future.result()
            except Exception as exc:
                print('%r generated an exception: %s' % (url, exc))
            else:
                print('%r page is %d bytes' % (url, len(data)))


if __name__ == "__main__":
    nums = list(range(1, 10))
    with cf.ThreadPoolExecutor() as tpe:
        for i in nums:
            res = tpe.submit(cube_calc, i)
            print("Result is : ", res.result())
            check(res)
    tpe_urllib()


"""
Explanation:
    We have taken a small function which calculates the cube of a given number, intially.
    We see how the object reacts with the cancel(), cancelled() and done() method.
    Next we have checked the same with urllib.requests.
"""