import numpy as np

class CyberSecurityEnv:
    def __init__(self):
        self.state = None
        self.steps = 0

        self.max_steps = 20
        self.action_space_n = 4
        self.observation_shape = (3,)

    def reset(self, seed=None, options=None):
        if seed is not None:
            np.random.seed(seed)

        self.steps = 0
        self.state = np.array(np.random.rand(3), dtype=np.float32)

        # IMPORTANT: return (obs, info)
        return self.state, {}

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

        terminated = bool(health <= 0)
        truncated = bool(self.steps >= self.max_steps)

        # IMPORTANT: return 5 values
        return self.state, float(reward), terminated, truncated, {}
