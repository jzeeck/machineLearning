#!/usr/bin/python

from cvxopt.solvers import qp
from cvxopt.base import matrix
from cvxopt import spmatrix
import numpy as np
import pylab
import random
import math
import scipy


print "Defining functions"
def RBFKernel(datapoint1, datapoint2, sigma=1, dummy=0):
	"Radial Basis Function kernels"
	value = []
	value.append(datapoint1[0]-datapoint2[0])
	value.append(datapoint1[1]-datapoint2[1])
	return math.exp(-(np.dot(value,value)/2*sigma**2))

def polyKernels(datapoint1, datapoint2, power=5, dummy=0):
	"Polynomial kernel function"
	return math.pow(np.dot(datapoint1, datapoint2) + 1, power)

def linKernel(datapoint1, datapoint2, dummya=0, dummyb=0):
	"Polynomial kernel function"
	return np.dot(datapoint1, datapoint2) + 1

def sigmoidKernel(datapoint1, datapoint2, k=0.05, delta=10):
	"Sigmoid kernel function"
	return math.tanh(k*np.dot(datapoint1, datapoint2) + delta)

def buildPMatrix(datapoints, kernel, par1, par2):
	tempMatrix = matrix(0.1,(len(datapoints),len(datapoints)))
	for i in range(len(datapoints)):
		for j in range(len(datapoints)):
			#print "solving P, point (x, y) (",i,", ",j,")"
			tempMatrix[i,j] = datapoints[i][2]*datapoints[j][2]*kernel(
				[datapoints[i][0], datapoints[i][1]], [datapoints[j][0], datapoints[j][1]], par1, par2)
	return tempMatrix

def indicator(xPoint, yPoint, alphaPoints, kernel, par1, par2):
	indValue = 0
	for alphaPoint in alphaPoints:
		indValue += alphaPoint[0]*alphaPoint[1][2]*kernel([xPoint, yPoint],[alphaPoint[1][0], alphaPoint[1][1]], par1, par2)
	return indValue

def svmMain(indata, kernel, figure, par1, par2, C):
	print "Defining the variables needed for vecktor machine"
	N = len(indata)
	P = matrix(buildPMatrix(indata, kernel, par1, par2))
	#G = spmatrix(-1.0, range(2*N), range(N))
	G = np.zeros((2*N,N))
	for i in range(0,N):
		G[i,i] = -1.0
	for i in range(N+1,2*N):
		G[i,i-N] = 1.0
	#print G
	G = matrix(G)
	q = matrix(np.linspace(-1,-1,N))
	h = matrix(np.zeros(2*N))
	for i in range(N, (2*N)-1):
		h[i] = C
	#print h

	print "Calling qp, solving the linear equation"
	r = qp(P, q, G, h)
	alpha = list(r['x'])

	print "Finding the non zero alpha that minimizes the linear equation"
	indicationMapping = []
	epsylon = 0.00001
	for i in range(N):
		if alpha[i] > epsylon:
			indicationMapping.append([alpha[i],data[i]])

	print "Found ", len(indicationMapping), " non zero alphas"

	print "Printing data!"
	figure.hold(True)
	figure.plot([p[0] for p in classA],
		[p[1] for p in classA],
		'bo')
	figure.plot([p[0] for p in classB],
		[p[1] for p in classB],
		'ro')


	print "Setting up massive grid"
	xrange = np.arange(-4, 4, 0.05)
	yrange = np.arange(-4, 4, 0.05)

	grid = matrix([[indicator(x, y, indicationMapping, kernel, par1, par2)
		for y in yrange]
		for x in xrange])

	figure.contour(xrange, yrange, grid, (-1.0, 0.0, 1.0),
	colors=('red', 'black', 'blue'), linewidths=(1, 3, 1))




print "Setting up test data"
classA = [(random.normalvariate(-1.5, 1),
	random.normalvariate(0.5, 1),
	1.0)
	for i in range(5)] + \
	[(random.normalvariate(1.5, 1),
	random.normalvariate(0.5,1),
	1.0)
	for i in range(5)]

classB = [(random.normalvariate(0.0, 2),
	random.normalvariate(-0.5, 2),
	-1.0)
	for i in range(10)]

data = classA + classB
random.shuffle(data)

#kernels = [[linKernel,"Linear"], [polyKernels,"Polynomial"], [RBFKernel,"Radial Basis Function"], [sigmoidKernel,"Sigmoid"]]

kernels = [[RBFKernel,"Radial Basis Function"]]

for ker in kernels:
	for par1 in pylab.frange(0.5, 0.5, 1.0):
		for par2 in pylab.frange(0.0, 0.0, 1.0):
			for C in pylab.frange(0.0, 0.0, 1):
				f = pylab.figure()
				f.canvas.set_window_title(ker[1])
				f.suptitle("Radial Basis Function Sigma=%.2f.png"%(par1))
				svmMain(data, ker[0],f.add_subplot(111), par1, par2, C)
				f.savefig("Radial Basis Function Sigma=%.2f.png"%(par1))

print "Done!"
pylab.show()













