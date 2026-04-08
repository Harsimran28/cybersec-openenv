class CyberSecurityTask:
    def __init__(self, level=1):
        self.level = level

    def describe(self):
        if self.level == 1:
            return "Handle low-level threats"
        elif self.level == 2:
            return "Maintain system health above 0.5"
        else:
            return "Survive high threat for 20 steps"