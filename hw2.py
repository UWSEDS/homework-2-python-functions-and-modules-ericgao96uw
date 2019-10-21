import numpy as np
import pandas as pd
import subprocess as sp

def readDF(URL):
    sp.call(["curl", "-o", "pronto.csv", URL], shell=True)
    df = pd.read_csv('pronto.csv')
    return df

def test_create_dataframe(df, names_list):
    if (df.columns.tolist() != names_list):
        return False
    type_list = df.dtype.tolist()
    for i in range(len(type_list)):
        if (type_list[i] != type_list[0]):
            return False
    if (df.shape[0] < 10):
        return False
    return True