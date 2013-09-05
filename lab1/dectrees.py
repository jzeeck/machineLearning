import monkdata as m
import dtree as dt
import math as math
import random as r
#import drawtree as draw


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

print "-------- Assignment 2 --------"
print 

gain_monk1  = []
gain_monk2  = []
gain_monk3  = []
for x in range(0, 6):
  gain_monk1.append(dt.averageGain(m.monk1,m.attributes[x]))
  gain_monk2.append(dt.averageGain(m.monk2,m.attributes[x]))
  gain_monk3.append(dt.averageGain(m.monk3,m.attributes[x]))

print "Dataset\tA1\t\tA2\t\tA3\t\tA4\t\tA5\t\tA6"
print "Monk1: ","\t".join(["%.7f"%y for y in gain_monk1])
print "Monk2: ","\t".join(["%.7f"%y for y in gain_monk2])
print "Monk3: ","\t".join(["%.7f"%y for y in gain_monk3])

print
print "------------------------------"

print "-------- Assignment 3 --------"
print 

partition1 = dt.select(m.monk1,m.attributes[4],1)
partition2 = dt.select(m.monk1,m.attributes[4],2)
partition3 = dt.select(m.monk1,m.attributes[4],3)
partition4 = dt.select(m.monk1,m.attributes[4],4)

gain_partition1  = []
gain_partition2  = []
gain_partition3  = []
gain_partition4  = []

for x in range(0, 6):
  gain_partition1.append(dt.averageGain(partition1,m.attributes[x]))
  gain_partition2.append(dt.averageGain(partition2,m.attributes[x]))
  gain_partition3.append(dt.averageGain(partition3,m.attributes[x]))
  gain_partition4.append(dt.averageGain(partition4,m.attributes[x]))

print "Dataset\tA1\t\tA2\t\tA3\t\tA4\t\tA5\t\tA6"
print "Part 1: ","\t".join(["%.7f"%y for y in gain_partition1])
print "Part 2: ","\t".join(["%.7f"%y for y in gain_partition2])
print "Part 3: ","\t".join(["%.7f"%y for y in gain_partition3])
print "Part 4: ","\t".join(["%.7f"%y for y in gain_partition4])

print
print "Own tree"
print "A5(",dt.mostCommon(partition1),"A4(",dt.mostCommon(partition2),")","A6",dt.mostCommon(partition3),")","A1(",dt.mostCommon(partition4), "))" 

print
print "BuildTree function"
print dt.buildTree(m.monk1,m.attributes,2)
#draw.drawTree(dt.buildTree(m.monk1,m.attributes,2))


print
print "Building Trees"
t1 = dt.buildTree(m.monk1,m.attributes)
t2 = dt.buildTree(m.monk2,m.attributes)
t3 = dt.buildTree(m.monk3,m.attributes)
print "Checking Full Tree"
print "Dataset\tE train\t\tE test"
print "Monk1\t","%.7f"%dt.check(t1,m.monk1), "\t%.7f"%dt.check(t1,m.monk1test)
print "Monk1\t","%.7f"%dt.check(t2,m.monk2), "\t%.7f"%dt.check(t2,m.monk2test)
print "Monk1\t","%.7f"%dt.check(t3,m.monk3), "\t%.7f"%dt.check(t3,m.monk3test)


print
print "------------------------------"


print "-------- Assignment 4 --------"
print
def part(data, frac):
	ldata = list(data)
	r.shuffle(ldata)
	p = int(len(ldata) * frac)
	return ldata[:p], ldata[p:]

monk1train, monk1val = part(m.monk1, 0.6)

print
print "------------------------------"

















