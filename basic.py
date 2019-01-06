import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("StudentsPerformance.csv", sep=',')
is_groupb = df['race/ethnicity'] == 'group B'
is_groupc = df['race/ethnicity'] == 'group C'
is_groupd = df['race/ethnicity'] == 'group D'
is_groupe = df['race/ethnicity'] == 'group E'
is_groupa = df['race/ethnicity'] == 'group A'



group_B = df[is_groupb]
group_C = df[is_groupc]
group_D = df[is_groupd]
group_E = df[is_groupe]
group_A = df[is_groupa]

averageB = group_B.mean()
averageC = group_C.mean()
averageD = group_D.mean()
averageE = group_E.mean()
averageA = group_A.mean()



y = np.concatenate((averageB, averageC, averageD, averageE, averageA))
width = 1/1.5
x = ['Group B', 'Group C', 'Group D', 'Group E','Group A', 'Group B', 'Group C', 'Group D', 'Group E','Group A', 'Group B', 'Group C', 'Group D', 'Group E','Group A']

plt.bar(x, y, color="blue")
#
plt.show()

print(y)
