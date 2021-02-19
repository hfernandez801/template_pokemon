# -*- coding: utf-8 -*-
from __future__ import unicode_literals

#Standar imports
#Related third party
from django.conf.urls import url
from django.urls import include
#Local imports
from api.views import pokemons_filter

urlpatterns = [
    url(r'^pokemons', pokemons_filter, name='api_pokemons_filter')
]
