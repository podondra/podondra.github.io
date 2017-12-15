Title: Deep Q-network
Date: 2017-12-11 08:51
Category: reinforcement learning
Tags: dqn, deep q-network, reinforcement learning, deep learning
Status: draft

Deep Q-network ([DQN][1]) is a DeepRL system which combines deep neural networks
with reinforcement learning and is able to master a diverse range of
[Atari 2600][3] games with only the raw pixels and score as input.
It represents a general-purpose agent that is able to adapt its
behaviour without any human intervanition.
It is a major technical step forward to general aritificial intelligence.
I am writing this article to get better understandig of it.

[1]: https://deepmind.com/research/dqn/ (DeepMind Blog Post)
[2]: https://www.youtube.com/watch?v=xN1d3qHMIEQ (Inside DeepMind Video)
[3]: https://en.wikipedia.org/wiki/Atari_2600 (Atari 2600 Wikipedia)

Truly intelligent artificial agents should excel at a wide variety of tasks.
This algorithm leverages recent breakthroughs in training deep neural networks
to show that DQN is able to achieve superhuman performance across a diverse
range of 49 game scenarios.

## Reinforcement Learning

Refer to book [Reinforcement Learning: An Introduction][4] by Sutton and Barto.

[4]: http://incompleteideas.net/book/bookdraft2017nov5.pdf
     (Sutton and Barto - Reinforcement Learning: An Introduction)

Reinforcement learning is a third machine learning paradigm alongside
supervised and unsupervised learning and perhaps others.
From all forms of machine learning it is the closest to the kind of learning
that humans and other animals do.
A coputational approach to learning from interaction.
Reinforcement learning is learning what to do (how to map situations to
actions) so as to maximize a numerical reward signal.
There are two main characteristics:

- trial-and-error search,
- delayed reward.

A learning agent interacting over time with its environment to achieve a goal.
It must be able to sense the state of its environment and able to take actions
that affect the state.

One of the challenges that arise in reinforcement learning is to balance
exploration and exploation.
The agent has to exploit an action to obtain reward but it also has to explore
to find new better action for future.

### Policy, Reward Signal, Value Function and Model of Environment

A policy, a reward signal, a value function and optionally a model of the
environment are four main subelements of a reinforcement learning system.

A policy is a mapping from perceived stated of the environment to actions
when in those stated. Therefore, it defines the learning agent's behaviour
at a given time.

A reward signal defines the goal in a reinforcement learning problem.
It is a single number send to the learning agent by the environment at every
time step.
The agent's objective is to maximalize the total reward over the long run.
Thus, the reward signal is the primary source for altering the policy.

On contrary to reward signal, which is good in an immediate sense,
value function specifies what is good in the long run.
What an agent can expect to accumulate from a state over the future.
While a reward signal might be low in some state it might have high value
as it is usually followed by states that yield high rewards.

The last element is a model of the environment which mimics the behaviour
of the environment or allows inferences about how the environment will behave.
They are used for estimating future situations before they are actually
experienced (planning).

Most of the reinforcement learning methods are concerned with estimating value
functions (except evolutionary methods).

## Q-learning

Q-learning is model-free reinforcement learning method which finds optimal
action-selection policy for a given finite Markov decision process (MDP)
by learning an action-value function `Q`:

`Q^{*}(s, a) = max_{\pi} \mathbb{E}[r_t + \gamma r_{t + 1} + \gamma ^ 2
r_{t + 2} + \dots | s_t = s, a_t = a, \pi]`

which is the maximum sum of rewards `r_t` discounted by `\gamma` at each time
step `t`, achievable by a behaviour policy `\pi = P(a|s)`,
after making an observation `s` and taking action `a`.

It is proven that Q-learning method will find a optimal policy
for any finite MDP.

[5]: http://www.cs.rhul.ac.uk/~chrisw/thesis.html
     (Learning from Delayed Rewards)
[6]: https://link.springer.com/article/10.1007/BF00992698
     (Technical Note Q-learning)

## Deep Q-network

To use reinforcement learning successfully agents must derive efficient
environment representations from high-dimensional sensory inputs
and generalize past experience to new situations.
The DQN bridges the gap between high-dimensional sensory inputs and actions
and so learning to excel at a diverse array of tasks
with same architecture and hyperparameters.

- [Playing Atari with Deep Reinforcement Learning][7]
- [Human-level control through deep reinforcement learning][6]

[6]: https://www.nature.com/articles/nature14236 (DQN Paper)
[7]: https://www.cs.toronto.edu/~vmnih/docs/dqn.pdf
     (Playing Atari with Deep Reinforcement Learning)

DQN is combination of reinforcement learning with deep convolutional networks.
Formally the neural network approximate the optimal action-value function
above, because neural networks are universal approximators.

### Variants

Provided on [OpenAI Baselines][8].

[Double Q-learning][9] corrects the stock DQN algorithm's tendency to sometimes
overestimate the values tied to specific actions.

[Prioritized Replay][10] extends DQN's experience replay function by learning
to replay memories where the real reward significantly diverges from the
expected reward, letting the agent adjust itself in response to developing
incorrect assumptions.

[Dueling DQN][11] splits the neural network into two.
One learns to provide an estimate of the value at every time step,
and the other calculates potential advantages of each action,
and the two are combined for a single action-advantage Q function.

[8]: https://blog.openai.com/openai-baselines-dqn/ (OpenAI Baselines)
[9]: https://arxiv.org/abs/1509.06461
     (Deep Reinforcement Learning with Double Q-learning)
[10]: https://arxiv.org/abs/1511.05952 (Prioritized Experience Replay)
[11]: https://arxiv.org/abs/1511.06581
      (Dueling Network Architectures for Deep Reinforcement Learning)
