from state_utils import *
from visualizer import *

# Parameter: limit for delta, under which delta stops being significant for loop to evaluate/improve
theta = 0.1

# Parameter: discount factor
gamma = 1

# Parameter: reward
reward = -1

# Parameter: use policy improvement?
use_policy_improvement = True

# Parameter: world size
world_size = 4

# Initialization: all states
states_n = world_size**2
states = range(states_n)
#print("States:{}", *states)

# Initialization: terminal states
# NOTE: feel free to add terminal states for experimenting
terminal_states = [0, states_n - 1]
#print("Terminal states:{}", terminal_states)

# Initialization: non-terminal states
non_terminal_states = [s for s in states if s not in terminal_states]
#print("Non-terminal states:{}", non_terminal_states)

# Initialization: value function (mapping)
values = dict.fromkeys(states, 0)

# Initialization: policy function (mapping)
# Contains probabilities in order [left, right, up, down]
policy = dict.fromkeys(non_terminal_states, [])

# Policy improvement algorithm (Barto & Sutton, bottom of page 80, step 3)
def improve_policy():
  new_policy = policy.copy()

  is_policy_stable = True
  for s in non_terminal_states:
    left = left_state(s, world_size)
    right = right_state(s, world_size)
    up = up_state(s, world_size)
    down = down_state(s, world_size)

    neighbour_values = [values[left], values[right], values[up], values[down]]
    allowed_neighbours = state_neighbour_mask(neighbour_values)
    policy_value = [neighbour / sum(allowed_neighbours) for neighbour in allowed_neighbours]
    
    if policy_value != new_policy[s]:
      new_policy[s] = policy_value
      is_policy_stable = False
    
  return is_policy_stable, new_policy

# Set initial policy (default "improvement")
# NOTE: initial policy will be initialized with all action probabilities (left, right, up, down) equal
_, policy = improve_policy()

# We want to begin with initial policy visualization
print("- Initial policy --------------------")
visualize_policy(policy, states, world_size)

# Policy evaluation algorithm (Barto & Sutton, bottom of page 80, step 2)
# Just a counter, to see how fast do we converge
k = 0
while True:
  delta = 0

  # NOTE: algorithm modified a bit, additional buffer new_values introduced
  # Barto & Sutton seem to have a bug in their algorithm (iterative estimation does not fit figure 4.1)
  # Instead of tracking one state value inside a loop, we track entire state value function mapping
  # outside that loop. Also note that after that change algorithm consumes more memory.
  new_values = [0] * states_n
  for s in non_terminal_states:
    # Evaluate state value under current policy
    next_states = get_next_states(s, policy[s], world_size)
    sum_items = [p * (reward + gamma * values[s_next]) for s_next, p in next_states.items()]
    new_values[s] = sum(sum_items)

    # Track delta
    delta = max(delta, abs(values[s] - new_values[s]))
  
  # (now we switch state value function buffer, instead of switching single state value in the loop)
  values = new_values

  if use_policy_improvement:
    # Policy_improvement is done inside improve_policy(), and if new policy is no better than the 
    # old one, return value of is_policy_stable is True
    is_policy_stable, improved_policy = improve_policy()
    if is_policy_stable:
      print("Policy is stable.")
      break
    else:
      print("- Improving policy... ----------------")
      policy = improved_policy
      visualize_policy(policy, states, world_size)
  
  # In case we don't track policy improvement, we need to track delta for the convergence sake
  if delta < theta:
    break

  # Track iteration count
  k += 1

print("--------------------------------------")
print(f"Number of iterations = {k}")
#print(f"Policy = {policy}")
print(f"Done.")
