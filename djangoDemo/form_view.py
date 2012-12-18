'''
Created on 2012-12-17

@author: wenpingliu
'''
from django.http import HttpResponse,Http404
from django.shortcuts import render_to_response


def search_from(request):
    return render_to_response('form/search.html')

'''
def search_from(request):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    return render_to_response('current_datetime_e.html',locals())
'''


    
    
