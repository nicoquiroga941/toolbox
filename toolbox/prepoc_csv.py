import numpy as np
import pandas as pd

def csv_to_df(csvfile):
    """ read your csv, convert it as a data frame, count your duplicates and show the info() and the describe()"""

    data = pd.read_csv()
    df = pd.DataFrame(data)

    duplicate_count = data.duplicated().sum()

    print(f'the file contein {duplicate_count} duplicates')

    return df
