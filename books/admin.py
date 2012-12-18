'''
Created on 2012-12-18

@author: wenpingliu
'''
from django.contrib import admin
from books.models import Auther,Book,Publisher

#custom admin panel
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')
    #add search bar
    search_fields = ('first_name', 'last_name')

class BookAdmin(admin.ModelAdmin):
    #custom list display filed
    list_display = ('title', 'publisher', 'publication_date')
    list_filter = ('publication_date',)
    date_hierarchy = ('publication_date',)
    #set default sort
    ordering = ('-publication_date',)
    #custom form filed
    fields = ('title', 'authors', 'publisher', 'publication_date')
    #filter_horizontal = ('authors',)
#/////////////////////////////////////////////

admin.site.register(Auther,AuthorAdmin)
admin.site.register(Book)
admin.site.register(Publisher)
print "finish import admin models"