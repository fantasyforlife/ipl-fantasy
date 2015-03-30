from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

import head2head.views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'iplh2h.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', head2head.views.index, name='index'),
    # url(r'^db', head2head.views.db, name='db'),
    url(r'^admin/', include(admin.site.urls)),
)
