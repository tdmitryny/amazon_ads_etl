import pandas as pd
import numpy as np
import openpyxl
import logging
import warnings
import asyncio


def transform_search_asins_orders(asin):
    """
    Adding customer search keywords to negative list without ASINS
    and returning new excel file
    """

    try:
        asin.columns = asin.columns.str.replace(' ', '_')
        set_dash = asin.loc[(asin['Clicks'] >= 17) & (asin["Orders"] <= 3) &
                            (asin["ACOS"] >= 0.20) & (asin['Customer_Search_Term'].str.contains('b0'))]
        logging.info(f"Successfully transformed ASINS data")
        return set_dash
    except Exception as e:
        logging.error(f"Couldn't transform the file {str(e)}")
        raise
