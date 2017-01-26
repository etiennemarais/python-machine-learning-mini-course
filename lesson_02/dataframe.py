# Dataframe

import numpy
import pandas

myArray = numpy.array([[1, 2, 3], [4, 5, 6]])
rowNames = ['a', 'b']
colNames = ['one', 'two', 'three']

myDataFrame = pandas.DataFrame(myArray, index = rowNames, columns = colNames)

print(myDataFrame)
