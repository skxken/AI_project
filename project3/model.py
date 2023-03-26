import torch


class Model(torch.nn.Module):

    def __init__(self, num_i, num_h, num_o, num_p):
        super(Model, self).__init__()

        self.linear1 = torch.nn.Linear(num_i, num_h)
        self.relu = torch.nn.ReLU()
        self.linear3 = torch.nn.Linear(num_h, num_o)
        self.linear5 = torch.nn.Linear(num_o, num_p)

    def forward(self, x):
        x = self.linear1(x)
        x = self.relu(x)
        x = self.linear3(x)
        x = self.relu(x)
        x = self.linear5(x)

        return x
