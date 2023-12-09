import os, sys

import numpy as np
import pandas as pd

def load_excel(file):
    """
    Load file into 2 df's; metadata and predictions
    """
    # df is dict(sheet_name, sheet_data)
    df = pd.read_excel(file, sheet_name = None)

    sheets = list(df.keys())
    for sheet in sheets:
        df[sheet] = [df[sheet].iloc[:10], df[sheet].iloc[10:]]
    return sheets, df
