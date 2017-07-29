from pyspark import SparkConf, SparkContext
import math


con = SparkConf()
sc = SparkContext(conf = con)
list1=[1,2,3,4,5,6,7,85,33,21,2,3,1,4]
rdd = sc.parallelize(list1)
rdd1 = rdd.filter((lambda x: True if x >10 else False))
data =rdd1.collect()
print data
