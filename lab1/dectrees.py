import monkdata as m
import dtree as dt

datasets  = [m.monk1,m.monk2,m.monk3]

#Assignment 1
init_entropy_monk1 = dt.entropy(datasets[0])
init_entropy_monk2 = dt.entropy(datasets[1])
init_entropy_monk3 = dt.entropy(datasets[2])

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
  gain_monk1.append(dt.averageGain(datasets[0],m.attributes[x]))
  gain_monk2.append(dt.averageGain(datasets[1],m.attributes[x]))
  gain_monk3.append(dt.averageGain(datasets[2],m.attributes[x]))

print "Monk1:"," ".join([str(y) for y in gain_monk1])
print "Monk2:"," ".join([str(y) for y in gain_monk2])
print "Monk3:"," ".join([str(y) for y in gain_monk3])

print
print "------------------------------"

print "Assignment 3"
print ""


print
print "------------------------------"
