import monkdata as m
import dtree as dt
import math as math


#Assignment 1
init_entropy_monk1 = dt.entropy(m.monk1)
init_entropy_monk2 = dt.entropy(m.monk2)
init_entropy_monk3 = dt.entropy(m.monk3)

#Printing results
print "-------- Assignment 1 --------"
print 

print "Monk1 entropy: ", init_entropy_monk1 
print "Monk2 entropy: ", init_entropy_monk2
print "Monk3 entropy: ", init_entropy_monk3

print
print "------------------------------"

print "Assignment 2"
print ""

gain_monk1  = []
gain_monk2  = []
gain_monk3  = []
for x in range(0, 6):
  gain_monk1.append(dt.averageGain(m.monk1,m.attributes[x]))
  gain_monk2.append(dt.averageGain(m.monk2,m.attributes[x]))
  gain_monk3.append(dt.averageGain(m.monk3,m.attributes[x]))

print "Dataset\ta1\t\ta2\t\ta3\t\ta4\t\ta5\t\ta6"
print "Monk1: ","\t".join(["%.7f"%y for y in gain_monk1])
print "Monk2: ","\t".join(["%.7f"%y for y in gain_monk2])
print "Monk3: ","\t".join(["%.7f"%y for y in gain_monk3])

print
print "------------------------------"

print "Assignment 3"
print ""

partition1 = dt.select(m.monk1,m.attributes[4],1)
partition2 = dt.select(m.monk1,m.attributes[4],2)
partition3 = dt.select(m.monk1,m.attributes[4],3)




print
print "------------------------------"

















