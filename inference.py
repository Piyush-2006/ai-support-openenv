from env import SupportEnv
from models import Action

print("[START]")

env = SupportEnv()

obs = env.reset()

print("[STEP] Observation:", obs)

# simple AI (rule-based)
if "refund" in obs.message.lower():
    action = Action(category="refund")
else:
    action = Action(category="query")

obs, reward, done, info = env.step(action)

print("[STEP] Reward:", reward)

print("[END]")