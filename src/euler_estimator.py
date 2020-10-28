class EulerEstimator:
  def __init__(self, derivative):
    self.derivative = derivative
  
  def calc_derivative_at_point(self, point):
    return self.derivative(point[0])

  def step_forward(self, point, step_size):
    dydx = self.calc_derivative_at_point(point)
    x = point[0]
    y = point[1]
    return (x + step_size, y + dydx*step_size)

  def calc_estimated_points(self, point, step_size, num_steps):
    point_list = [point]
    current_point = point
    for step_num in range(num_steps):
      current_point = self.step_forward(current_point, step_size)
      point_list.append(current_point)
    return point_list