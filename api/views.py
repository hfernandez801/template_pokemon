# -*- coding: utf-8 -*-
from __future__ import unicode_literals

#Standar imports
from os import path

#Related third party
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.conf import settings
import csv


@api_view(['GET'])
def pokemons_filter(request):
    """
    This webservice allows to search a filter keyword in pokemon name. Remember the CSV file only contains pokemons with slot = 2

    :param request: filter keyword

    :return: List pokemons in slot = 2  which matches name
    """
    source_path = path.join(settings.RESOURCES, "twoslotgroundpokemons.csv")
    context = []

    if request.method == 'GET':
        _filter_param = request.GET.get('filter', None)

        if _filter_param is not None and _filter_param!='':
            search_filter = _filter_param.upper()
            #Read file CSV and conver into JSON.
            with open(source_path, mode='r') as file:
                content = csv.reader(file)

                for row in content:
                    if search_filter in row[0].upper():
                        context.append(row[0])


        return Response(context, status=status.HTTP_200_OK)

    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

