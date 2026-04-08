import numpy as np

class CyberSecurityEnv:
    def __init__(self):
        self.state = None
        self.steps = 0

    def reset(self):
        self.state = np.random.rand(3)
        self.steps = 0
        return self.state

    def step(self, action):
        threat, health, traffic = self.state

        threat = np.clip(threat + np.random.uniform(-0.1, 0.2), 0, 1)
        traffic = np.clip(traffic + np.random.uniform(-0.1, 0.1), 0, 1)

        reward = 0

        if action == 1:
            reward = 1 if threat > 0.5 else -1
        elif action == 2:
            reward = 0.5
        elif action == 3:
            reward = 2 if threat > 0.5 else -0.5

        health = np.clip(health - threat * 0.1, 0, 1)

        self.state = np.array([threat, health, traffic])
        self.steps += 1

        done = self.steps >= 20 or health <= 0

        return self.state, reward, done, {}