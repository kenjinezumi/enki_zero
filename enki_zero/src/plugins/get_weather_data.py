"""
Created by KenjiNezumi - 2022

Class to collect NOOA data.
"""
from commons.helpers import requests_data
import requests
import time
import logging


class NooaWeatherData:
    def __init__(self,
                 *args, **kwargs) -> None:
        """Init function.
        :return none:

        """

    def get_all_stations(self):
        """Get the list of all stations with the parameter ALL."""

        url_request = f"https://www.ncei.noaa.gov/cdo-web/api/v2/stations?datatypeid=ALL"
        res = requests_data(url_request)
        return res

    def get_all_data_types(self):
        """For reference only, get the types of data."""

        url_request = f"https://www.ncei.noaa.gov/cdo-web/api/v2/datatypes"
        res = requests_data(url_request)
        return res

    def get_all_dataset_types(self):
        """For reference only, get the types of datasets."""
        """
        :return: a dictionary with the list of datasets. 
        """
        url_request = f"https://www.ncei.noaa.gov/cdo-web/api/v2/datasets"
        res = requests_data(url_request)
        return res

    def get_all_location_categories(self):
        url_request = f"https://www.ncei.noaa.gov/cdo-web/api/v2/locationcategories"
        res = requests_data(url_request)
        return res