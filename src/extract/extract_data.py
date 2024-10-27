import pandas as pd
import numpy as np
import openpyxl
import logging
import warnings

warnings.filterwarnings('ignore', category=UserWarning, module='openpyxl')

file_path = "../../data/raw/bulk.xlsx"


def read_search_terms(file_path, sheet_name="SP Search Term Report"):
    """
    Extract Search terms for campaing
    """
    try:
        df = pd.read_excel(file_path, sheet_name=sheet_name)
        logging.info(f"Succefully read search data from { file_path }")
        return df
    except Exception as e:
        logging.error(f"Could read the file {str(e)}")
        raise


def main():
    try:
        file_path = "../../data/raw/bulk.xlsx"
        search_terms = read_search_terms(file_path)
        return search_terms

    except Exception as e:
        logging.error(f"Extraction process failed {str(e)}")
    raise




if __name__ == '__main__':
    test = main()
    print(test)

