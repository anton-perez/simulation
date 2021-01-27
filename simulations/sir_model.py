import sys
sys.path.append('src')
from euler_estimator import EulerEstimator

derivatives = {
    'S': (lambda t,x: -0.01*0.03*x['S']*x['I']),
    'I': (lambda t,x: 0.01*0.03*x['S']*x['I'] - 0.02*x['I']),
    'R': (lambda t,x: 0.02*x['I']) 
  }
euler = EulerEstimator(derivatives)

initial_values = {'S': 1000, 'I': 1, 'R': 0}
initial_point = (0, initial_values)

euler.plot(point=initial_point, step_size=0.05, num_steps=4000)