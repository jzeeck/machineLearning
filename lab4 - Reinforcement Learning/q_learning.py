from enviroment import *
from random import *
from animate import * 
from sys import *

def refresh_Q(Q, s_Prime, r, s, a):
	eta = 0.5
	gamma = 0.5
	q_max = - maxint -1
	for i in range(4):
		if Q[s_Prime][i] > q_max:
			q_max = Q[s_Prime][i]
	return eta*(r + gamma*q_max - Q[s][a])





Q = [[0 for x in range(4)] for y in range(16)]

epsilon = 0.3

e = Enviroment()
T = 500
s = [0 for i in range(T+1)]

for t in range(T):
	val = random()
	if val < epsilon:
		a = randint(0,3)
	else:
		q_max = - maxint -1
		a = -1
		for i in range(4):
			if Q[s[t]][i] > q_max:
				q_max = Q[s[t]][i]
				a = i

	state, reward = e.go(a)
	Q[s[t]][a] = Q[s[t]][a] + refresh_Q(Q, state, reward, s[t],a)
	s[t+1] = state

print Q


			
