"""
Created by KenjiNezumi - 2022

Class to collect crime data from UK police.
https://data.police.uk/docs/method/crime-categories/
"""
from commons.helpers import requests_data
import requests
import time
import logging


class CrimeDataUK:
    def __init__(self,
                 lat:float,
                 long:float,
                 date:str=None,
                 crime_category:str="all-crime",
                 *args, **kwargs) -> None:
        """Init function.

        :param lat: latitude
        :param long: longitude
        :param date: date YYYY-MM
        :return none:

        """
        self.lat = lat,
        self.long = long,
        self.date = date,
        self.crime_category = crime_category



    def get_crime_data(self) -> dict:
        r = requests.get('https://data.police.uk/api/crimes-street/{crime_category}?lat={lat}&lng={long}&date={date}',
                         params={ self.crime_category, self.lat, self.long})
        return r.json

