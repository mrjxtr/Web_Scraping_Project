import os

import numpy as np
import pandas as pd
from utility.config import Encrypt

enc = Encrypt()

script_dir = os.path.dirname(__file__)
data_path = os.path.join(script_dir, "../data/raw/data_list.csv")

df = enc.read_csv(data_path)

data_cleaning = df.copy()
data_cleaning = data_cleaning.dropna()
data_cleaning = data_cleaning.drop_duplicates()
data_cleaning = data_cleaning[
    data_cleaning["URL"].str.contains(r"https://www.*ein", na=False)
]
data_cleaning = data_cleaning.sort_values(by="Charity Name")

df_cleaned = data_cleaning.copy()

export_path = os.path.join(script_dir, "../data/processed/cleaned_data_list.csv")
enc.to_csv(df_cleaned, export_path, index=False)
