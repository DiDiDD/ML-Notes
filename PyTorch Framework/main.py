import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.utils.data import DataLoader
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


from argparse_setup import parse_args
from _NN_data_utils import MyBTCDataset, split_dataframe
from _train import train_model
from _test import test_model


def main():
    # retrieve arguments from argparser
    args = parse_args()
    model_name = args.model_name
    input_dim = args.input_dim
    hidden_dim = args.hidden_dim
    output_dim = args.output_dim
    num_layers = args.num_layers
    if_train = args.if_train
    best_ckpt_path = args.best_ckpt_path
    final_ckpt_path = args.final_ckpt_path
    previous_window_size = 24
    lr = 0.0005
    train_epochs = args.num_epochs


if __name__ == "__main__":
    main()