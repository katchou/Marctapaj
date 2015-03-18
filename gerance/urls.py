from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gerance.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^marctapaj/', include('marctapaj.urls', namespace='marctapaj')),
    url(r'^admin/', include(admin.site.urls)),
)
