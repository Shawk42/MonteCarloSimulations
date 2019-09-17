""""
The intention of this script is to detect a distribution type of a model
"""

import matplotlib.pyplot as plt
import numpy as np
from prettytable import PrettyTable
from scipy import stats

""" Functions """

def sample():
    select = np.random.randint(1, 4, 1)
    select = select.item(0)
    if select == 1:
        dist_type = "Uniform"
        dist = np.random.uniform(0, 10, 250)
    elif select == 2:
        dist_type = "Normal"
        dist = np.random.normal(5, 2, 250)
    else:
        dist_type = "Triangular"
        dist = np.random.triangular(2, 5, 7, 250)

    return dist_type,dist


"""Initial Plot"""
t, x = sample()

print("Distribution type is ", t)

buck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
plt.hist(x, buck, align= 'left',rwidth= 0.8)
plt.xlim(0,10)
plt.xticks(buck)

# plt.show()   #Quick removal earlier plot show

"""Count and Count Graphs"""
# TT is a troubleshooting table used

# TT = PrettyTable()

# TT.field_names = ["i","Current Bucket","Current Sum"]

i = 0
bucket = np.array([])
count = np.array([])

while i < len(buck):
    cur_buck = buck[i]
    cur = np.logical_and(x > cur_buck - 1, x <= cur_buck)
    cur_sum = np.sum(cur)
    bucket = np.append(bucket,cur_buck)
    count = np.append(count,cur_sum)
    # TT.add_row([i, cur_buck, cur_sum])
    # print(TT)
    i = i + 1

count_sum = np.cumsum(count)


"""Uniform distribution checking"""

regress_raw = stats.linregress(bucket, count_sum)

slope, intercept, r_val, p_val, std_err = regress_raw

lin_reg = intercept + (slope * bucket)


"""Plotting"""
plt.subplot(2,2,1)
plt.subplots_adjust(hspace=0.3)

plt.hist(x, buck, align= 'left',rwidth= 0.8)
plt.xlim(0,10)
plt.xticks(buck)
plt.title("Histogram")

plt.subplot(2,2,2)
plt.plot(bucket,count)
plt.title("Count")

plt.subplot(2,2,3)
plt.plot(bucket,count_sum)
plt.title("Cumulative Sum")

plt.subplot(2,2,4)
plt.plot(bucket, count_sum)
plt.plot(bucket,lin_reg)
plt.title("Uniform distribution test")
plt.legend(("Culmative Sum", "Linear Regression"))
plt.text(8,-10,round(r_val**2,2))

plt.show()








