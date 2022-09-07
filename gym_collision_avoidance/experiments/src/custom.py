import os
import numpy as np
import gym
gym.logger.set_level(40)
os.environ['GYM_CONFIG_CLASS'] = 'Train'
from gym_collision_avoidance.experiments.src.env_utils import create_env
def main():
    # env: a VecEnv wrapper around the CollisionAvoidanceEnv
    # one_env: an actual CollisionAvoidanceEnv class (the unwrapped version of the first env in the VecEnv)
    env, one_env = create_env()
    num_episodes = 100
    obs = env.reset()
    for i in range(num_episodes):
        actions = {}
        rl_action = model.sample(obs)
        actions[0] = rl_action
        # No need to supply actions for non-learning agents
        # Run a simulation step (check)
if __name__=="__main__":
    main()