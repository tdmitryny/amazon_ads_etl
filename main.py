import pandas as pd
import numpy as np
import openpyxl
import time
import logging
from src.extract.extract_data import read_search_terms
from src.transform.transform_data import transform_search_keywords
from src.transform.transform_asin import transform_search_asins
from src.transform.transform_asin_clicks import transform_search_asins_orders
from src.transform.transform_add_keywords import transform_add_keywords
from src.transform.transform_data_keywords import transform_search_keywords_orders
from src.load.load_add_keywords import load_data_keywords
from src.load.load_data_keywords_clicks import load_data_keywords_orders
from src.load.load_data_asin_clicks import load_data_asin_orders
from src.load.load_data_asin import load_data_asin
from src.load.load_data import load_data

start = time.perf_counter()


def run_etl():
    logging.basicConfig(
        level=logging.INFO,
        # filename="etl.log",
        # filemode="w",
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

    logging.info("Starting optimization")

    file_path = "data/raw/bulk.xlsx"
    raw_data = read_search_terms(file_path)

    # Negative search terms keywords
    transformed_data = transform_search_keywords(raw_data)
    keyword_data = load_data(transformed_data)

    # Negative search asins terms
    asins = transform_search_asins(raw_data)
    asins_data = load_data_asin(asins)

    # Negative search terms asins <= 1 orders
    transformed_data_clicks = transform_search_asins_orders(raw_data)
    asins_data_clicks = load_data_asin_orders(transformed_data_clicks)

    # Negative search keywords terms
    keywords_clicks = transform_search_keywords_orders(raw_data)
    keyword_data_clicks = load_data_keywords_orders(keywords_clicks)

    # Add new keywords
    adding_transform_keywords = transform_add_keywords(raw_data)
    adding_keywords = load_data_keywords(adding_transform_keywords)

    return keyword_data, asins_data, asins_data_clicks, keyword_data_clicks, adding_keywords


if __name__ == '__main__':
    run_etl()
    end = time.perf_counter()
    print(f"It took{end - start: .2f}s")
