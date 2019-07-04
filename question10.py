# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 08:39:39 2018

@author: anna.aleshko
"""
import re

messages = {}

try:
    open_file = open('email.txt')

except:
    print ('Missing email.txt in current directory')

for line in open_file:

    if line.startswith('From '):
        email = re.findall(r'[\w\.-]+@[\w\.-]+', line)
        for i in email:
            if i in messages:
                messages[i]  +=1
            else:
                messages[i] = 1
    else:
        pass

asc_messages = sorted(messages.items(), key = lambda t:t[1], reverse=True)

print(asc_messages)

top = asc_messages[0]

print('The email with most messages \n', top[0] , ':', top[1])
