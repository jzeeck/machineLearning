#!/usr/bin/python

from cvxopt.solvers import qp
from cvxopt.base import matrix
from cvxopt import spmatrix
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
	-1.0)
	for i in range(10)]

data = classA + classB
random.shuffle(data)


def RBFKernels(datapoint1, datapoint2, sigma=10):
	"Radial Basis Function kernels"
	value = []
	value.append(datapoint1[0]-datapoint2[0])
	value.append(datapoint1[1]-datapoint2[1])
	return math.exp(-(np.dot(value,value)/2*sigma**2))


def polyKernels(datapoint1, datapoint2, power=1):
	"Polynomial kernel function"
	print datapoint1
	print datapoint2
	print math.pow(np.dot(datapoint1, datapoint2) + 1, power)
	return math.pow(np.dot(datapoint1, datapoint2) + 1, power)

def buildPMatrix(datapoints, kernel):
	tempMatrix = matrix(0.1,(len(datapoints),len(datapoints)))
	for i in range(len(datapoints)):
		for j in range(len(datapoints)):
			print "solving P, point (x, y) (",i,", ",j,")"
			tempMatrix[i,j] = datapoints[i][2]*datapoints[j][2]*kernel(
				[datapoints[i][0], datapoints[i][1]], [datapoints[j][0], datapoints[j][1]])
	return tempMatrix

N = len(data)
P = buildPMatrix(data, polyKernels)

G = spmatrix(-1.0, range(N), range(N))

q = np.linspace(-1,-1,N)
h = np.zeros(N)

#print "Calling qp"

r = qp(matrix(P) , matrix(q) , matrix(G) , matrix(h))
alpha = list(r['x'])

indicationMapping = []
epsylon = 0.00001
for i in range(N):
	if alpha[i] > epsylon:
		indicationMapping.append([alpha[i],data[i]])

print indicationMapping
print len(indicationMapping)


def indicator(a, b):
	return 1


pylab.hold(True)
pylab.plot([p[0] for p in classA],
	[p[1] for p in classA],
	'bo')
pylab.plot([p[0] for p in classB],
	[p[1] for p in classB],
	'ro')


pylab.show()













