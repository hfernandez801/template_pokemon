# -*- coding: utf-8 -*-
from __future__ import unicode_literals

#Standar imports
#Related third party
from django.conf.urls import url, include
from django.views.static import serve
from django.conf import settings
from django.conf.urls.static import static
#Local imports


urlpatterns = [
    #path('admin/', admin.site.urls),
    url(r'^api/', include('api.urls')),

    # PRODUCTION LINUX ENVIRONMENT
    url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    #url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
]
