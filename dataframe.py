from pyspark import SparkConf, SparkContext, SQLContext
import math

con = SparkConf()
sc = SparkContext(conf = con)#
sql = SQLContext(sc)

rdd1 = sc.textFile("file:///home/cloudera/data.txt")
rdd2 = rdd1.map(lambda x: x.split(","))
df = sql.createDataFrame(rdd2)
df.show()