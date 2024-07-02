import torch
import torch.nn as nn
from _model_utils import count_parameters


class MyModel(nn.Module):
    def __init__(self,input_dim, hidden_dim, output_dim, num_layers):
        super(self).__init__()


    def forward(self, x):
        return x
    
    def print_parameters(self):
        count_parameters(self)


# if __name__ == "__main__":
#     model = LSTM(3, 100, 5, 1)
#
#     x = torch.randn(1, 10, 3)
#     output = model(x)
#     print(output.shape)


