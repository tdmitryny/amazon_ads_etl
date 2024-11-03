import pandas as pd
import numpy as np
import openpyxl
import logging
import warnings
import asyncio


def transform_add_keywords(keywordss):
    """
    Adding customer search keywords to negative list without ASINS
    and returning new Excel file
    """
    try:
        keywords.columns = keywords.columns.str.replace(' ', '_')
        set_dash = keywords.loc[(keywords['Clicks'] >= 5) & (keywords["ACOS"] <= 0.20) &
                                (keywords["ACOS"] > 0) &
                                (~keywords['Customer_Search_Term'].str.contains('b0')) &
                                (keywords["Campaign_Name_(Informational_only)"]).str.contains('Manual')]
        logging.info(f"Successfully transformed customer search to keywords")
        return set_dash
    except Exception as e:
        logging.error(f"Couldn't transform the file {str(e)}")
        raise


