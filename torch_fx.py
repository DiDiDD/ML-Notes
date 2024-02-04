import torch
from torch.fx import symbolic_trace
class MyModule(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.param = torch.nn.Parameter(torch.rand(3, 4))
        self.linear = torch.nn.Linear(4, 5)

    def forward(self, x):
        return self.linear(x + self.param)*13

module = MyModule()

# Symbolic tracing frontend - captures the semantics of the module
gm: torch.fx.GraphModule = symbolic_trace(module)

# High-level intermediate representation (IR) - Graph representation
print(gm.graph.print_tabular())

for fx_node in gm.graph.nodes:
    print(fx_node)
