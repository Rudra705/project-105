import pandas as pd 
import statistics

file = pd.read_csv("project-105.csv")
data = [60, 61, 65, 63, 98, 99, 90, 95, 91, 96]
standard_deviation = statistics.stdev(data)
print(standard_deviation)

