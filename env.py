from models import Observation, Action

class SupportEnv:

    def __init__(self):
        self.tasks = [
            {"message": "I want refund", "answer": "refund"},
            {"message": "This product is bad", "answer": "complaint"},
            {"message": "How to use this?", "answer": "query"}
        ]
        self.current_task = 0
        self.current_message = ""

    def reset(self):
        task = self.tasks[self.current_task]
        self.current_message = task["message"]
        return Observation(message=self.current_message)

    def step(self, action: Action):
        correct = self.tasks[self.current_task]["answer"]

        if action.category == correct:
            reward = 1.0
        else:
            reward = 0.3

        self.current_task += 1
        done = self.current_task >= len(self.tasks)

        return Observation(message=self.current_message), reward, done, {}

    def state(self):
        return {"message": self.current_message}
    