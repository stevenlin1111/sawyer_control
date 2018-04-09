from sawyer_reaching import SawyerJointSpaceReachingEnv
import numpy as np
import pdb

env = SawyerJointSpaceReachingEnv(desired=np.ones(7),
                                  action_mode='angles',
                                  use_safety_checks='True')
#env.reset()
def send_zeros(env, n):
    zeros = np.zeros(7)
    for _ in range(n):
        env.step(zeros)

deltas = np.zeros(7)#np.array([0, 0, -0.01, 0, 0, 0, 0])
n = 500
for _ in range(n):
    env.step(deltas)


pdb.set_trace()



