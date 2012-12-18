'''
Created on 2012-12-17

@author: wenpingliu
'''
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.shortcuts import render_to_response
from books.models import Auther


def search_from(request):
    return render_to_response('search.html')

def search(request,template_name):
    
    # The following line will raise KeyError if 'q' hasn't
    # been submitted!  bad example
    # message = 'You searched for: %r' % request.GET['q']
    
    if 'q' in request.GET:
        qstr = request.GET['q']
        message =  'You searched for: %r' % qstr
        authers = Auther.objects.filter(first_name=qstr)
        for auther in authers:
            message += "<p>" + str(auther.id)
        return render_to_response('search_result.html',{'authers':authers})
        
        
    else:
        message = 'You submitted and empty form.'
        print message
        return render_to_response(template_name,{'error':True})
    #return render_to_response(message)


    
    
