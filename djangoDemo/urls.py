from django.conf.urls import patterns, include, url
from django.conf.urls.defaults import *
from djangoDemo import views
from django.contrib import admin
from books.views import search_from,search
from django.conf import settings
from books import models
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('djangoDemo.views',
    # Examples:
    # url(r'^$', 'djangoDemo.views.home', name='home'),
    # url(r'^djangoDemo/', include('djangoDemo.foo.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
        #('^hello/$', hello),
        #('^requesttest/$', request_test),
        #('^$',my_homepage_view),
        #('^datetime/$', datetime_view),
        #(r'^time/plus/(\d{1,2})/$', hours_ahead),
        #(r'^search-form/$', search_from),
        #(r'^search-test/$', search),
        ('^hello/$', 'hello'),
        ('^requesttest/$', 'request_test'),
        ('^$','my_homepage_view'),
        ('^datetime/$', 'datetime_view'),
        #(r'^time/plus/(\d{1,2})/$', 'hours_ahead'),

)

urlpatterns += patterns('books.views',
        (r'^search-form/$', 'search_from'),
)

#debug model
if settings.DEBUG:
    urlpatterns += patterns('',
        #(r'^debuginfo/$', ''),
    )
    
#user param name replace pos
urlpatterns += patterns('djangoDemo.views',
    (r'^time/plus/(?P<offset>\d{1,2})/$', 'hours_ahead'),
    (r'^method_splitter/(?P<testparam1>\d{1,2})/(?P<testparam2>\d{1,2})/(\d{1,2})/$','method_splitter', {'GET': views.get_view, 'POST': views.post_view}),
    
    #(r'^time/plus/(\d{1,2})/$', 'hours_ahead'),
    #(r'^articles/(?P<year>\d{4})/$', ''),
    #(r'^articles/(?P<year>\d{4})/(?P<month>\d{2})/$', ''),
)

#set param in urlconf
urlpatterns += patterns('books.views',
        (r'^search-test/$', 'search',{'template_name':'search.html'}),
)

urlpatterns += patterns('common.views',
    (r'^auther/list/$', 'object_list',{'model': models.Auther,'template_name':'auther_list.html'}),
    (r'^book/list/$','object_list', {'model': models.Book,'template_name':'book_list.html'}),
)

