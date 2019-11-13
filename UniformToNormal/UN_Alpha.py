import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import shapiro

"""Distribution Parameters"""
master_min = 2
master_max = 4

a_min = np.random.uniform(master_min, master_max,1)
a_max = np.max(a_min) + np.random.uniform(master_min,master_max,1) * np.random.uniform(0,1,1)
n = np.random.randint(0,250,1)
alpha = 0.05

""" Addition """
p = 0
u = 0
i = 0
i_add = np.array([])
p_add = np.array([])
ii = 0
while ii < 250:
    #print(ii)
    p = 0
    u = 0
    i = 0
    while p < alpha:
        u_cur = np.random.uniform(a_min, a_max, n)
        u = u + u_cur
        stat, p = shapiro(u)
        i_add = np.append(i_add,i)
        p_add = np.append(p_add, p)
        i = i + 1

    i_add = np.append(i_add,i)
    p_add = np.append(p_add, p)
    ii = ii + 1


obv = i_add * n
#print(obv)
#print(i_add)
#print(p_add)

plt.plot(obv, p_add, "*")
plt.hlines(alpha, 0, np.max(obv), colors = "red", linestyles= "dashed")
plt.grid()
plt.xlabel("Observations")
plt.ylabel("p")
plt.show()

"""
plt.plot(i_add,p_add)
plt.show()


y, w = np.histogram(u, bins = "auto")

y_cs = np.cumsum(y)

plt.subplot(1,2,1)
plt.plot(y)
plt.ylim((0,np.max(y)+5))

plt.subplot(1,2,2)
plt.plot(y_cs)

plt.show()
"""


