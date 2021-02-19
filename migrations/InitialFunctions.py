# -*- coding: utf-8 -*-
from __future__ import unicode_literals

#Standar imports
import requests
import json
from os import path, makedirs

#Related third party
from django.conf import settings
import csv

#Local imports
from PokemonFilter.settings import POKEMON_URL_ENDOINT


class InitialFunctions:
    def __init__(self, type=5, slot=2):
        self.resources_folder = settings.RESOURCES
        self.type=type
        self.search_key='pokemon'

    def get_path_resources(self):
        return self.resources_folder


    def download_json_pokemon(self):
        """
        This method connects to pokemon api site and download pokemons with type ground or equal to type=5
        :return: None, just create a json file with pokemon information
        """
        url_query = "{}/type/{}".format(POKEMON_URL_ENDOINT, self.type)
        query_response = requests.get(url_query)

        if query_response.status_code == 200:
            _results = query_response.content#.decode()
            #_results = json.loads(_results)

            self.create_file_toserver(_results, "pokeGround.json")

    def filter_search_slot(self):
        """
        This method use a json file which contains pokemons information and filter all pokemons with slot = 2
        :return: None, Just create a CSV with name and pokemon url  wich slot = 2
        """
        source_path = path.join(settings.RESOURCES, "pokeGround.json")
        pokemons_info = dict()
        results = []

        with open(source_path, 'r', encoding='utf-8') as f:
            pokemons_info = json.load(f)

        #Filter slot, and create and csv
        if self.search_key in pokemons_info:
            list_items = pokemons_info[self.search_key]
            results = [ [item['pokemon']['name'],item['pokemon']['url']] for item in list_items if item['slot']==2 ]


        self.create_csv_toserver(results, "twoslotgroundpokemons.csv")



    def create_csv_toserver(self, results, file_name):
        full_url = path.join(settings.RESOURCES, file_name)

        try:
            with open(full_url, 'w', newline='') as file:
                writer = csv.writer(file)

                for item in results:
                    writer.writerow(item)
        except IOError as e:
            pass

        return full_url



    def create_file_toserver(self,memory_file, file_name):
        full_url = path.join(settings.RESOURCES, file_name)

        try:
            if not path.exists(settings.RESOURCES):
                makedirs(settings.RESOURCES)

            with open(full_url, 'wb+') as temp_file:
                temp_file.write(memory_file)
                temp_file.close()

        except IOError as e:
            pass

        return full_url



