from env import CyberSecurityEnv
from agent import Agent
from grader import CyberGrader

env = CyberSecurityEnv()
agent = Agent()
grader = CyberGrader()

state, _ = env.reset()
trajectory = []

while True:
    action = agent.select_action(state)
    next_state, reward, terminated, truncated, _ = env.step(action)
    done = terminated or truncated

    trajectory.append((state, action, reward))
    state = next_state

    if done:
        break

score = grader.grade(trajectory)

print("Final Score:", score)
