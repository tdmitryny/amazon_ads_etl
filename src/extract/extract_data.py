import pandas as pd
import numpy as np
import openpyxl
import logging
import warnings

warnings.filterwarnings('ignore', category=UserWarning, module='openpyxl')


def read_search_terms(file_path, sheet_name="SP Search Term Report"):
    """
    Extracting customer search
    """
    try:
        df = pd.read_excel(file_path, sheet_name=sheet_name)
        logging.info(f"Successfully read search data from {file_path}")
        return df
    except Exception as e:
        logging.error(f"Could read the file {str(e)}")
        raise