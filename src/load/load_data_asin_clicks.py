import pandas as pd
import numpy as np
import openpyxl
import logging
import warnings
from data.asin_sheet import asin_data
from datetime import datetime
import os


def load_data_asin_orders(data):
    """Create new DataFrame file with loaded negative keywords"""
    # Define the column mappings and values to assign
    try:
        logging.info("Getting ASINS data")
        df1 = pd.DataFrame(columns=asin_data)
        df1.columns = df1.columns.str.replace(" ", "_")

        column_mappings = {
            "Product": data["Product"],
            "Entity": "Negative Product Targeting",
            "Operation": "Create",
            "Campaign_ID": data["Campaign_ID"],
            "Ad_Group_ID": data["Ad_Group_ID"],
            "Keyword_ID": data["Keyword_ID"],
            "Product_Targeting_ID": data["Product_Targeting_ID"],
            "Campaign_Name_(Informational_only)": data["Campaign_Name_(Informational_only)"],
            "Ad_Group_Name_(Informational_only)": data["Ad_Group_Name_(Informational_only)"],
            "State": "enabled",
            "Product_Targeting_Expression": data['Customer_Search_Term'].apply(lambda x: f'asin="{x.upper()}"'),
            "Clicks": data["Clicks"].astype('int'),
            "Orders": data["Orders"],
            "ACOS": data["ACOS"]
        }

        # Drop duplicate rows based on 'Keyword_Text' if needed
        df1 = df1.drop_duplicates(subset=["Keyword_Text"])

        for column, value in column_mappings.items():
            df1[column] = value

        df1.columns = df1.columns.str.replace("_", " ")

        # Creating path to folder
        counter = 1
        current_date = datetime.now().strftime("%m-%d")
        folder_path = "data/processed/asins"
        os.makedirs(folder_path, exist_ok=True)
        file_name = f"search-negative-asin-orders-{current_date}.xlsx"
        file_path = os.path.join(folder_path, file_name)

        while os.path.exists(file_path):
            file_name = f"search-negative-asin-orders-{current_date}-v{counter}.xlsx"
            file_path = os.path.join(folder_path, file_name)
            counter += 1

        with pd.ExcelWriter(file_path) as writer:
            df1.to_excel(writer, sheet_name="negative-search", index=False)

        logging.info("Successfully received ASINS data")
    except Exception as e:
        logging.error(f"Couldn't transform the file {str(e)}")
        raise
