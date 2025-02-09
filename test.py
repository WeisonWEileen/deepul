import torch

num_distribs = 4
plot_batch = torch.arange(20, device='cuda')
print(plot_batch)
    
for i in range(num_distribs):
        probabilities_dis[i] = pi[i] * (torch.exp((plot_batch[i] + 0.5 - u[i]) / s[i]) - torch.exp((plot_batch[i] - 0.5 - u[i]) / s[i]))
probabilities = torch.sum(probabilities_dis, dim=0)
    norm_pro = probabilities / torch.sum(probabilities)