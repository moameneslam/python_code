from pyspark import SparkConf, SparkContext
from itertools import izip, cycle, tee
import math

def split2(var):
	Record = var.split("|")
	return(Record[0], Record[1], Record[2])

def process(A):
	out = (A[0], A[2])
	return out

def calculateM(A):
	total = 0
	prevCounter = A[0][0]
	#print prevCounter
	y =[]
	for i in A:
		curCounter = i[(0)]
		
		
		if prevCounter == i[(0)]:
			total= total+(int(i[(1)]))
			#print 'boom'
		#print marksArray
		else:

			
			y.append((i[0], total ))
			#print y
			
			total =  int(i[(1)])
			

		prevCounter = curCounter
	return y	
#for i in A:
def report(reg, name, address, total):	
	#print reg
	#print Name
	#print address
	#print "_________________________________________"
	#print Total marks
	#print Percentage
	#print grade
	return 0


con = SparkConf()
sc = SparkContext()

results=sc.textFile("file:///home/cloudera/results.txt")
personal=sc.textFile("file:///home/cloudera/personal.txt")

split= results.map(split2)
header = personal.first()
outP = personal.filter(lambda line: line!= header)
split1= outP.map(split2)


#calculate marks
marks = split.map(process)
mark = marks.collect()
x = calculateM(mark)
join= split.union(split1)


out = split1.collect()
print x