import torch
import torch.nn as nn
import torch.optim as optim
import random
from collections import deque

class DQN(nn.Module):
    def __init__(self):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(3, 64),
            nn.ReLU(),
            nn.Linear(64, 4)
        )

    def forward(self, x):
        return self.net(x)

class Agent:
    def __init__(self):
        self.model = DQN()
        self.optimizer = optim.Adam(self.model.parameters(), lr=0.001)
        self.loss_fn = nn.MSELoss()

        self.memory = deque(maxlen=1000)
        self.epsilon = 1.0
        self.epsilon_decay = 0.995
        self.epsilon_min = 0.01

    def select_action(self, state):
        if random.random() < self.epsilon:
            return random.randint(0, 3)

        state = torch.FloatTensor(state)
        return torch.argmax(self.model(state)).item()

    def store(self, state, action, reward, next_state, done):
        self.memory.append((state, action, reward, next_state, done))

    def train_step(self):
        if len(self.memory) < 32:
            return

        batch = random.sample(self.memory, 32)

        for state, action, reward, next_state, done in batch:
            state = torch.FloatTensor(state)
            next_state = torch.FloatTensor(next_state)

            q_values = self.model(state)
            target = q_values.clone().detach()

            if done:
                target[action] = reward
            else:
                target[action] = reward + 0.99 * torch.max(self.model(next_state))

            loss = self.loss_fn(q_values, target)

            self.optimizer.zero_grad()
            loss.backward()
            self.optimizer.step()

        if self.epsilon > self.epsilon_min:
            self.epsilon *= self.epsilon_decay