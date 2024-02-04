import torch
import torchvision
import torch.nn as nn
import tqdm
from prettytable import PrettyTable

class res_block(nn.Module):
    def __init__(self, in_ch, out_ch ):
        super().__init__()
        self.conv1 = nn.Conv2d(in_channels=in_ch, out_channels=out_ch,kernel_size=3)
        self.relu1 = nn.ReLU()
        self.conv2 = nn.Conv2d(in_channels=out_ch, out_channels=out_ch,kernel_size=3)
        self.relu2 = nn.ReLU()

    def forward(self, input):
        out = self.conv1(input)
        out = self.relu1(out)
        out = self.conv2(out)
        out = self.relu2(out)

        return out


x = torch.rand((3,3,12,12)).to('mps')
model = res_block(in_ch=3,out_ch=12).to('mps')
y = model(x)

def count_parameters(model):
    table = PrettyTable(["Modules", "Parameters"])
    total_params = 0
    for name, parameter in model.named_parameters():
        if not parameter.requires_grad:
            continue
        param = parameter.numel()
        table.add_row([name, param])
        total_params+=param
    print(table)
    print(f"Total Trainable Params: {total_params}")
    return total_params

count_parameters(model)
