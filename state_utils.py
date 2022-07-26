def left_state(s, world_size):
  return s if s % world_size == 0 else s - 1

def right_state(s, world_size):
  return s if s % world_size == (world_size - 1) else s + 1

def up_state(s, world_size):
  return s if (s - world_size) < 0 else s - world_size

def down_state(s, world_size):
  return s if (s + world_size) >= world_size**2 else s + world_size

def get_next_states(s, a, world_size):
  ret_val = {}
  left = left_state(s, world_size)
  ret_val[left] = ret_val.get(left, 0) + a[0]
  right = right_state(s, world_size)
  ret_val[right] = ret_val.get(right, 0) + a[1]
  up = up_state(s, world_size)
  ret_val[up] = ret_val.get(up, 0) + a[2]
  down = down_state(s, world_size)
  ret_val[down] = ret_val.get(down, 0) + a[3]
  return ret_val

def state_neighbour_mask(neighbour_values) -> list[int]:
    max_value = max(neighbour_values)
    allowed_neighbours = [1 if tran_value == max_value else 0 for tran_value in neighbour_values]
    return allowed_neighbours

if __name__ == '__main__':
  print("Wrong usage, exiting")
  exit()
