import pandas as pd
import numpy as np
import openpyxl
import logging


# Define the file path with a different name
file_path = "../data/raw/bulk.xlsx"


# Define the function for Search Terms
def exract_data(file_path, sheet_name="SP Search Term Report"):
    xls = pd.read_excel(file_path, sheet_name=sheet_name)
    return xls


# Call the function with the file path
extracted = exract_data(file_path)


