from cvxopt.solvers import qp
from cvxopt.base import matrix
import numpy as np
import pylab
import random
import math
import scipy

classA = [(random.normalvariate(1.5, 1),
	random.normalvariate(0.5, 1),
	1.0)
	for i in range(5)] + \
	[(random.normalvariate(1.5, 1),
	random.normalvariate(0.5,1),
	1.0)
	for i in range(5)]

classB = [(random.normalvariate(0.0, 0.5),
	random.normalvariate(0.5, 0.5),
	1.0)
	for i in range(10)]

data = classA + classB
random.shuffle(data)

def polyKernels(datasetX, datasetY, power=1):
	"Polynomial kernel function"
	return math.pow(np.dot(datasetX, datasetY) + 1, power)


def buildPMatrix(dataset1, dataset2, kernel):
	P = matrix
	for i in range(len(dataset1)):
		for j in range(len(dataset2)):


buildPMatrix(classA,classB,polyKernels)

print classA
print classB




pylab.hold(True)
pylab.plot([p[0] for p in classA],
	[p[1] for p in classA],
	'bo')
pylab.plot([p[0] for p in classB],
	[p[1] for p in classB],
	'ro')
pylab.show()