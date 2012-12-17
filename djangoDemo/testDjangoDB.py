'''
Created on 2012-12-17

@author: wenpingliu
'''
from django.db import connection
cursor = connection.cursor()
print cursor