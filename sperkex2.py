from pyspark import SparkConf, SparkContext
import math

def square(x):
	return x^6**8;

def agg(x):
	return math.fsum(x);

con = SparkConf()
sc = SparkContext(conf = con)
list1 = (2,6,8,8,0,80,45,7)
rdd1 = sc.parallelize(list1)
rdd2 = rdd1.map(square)

data = ghj.collect()
print(data)
