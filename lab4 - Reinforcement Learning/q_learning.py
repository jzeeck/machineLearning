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


def argmax(f, args):
	mi = None
	m = -1e10
	for i in args:
		v = f(i)
		if(v > m):
			m = v
			mi = i
	return mi

trans = ((1, 3, 4, 12), 
	(0, 2, 5, 13),
	(3, 1, 6, 14),
	(2, 0, 7, 15),
	(5, 7, 0, 8),
	(4, 6, 1, 9),
	(7, 5, 2, 10),
	(6, 4, 3, 11),
	(9, 11, 12, 4),
	(8, 10, 13, 5),
	(11, 9, 14, 6),
	(10, 8, 15, 7),
	(13, 15, 8, 0),
	(12, 14, 9, 1),
	(15, 13, 10, 2),
	(14, 12, 11, 3))





Q = [[0 for x in range(4)] for y in range(16)]

epsilon = 0.3

e = Enviroment()
T = 50000
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


print "Q: ",Q

#we have 16 states we can go from
policy = [None for s in range(16)]
for i in range(len(policy)):
	policy[i] = argmax( lambda(a): Q[i][a], range(4))


print "policy: ", policy

#init start state
current_state = 10
number_of_steps = 100
walk_cycle = [-1 for i in range(number_of_steps)]
for i in range(number_of_steps):
	walk_cycle[i] = current_state
	current_state = trans[current_state][policy[current_state]]

print "walk cycle: ", walk_cycle

draw(walk_cycle)




			
