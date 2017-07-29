from pyspark import SparkConf, SparkContext
import math

con = SparkConf()
sc = SparkContext(conf = con)
list1=[1,2,3,4,5,6,7,85,33,21,2,3,1,4]
rdd = sc.parallelize(list1)
num =rdd.count()
data1= rdd.countByValue()

for x in data1:
	print x, "-", data1[x]
