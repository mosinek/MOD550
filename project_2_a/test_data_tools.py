"""
This file contains a function that corrupt data.
"""
import numpy as np

def corrupt_data(df):
    """
    This function takes dataframe as an argument and corrupt it, by
    inserting NaN values, a duplicate, an impossible value and dropping a column.
    """
    df_corrupted = df.copy()

    df_corrupted.mask(np.random.rand(*df_corrupted.shape) < 0.01, np.nan, inplace=True)

    cols = ["Humidity", "Wind speed", "Average rainfall"]
    df_corrupted[cols] = df_corrupted[cols].mask(np.random.rand(
        len(df_corrupted), len(cols)) < 0.05, -df_corrupted[cols])

    # duplicate should be at the end of transformation (beside drop),
    # so that we don't accidentally make it unique
    df_corrupted.loc[len(df_corrupted)] = df_corrupted.loc[100]

    #df_corrupted.drop(columns=np.random.choice(df_corrupted.columns), inplace=True)
    df_corrupted.drop(columns='Air pressure', inplace=True)

    return df_corrupted
