# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 16:55:14 2021

@author: Ishika
"""

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import re
import getpass
import time
import sys
import random


class FBPost:
    
    def __init__(self):
        self.checkout()
        linkedin_cred = open('fb_credentials.txt', 'r')
        details = linkedin_cred.readlines()
        linkedin_cred.close()
        self.email_ = details[0].strip()
        self.pass_ = details[1].strip()
        
    
    def checkout(self):
        try:
            linkedin_cred = open('fb_credentials.txt', 'r')
            linkedin_cred.close()
        except:
            regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
            while True:
                email_ = input("Enter Facebook email ID please : ")
                if (re.search(regex, email_)):
                    break
                else:
                    print("Enter a valid email please")
            pass_ = getpass.getpass()
            
            linkedin_credw = open('fb_credentials.txt', 'w')
            linkedin_credw.write(email_)
            linkedin_credw.write('\n')
            linkedin_credw.write(pass_)
            linkedin_credw.write('\n')
            
            linkedin_credw.close()
    
    
    def setup(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--window-size=1036, 674')  
        # chrome_options.add_argument('--headless')
        chrome_options.add_argument("--log-level=3")
        chrome_options.add_experimental_option("prefs", {
        "profile.default_content_setting_values.notifications": 1
        })
        
        self.browser = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=chrome_options, )
        self.browser.get('https://www.facebook.com/')
        
        time.sleep(2)
        email = self.browser.find_element_by_id('email')
        email.send_keys(self.email_)
        
        time.sleep(2)
        password = self.browser.find_element_by_id('pass')
        password.send_keys(self.pass_)
        
        time.sleep(2)
        submit_button = self.browser.find_element_by_name('login')
        submit_button.click()
        time.sleep(2)
        pagename = 'Your page name'
        self.browser.get('https://www.facebook.com/' + pagename)
    
    
    def post_on_facebook(self, group_url):
        print('Posting  on Facebook group: ', group_url)
        
        
        time.sleep(4)
        self.browser.get(group_url)
        time.sleep(2)
        
        
        text_to_post = 'The text you wish to psot goes here'
        
        try:
            post_class = 'oajrlxb2 b3i9ofy5 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 j83agx80 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x cxgpxx05 d1544ag0 sj5x9vvc tw6a2znq i1ao9s8h esuyzwwr f1sip0of lzcic4wl l9j0dhe7 abiwlrkh p8dawk7l bp9cbjyn orhb3f3m czkt41v7 fmqxjp7s emzo65vh btwxx1t3 buofh1pr idiwt2bm jifvfom9 kbf60n1y'
            post_class = post_class.replace(' ', '.')
            click_post = self.browser.find_element_by_class_name(post_class)
            click_post.click()
            time.sleep(5)
            
            
            post_content = self.browser.find_element_by_class_name('notranslate._5rpu')
            post_content = self.browser.switch_to_active_element()
            post_content.send_keys(text_to_post)
            time.sleep(5)
            
            soup = BeautifulSoup(self.browser.page_source, 'html.parser')
            all_pc = soup.find_all('div', attrs={'id': re.compile("^mount_0_0_")})
            id_ = str(all_pc[0].get('id'))
            xpath = '//*[@id="' + id_ + '"]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div[1]/form/div/div[1]/div/div/div[1]/div/div[3]/div[2]/div[1]/div'
            post = self.browser.find_element_by_xpath(xpath)
            post.click()
            time.sleep(5)
            
        except:

            print("Something went wrong, exiting script to avoid conflicts")
            sys.exit()

    
    def close_browser(self):
        self.browser.close()


fb = FBPost()
fb.setup()

groups = ['group id here']

for group in groups:
    group_url = 'https://www.facebook.com/groups/' + group
    fb.post_on_facebook(group_url)
fb.close_browser()
