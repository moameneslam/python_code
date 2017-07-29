from pyspark import SparkConf, SparkContext

con = SparkConf()
sc = SparkContext(conf = con)
List1 = [1,2,3,4,56,7]
rdd1 = sc.parallelize(List1)
data= rdd1.collect()
for A in data:
	print(A)

