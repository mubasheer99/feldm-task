#  File        : currencyconverter.py
#  Project     : FELDM
#  Author      : MM
#  Description : Generic Module to convert currency
######################################################################
#  Changelog :
#  23.04.2022   MM  : initial definition of  currencyconverter file
############################################################################


from urllib.request import urlopen
import pandas as pd
import pandas_read_xml as pdx
from pandas_read_xml import flatten, fully_flatten, auto_separate_tables


def get_latest_conversion(url, xpath_var, curr):
    """
        Get the latest currency information from ECB
        :param url: URL  of the ECB XML
        :param xpath_var:xpath variable
        :param curr:currency for which rate is needed
        :return: returns the current currency rate for the given currency
    """

    df = pd.read_xml(urlopen(url), xpath=xpath_var)
    result = (df[df.currency == curr]['rate'])

    return round(1/float(result.to_string(index=False)), 4)


def get_historical_conversion(path, xpath_root, curr):
    """
        Get the historical currency information from the xml provided
        :param path: path  of the ECB XML
        :param xpath_root:xpath variable
        :param curr:currency for which rate is needed
        :return: returns the dataframe of currency rate for the given currency
        """

    df = pdx.read_xml(path, xpath_root)
    df = df.pipe(flatten)
    df = df.pipe(flatten)
    df = df.pipe(flatten)
    df = df.pipe(flatten)
    df.columns = ['date', 'currency', 'rate']
    df['date'] = pd.to_datetime(df['date'], format="%Y-%m-%d")
    df['rate'] = df['rate'].astype(float)
    result = (df[df.currency == curr])
    return result

    # return round(1/float(result.to_string(index=False)), 4)













