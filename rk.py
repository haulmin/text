def prob5(yp_0, y_0, t_0, dt, num):
  def dypdt(yp, y, t):
    return -1 * y * t ** 2 / (1 + t ** 2);

  def dydt(yp, y, t):
    return yp;

  def runge_kutta_two_var(func_x, func_y, x_0, y_0, t_0, dt, num):
    x_list = []; y_list = [];

    #Init
    x = x_0; y = y_0; t = t_0; x_list.append(x), y_list.append(y)
    for i in range(num):
      x_1 = func_x(x, y, t);
      y_1 = func_y(x, y, t);

      x_2 = func_x(x + 0.5*x_1*dt, y + 0.5*y_1*dt, t+0.5*dt);
      y_2 = func_y(x + 0.5*x_1*dt, y + 0.5*y_1*dt, t+0.5*dt); 

      x_3 = func_x(x + 0.5*x_2*dt, y + 0.5*y_2*dt, t+0.5*dt);
      y_3 = func_y(x + 0.5*x_2*dt, y + 0.5*y_2*dt, t+0.5*dt); 

      x_4 = func_x(x + x_3*dt, y + y_3*dt, t+dt);
      y_4 = func_y(x + x_3*dt, y + y_3*dt, t+dt); 

      #Execute
      x += dt * (x_1 + 2*x_2 + 2*x_3 + x_4) / 6
      y += dt * (x_1 + 2*x_2 + 2*x_3 + x_4) / 6
      t += dt

      #Append
      x_list.append(x); y_list.append(y)

  def main():
    pass

### ############################################################################

import numpy as np

class FunctionCountError(Exception):
  def __init__(self):
    super().__init__("Number of variable and function doesn't match.")


class InitialValueCountError(Exception):
  def __init__(self):
    super().__init__("Number of initial value is different from the number of variables.")

class dtError(Exception):
  def __init__(self):
    super().__init__("Delta t should be positive.")


# ##################################################################### 

rk_version = ["RK4"]

class Runge_kutta:
  def __init__(self, version, varc, func_list, init, dt, num, init_time = 0):
    try:
      if len(func_list) != varc:
        raise FunctionCountError

      if len(init) != varc:
        raise InitialValueCountError

      if dt <= 0:
        raise dtError

    finally:
      self.version = version
      self.varc = varc
      self.func_list = func_list
      self.init = init
      self.t = init_time
      
      self.var_arr = [[0]] * self.varc
      for i in range(self.varc):
        self.var_arr[i][0] = self.init[i]

      self.var = np.array(self.var_arr)

  def runge_kutta4(self):
    def first(var, t):
      return np.array([var, t])

    def second(var, t):
      for i in range(len(var)):
        var[i] += 0.5 * first(var, t)[i] * self.dt
        t += 

    def third(var, t):
      pass

    def fourth(var, t):
      pass


    for i in range(self.num):
      incre = [[0,0,0,0]] * self.varc
      for j in range(self.varc):
        incre[j][0] = self.func_list[j](var, t)



def dydt(yp, y, t):
  return yp;

a = Runge_kutta(0, 2, [dydt, dydt], [1, 0], 0.1, 1000, 0)
a.runge_kutta4()
    
