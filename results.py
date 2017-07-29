from pyspark import SparkConf, SparkContext
import math

def filter1(rec):
	Record = rec.split("|")
	return(Record[0], Record[2])

def addResults(A,B):

	result = float(A)+float(B)
	#out = (result/300)*100
	
	return result

def percent(rec):
	print rec[1]
	out = (float(rec[1])/300)*100
	
	return out

con = SparkConf()
sc = SparkContext(conf = con)

rdd=sc.textFile("file:///home/cloudera/results.txt")

rdd1=rdd.map(filter1)
rdd2 = rdd1.reduceByKey(addResults)
rdd3 = rdd2.map(percent)
data =  rdd3.collect()
print data

#rdd = rdd.reduceByKey(function)

