import pandas as pd
import numpy as np
import openpyxl
import logging
import warnings


def transform_search_keywords(keywords):
    """
    Adding customer search keywords to negative list without ASINS
    and returning new excel file
    """
    try:
        keywords.columns = keywords.columns.str.replace(' ', '_')
        set_dash = keywords.loc[(keywords['Clicks'] >= 10) & (keywords["Orders"] == 0) &
                                (~keywords['Customer_Search_Term'].str.contains('b0'))]
        logging.info(f"Successfully transformed data from {keywords}")
        return set_dash
    except Exception as e:
        logging.error(f"Couldn't transform the file {str(e)}")
        raise
