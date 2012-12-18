'''
Created on 2012-12-17

@author: wenpingliu
'''
from django.http import HttpResponse,Http404
from django.shortcuts import render_to_response
from django.template.loader import get_template
from django.template import Context
import datetime

#first hello world
def hello(request):
    return HttpResponse("Hello world")

#set root page
def my_homepage_view(request):
    return HttpResponse("Home")

#dynamics page
def datetime_view(request):
    now = datetime.datetime.now();
    html = "<html><body>It is now %s. </body></html>" % now
    return HttpResponse(html)

#url param and template example
def hours_ahead(request,offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    now = datetime.datetime.now();
    result_time = now + datetime.timedelta(hours=offset)
    #old implement
    #html = "<html><body>It is now %s ,after %s hour , it will be %s. </body></html>" % (now,offset,result_time)
    #old template implement
    #template = get_template('current_datetime.html')
    #html = template.render(Context({'now':now,'offset':offset,'result_time':result_time}))
    # return HttpResponse(html)
    # locals() god like method, return all var in this method
    #return render_to_response('current_datetime.html',{'now':now,'offset':offset,'result_time':result_time})
    return render_to_response('current_datetime_e.html',locals())

#request test
def request_test(request):
    test = "Welcome to the page at %s" % request.path
    test += "<p> " + request.get_host()+"\n"
    test += "<p> " + request.get_full_path()+"\n"
    #test = test + " " + request.is_secure()
    print request.is_secure()
    #test = test + " " + request.META.get('HTTP_REFERER', 'unknown')
    #test = test + " " + request.META.get('HTTP_USER_AGENT', 'unknown')
    #recommed method to get meta info
    #test = test + " " + request.META.get('REMOTE_ADDR', 'unknown')
    metas = request.META.items()
    metas.sort()
    for k,v in metas:
        k = unicode(k)
        v = unicode(v)
        print k
        print v
        test += "<p> " + k + "/" + v +"\n"
    
    return HttpResponse(test)
    
    
