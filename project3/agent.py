import torch
import torch.nn as nn
import time
from typing import Tuple
from src import FEATURE_DIM, RADIUS, splev, N_CTPS, P, evaluate, compute_traj


global model


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


class Agent:
    def __init__(self) -> None:
        global model
        model = torch.load("project3/model.pth")
        """Initialize the agent, e.g., load the classifier model. """
        # TODO: prepare your agent here

    def get_action(self,
                   target_pos: torch.Tensor,
                   target_features: torch.Tensor,
                   class_scores: torch.Tensor,
                   ) -> Tuple[torch.Tensor, torch.Tensor]:
        starttime = time.time()
        """Compute the parameters required to fire a projectile. 
        
        Args:
            target_pos: x-y positions of shape `(N, 2)` where `N` is the number of targets. 
            target_features: features of shape `(N, d)`.
            class_scores: scores associated with each class of targets. `(K,)` where `K` is the number of classes.
        Return: Tensor of shape `(N_CTPS-2, 2)`
            the second to the second last control points
        """
        # print(len(target_pos))
        assert len(target_pos) == len(target_features)
        target_cls = torch.Tensor(len(target_pos))
        for i in range(len(target_features)):
            _, name = torch.max(model(target_features[i]).data, 0)
            target_cls[i] = name
            # print(name)
            # print(i)
        # TODO: compute the firing speed and angle that would give the best score.
        # Example: return a random configuration
        # print(target_cls)
        # print(class_scores)
        ctps_inter = torch.rand((N_CTPS - 2, 2)) * torch.tensor([N_CTPS - 2, 2.]) + torch.tensor([1., -1.])
        ans = ctps_inter
        maxnum = -1000
        while time.time() - starttime < 0.29:
            ctps_inter = torch.rand((N_CTPS - 2, 2)) * torch.tensor([N_CTPS - 2, 2.]) + torch.tensor([1., -1.])
            score = evaluate(compute_traj(ctps_inter), target_pos, class_scores[target_cls.long()], RADIUS)
            if score > maxnum:
                maxnum = score
                ans = ctps_inter
                # print(ans)
                # print(maxnum)
        return ans
