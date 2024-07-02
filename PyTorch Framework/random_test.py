import pandas as pd
import numpy as np


def remove_high_zero_nan_columns(df, threshold=0.8):
    """
    Remove columns from the DataFrame if 80% or more of the column's values are 0 or NaN.

    Parameters:
    df (pd.DataFrame): The input DataFrame.
    threshold (float): The percentage threshold to remove columns. Default is 0.8.

    Returns:
    pd.DataFrame: The DataFrame with specified columns removed.
    """
    # Calculate the threshold value based on the number of rows
    threshold_value = threshold * len(df)

    # Iterate over columns and drop those that meet the condition
    columns_to_drop = []
    for column in df.columns:
        zero_nan_count = (df[column] == 0).sum() + df[column].isna().sum()
        if zero_nan_count >= threshold_value:
            columns_to_drop.append(column)

    return df.drop(columns=columns_to_drop)


# Example usage
data = {
    'A': [0, 0, 0, 0, 0],
    'B': [1, np.nan, 3, np.nan, 5],
    'C': [np.nan, np.nan, np.nan, np.nan, np.nan],
    'D': [0, 0, 2, 3, 4]
}

df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

df_cleaned = remove_high_zero_nan_columns(df)
print("\nDataFrame after removing columns with 80% or more 0 or NaN values:")
print(df_cleaned)
