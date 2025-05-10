from gymnasium.envs.registration import register

register(
    id="CustomHumanoid-v5",
    entry_point="gymnasium.envs.mujoco.humanoid_v5:HumanoidEnv",
    max_episode_steps=1000,
)
