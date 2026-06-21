
import torch
import torch.nn as nn
import torch.nn.functional as F


class DiffusionGenerator(nn.Module):
    def __init__(self, hidden_dim=64, timesteps=5):
        super().__init__()

        self.timesteps = timesteps

        self.noise_predictor = nn.Sequential(
            nn.Linear(hidden_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, hidden_dim)
        )
        self.edge_predictor = nn.Sequential(
            nn.Linear(hidden_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, 1)
        )

    def forward_diffusion(self, x):
        noise = torch.randn_like(x)
        x_noisy = x + 0.1 * noise
        return x_noisy, noise

    def reverse_diffusion(self, x):
        for _ in range(self.timesteps):
            pred_noise = self.noise_predictor(x)
            x = x - 0.1 * pred_noise
        return x

    def generate(self, node_emb, edge_emb):

        node_noisy, noise1 = self.forward_diffusion(node_emb)
        edge_noisy, noise2 = self.forward_diffusion(edge_emb)

        node_gen = self.reverse_diffusion(node_noisy)
        edge_gen = self.reverse_diffusion(edge_noisy)

        loss = (
            F.mse_loss(node_gen, node_emb) +
            F.mse_loss(edge_gen, edge_emb)
        )

        return loss, node_gen, edge_gen
    def generate_edge_prob(self, src_emb, dst_emb):

        edge_feat = src_emb * dst_emb

        score = self.edge_predictor(edge_feat)

        prob = torch.cat(
            [-score, score],
            dim=1
        )

        edge_weight = F.gumbel_softmax(
            prob,
            tau=1.0,
            hard=True
        )

        keep_prob = edge_weight[:,1]

        return keep_prob
