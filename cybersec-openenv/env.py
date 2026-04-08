import numpy as np

class CyberSecurityEnv:
    def __init__(self):
        self.state = None
        self.steps = 0

        # Define observation space manually (important for OpenEnv)
        self.observation_shape = (3,)
        self.action_space_n = 4

    def reset(self):
        self.steps = 0

        # FIX: ensure correct dtype + shape
        self.state = np.array(
            np.random.rand(3),
            dtype=np.float32
        )

        return self.state

    def step(self, action):
        assert 0 <= action < self.action_space_n, "Invalid action"

        threat, health, traffic = self.state

        threat = np.clip(threat + np.random.uniform(-0.1, 0.2), 0, 1)
        traffic = np.clip(traffic + np.random.uniform(-0.1, 0.1), 0, 1)

        reward = 0.0

        if action == 1:
            reward = 1.0 if threat > 0.5 else -1.0
        elif action == 2:
            reward = 0.5
        elif action == 3:
            reward = 2.0 if threat > 0.5 else -0.5

        health = np.clip(health - threat * 0.1, 0, 1)

        self.state = np.array([threat, health, traffic], dtype=np.float32)
        self.steps += 1

        done = bool(self.steps >= 20 or health <= 0)

        return self.state, float(reward), done, {}
