import numpy as np

n_simulations = 100000
n_points_circle = 0

for i in range(n_simulations):
    
    # x is randomly drawn from a continuous uniform distribution
    x = np.random.uniform(-1, 1)
    
    # y is randomly drawn from a continuous uniform distribution
    y = np.random.uniform(-1, 1)
    
    # calculate the distance between the point and the origin
    dist_from_origin = x ** 2 + y ** 2
    
    # if the distance is smaller than or equal to 1, the point is in the circle
    if dist_from_origin <= 1:
        n_points_circle += 1
    
# estimate the value of pi, We use n_simulation instead of n points squared because the quantity is the same
pi = 4 * n_points_circle / n_simulations
print(pi)   