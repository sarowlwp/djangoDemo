'''
Created on Dec 18, 2012

@author: wenpingliu
'''
from books.models import *
#save example
#a = Auther.objects.create(first_name="sarow",last_name="lwp",email="sarowlwp@live.cn")
#a.save()

#list example
#a = Auther.objects.create(first_name="sarow1",last_name="lwp1",email="sarowlwp@live.cn")
#a.save()
#list = Auther.objects.all()
#print list

#filter example
#list = Auther.objects.filter(first_name="sarow")
#print list

#order limit example
list = Auther.objects.filter(first_name="sarow").order_by("id")
print list
#[0:5] is limit
list = Auther.objects.filter(first_name="sarow").order_by("-id")[0:5]
print list
count = Auther.objects.count()
print count
