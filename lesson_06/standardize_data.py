# Standardise the data

from sklearn.preprocessing import StandardScaler
import pandas
import numpy
url = "https://goo.gl/vhm1eU"
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
dataFrame = pandas.read_csv(url, names=names)

# Separate array into input and output components
array = dataFrame.values
X = array[:, 0:8]
Y = array[:, 8]

scaler = StandardScaler().fit(X)
rescaledX = scaler.transform(X)

# Summarize

numpy.set_printoptions(precision=3)
print(rescaledX[0:5, :])
