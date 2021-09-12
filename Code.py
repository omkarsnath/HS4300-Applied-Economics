import numpy as np
from sklearn.linear_model import LinearRegression

# Create Input Data:
data = []

file = open('Age.txt', 'r')
for line in file.readlines():
    data.append([float(line[:-1])])
file.close()

file = open('Beds.txt', 'r')
for idx, line in enumerate(file.readlines()):
    data[idx].append(float(line[:-1]))
file.close()

file = open('DemocraticPercentExitPoll.txt', 'r')
for idx, line in enumerate(file.readlines()):
    data[idx].append(float(line[:-1]))
file.close()

file = open('Education.txt', 'r')
for idx, line in enumerate(file.readlines()):
    data[idx].append(float(line[:-1]))
file.close()

file = open('Income.txt', 'r')
for idx, line in enumerate(file.readlines()):
    data[idx].append(float(line[:-1]))
file.close()

file = open('Population.txt', 'r')
for idx, line in enumerate(file.readlines()):
    data[idx].append(float(line[:-1]))
file.close()

file = open('Temperature.txt', 'r')
for idx, line in enumerate(file.readlines()):
    data[idx].append(float(line[:-1]))
file.close()

data = np.array(data)

# Create Output:
output = []
file = open('CovidData.txt', 'r')
for line in file.readlines():
    output.append(float(line[:-1]))
file.close()

output = np.array(output)

# Linear Regression on input vs output:
model = LinearRegression(normalize=True).fit(data, output)

# Print out the coefficients:
r_sq = model.score(data, output)
print('coefficient of determination: ', r_sq)
print('coefficients of factors: ', model.coef_)
print('intercept: ', model.intercept_)
