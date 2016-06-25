from django.conf.urls import patterns, include, url
from django.contrib import admin
from seghack import settings

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'seghack.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^s/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_MEDIA}),
                       url(r'^', include('core.urls')),
                       )
