from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    # Examples:
    # url(r'^$', 'AuraSoft.views.home', name='home'),
    # url(r'^AuraSoft/', include('AuraSoft.foo.urls')),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^/', include('aura.urls')),
    url(r'^$', 'aura.views.main'),
)
