import sys
sys.path.append('src')
from euler_estimator import EulerEstimator
import math

###############################
### constants

C = 1.0
V_Na = 115
V_K = -12
V_L = 10.6

bar_g_Na = 120
bar_g_K = 36
bar_g_L = 0.3
###############################
### main variables: V, n, m, h

def dV_dt(t,x):
  V = x['V']
  n = x['n']
  m = x['m']
  h = x['h']
  return (s(t) - I_Na(t,x) - I_K(t,x) - I_L(t,x))/C

def dn_dt(t,x):
  V = x['V']
  n = x['n']
  return alpha_n(t,x) * (1-n) - beta_n(t,x) * n

def dm_dt(t,x):
  V = x['V']
  m = x['m']
  return alpha_m(t,x) * (1-m) - beta_m(t,x) * m

def dh_dt(t,x):
  V = x['V']
  h = x['h']
  return alpha_h(t,x) * (1-h) - beta_h(t,x) * h

###############################
### intermediate variables: alphas, betas, stimulus (s), currents (I's), ...

def alpha_n(t,x):
  V = x['V']
  return 0.01*(10 - V)/(math.exp(0.1*(10 - V))-1)

def beta_n(t,x): 
  V = x['V']
  return 0.125*math.exp(-V/80)

def alpha_m(t,x):
  V = x['V']
  return 0.1*(25 - V)/(math.exp(0.1*(25 - V))-1)

def beta_m(t,x): 
  V = x['V']
  return 4*math.exp(-V/18)

def alpha_h(t,x):
  V = x['V']
  return 0.07*math.exp(-V/20)

def beta_h(t,x): 
  V = x['V']
  return 1/(math.exp(0.1*(30 - V))+1)

def I_Na(t,x):
  V = x['V']
  m = x['m']
  h = x['h']
  return g_Na(m,h)*(V - V_Na)

def I_K(t,x):
  V = x['V']
  n = x['n']
  return g_K(n)*(V - V_K)

def I_L(t,x):
  V = x['V']
  n = x['n']
  return g_L()*(V - V_K)

def g_Na(m,h):
  return bar_g_Na*h*m**3

def g_K(n):
  return bar_g_K*n**4

def g_L():
  return bar_g_L

def s(t):
  int_1 = t >= 10 and t <= 11
  int_2 = t >= 20 and t <= 21 
  int_3 = t >= 30 and t <= 41
  int_4 = t >= 50 and t <= 51
  int_5 = t >= 53 and t <= 54
  int_6 = t >= 56 and t <= 57
  int_7 = t >= 59 and t <= 60
  int_8 = t >= 62 and t <= 63
  int_9 = t >= 65 and t <= 66

  if int_1 or int_2 or int_3 or int_4 or int_5 or int_6 or int_7 or int_8 or int_9:
    return 150
  return 0

################################
### input into EulerEstimator

V_0 = 0
n_0 = alpha_n(0, {'V':V_0})/(alpha_n(0, {'V':V_0})+beta_n(0, {'V':V_0}))
m_0 = alpha_m(0, {'V':V_0})/(alpha_m(0, {'V':V_0})+beta_m(0, {'V':V_0}))
h_0 = alpha_h(0, {'V':V_0})/(alpha_h(0, {'V':V_0})+beta_h(0, {'V':V_0}))

derivatives = {
  'V': dV_dt,
  'n': dn_dt,
  'm': dm_dt,
  'h': dh_dt,
}

euler = EulerEstimator(derivatives)

initial_values = {'V':V_0, 'n':n_0, 'm':m_0, 'h':h_0}
initial_point = (0, initial_values)

euler.plot(point=initial_point, step_size=0.01, num_steps=8000, additional_functions={'stimulus':s})