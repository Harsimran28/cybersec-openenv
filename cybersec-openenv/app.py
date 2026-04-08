import streamlit as st
from env import CyberSecurityEnv
from agent import Agent

st.set_page_config(page_title="Cyber RL", layout="centered")

st.title("CyberSecurity RL Simulator")

env = CyberSecurityEnv()
agent = Agent()

if st.button("Run Simulation"):
    state, _ = env.reset()
    total_reward = 0

    for step in range(20):
        action = agent.select_action(state)

        next_state, reward, terminated, truncated, _ = env.step(action)
        done = terminated or truncated

        st.write(f"Step {step}")
        st.write(f"State: {state}")
        st.write(f"Action: {action}")
        st.write(f"Reward: {reward}")
        st.write("---")

        state = next_state
        total_reward += reward

        if done:
            break

    st.success(f"Final Reward: {total_reward}")
