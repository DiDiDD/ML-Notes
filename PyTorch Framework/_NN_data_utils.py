import pandas as pd
import torch
from torch.utils.data import Dataset, DataLoader


class MyDataset(Dataset):
    def __init__(self, df):
        self.df = df


    def __len__(self):
        return 

    def __getitem__(self, idx):
        return 


def split_dataframe(df, percentage_list: list[float], previous_window_size):
    assert sum(percentage_list) == 1, '3 Split percentage should sum up to 1'
    assert 0 not in percentage_list, 'No split should be zero'

    train_df_end = int(percentage_list[0] * len(df))
    val_df_end = int(sum(percentage_list[0:2]) * len(df))

    train_df = df.iloc[:train_df_end]
    val_df = df.iloc[train_df_end-previous_window_size: val_df_end]
    test_df = df.iloc[val_df_end-previous_window_size:]

    return train_df, val_df, test_df
