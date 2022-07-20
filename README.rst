=========
enki_zero
=========


.. image:: https://img.shields.io/pypi/v/enki_zero.svg
        :target: https://pypi.python.org/pypi/enki_zero

.. image:: https://img.shields.io/travis/kenjinezumi/enki_zero.svg
        :target: https://travis-ci.com/kenjinezumi/enki_zero

.. image:: https://readthedocs.org/projects/enki-zero/badge/?version=latest
        :target: https://enki-zero.readthedocs.io/en/latest/?version=latest
        :alt: Documentation Status




Python library to fetch real estate property prices from Zoopla


* Free software: MIT license
* Documentation: https://enki-zero.readthedocs.io.


Features
--------

NOOA data:
NOOA type of datasets. NOOA provides different type of data. The full list is accessible via the request

https://www.ncei.noaa.gov/cdo-web/api/v2/datasets

List of available datasets:
Daily summaries: GHCND
Global summary of the month: GSOM
Global summary of the year: GSOY
Weather Radar (Level II): NEXRAD2
Weather Radar (Level III): NEXRAD3
Normals Annual/Seasonal: NORMAL_ANN
Normals Daily: NORMAL_DLY
Normals Hourly: NORMAL_HLY
Normals Monthly: NORMAL_MLY
Precipitation 15 Minute: PRECIP_15
Precipitation Hourly: PRECIP_HLY

NOOA type of location categories. NOOA provides different type of location parameter for the request, the list is
accessible via the URL

https://www.ncei.noaa.gov/cdo-web/api/v2/locationcategories

List of available parameters
City: CITY
Climate Divison: CLIM_DIV
Climate Region: CLIM_REG
Country: CNTRY
County: CNTY
Hydrologic Accounting Unit: HYD_ACC
Hydrologic Cataloging Unit: HYD_CAT
Hydrologic Region: HYD_REG
Hydrologic Subregion: HYD_SUB
State: ST
US Territory: US_TERR
Zip Code: ZIP
Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
