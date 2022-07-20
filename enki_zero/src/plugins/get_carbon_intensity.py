"""
Created by KenjiNezumi - 2022

Class to collect NationalGrid Carbon Intensity data.
"""
from commons.helpers import requests_data
import time, requests
import logging


class CarbonIntensity:
    def __init__(self,
                 from_date: str,
                 to_date: str,
                 postcode: str,
                 *args, **kwargs) -> None:
        """Init function

        :param from_date: start date
        :param to_date: end_date
        :param postcode: outward postcode
        """
        self.from_date = from_date
        self.to_date = to_date
        self.postcode = postcode


    def get_region_intensity(self) -> dict:
        headers = {
            'Accept': 'application/json'
        }

        r = requests.get('https://api.carbonintensity.org.uk/regional/intensity/{from}/{to}/postcode/{postcode}',
                         params={self.from_date, self.to_date, self.postcode},
                         headers=headers)
        return r.json

