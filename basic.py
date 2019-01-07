import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("StudentsPerformance.csv", sep=',')


# Scatter Plot
def scatterplot():
    math_score = df['math score']
    reading_score = df['reading score']

    y = math_score
    x = reading_score

    plt.scatter(x, y, color='blue')
    xy= range(0, 100)
    plt.plot(xy, xy, color='red')
    plt.show()

scatterplot()
