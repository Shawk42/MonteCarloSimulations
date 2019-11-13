import numpy as np
import matplotlib.pyplot as plt

""" Member Parameters """
a = 5
L = 2
area = a**2

"""Force """

F_min = 0
F_max = 1000
F_mid = (F_max + F_min) / 2
n = 250
F_limit = np.array([F_min, F_mid,F_max])
F_uni = np.random.uniform(F_min, F_max, n)
F_tri = np.random.triangular(F_min, F_mid, F_max, n)
#F = np.array([])
#F = np.append(F, F_limit)
#F = np.append(F, F_uni)
#F = np.append(F, F_tri)

F = np.concatenate((F_limit, F_uni, F_tri))

""" Axial Load """
sigma_ax = F / a

""" Bending Load """
M = F * L
I = (a*a**3) / 12
y = a / 2
sigma_bn = (M * y) / I

"""Post Processing"""
standoff = len(F_limit)
n_array = np.linspace(0, n - 1, n)
n_uni = n_array + standoff
n_tri = n_array + n_uni
n_lim = np.array([0, 1, 2])

n_uni = n_uni.astype(int)
n_tri = n_tri.astype(int)

axial_lim = np.take(sigma_ax, n_lim)
bend_lim = np.take(sigma_bn, n_lim)

axial_uni = np.take(sigma_ax, n_uni)
bend_uni = np.take(sigma_bn, n_uni)

axial_tri = np.take(sigma_ax, n_tri)
bend_tri = np.take(sigma_bn, n_tri)

plt.subplot(2,1,1)
plt.plot(F_limit, axial_lim)
plt.plot(F_uni, axial_uni, "*")
plt.plot(F_tri, axial_tri, "*")

plt.subplot(2,1,2)
plt.plot(F_limit, bend_lim)
plt.plot(F_uni, bend_uni, "*")
plt.plot(F_tri, bend_tri, "*")

plt.show()



