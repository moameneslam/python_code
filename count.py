from pyspark import SparkConf, SparkContext
import math

#first takes first
#take(numberof records)
def record(rec):
	Record = rec.split("|")
	return(Record[3])

def filter1(record):
	Record = record.split("|")
	if (Record[3]== 'job'):
		return False
	else:
		return True

con = SparkConf()
sc = SparkContext(conf = con)

rdd1=sc.textFile("file:///home/cloudera/Downloads/Users.txt")
rdd2=rdd1.filter(filter1)
rdd3 = rdd2.map(record)
rdd4 = rdd3.distinct()
data =  rdd4.collect()
count = rdd3.countByValue()
print count
