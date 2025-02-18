import os
from matplotlib import pyplot as graph

# Initilize stuff

F = 1
m = 1
x0 = 0
v0 = 0
dt = 0.01

# define values for plotting graph
x_values = [x0]
v_values = [v0]

# custom function to generate decimal values in a given range
def makeDecimalList(start,end,step):
    try:
        values_size = int(end/step) +1
        values = [(d*step) for d in range(start,values_size)]
        return values
    except Exception as ex:
        print(f"Error occured while generating decimal list: {ex}")
        return []


# generate tuime
time_vals = makeDecimalList(1,10,0.01)


'''

# Formulae :
* v = v(t)+ (F/m) × dt
* x = x(t) + v(t) ×dt

** Analytical approach
* v = u + at
* x = v•t + (1/2)at^2
* a = F/m

'''


for t in time_vals:
    v = v_values[-1] + ((F/m) * dt)
    x = x_values[-1] + (v * dt)
    v_values.append(v)
    x_values.append(x)

    print('t = {:.2f}s; x = {:.3f}m; v(t) = {:.2f}m/s'.format(t, x, v))


#TODO: Plot graph
