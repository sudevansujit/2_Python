# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 22:40:30 2020

@author: Sujit

Average Words Length

eg "Hello world welcome to Python"

"""

sent  = input("Enter your Sentence: ")

sent_length = len(sent.split())
word_length = [len(word) for word in sent.split()]
word_length
average = sum(word_length)/ sent_length
print(average)