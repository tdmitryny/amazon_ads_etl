import pandas as pd
import numpy as np
import openpyxl
import logging
from src.extract.extract_data import read_search_terms
from src.transform.transform_data import transform_search_keywords
from src.load.load_data import load_data


def run_etl():
    file_path = "data/raw/bulk.xlsx"
    raw_data = read_search_terms(file_path)
    transformed_data = transform_search_keywords(raw_data)
    newe_date = load_data(transformed_data)

    return newe_date






if __name__ == '__main__':
    run_etl()


