# Barto & Sutton - gridworld playground

## Intro

This is an exercise in dynamic programming. It's an implementation of the dynamic programming algorithm presented in the book *"Reinforcement Learning - An Introduction, second edition"* from Richard S. Sutton and Andrew G. Barto. 

The algorithm implementation is deliberately written with no reference to *NumPy* package. This is in order for Python ML newcomers to be able to focus on the algorithm (and not on *NumPy* structures) to understand it more easily.

The algorithm itself is described in *Chapter 4 - Dynamic Programming*, sections *4.1 Policy Evaluation (Prediction)* and *4.2 Policy Improvement*. The specification is given on page 80.

## Parameters

You can use parameters to change the program execution.

1. Parameter **theta**: limit for delta, under which delta stops being significant for loop to evaluate/improve. It's a state function convergence measure. After the delta reaches theta, algorithm stops. See source literature. Default is **0.1**.

2. Parameter **gamma**: it's a discount factor. Measurement of MDP - how important is the future? Closer to 1 means important. Closer to 0 means less important. See source literature. Default is **1**.

3. Parameter **reward**: reward amount for all the actions that do not lead to terminal states. Actually punishment. See source literature. Default is **-1**.

4. Parameter **use_policy_improvement**: Do we use policy improvement? If not using policy improvement, initial policy is used for all iterations. It means that we have to track how fast we are changing the value function, or how quick is the convergence of the value function, and stop if that speed is slow enough. Otherwise the algorithm wouldn't stop (see parameter **theta**). If we opt to use policy improvement, we check every time if we have a better policy. We stop the program when there is no improvement on the current policy. If we do use policy improvement, the algorithm is significantly faster. See source literature. Default is **True**.

5. Parameter **world_size**: gridworld size is NxN, and this parameter represents N. Default is **4**.

6. Variable **terminal_states**: initialization is done in the way that by default **the first** and **the last** states are terminal states. You can experiment with that and either add more terminal states or e.g. leave just one terminal state. Default is **[0, states_n - 1]**.

## Notes

It seems that the original algorithm has a bug, since value function (mapping) is updated one by one value in the source mapping structure. Why is that incorrect?  It means that inside the loop for each s (of set S), in the same evaluation loop pass, the next value of the element s (e.g. s_2 of set S) will be evaluated from the *newly* evaluated element in that pass (e.g. s_1 of set S), instead of s from the *current* iteration.
This problem is avoided here using double buffering technique. Additional buffer is used for new values of set S. It also means that program uses more memory because of that buffer.

## Running

You need Python 3.10 to run this implementation. Maybe Python 3.9. would work as well, but It's not tested against it. Python 3.8. will surely *not* work.

Files: 
* **policy-evaluation-prediction.py** - entrypoint, you should run that file
* **state_utils.py** - helper functions for the gridworld
* **visualizer.py** - policy visualization functions for the gridworld
