from pyspark import SparkConf, SparkContext
import math

def record(rec):
	Record = rec.split("|")
	if Record[2]=="M":
		return True
	else:
		return False

con = SparkConf()
sc = SparkContext(conf = con)

rdd1=sc.textFile("file:///filename.bat")
rdd2 = rdd1.filter(record)
data =  rdd.collect()
male = rdd2.count()
total = rdd.count()
print "males =", male
print "females =", total-male
