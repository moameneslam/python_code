from pyspark import SparkConf, SparkContext
import math
def max(a,b):
	if (a > b):
		return a
	else:
		return b

con = SparkConf()
sc = SparkContext(conf = con)
list1 = [1,2,3,4,5,5]
rdd = sc.parallelize(list1)
product = rdd.reduce(max)
#data =  product.collect()
print product