import pandas as pd
import numpy as np
import openpyxl
import logging
import warnings
import asyncio


def transform_search_keywords_orders(keywords):
    """
    Adding customer search keywords to negative list without ASINS
    and returning new excel file
    """

    try:
        keywords.columns = keywords.columns.str.replace(' ', '_')
        set_dash = keywords.loc[(keywords['Clicks'] >= 17) & (keywords["Orders"] <= 3) &
                            (keywords["ACOS"] >= 0.20) & (~keywords['Customer_Search_Term'].str.contains('b0'))]
        logging.info(f"Successfully transformed ASINS data")
        return set_dash
    except Exception as e:
        logging.error(f"Couldn't transform the file {str(e)}")
        raise
