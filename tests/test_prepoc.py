from toolbox.prepoc_csv import csv_to_df
import pandas as pd

def check_for_df():
    isinstance(csv_to_df(), pd.DataFrame)
