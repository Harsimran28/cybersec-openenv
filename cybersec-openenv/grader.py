class CyberGrader:
    def grade(self, trajectory):
        total_reward = sum([step[2] for step in trajectory])
        final_state = trajectory[-1][0]

        health = final_state[1]
        steps = len(trajectory)

        score = 0

        if total_reward > 5:
            score += 1

        if health > 0.5:
            score += 1

        if steps >= 20:
            score += 1

        return score