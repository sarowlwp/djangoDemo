from django.conf.urls import patterns, include, url
from djangoDemo.views import hello,my_homepage_view,datetime_view,hours_ahead
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'djangoDemo.views.home', name='home'),
    # url(r'^djangoDemo/', include('djangoDemo.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

        ('^hello/$', hello),
        ('^$',my_homepage_view),
        ('^datetime/$', datetime_view),
        (r'^time/plus/(\d{1,2})/$', hours_ahead),
)
