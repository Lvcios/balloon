from django.conf.urls import patterns, include, url



# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'balloon.views.home', name='home'),
    # url(r'^balloon/', include('balloon.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    (r'^tweets/$', 'mexicosays.views.tweets'),
    (r'^carrusel/$', 'mexicosays.views.carrusel'),
    #(r'^mexicosays/$', 'mexicosays.views.tweets'),
    (r'^mexicosays/$', 'mexicosays.views.mexicosays'),
    (r'^mexicomustwatch/$', 'mexicomustwatch.views.mexicomustwatch'),
    
)
