from env import CyberSecurityEnv
from agent import Agent
import matplotlib.pyplot as plt

env = CyberSecurityEnv()
agent = Agent()

rewards = []

for episode in range(100):
    state = env.reset()
    total_reward = 0

    while True:
        action = agent.select_action(state)
        next_state, reward, done, _ = env.step(action)

        agent.store(state, action, reward, next_state, done)
        agent.train_step()

        state = next_state
        total_reward += reward

        if done:
            print(f"Episode {episode}, Reward: {total_reward}")
            rewards.append(total_reward)
            break

# Plot performance
plt.plot(rewards)
plt.xlabel("Episode")
plt.ylabel("Reward")
plt.title("Training Performance")
plt.show()