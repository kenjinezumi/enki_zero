"""
Created by KenjiNezumi - 2022

Class to collect Zoopla data.
The Zoopla API can be used to:
1)Provide contextual local data on average current property values or average sold prices by property type.
2)Show listing for sale, rent properties on maps, including supporting descriptions, images and agent contact details.
3)Display graphs showing local property value and data tremnds.
"""
import requests

class RealEstatePrices:

    def __init__(self,
                 area: str,
                 street: str=None,
                 town: str=None,
                 postcode: str=None,
                 county: str=None,
                 latitude: str=None,
                 longitude: str=None,
                 lat_min: str=None,
                 lat_max: str=None,
                 lon_min: str=None,
                 lon_max: str=None,
                 output_type: str=None,
                 *args, **kwargs) -> None:
        """Init function.

        :param area: Arbitrary area name, or postcode.
        :param street: Name of street to locate.
        :param town: Name of a town to locate.
        :param postcode: Full or partial postcode.
        :param county: The name of a county.
        :param country: The name of a country.
        :param latitude: Exact latitude of a location, must be
        used in conjunction with longitude and will take
        priority over other parameters specified. Valid values are in the interval [-90,90].
        :param longitude: location of the real estate asset to query.
        :param lat_min: location of the real estate asset to query.
        :param lat_max: location of the real estate asset to query.
        :param lon_min: location of the real estate asset to query.
        :param lon_max: location of the real estate asset to query.
        :return none:

        """
        def  __init__(self):
           self.area= area,
           self.street= street,
           self.town = town,
           self.postcode = postcode,
           self.county = county,
           self.latitude = latitude,
           self.longitude = longitude,
           self.postcode = postcode,
           self.county = county,
           self.latitude = latitude,
           self.longitude = longitude,
           self.lat_min = lat_min,
           self.lon_min = lon_min,
           self.lon_max = lon_max,
           self.lat_min = lat_min,
           self.lat_max = lat_max,
           self.output_type = output_type

        def get_real_estate_prices(self):

