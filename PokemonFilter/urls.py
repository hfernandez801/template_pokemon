# -*- coding: utf-8 -*-
from __future__ import unicode_literals

#Standar imports
#Related third party
from django.conf.urls import url, include
#Local imports


urlpatterns = [
    #path('admin/', admin.site.urls),
    url(r'^api/', include('api.urls')),
]
