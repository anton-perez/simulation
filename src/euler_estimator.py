import matplotlib.pyplot as plt

class EulerEstimator:
  def __init__(self, derivatives):
    self.derivatives = derivatives
  
  def calc_derivative_at_point(self, point):
    return {f:self.derivatives[f](point[0], point[1]) for f in self.derivatives}

  def step_forward(self, point, step_size):
    dydx = self.calc_derivative_at_point(point)
    t = point[0]
    d = self.calc_derivative_at_point(point)
    x = {f:point[1][f]+d[f]*step_size for f in self.derivatives}
    return (t + step_size, x)

  def calc_estimated_points(self, point, step_size, num_steps):
    point_list = [point]
    current_point = point
    for step_num in range(num_steps):
      current_point = self.step_forward(current_point, step_size)
      point_list.append(current_point)
    return point_list

  def plot(self, point, step_size, num_steps):
    points = self.calc_estimated_points(point, step_size, num_steps)
    plt.clf()
    plt.style.use('bmh')
    plt.plot(
      [point[0] for point in points],
      [point[1] for point in points])
    plt.gca().set_aspect("equal")
    plt.savefig(self.__class__.__name__+'.png')