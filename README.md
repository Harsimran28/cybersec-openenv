# CyberSecurity RL Agent (OpenEnv Style)

## Overview

This project presents a Reinforcement Learning-based Cybersecurity Simulation where an intelligent agent learns to defend a system against dynamic threats.

The agent continuously observes the environment (threat level, system health, network traffic) and takes optimal actions such as blocking malicious activity, scanning systems, or shutting down compromised nodes.

The system is designed using an OpenEnv-style modular architecture, enabling structured evaluation, scalability, and reproducibility.

---

## Key Features

* DQN-based RL Agent using Deep Q-Networks
* Experience Replay and Epsilon Decay for stable learning
* Cybersecurity Simulation Environment

  * Threat detection
  * System health management
  * Dynamic traffic conditions
* Training Visualization (Reward vs Episode graph)
* Automated Grader System

  * Evaluates performance based on:

    * Total reward
    * System health
    * Survival duration
* Interactive Streamlit UI

  * Real-time simulation
  * Step-by-step agent decisions
* Modular OpenEnv-style Design

  * Environment
  * Task
  * Grader
  * Agent

---

## Tech Stack

* Python 3.12
* PyTorch (Deep Learning and RL model)
* NumPy (Numerical computations)
* Matplotlib (Training visualization)
* Streamlit (Interactive UI)

---

## How to Run

### 1. Clone Repository

```bash
git clone YOUR_REPO_LINK
cd cybersec-rl-openenv
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Train the RL Agent

```bash
python train.py
```

Outputs:

* Episode-wise rewards
* Training graph (learning curve)

---

### 4. Evaluate Performance

```bash
python evaluate.py
```

Outputs:

* Final Score (based on grading logic)

---

### 5. Run Interactive Demo

```bash
python -m streamlit run app.py
```

This will open a browser showing:

* Live simulation
* Agent decisions
* Rewards and system state

---

## Project Architecture

| Component   | Description                             |
| ----------- | --------------------------------------- |
| env.py      | Cybersecurity simulation environment    |
| agent.py    | DQN-based RL agent                      |
| task.py     | Task definitions with difficulty levels |
| grader.py   | Automated evaluation logic              |
| train.py    | Training loop                           |
| evaluate.py | Performance scoring                     |
| app.py      | Streamlit UI                            |

---

## Evaluation Criteria Covered

* Runtime Correctness: Fully executable without errors
* Interface Compliance: OpenEnv-style modular structure
* Task Design: Realistic cybersecurity scenarios with scaling difficulty
* Grading Logic: Multi-factor scoring system
* Reward System: Logical and meaningful feedback mechanism

---

## Sample Workflow

1. Agent observes system state
2. Takes defensive action
3. Environment updates (threat, health, traffic)
4. Reward assigned based on effectiveness
5. Agent improves through learning

---

## Future Improvements

* Multiple attack types (DDoS, Phishing, Malware)
* Advanced RL algorithms (Double DQN, PPO)
* Model saving and loading
* Multi-agent cybersecurity simulation
* Advanced analytics dashboard

---

## Final Note

This project demonstrates how Reinforcement Learning can be applied to real-world cybersecurity challenges, enabling adaptive and intelligent defense systems.
