import argparse as ap
from state_utils import *

if __name__ == '__main__':
  print("Wrong usage, exiting")
  exit()

STATE_VIS = ap.Namespace(
  add = ['NONE', 'ALL', 'draw'],
  SINGLE = ap.Namespace(add = ['LEFT', 'UP', 'RIGHT', 'DOWN']),
  DOUBLE = ap.Namespace(add = ['LEFTRIGHT', 'UPDOWN', 'RIGHTDOWN', 'LEFTDOWN', 'RIGHTUP', 'LEFTUP']),
  TRIPLE = ap.Namespace(add = ['NOLEFT', 'NOUP', 'NORIGHT', 'NODOWN'])
)

STATE_VIS.NONE = u'\u25a1'
STATE_VIS.SINGLE.LEFT = u'\u21d0'
STATE_VIS.SINGLE.UP = u'\u21d1'
STATE_VIS.SINGLE.RIGHT = u'\u21d2'
STATE_VIS.SINGLE.DOWN = u'\u21d3'
STATE_VIS.DOUBLE.LEFTRIGHT = u'\u2550'
STATE_VIS.DOUBLE.UPDOWN = u'\u2551'
STATE_VIS.DOUBLE.RIGHTDOWN = u'\u2554'
STATE_VIS.DOUBLE.LEFTDOWN = u'\u2557'
STATE_VIS.DOUBLE.RIGHTUP = u'\u255a'
STATE_VIS.DOUBLE.LEFTUP = u'\u255d'
STATE_VIS.TRIPLE.NOLEFT = u'\u2560'
STATE_VIS.TRIPLE.NORIGHT = u'\u2563'
STATE_VIS.TRIPLE.NOUP = u'\u2566'
STATE_VIS.TRIPLE.NODOWN = u'\u2569'
STATE_VIS.ALL = u'\u256c'

def visualize_policy_mapper(left, right, up, down):
  match left, right, up, down:
    case 0, 0, 0, 0:
      return STATE_VIS.NONE

    case 1, 0, 0, 0:
      return STATE_VIS.SINGLE.LEFT
    case 0, 1, 0, 0:
      return STATE_VIS.SINGLE.RIGHT
    case 0, 0, 1, 0:
      return STATE_VIS.SINGLE.UP
    case 0, 0, 0, 1:
      return STATE_VIS.SINGLE.DOWN

    case 1, 1, 0, 0:
      return STATE_VIS.DOUBLE.LEFTRIGHT
    case 0, 0, 1, 1:
      return STATE_VIS.DOUBLE.UPDOWN
    case 0, 1, 0, 1:
      return STATE_VIS.DOUBLE.RIGHTDOWN
    case 1, 0, 0, 1:
      return STATE_VIS.DOUBLE.LEFTDOWN
    case 0, 1, 1, 0:
      return STATE_VIS.DOUBLE.RIGHTUP
    case 1, 0, 1, 0:
      return STATE_VIS.DOUBLE.LEFTUP

    case 0, 1, 1, 1:
      return STATE_VIS.TRIPLE.NOLEFT
    case 1, 0, 1, 1:
      return STATE_VIS.TRIPLE.NORIGHT
    case 1, 1, 0, 1:
      return STATE_VIS.TRIPLE.NOUP
    case 1, 1, 1, 0:
      return STATE_VIS.TRIPLE.NODOWN

    case 1, 1, 1, 1:
      return STATE_VIS.ALL

    case _:
      return "?"

def visualize_policy(policy, states, world_size):
  for i in states:
    is_last_sym = i % world_size == (world_size - 1)
    if i not in policy:
      if is_last_sym:
        print(STATE_VIS.NONE)
      else:
        print(STATE_VIS.NONE, end='')
      continue

    left, right, up, down = state_neighbour_mask(policy[i])
    sym = visualize_policy_mapper(left, right, up, down)

    if is_last_sym:
      print(sym)
    else:
      print(sym, end='')
  
  print()