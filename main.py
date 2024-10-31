import pandas as pd
import numpy as np
import openpyxl
import logging
from src.extract.extract_data import read_search_terms
from src.transform.transform_data import transform_search_keywords
from src.transform.transform_asin import transform_search_asins
from src.load.load_data_asin import load_data_asin
from src.load.load_data import load_data




def run_etl():

    logging.basicConfig(
        level=logging.INFO,
        filename="etl.log",
        filemode="w",
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

    file_path = "data/raw/bulk.xlsx"
    raw_data = read_search_terms(file_path)

    # Negative search  terms keywords
    transformed_data = transform_search_keywords(raw_data)
    keyword_data = load_data(transformed_data)

    # Negative search asins terms
    asins = transform_search_asins(raw_data)
    asins_data = load_data_asin(asins)

    return keyword_data, asins_data






if __name__ == '__main__':
    run_etl()


