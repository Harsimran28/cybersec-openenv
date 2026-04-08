import streamlit as st
from env import CyberSecurityEnv
from agent import Agent

st.title("🛡️ CyberSecurity RL Simulator")

env = CyberSecurityEnv()
agent = Agent()

if st.button("Run Simulation"):
    state = env.reset()
    total_reward = 0

    for step in range(20):
        action = agent.select_action(state)
        state, reward, done, _ = env.step(action)

        st.write(f"Step {step}")
        st.write(f"State: {state}")
        st.write(f"Action: {action}")
        st.write(f"Reward: {reward}")
        st.write("---")

        total_reward += reward

        if done:
            break

    st.success(f"Final Reward: {total_reward}")