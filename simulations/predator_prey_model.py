import sys
sys.path.append('src')
from euler_estimator import EulerEstimator

derivatives = {
    'D': (lambda t,x: 0.6*x['D'] - 0.05*x['D']*x['W']),
    'W': (lambda t,x: -0.9*x['W'] + 0.02*x['D']*x['W'])
  }
euler = EulerEstimator(derivatives)

initial_values = {'D': 100, 'W': 10}
initial_point = (0, initial_values)

euler.plot(point=initial_point, step_size=0.001, num_steps=100000)