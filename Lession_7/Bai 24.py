import numpy as np

def initialize_policy(num_actions):
    return np.random.rand(num_actions)
def collect_trajectories():
    state = [1,2,3],[4,5,6],[7,8,9]
    action = [0,1,2]
    reward = [0.1,0.5,0.2]
    return state,action,reward

def compute_returns(rewards):
    pass
def conpute_policy_gradient(state,action,reward):
    pass
def update_policy_paramentrs(policy_gradient):
    pass

num_actions = 3
policy_parameters = initialize_policy(num_actions)
#Vong lap
num_episodes = 1000
for episode in range(num_episodes):
    #Thu thap quy dao
    state,action,reward = collect_trajectories()
    #Tinh toan loi nhuan
    returns = compute_returns(reward)
    #Tinh do doc chinh sach
    policy_gradient = conpute_policy_gradient(state,action,returns)
    #Cap nhat tham so chinh sach
    update_policy_paramentrs(policy_gradient)

#Chinh sach cuoi cung
final_policy_parameters = policy_parameters
print("Final Policy Parameters: ", final_policy_parameters)
